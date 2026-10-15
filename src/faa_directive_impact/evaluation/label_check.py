"""Blind packets and comparison for the independent label check.

The coverage pre-registration (``evaluation/coverage/PREREGISTRATION.md``)
has a second reviewer derive each case's outcome without seeing the label.
``blind_case`` removes everything that states or explains the answer;
``compare`` lines the reviewer's derived outcome up against the label field
by field, so every disagreement can be adjudicated in writing.
"""

from typing import Any

# Fields that state or explain the expected answer.
HIDDEN_CASE_FIELDS = ("expected", "forbidden_claims", "notes", "title", "slice")
HIDDEN_LABEL_FIELDS = ("rationale",)
COMPARED_FIELDS = ("applicability", "action_status", "required_missing_facts")


def blind_case(record: dict[str, Any]) -> dict[str, Any]:
    """The case as the reviewer sees it: facts and candidates, no answer."""
    blind = {k: v for k, v in record.items() if k not in HIDDEN_CASE_FIELDS}
    blind["label"] = {
        k: v for k, v in record["label"].items() if k not in HIDDEN_LABEL_FIELDS
    }
    return blind


def compare(
    record: dict[str, Any], derived: list[dict[str, Any]]
) -> list[dict[str, Any]]:
    """One row per (directive, field) where label and reviewer differ.

    ``derived`` uses the case's own outcome fields: ``directive``,
    ``applicability``, ``action_status``, ``required_missing_facts``, and a
    free-text ``timing``. Timing is compared by a person, not here.
    """
    theirs = {item["directive"]: item for item in derived}
    rows = []
    for expected in record["expected"]:
        directive = expected["directive"]
        other = theirs.get(directive)
        if other is None:
            rows.append(_row(record, directive, "outcome", expected, None))
            continue
        for field in COMPARED_FIELDS:
            ours, reviewer = expected.get(field), other.get(field)
            if field == "required_missing_facts":
                ours, reviewer = bool(ours), bool(reviewer)
            if ours != reviewer:
                rows.append(
                    _row(
                        record, directive, field, expected.get(field), other.get(field)
                    )
                )
    return rows


def _row(
    record: dict[str, Any], directive: str, field: str, ours: Any, reviewer: Any
) -> dict[str, Any]:
    return {
        "case_id": record["case_id"],
        "directive": directive,
        "field": field,
        "label": ours,
        "reviewer": reviewer,
    }
