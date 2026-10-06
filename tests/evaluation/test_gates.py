import re
from pathlib import Path

import pytest

from faa_directive_impact.evaluation.seed import load_seed_cases

REPO = Path(__file__).resolve().parents[2]
CASES = REPO / "evaluation" / "seed" / "cases"
GATES = REPO / "evaluation" / "GATES.md"
S1_DIRECTIVE = "2025-18469"

ACTION = {"action_required", "action_required_on_event"}
CLEAR = {"does_not_apply", "no_action_triggered"}


def units() -> list[tuple[str, dict, dict]]:
    """Every (unit name, case, expected outcome), named as GATES.md names it."""
    result = []
    for case in load_seed_cases(CASES):
        record = case.record
        several = len(record["expected"]) > 1
        for outcome in record["expected"]:
            name = record["case_id"]
            if several:
                name = f"{name}/{outcome['directive']}"
            result.append((name, record, outcome))
    return result


def outcome_status(outcome: dict) -> str:
    return outcome.get("action_status") or outcome["applicability"]


def is_determinate(record: dict, outcome: dict) -> bool:
    label = record["label"]
    unadjudicated_expert = (
        label["provenance"] == "expert_required" and label["status"] != "adjudicated"
    )
    return (
        not outcome.get("required_missing_facts")
        and outcome["applicability"] != "unknown"
        and outcome.get("action_status") != "needs_review"
        and not unadjudicated_expert
    )


SELECTORS = {
    "1": lambda _, o: (
        o["applicability"] == "applies" and o.get("action_status") in ACTION
    ),
    "2": lambda _, o: o["applicability"] == "outside_supported_scope",
    "3": lambda _, o: (
        o["applicability"] == "unknown" or o.get("action_status") == "needs_review"
    ),
    "4": lambda _, o: bool(o.get("required_missing_facts")),
    "7": lambda _, o: o.get("authority_state", "in_force") != "in_force",
    "8": lambda _, o: "computed" in o,
    "9": lambda r, _: r["slice"] in {"unaffected_part", "part_identity"},
    "12": is_determinate,
    "13": lambda _, o: outcome_status(o) in CLEAR,
}


def documented_coverage() -> dict[str, tuple[list[str], int]]:
    rows = re.findall(
        r"^\| (\d+) \| Covers: ([^|]+) \| (\d+) \|$",
        GATES.read_text(encoding="utf-8"),
        flags=re.MULTILINE,
    )
    return {
        gate: ([name.strip() for name in names.split(",")], int(s1))
        for gate, names, s1 in rows
    }


def test_every_selector_has_a_documented_coverage_row() -> None:
    assert documented_coverage().keys() == SELECTORS.keys()


@pytest.mark.parametrize("gate", sorted(SELECTORS, key=int))
def test_documented_coverage_matches_seed_cases(gate: str) -> None:
    selected = [
        (name, outcome)
        for name, record, outcome in units()
        if SELECTORS[gate](record, outcome)
    ]
    names, s1_count = documented_coverage()[gate]

    assert names == [name for name, _ in selected]
    assert s1_count == sum(o["directive"] == S1_DIRECTIVE for _, o in selected)


def test_s1_slice_size_matches_gates_document() -> None:
    s1_units = [name for name, _, o in units() if o["directive"] == S1_DIRECTIVE]

    assert len(units()) == 33
    assert len(s1_units) == 18
