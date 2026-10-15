"""R0: the identifier-match lexical retriever (``evaluation/retrieval/PREREGISTRATION.md``).

An engine's model designation is looked up in each directive's applicability
paragraph (c); each installed part number is looked up as a whole token in
the regulatory text. Either match makes the directive a candidate. Only
documents published on or before the as-of date count, and a retrieved final
rule brings the corrections published by then.

Retrieval decides relevance only. It never clears an engine: what it returns
goes to a screener, and a candidate with no rule record goes to review.
"""

from datetime import date
from typing import Any

from faa_directive_impact.retrieval.corpus import identifiers, normalize

RETRIEVER_VERSION = "R0"
UNKNOWN = "unknown"
VIA_PART_NUMBER = "part_number"
VIA_MODEL = "engine_model"
VIA_THREAD = "correction_of_candidate"
VIA_ORDER = (VIA_PART_NUMBER, VIA_MODEL, VIA_THREAD)


def query_tokens(asset: dict[str, Any]) -> tuple[str | None, set[str]]:
    """The engine model and the installed part numbers, normalized."""
    model = asset.get("engine", {}).get("engine_model")
    parts = set()
    for component in asset.get("installed_components", []):
        part_number = component.get("part_number")
        if isinstance(part_number, str) and part_number.strip().lower() != UNKNOWN:
            parts |= identifiers(part_number.upper())
    return (
        normalize(model) if isinstance(model, str) and model.strip() else None
    ), parts


def retrieve(
    records: list[dict[str, Any]], asset: dict[str, Any], as_of: date
) -> list[dict[str, Any]]:
    """Return the candidate directives for one engine, most specific first."""
    model, parts = query_tokens(asset)
    published = {
        record["document"]: record
        for record in records
        if date.fromisoformat(record["publication_date"]) <= as_of
    }
    candidates: dict[str, dict[str, Any]] = {}
    for number, record in published.items():
        matched_parts = sorted(parts & record["identifiers"].keys())
        if matched_parts:
            candidates[number] = _candidate(
                record,
                VIA_PART_NUMBER,
                [
                    {"token": part, "paragraphs": record["identifiers"][part]}
                    for part in matched_parts
                ],
            )
        elif model and model in record["applicability_models"]:
            candidates[number] = _candidate(
                record, VIA_MODEL, [{"token": model, "paragraphs": ["(c)"]}]
            )
    for number in list(candidates):
        for link in published[number]["relationships"]:
            correction = link["document"]
            if (
                link["type"] == "corrects"
                and link["direction"] == "from"
                and correction in published
                and correction not in candidates
            ):
                candidates[correction] = _candidate(
                    published[correction], VIA_THREAD, [{"token": number}]
                )
    return sorted(
        candidates.values(),
        key=lambda c: (
            VIA_ORDER.index(c["via"]),
            -date.fromisoformat(c["publication_date"]).toordinal(),
            c["document"],
        ),
    )


def _candidate(
    record: dict[str, Any], via: str, matches: list[dict[str, Any]]
) -> dict[str, Any]:
    return {
        "document": record["document"],
        "kind": record["kind"],
        "title": record["title"],
        "publication_date": record["publication_date"],
        "via": via,
        "matches": matches,
    }
