"""Normalize AD 2025-19-13 (HPT hub quality escape) from its frozen XML.

The record is derived data. The Federal Register XML in an accepted raw
generation stays the source of truth, so the builder refuses bytes whose
SHA-256 does not match that generation's receipt. The record carries:

- a paragraph index of the regulatory text, with ids in the form the seed
  cases cite: ``(c)``, ``(i)(2)``, ``(i)(2)(i)``;
- table 1 to paragraph (g), one entry per row;
- the effective date from paragraph (a), the models from paragraph (c), and
  the flight-cycle window after the effective date from paragraph (g).

Rebuilding from the same bytes gives a byte-identical record.
"""

import hashlib
import json
import re
from datetime import datetime
from pathlib import Path
from typing import Any
from xml.etree.ElementTree import Element

from defusedxml import ElementTree

NORMALIZER_VERSION = "1"
DOCUMENT_NUMBER = "2025-18469"
AD_NUMBER = "AD 2025-19-13"
REPRESENTATION_ROLE = "full_text_xml"
TABLE_PARAGRAPH = "(g)"

LETTERED_HEADING = re.compile(r"^\(([a-z])\)\s*(.+)$")
NUMBERED_ITEM = re.compile(r"^\(([0-9]+)\)\s")
ROMAN_ITEM = re.compile(r"^\(([ivx]+)\)\s")
EFFECTIVE_DATE = re.compile(r"effective (\w+ \d{1,2}, \d{4})")
MODEL = re.compile(r"\bV25\d\d[EM]?-[ADE]5\b")
GRACE_WINDOW = re.compile(r"within (\d+) flight cycles from the effective date")


class SourceMismatch(ValueError):
    """The supplied bytes are not the artifact the generation recorded."""


def build_record(xml_bytes: bytes, generation_dir: Path) -> dict[str, Any]:
    """Verify the XML against its receipt, then derive the normalized record."""
    sha256 = hashlib.sha256(xml_bytes).hexdigest()
    expected = receipt_sha256(generation_dir, DOCUMENT_NUMBER)
    if sha256 != expected:
        raise SourceMismatch(
            f"{DOCUMENT_NUMBER} XML hashes to {sha256}, receipt records {expected}"
        )
    root = ElementTree.fromstring(xml_bytes)
    paragraphs = index_paragraphs(root)
    text = {paragraph["id"]: paragraph["text"] for paragraph in paragraphs}

    effective = EFFECTIVE_DATE.search(text["(a)"])
    if effective is None:
        raise ValueError("paragraph (a) states no effective date")
    models = sorted(set(MODEL.findall(text["(c)"])))
    grace = GRACE_WINDOW.search(text["(g)"])
    rows = table_rows(root)
    if not models or not rows or grace is None:
        raise ValueError("paragraph (c) models, (g) window, or table 1 rows missing")

    record: dict[str, Any] = {
        "record_type": "normalized_directive",
        "normalizer": "hpt_hub_record",
        "normalizer_version": NORMALIZER_VERSION,
        "document": DOCUMENT_NUMBER,
        "ad_number": AD_NUMBER,
        "source": {
            "generation_id": generation_dir.name,
            "representation_role": REPRESENTATION_ROLE,
            "sha256": sha256,
        },
        "effective_date": datetime.strptime(effective.group(1), "%B %d, %Y")
        .date()
        .isoformat(),
        "applicable_models": models,
        "grace_flight_cycles_after_effective_date": int(grace.group(1)),
        "paragraphs": paragraphs,
        "table_1": {"paragraph": TABLE_PARAGRAPH, "rows": rows},
    }
    record["record_sha256"] = record_hash(record)
    return record


def record_hash(record: dict[str, Any]) -> str:
    """Hash the record's canonical JSON, excluding the hash field itself."""
    body = {key: value for key, value in record.items() if key != "record_sha256"}
    return hashlib.sha256(canonical_json(body).encode("utf-8")).hexdigest()


def canonical_json(value: Any) -> str:
    return json.dumps(value, sort_keys=True, ensure_ascii=False, indent=2) + "\n"


def receipt_sha256(generation_dir: Path, document: str) -> str:
    """Return the recorded SHA-256 of a document's full-text XML."""
    for path in sorted((generation_dir / "receipts").glob("*/*.json")):
        receipt = json.loads(path.read_text(encoding="utf-8"))
        if (
            receipt["representation_role"] == REPRESENTATION_ROLE
            and receipt["source_document_identity"]["value"] == document
        ):
            return receipt["artifact"]["sha256"]
    raise SourceMismatch(f"{generation_dir.name} has no XML receipt for {document}")


def index_paragraphs(root: Element) -> list[dict[str, str]]:
    """Index the regulatory text from paragraph (a) to the signature.

    Lettered paragraphs come from headings. Within one, a ``(1)`` item opens a
    numbered subparagraph and a following ``(i)`` item nests under it. Text
    before the first lettered heading (the preamble) is not indexed.
    """
    paragraphs: list[dict[str, str]] = []
    letter = number = None
    for element in root.iter():
        if element.tag == "SIG":
            break
        text = _text(element)
        if element.tag == "HD":
            heading = LETTERED_HEADING.match(text)
            if heading:
                letter, number = f"({heading.group(1)})", None
                paragraphs.append(
                    {"id": letter, "heading": heading.group(2), "text": ""}
                )
            # Other headings inside the regulatory text, such as "Note 1 to
            # paragraph (g)(1):", do not start a paragraph; their text joins
            # the current lettered paragraph.
            continue
        if letter is None or element.tag != "P":
            continue
        if numbered := NUMBERED_ITEM.match(text):
            number = f"{letter}({numbered.group(1)})"
            paragraphs.append({"id": number, "text": text})
        elif (roman := ROMAN_ITEM.match(text)) and number is not None:
            paragraphs.append({"id": f"{number}({roman.group(1)})", "text": text})
        else:
            parent = next(p for p in paragraphs if p["id"] == letter)
            parent["text"] = f"{parent['text']} {text}".strip()
    return paragraphs


def table_rows(root: Element) -> list[dict[str, Any]]:
    """Read the four-column rows of table 1 to paragraph (g)."""
    rows = []
    in_g = False
    for element in root.iter():
        if element.tag == "HD":
            heading = LETTERED_HEADING.match(_text(element))
            if heading:
                in_g = f"({heading.group(1)})" == TABLE_PARAGRAPH
        elif element.tag == "ROW" and in_g:
            cells = [_text(cell) for cell in element]
            if len(cells) != 4:
                raise ValueError(f"table 1 row has {len(cells)} cells: {cells}")
            component, part_number, serial_number, limit = cells
            rows.append(
                {
                    "component": component,
                    "part_number": part_number,
                    "serial_number": serial_number,
                    "removal_limit_cycles_since_new": int(limit.replace(",", "")),
                }
            )
    return rows


def _text(element: Element) -> str:
    return " ".join("".join(element.itertext()).split())
