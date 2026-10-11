"""The general rule interpreter, on the hand-written reference records."""

import copy
import json
from datetime import date
from pathlib import Path

import pytest
from jsonschema import Draft202012Validator

from faa_directive_impact.directives.hpt_hub_record import build_record
from faa_directive_impact.evaluation.s1_scoring import units
from faa_directive_impact.evaluation.seed import load_seed_cases
from faa_directive_impact.impact.hpt_hub_rules import screen
from faa_directive_impact.rules.interpreter import screen_rules
from faa_directive_impact.schema_validation import load_schema

REPO = Path(__file__).resolve().parents[2]
REFERENCE = REPO / "evaluation/b3/reference"
HUB = json.loads((REFERENCE / "2025-18469.json").read_text())
BLADE = json.loads((REFERENCE / "2026-16954.json").read_text())
AS_OF = date(2026, 10, 5)


def blade_engine(part_number: str | None = "6A8353", events=()) -> dict:
    components = []
    if part_number is not None:
        components.append(
            {
                "component_name": "3rd stage HPC rotor blade set",
                "part_number": part_number,
                "serial_number": "not tracked at set level",
            }
        )
    return {
        "engine": {"engine_model": "V2527-A5", "engine_serial_number": "SYN-T"},
        "installed_components": components,
        "events": list(events),
    }


def visit(at: str) -> dict:
    return {
        "event_type": "shop_visit_induction",
        "at": at,
        "qualifies_as_engine_shop_visit": {"AD 2026-17-03": "yes"},
    }


def cited(screen_result) -> set[tuple[str, str]]:
    return {(c.document, c.paragraph) for c in screen_result.citations}


@pytest.mark.parametrize("record", [HUB, BLADE])
def test_reference_records_follow_the_rule_schema(record) -> None:
    schema = load_schema("b3-rule-record.schema.json")
    assert not list(Draft202012Validator(schema).iter_errors(record))


def test_listed_blade_makes_the_action_due_on_the_next_exposure() -> None:
    result = screen_rules(BLADE, blade_engine(), AS_OF)
    assert (result.applicability, result.action_status) == (
        "applies",
        "action_required_on_event",
    )
    assert {("2026-18423", "(c)"), ("2026-18423", "(g)")} <= cited(result)


def test_eligible_blade_clears_the_engine_with_its_definition_cited() -> None:
    result = screen_rules(BLADE, blade_engine("6C8368"), AS_OF)
    assert result.applicability == "does_not_apply"
    assert ("2026-18423", "(h)(1)(i)") in cited(result)


def test_unknown_blade_part_number_is_not_evidence_of_absence() -> None:
    result = screen_rules(BLADE, blade_engine("unknown"), AS_OF)
    assert (result.applicability, result.action_status) == ("unknown", "needs_review")
    assert result.missing_facts == [
        "installed_components[3rd stage HPC rotor blade set].part_number"
    ]


def test_missing_blade_record_goes_to_review() -> None:
    result = screen_rules(BLADE, blade_engine(None), AS_OF)
    assert result.applicability == "unknown"
    assert result.missing_facts == ["installed_components[3rd stage HPC rotor blade]"]


def test_visit_inducted_before_the_effective_date_does_not_trigger() -> None:
    result = screen_rules(BLADE, blade_engine(events=[visit("2026-09-14")]), AS_OF)
    assert result.action_status == "action_required_on_event"


def test_conditional_trigger_at_a_later_visit_is_left_to_a_person() -> None:
    result = screen_rules(BLADE, blade_engine(events=[visit("2026-10-01")]), AS_OF)
    assert result.action_status == "needs_review"
    assert any("not a structured record field" in note for note in result.notes)


def test_unclear_combination_is_declined_not_guessed() -> None:
    rules = copy.deepcopy(HUB)
    rules["required_actions"][0]["combination"] = "unclear"
    case = next(u for u in s1_units() if u.name == "seed-001")
    result = screen_rules(rules, case.record["asset_snapshot"], as_of(case))
    assert result.action_status == "needs_review"
    assert "latest_engine_flight_cycles" not in result.computed
    assert any("is not evaluated" in note for note in result.notes)


def test_whichever_first_takes_the_earlier_deadline() -> None:
    rules = copy.deepcopy(HUB)
    rules["required_actions"][0]["combination"] = "whichever_occurs_first"
    case = next(u for u in s1_units() if u.name == "seed-001")
    later = screen_rules(HUB, case.record["asset_snapshot"], as_of(case))
    first = screen_rules(rules, case.record["asset_snapshot"], as_of(case))
    assert (
        first.computed["latest_engine_flight_cycles"]
        <= later.computed["latest_engine_flight_cycles"]
    )


def test_not_yet_effective_requires_nothing_yet() -> None:
    result = screen_rules(BLADE, blade_engine(), date(2026, 9, 1))
    assert result.authority_state == "published_not_yet_effective"
    assert result.action_status == "no_action_triggered"


def test_reference_rules_match_s1_except_where_s1_follows_the_faa_answer() -> None:
    record = build_record(
        (
            REPO / "tests/fixtures/federal-register/2025-18469/full-text.xml"
        ).read_bytes(),
        REPO / "generations/gen-20260926T215105Z-7fe9da08",
    )
    for unit in s1_units():
        asset = unit.record["asset_snapshot"]
        s1 = screen(record, asset, as_of(unit))
        general = screen_rules(HUB, asset, as_of(unit))
        if unit.name == "seed-005":
            assert general.action_status == "needs_review"
            assert set(general.computed["readings"]) == {"A", "B"}
            continue
        assert (general.applicability, general.action_status, general.computed) == (
            s1.applicability,
            s1.action_status,
            s1.computed,
        ), unit.name


def s1_units():
    cases = [c.record for c in load_seed_cases(REPO / "evaluation/seed/cases")]
    return [u for u in units(cases) if u.in_s1]


def as_of(unit) -> date:
    return date.fromisoformat(unit.record["source_snapshot"]["as_of"])
