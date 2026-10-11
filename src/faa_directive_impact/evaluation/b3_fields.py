"""Field accuracy of a drafted rule record against the hand-written reference.

Each check is one field, scored exactly: right or wrong, with what was
expected and what was drafted. Fields are compared as the interpreter would
use them (sets where order carries no meaning, paragraph labels as written).
Prose (descriptions, reasons, notes) is not scored here; a proofreader reads
it.

Ambiguity flagging is scored separately. A reference ambiguity counts as
flagged when the draft lists an ambiguity on the same paragraph; whether the
draft's readings mean the same thing goes to the proofreader. Ambiguities the
draft lists that the reference does not are reported, not penalized: a
proofreader decides whether each is real.
"""

from typing import Any


def compare(draft: dict[str, Any], reference: dict[str, Any]) -> dict[str, Any]:
    checks: list[dict[str, Any]] = []

    def check(field: str, expected: Any, drafted: Any) -> None:
        checks.append(
            {
                "field": field,
                "correct": expected == drafted,
                "expected": _plain(expected),
                "drafted": _plain(drafted),
            }
        )

    check(
        "governing_document",
        reference["governing_document"]["document"],
        draft["governing_document"]["document"],
    )
    check(
        "corrections.paragraphs",
        {(c["document"], c["paragraph"]) for c in reference["corrections"]},
        {(c["document"], c["paragraph"]) for c in draft["corrections"]},
    )
    check(
        "effective_date",
        reference["effective_date"]["date"],
        draft["effective_date"]["date"],
    )
    check(
        "effective_date.source",
        _source(reference["effective_date"]["source"]),
        _source(draft["effective_date"]["source"]),
    )
    ref_app, app = reference["applicability"], draft["applicability"]
    check(
        "applicability.engine_models",
        set(ref_app["engine_models"]),
        set(app["engine_models"]),
    )
    check(
        "applicability.models_source",
        _source(ref_app["models_source"]),
        _source(app["models_source"]),
    )
    ref_condition, condition = ref_app["part_condition"], app["part_condition"]
    check(
        "applicability.part_condition.part_numbers",
        set(ref_condition["part_numbers"]) if ref_condition else None,
        set(condition["part_numbers"]) if condition else None,
    )
    if ref_condition and condition:
        check(
            "applicability.part_condition.source",
            _source(ref_condition["source"]),
            _source(condition["source"]),
        )
    check(
        "affected_parts",
        {_row(row) for row in reference["affected_parts"]},
        {_row(row) for row in draft["affected_parts"]},
    )
    check(
        "affected_parts.component_names",
        {row["component"] for row in reference["affected_parts"]},
        {row["component"] for row in draft["affected_parts"]},
    )
    check(
        "eligible_parts.part_numbers",
        {n for part in reference["eligible_parts"] for n in part["part_numbers"]},
        {n for part in draft["eligible_parts"] for n in part["part_numbers"]},
    )
    check(
        "required_actions.paragraphs",
        sorted(a["paragraph"] for a in reference["required_actions"]),
        sorted(a["paragraph"] for a in draft["required_actions"]),
    )
    drafted_actions = {a["paragraph"]: a for a in draft["required_actions"]}
    for ref_action in reference["required_actions"]:
        paragraph = ref_action["paragraph"]
        action = drafted_actions.get(paragraph)
        prefix = f"required_actions[{paragraph}]"
        for key in (
            "applies_to",
            "trigger",
            "shop_visit_definition_paragraph",
            "combination",
        ):
            check(f"{prefix}.{key}", ref_action[key], action[key] if action else None)
        check(
            f"{prefix}.condition.definition_paragraph",
            _condition(ref_action),
            _condition(action) if action else None,
        )
        check(
            f"{prefix}.limits",
            {(limit["kind"], limit["value"]) for limit in ref_action["limits"]},
            {(limit["kind"], limit["value"]) for limit in action["limits"]}
            if action
            else None,
        )
    check(
        "installation_prohibitions",
        {
            (p["paragraph"], p["applies_to"])
            for p in reference["installation_prohibitions"]
        },
        {(p["paragraph"], p["applies_to"]) for p in draft["installation_prohibitions"]},
    )
    check(
        "definitions.paragraphs",
        {d["paragraph"] for d in reference["definitions"]},
        {d["paragraph"] for d in draft["definitions"]},
    )
    check("amoc_paragraph", reference["amoc_paragraph"], draft["amoc_paragraph"])

    drafted_paragraphs = {a["paragraph"] for a in draft["ambiguities"]}
    reference_paragraphs = {a["paragraph"] for a in reference["ambiguities"]}
    ambiguities = {
        "expected": [
            {
                "paragraph": a["paragraph"],
                "description": a["description"],
                "flagged": a["paragraph"] in drafted_paragraphs,
            }
            for a in reference["ambiguities"]
        ],
        "additional": [
            a
            for a in draft["ambiguities"]
            if a["paragraph"] not in reference_paragraphs
        ],
    }
    correct = sum(c["correct"] for c in checks)
    return {
        "fields": len(checks),
        "correct": correct,
        "accuracy": round(correct / len(checks), 4),
        "checks": checks,
        "ambiguities": ambiguities,
    }


def _source(source: dict[str, Any]) -> tuple[str, str]:
    return (source["document"], source["paragraph"])


def _row(row: dict[str, Any]) -> tuple[Any, ...]:
    return (
        row["part_number"],
        row["serial_number"],
        row["removal_limit_cycles_since_new"],
    )


def _condition(action: dict[str, Any]) -> str | None:
    condition = action["condition"]
    if condition is None:
        return None
    return condition["definition_paragraph"] or "(no definition paragraph)"


def _plain(value: Any) -> Any:
    """Make sets and tuples JSON-friendly, sorted for stable output."""
    if isinstance(value, set):
        return sorted((_plain(v) for v in value), key=repr)
    if isinstance(value, tuple):
        return [_plain(v) for v in value]
    if isinstance(value, list):
        return [_plain(v) for v in value]
    return value
