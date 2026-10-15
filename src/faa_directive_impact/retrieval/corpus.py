"""Normalize a frozen generation into retrieval records.

A retrieval record keeps only what candidate retrieval reads, plus enough
identity to cite it: the document's kind and dates, its relationships, the
models statement of its applicability paragraph (c), and every identifier
token in its regulatory text with the paragraph it appears in. The records
are committed (Federal Register text is a U.S. Government work; see
``REDISTRIBUTION.md``), so the index can be rebuilt without raw bytes. The
index is derived from them and is never the source of truth.
"""

import re
from pathlib import Path
from typing import Any
from xml.etree.ElementTree import Element

from defusedxml import ElementTree

from faa_directive_impact.directives.source_text import load_generation

RECORD_VERSION = 2
PARAGRAPH_HEADING = re.compile(r"^\(([a-z])\)\s")
APPLICABILITY_HEADING = re.compile(r"^\(c\)\s*Applicability$")
# An identifier: letters, digits, and inner hyphens or slashes, containing a
# digit, at least four characters. Part numbers (2A5001, 6A8353-001) and
# model designations (V2527-A5, CFM56-5B4/3) both qualify.
IDENTIFIER = re.compile(r"(?<![\w/-])[A-Z0-9][A-Z0-9/-]*[A-Z0-9](?![\w/-])")
HYPHEN_SPACE = re.compile(r"-\s+")
# The amendment line of a final rule: "2025-19-13 International Aero Engines
# AG: Amendment 39-23153; ..."
AMENDMENT_LINE = re.compile(r"^(\d{4}-\d{2}-\d{2})\b[^.]*Amendment 39-\d+")
KINDS = {"Proposed Rule": "proposal", "Rule": "final_rule"}


def normalize_generation(
    generation_dir: Path, storage_root: Path
) -> list[dict[str, Any]]:
    """Return one retrieval record per document, sorted by document number."""
    documents, relationships = load_generation(generation_dir, storage_root)
    links: dict[str, list[dict[str, str]]] = {number: [] for number in documents}
    for link in relationships:
        for here, there, direction in (
            (link.source, link.target, "to"),
            (link.target, link.source, "from"),
        ):
            if here in links:
                links[here].append(
                    {"type": link.kind, "direction": direction,
                     "document": there}
                )  # fmt: skip
    records = []
    for number, document in sorted(documents.items()):
        root = ElementTree.fromstring(document.xml)
        corrects = [
            item["document"]
            for item in links[number]
            if item["type"] == "corrects" and item["direction"] == "to"
        ]
        records.append(
            {
                "record_version": RECORD_VERSION,
                "document": number,
                "kind": "correction"
                if corrects
                else KINDS.get(document.document_type, document.document_type),
                "title": document.title,
                "ad_number": ad_number(root),
                "publication_date": document.publication_date.isoformat(),
                "effective_date": document.effective_date.isoformat()
                if document.effective_date
                else None,
                "relationships": sorted(
                    links[number], key=lambda item: (item["type"], item["document"])
                ),
                "applicability_statement": applicability_statement(root),
                "applicability_models": applicability_models(root),
                "identifiers": regulatory_identifiers(root),
            }
        )
    return records


def ad_number(root: Element) -> str | None:
    """The AD number from a final rule's amendment line, if it has one."""
    for element in root.iter():
        if element.tag in ("P", "FP"):
            match = AMENDMENT_LINE.match(_text(element))
            if match:
                return f"AD {match.group(1)}"
    return None


def applicability_statement(root: Element) -> str | None:
    """Every paragraph under the "(c) Applicability" heading, joined.

    Many directives state applicability as a lead-in ("This AD applies to:")
    followed by a list of models in later paragraphs, so the whole section is
    read, up to the next heading.
    """
    elements = list(root.iter())
    for index, element in enumerate(elements):
        if element.tag != "HD" or not APPLICABILITY_HEADING.fullmatch(_text(element)):
            continue
        parts = []
        for following in elements[index + 1 :]:
            if following.tag == "HD":
                break
            if following.tag in ("P", "FP"):
                parts.append(_text(following))
        return " ".join(parts) or None
    return None


def applicability_models(root: Element) -> list[str]:
    """Every identifier in the applicability statement, normalized."""
    statement = applicability_statement(root)
    if statement is None:
        return []
    text = HYPHEN_SPACE.sub("-", statement)
    return sorted(identifiers(text))


def regulatory_identifiers(root: Element) -> dict[str, list[str]]:
    """Identifier token -> paragraphs it appears in, from paragraph (a) on.

    The regulatory text starts at the first heading "(a) ..."; the preamble
    before it is discussion, not the rule. Tables are read cell by cell.
    """
    found: dict[str, set[str]] = {}
    paragraph = None
    for element in root.iter():
        if element.tag == "HD":
            heading = PARAGRAPH_HEADING.match(_text(element))
            if heading:
                paragraph = f"({heading.group(1)})"
            continue
        if paragraph is None or element.tag not in ("P", "FP", "ENT"):
            continue
        text = HYPHEN_SPACE.sub("-", _text(element))
        for token in identifiers(text):
            found.setdefault(token, set()).add(paragraph)
    return {token: sorted(paragraphs) for token, paragraphs in sorted(found.items())}


def identifiers(text: str) -> set[str]:
    """Normalized identifier tokens in ``text``: four or more characters, one a digit."""
    return {
        normalize(token)
        for token in IDENTIFIER.findall(text)
        if len(token) >= 4 and any(character.isdigit() for character in token)
    }


def normalize(token: str) -> str:
    return "".join(token.upper().split())


def _text(element: Element) -> str:
    return " ".join("".join(element.itertext()).split())
