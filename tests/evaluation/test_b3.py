"""B3 prompt freeze, field accuracy, escalation classes, and offline replay."""

import copy
import json
from datetime import date
from pathlib import Path

from faa_directive_impact.evaluation.b3_fields import compare
from faa_directive_impact.evaluation.b3_prompt import PROMPT, PROMPT_VERSION, question
from faa_directive_impact.evaluation.b3_summary import classify_unit
from faa_directive_impact.evaluation.s1_scoring import units
from faa_directive_impact.evaluation.seed import load_seed_cases
from faa_directive_impact.rules.interpreter import screen_rules

REPO = Path(__file__).resolve().parents[2]
REFERENCE = REPO / "evaluation/b3/reference"
REFERENCES = {p.stem: json.loads(p.read_text()) for p in REFERENCE.glob("*.json")}
RUN = REPO / "evaluation/runs/b3-opus-5-5-high-r1-20261011T155547Z-9f32a55"

# Every frozen prompt version, oldest first. A new version needs a stated
# reason and new runs, never a quiet edit.
FROZEN_PROMPT_VERSIONS = {
    "93fa052fe394": "v1, frozen 2026-10-11 after plumbing b3-plumbing-20261011T155454Z",
}


def test_prompt_is_frozen() -> None:
    assert PROMPT_VERSION == list(FROZEN_PROMPT_VERSIONS)[-1]


def test_prompt_never_contains_labels_references_or_adjudications() -> None:
    text = PROMPT + question("2025-18469") + question("2026-16954")
    cases = [c.record for c in load_seed_cases(REPO / "evaluation/seed/cases")]
    for case in cases:
        assert case["title"] not in text
        for outcome in case["expected"]:
            assert outcome["reason"] not in text
    for reference in REFERENCES.values():
        for ambiguity in reference["ambiguities"]:
            assert ambiguity["description"] not in text
    assert "faa-informal" not in text


def test_reference_matches_itself_on_every_field() -> None:
    for reference in REFERENCES.values():
        result = compare(reference, reference)
        assert result["correct"] == result["fields"]
        assert all(a["flagged"] for a in result["ambiguities"]["expected"])


def test_wrong_serial_and_missing_ambiguity_are_counted() -> None:
    reference = REFERENCES["2025-18469"]
    draft = copy.deepcopy(reference)
    draft["affected_parts"][0]["serial_number"] = "PKLBSK9288"
    draft["ambiguities"] = []
    result = compare(draft, reference)
    wrong = [c["field"] for c in result["checks"] if not c["correct"]]
    assert wrong == ["affected_parts"]
    assert not result["ambiguities"]["expected"][0]["flagged"]


def test_declined_action_is_a_safe_escalation_but_a_false_clear_never_is() -> None:
    declined = {
        "output": {
            "notes": ["... is not evaluated: this interpreter does not support x"]
        },
        "extraction_errors": ["1", "8", "12"],
    }
    assert classify_unit(declined) == {
        "safe_escalation": ["8", "12"],
        "substantive": ["1"],
    }
    plain = {"output": {"notes": []}, "extraction_errors": ["8"]}
    assert classify_unit(plain) == {"safe_escalation": [], "substantive": ["8"]}


def test_one_combination_correction_reproduces_the_reference_in_every_repeat() -> None:
    """The write-up's claim: fixing (g)'s "unclear" gives the reference outcomes."""
    cases = [c.record for c in load_seed_cases(REPO / "evaluation/seed/cases")]
    by_name = {u.name: u for u in units(cases)}
    runs = sorted((REPO / "evaluation/runs").glob("b3-opus-5-5-high-r*"))
    assert len(runs) == 3
    for run in runs:
        for unit in json.loads((run / "units.json").read_text()):
            draft = json.loads(
                (run / "extractions" / f"{unit['directive']}.json").read_text()
            )
            for action in draft["required_actions"]:
                if action["combination"] == "unclear":
                    action["combination"] = "whichever_occurs_later"
            case = by_name[unit["unit"]]
            asset = case.record["asset_snapshot"]
            as_of = date.fromisoformat(case.record["source_snapshot"]["as_of"])
            drafted = screen_rules(draft, asset, as_of)
            reference = screen_rules(REFERENCES[unit["directive"]], asset, as_of)
            assert (
                drafted.applicability,
                drafted.action_status,
                drafted.computed,
            ) == (
                reference.applicability,
                reference.action_status,
                reference.computed,
            ), (run.name, unit["unit"])


def test_recorded_run_replays_offline_through_the_interpreter() -> None:
    recorded = json.loads((RUN / "units.json").read_text())
    cases = [c.record for c in load_seed_cases(REPO / "evaluation/seed/cases")]
    by_name = {u.name: u for u in units(cases)}
    for unit in recorded:
        draft = json.loads(
            (RUN / "extractions" / f"{unit['directive']}.json").read_text()
        )
        case = by_name[unit["unit"]]
        result = screen_rules(
            draft,
            case.record["asset_snapshot"],
            date.fromisoformat(case.record["source_snapshot"]["as_of"]),
        ).to_dict()
        assert [result["applicability"], result["action_status"]] == unit["drafted"]
        assert result["computed"] == unit["output"]["computed"]
