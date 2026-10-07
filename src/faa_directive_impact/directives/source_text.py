"""Load a generation's directive documents and render them as readable text.

The Federal Register's own plain-text representation drops image-only tables
without a trace: AD 2021-14268's serial-number tables simply vanish. A reader
of that text cannot know anything is missing. Rendering from the XML instead
keeps every heading, paragraph, and table, and marks each image with an
explicit placeholder.

Every document is read from local storage and checked against the SHA-256
its generation's receipt records before use.
"""

import hashlib
import json
from dataclasses import dataclass
from datetime import date
from pathlib import Path
from xml.etree.ElementTree import Element

from defusedxml import ElementTree

IDENTITY_NAMESPACE = "federal_register_document_number"
BLOCK_TAGS = {
    "HD", "P", "FP", "AMDPAR", "SUBJECT", "AGENCY", "SUBAGY", "CFR", "DEPDOC",
    "RIN", "ACT", "DATED", "NAME", "TITLE", "FRDOC", "NOTE", "LI", "SECTNO",
}  # fmt: skip
SKIP_TAGS = {"PRTPAGE", "BILCOD", "FTREF"}


class SourceMismatch(ValueError):
    """Local bytes differ from what the generation's receipt recorded."""


@dataclass(frozen=True)
class SourceDocument:
    number: str
    document_type: str  # "Rule" or "Proposed Rule"
    publication_date: date
    effective_date: date | None
    title: str
    xml: bytes

    @property
    def text(self) -> str:
        return render_text(ElementTree.fromstring(self.xml))


@dataclass(frozen=True)
class Relationship:
    kind: str  # proposal_final, corrects, supersedes
    source: str
    target: str


def load_generation(
    generation_dir: Path, storage_root: Path
) -> tuple[dict[str, SourceDocument], list[Relationship]]:
    """Read every document's XML and API record, verifying each hash."""
    generation_id = generation_dir.name
    run_id = f"run-{generation_id.removeprefix('gen-')}"
    receipts = {}
    for path in sorted((generation_dir / "receipts" / run_id).glob("*.json")):
        receipt = json.loads(path.read_text(encoding="utf-8"))
        identity = receipt["source_document_identity"]
        if identity["namespace"] != IDENTITY_NAMESPACE:
            continue
        role = receipt["representation_role"]
        if role in ("full_text_xml", "api_json"):
            receipts[(identity["value"], role)] = receipt

    documents = {}
    for number in sorted({number for number, _ in receipts}):
        xml = _verified_bytes(storage_root, receipts[(number, "full_text_xml")])
        api = json.loads(_verified_bytes(storage_root, receipts[(number, "api_json")]))
        effective = api.get("effective_on")
        documents[number] = SourceDocument(
            number=number,
            document_type=api["type"],
            publication_date=date.fromisoformat(api["publication_date"]),
            effective_date=date.fromisoformat(effective) if effective else None,
            title=api["title"],
            xml=xml,
        )

    manifest_path = (
        generation_dir / "manifests" / f"raw-generation-{generation_id}.json"
    )
    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    relationships = [
        Relationship(
            item["relationship_type"],
            item["from_identity"]["value"],
            item["to_identity"]["value"],
        )
        for item in manifest["relationships"]
    ]
    return documents, relationships


def documents_for(
    directive: str,
    as_of: date,
    documents: dict[str, SourceDocument],
    relationships: list[Relationship],
) -> list[SourceDocument]:
    """The directive plus its thread, as published on or before ``as_of``.

    The thread is every document linked by a recorded relationship
    (proposal and final rule, correction, supersession). A reader on the
    question date could not have seen anything published later, so later
    documents are left out; the directive itself is always included.
    """
    thread, frontier = {directive}, [directive]
    while frontier:
        current = frontier.pop()
        for link in relationships:
            for here, there in ((link.source, link.target), (link.target, link.source)):
                if here == current and there not in thread:
                    thread.add(there)
                    frontier.append(there)
    selected = [
        documents[number]
        for number in sorted(thread)
        if number == directive or documents[number].publication_date <= as_of
    ]
    return sorted(selected, key=lambda doc: (doc.publication_date, doc.number))


def render_text(root: Element) -> str:
    """Render Federal Register XML as plain text with image placeholders."""
    lines: list[str] = []
    _render(root, lines)
    text = "\n\n".join(line for line in lines if line)
    return text + "\n"


def _render(element: Element, lines: list[str]) -> None:
    tag = element.tag
    if tag in SKIP_TAGS:
        return
    if tag == "GPH":
        names = [_text(gid) for gid in element.iter("GID")]
        lines.append(
            f"[Image {', '.join(names)} is not included in this text. It may "
            "contain a table or figure.]"
        )
        return
    if tag == "GPOTABLE":
        lines.append(_render_table(element))
        return
    if tag in BLOCK_TAGS:
        lines.append(_text(element))
        return
    for child in element:
        _render(child, lines)


def _render_table(table: Element) -> str:
    rows = []
    title = table.find("TTITLE")
    if title is not None and _text(title):
        rows.append(_text(title))
    headers = [_text(cell) for cell in table.iter("CHED")]
    if headers:
        rows.append(" | ".join(headers))
    for row in table.iter("ROW"):
        rows.append(" | ".join(_text(cell) for cell in row))
    return "\n".join(rows)


def _text(element: Element) -> str:
    return " ".join("".join(element.itertext()).split())


def _verified_bytes(storage_root: Path, receipt: dict) -> bytes:
    artifact = receipt["artifact"]
    path = storage_root / artifact["relative_path"]
    data = path.read_bytes()
    digest = hashlib.sha256(data).hexdigest()
    if digest != artifact["sha256"]:
        raise SourceMismatch(
            f"{path} hashes to {digest}, receipt has {artifact['sha256']}"
        )
    return data
