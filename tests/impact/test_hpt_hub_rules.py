"""The S1 rules against the seed and against the reference derivation."""

import copy
from datetime import date
from pathlib import Path

import pytest
from defusedxml import ElementTree

from faa_directive_impact.directives.hpt_hub_record import build_record
from faa_directive_impact.evaluation.hpt_hub_reference import (
    derive,
    read_directive_facts,
)
from faa_directive_impact.evaluation.seed import load_seed_cases
from faa_directive_impact.impact.hpt_hub_rules import screen

REPO = Path(__file__).resolve().parents[2]
XML = REPO / "tests/fixtures/federal-register/2025-18469/full-text.xml"
GENERATION = REPO / "generations/gen-20260926T215105Z-7fe9da08"
DIRECTIVE = "2025-18469"
CASES = {
    case.record["case_id"]: case.record
    for case in load_seed_cases(REPO / "evaluation/seed/cases")
}
S1_CASES = [
    record
    for record in CASES.values()
    if any(o["directive"] == DIRECTIVE for o in record["expected"])
]


@pytest.fixture(scope="module")
def record():
    return build_record(XML.read_bytes(), GENERATION)


@pytest.fixture(scope="module")
def facts():
    return read_directive_facts(ElementTree.fromstring(XML.read_bytes()))


def run(record, case: dict, asset: dict | None = None):
    as_of = date.fromisoformat(case["source_snapshot"]["as_of"])
    return screen(record, asset or case["asset_snapshot"], as_of)


@pytest.mark.parametrize("case", S1_CASES, ids=[c["case_id"] for c in S1_CASES])
def test_rules_agree_with_reference_derivation(record, facts, case) -> None:
    """The rules are a port of the oracle; this guards against drift."""
    as_of = date.fromisoformat(case["source_snapshot"]["as_of"])
    result = run(record, case)
    reference = derive(case["asset_snapshot"], facts, as_of)

    assert result.applicability == reference.applicability
    assert result.action_status == reference.action_status
    assert result.authority_state == reference.authority_state
    assert sorted(result.missing_facts) == sorted(reference.missing_facts)
    assert [o["paragraph"] for o in result.continuing_obligations] == (
        reference.continuing_obligations
    )
    assert result.computed.get("latest_engine_flight_cycles") == (
        reference.latest_engine_flight_cycles
    )
    assert result.computed.get("component_cycles_remaining") == (
        reference.component_cycles_remaining
    )
    assert result.computed.get("readings", {}) == reference.readings


@pytest.mark.parametrize(
    ("part_number", "serial_number", "status"),
    [
        ("2A5001-01", "PKLBSK9287", "needs_review"),
        ("2a5001", "PKLBSK9287", "needs_review"),
        ("2A5001", "pklbsk 9287", "needs_review"),
        ("2A5001", "PKLBSK9288", "no_action_triggered"),
        ("2A5001", "PKLBSK9287-R", "no_action_triggered"),
    ],
)
def test_part_identity_needs_exact_pair_and_never_fuzzy_matches(
    record, facts, part_number, serial_number, status
) -> None:
    asset = {
        "engine": {"engine_model": "V2525-D5"},
        "installed_components": [
            {
                "component_name": "HPT 1st-stage hub",
                "part_number": part_number,
                "serial_number": serial_number,
            },
            {
                "component_name": "HPT 2nd-stage hub",
                "part_number": "2A4802",
                "serial_number": "SYN-HUB2",
            },
        ],
        "events": [],
    }
    result = screen(record, asset, date(2026, 1, 1))

    assert result.action_status == status
    assert result.missing_facts == derive(asset, facts).missing_facts


@pytest.mark.parametrize("case", S1_CASES, ids=[c["case_id"] for c in S1_CASES])
def test_every_answer_cites_the_paragraph_it_rests_on(record, case) -> None:
    result = run(record, case)
    paragraphs = {c.paragraph for c in result.citations}

    assert "(c)" in paragraphs
    if result.action_status == "no_action_triggered":
        assert ("(g)" if result.authority_state == "in_force" else "(a)") in (
            paragraphs
        )
    if result.continuing_obligations:
        assert "(h)" in paragraphs
    if result.computed.get("latest_engine_flight_cycles") is not None:
        assert {"(a)", "(i)(2)"} <= paragraphs
    assert all(c.document == DIRECTIVE for c in result.citations)


def test_operator_record_saying_not_applicable_does_not_clear(record) -> None:
    case = CASES["seed-028"]
    result = run(record, case)

    assert result.action_status == "action_required"
    assert any("operator's AD record" in note for note in result.notes)


def test_unverified_amoc_keeps_the_ad_action_and_is_named(record) -> None:
    result = run(record, CASES["seed-027"])

    assert result.action_status == "action_required"
    assert "amoc_claims[AD 2025-19-13]" in result.missing_facts
    assert "(j)" in {c.paragraph for c in result.citations}
    assert "AMOC could change this deadline" in (result.timing or "")


def test_repair_events_do_not_change_the_outcome(record) -> None:
    case = CASES["seed-026"]
    asset = copy.deepcopy(case["asset_snapshot"])
    asset["events"] = []

    assert (
        run(record, case).to_dict()["computed"]
        == run(record, case, asset).to_dict()["computed"]
    )
    assert run(record, case).action_status == "action_required"


def test_several_listed_hubs_report_the_earliest_deadline(record) -> None:
    result = run(record, CASES["seed-007"])

    assert result.computed["latest_engine_flight_cycles"] == 30800
    assert "earliest deadline is the HPT 1st-stage hub's" in (result.timing or "")


def test_before_effective_date_nothing_is_required_and_no_prohibition_binds(
    record,
) -> None:
    result = run(record, CASES["seed-018"])

    assert result.authority_state == "published_not_yet_effective"
    assert result.action_status == "no_action_triggered"
    assert result.continuing_obligations == []
    assert result.computed == {}


def test_outside_scope_makes_no_determination(record) -> None:
    result = run(record, CASES["seed-010"])

    assert result.applicability == "outside_supported_scope"
    assert result.action_status is None
    assert result.hubs == []
    assert result.queue == "no_action_or_not_applicable"
