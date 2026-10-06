"""The scorer must catch each failure it exists to catch."""

import copy
from datetime import date
from pathlib import Path

import pytest

from faa_directive_impact.directives.hpt_hub_record import build_record
from faa_directive_impact.evaluation.s1_scoring import (
    conclude,
    hand_review_template,
    score_unit,
    summarize,
    units,
)
from faa_directive_impact.evaluation.seed import load_seed_cases
from faa_directive_impact.impact.hpt_hub_rules import screen

REPO = Path(__file__).resolve().parents[2]
XML = REPO / "tests/fixtures/federal-register/2025-18469/full-text.xml"
GENERATION = REPO / "generations/gen-20260926T215105Z-7fe9da08"
UNITS = {
    unit.name: unit
    for unit in units(
        [c.record for c in load_seed_cases(REPO / "evaluation/seed/cases")]
    )
}
S1 = [name for name, unit in UNITS.items() if unit.in_s1]


@pytest.fixture(scope="module")
def record():
    return build_record(XML.read_bytes(), GENERATION)


def output_for(record, name: str) -> dict:
    unit = UNITS[name]
    as_of = date.fromisoformat(unit.record["source_snapshot"]["as_of"])
    return screen(record, unit.record["asset_snapshot"], as_of).to_dict()


def failed(record, name: str, output: dict) -> set[str]:
    gates = score_unit(UNITS[name], output, record)
    return {number for number, gate in gates.items() if not gate["passed"]}


def scored(record, outputs: dict[str, dict] | None = None) -> list[dict]:
    outputs = outputs or {}
    return [
        {
            "unit": name,
            "slice": UNITS[name].record["slice"],
            "severity": UNITS[name].record["severity"],
            "has_action_timing": "action_timing" in UNITS[name].expected,
            "gates": score_unit(
                UNITS[name], outputs.get(name) or output_for(record, name), record
            ),
        }
        for name in S1
    ]


def test_s1_has_the_eighteen_units_gates_md_names() -> None:
    assert len(S1) == 18
    assert "seed-023/2025-18469" in S1


@pytest.mark.parametrize("name", S1)
def test_rules_output_passes_every_mechanical_gate(record, name) -> None:
    assert failed(record, name, output_for(record, name)) == set()


def mutate(record, name: str, change) -> set[str]:
    output = copy.deepcopy(output_for(record, name))
    change(output)
    return failed(record, name, output)


def test_false_clear_trips_gate_1(record) -> None:
    def clear(o):
        o["action_status"] = "no_action_triggered"

    assert "1" in mutate(record, "seed-001", clear)


def test_answer_for_out_of_scope_engine_trips_gate_2(record) -> None:
    def decide(o):
        o["applicability"], o["action_status"] = "applies", "needs_review"

    assert "2" in mutate(record, "seed-010", decide)


def test_settled_answer_without_the_fact_trips_gate_3(record) -> None:
    def settle(o):
        o["action_status"] = "action_required"

    assert "3" in mutate(record, "seed-003", settle)


def test_dropping_a_required_missing_fact_trips_gate_4(record) -> None:
    def drop(o):
        o["missing_facts"] = []

    assert "4" in mutate(record, "seed-008", drop)


@pytest.mark.parametrize(
    ("paragraph", "locator"),
    [("(m)", None), ("(g)", "table 1 row S/N PKLBSX0000"), ("(c)", "table 1")],
)
def test_fabricated_citation_trips_gate_6(record, paragraph, locator) -> None:
    def fabricate(o):
        o["citations"].append(
            {
                "document": "2025-18469",
                "paragraph": paragraph,
                "locator": locator,
                "supports": "",
            }
        )

    assert "6" in mutate(record, "seed-001", fabricate)


def test_citation_to_another_document_trips_gate_6(record) -> None:
    def elsewhere(o):
        o["citations"][0]["document"] = "2026-16954"

    assert "6" in mutate(record, "seed-001", elsewhere)


def test_treating_a_not_yet_effective_ad_as_in_force_trips_gate_7(record) -> None:
    def in_force(o):
        o["authority_state"] = "in_force"

    assert "7" in mutate(record, "seed-018", in_force)


def test_off_by_one_cycle_count_trips_gate_8(record) -> None:
    def off_by_one(o):
        o["computed"]["latest_engine_flight_cycles"] += 1

    assert "8" in mutate(record, "seed-001", off_by_one)


def test_matching_on_part_number_alone_trips_gate_9(record) -> None:
    def flag(o):
        o["action_status"] = "action_required"

    assert {"9", "13"} <= mutate(record, "seed-002", flag)


def test_inexact_match_anywhere_trips_gate_9(record) -> None:
    def inexact(o):
        o["hubs"][0]["serial_number"] = "PKLBST5012"

    assert "9" in mutate(record, "seed-001", inexact)


def test_missing_required_evidence_trips_gate_10(record) -> None:
    def uncite(o):
        o["citations"] = [c for c in o["citations"] if c["paragraph"] != "(c)"]

    assert "10" in mutate(record, "seed-001", uncite)


def test_clear_without_its_clearing_paragraph_trips_gate_10(record) -> None:
    def uncite(o):
        o["citations"] = [c for c in o["citations"] if c["paragraph"] != "(g)"]

    assert "10" in mutate(record, "seed-024", uncite)


def test_needless_escalation_trips_gate_12(record) -> None:
    def escalate(o):
        o["action_status"] = "needs_review"

    assert "12" in mutate(record, "seed-001", escalate)


def test_all_needs_review_system_fails_gate_12_only_on_budget(record) -> None:
    outputs = {}
    for name in S1:
        output = output_for(record, name)
        if output["applicability"] == "applies":
            output["action_status"] = "needs_review"
        outputs[name] = output
    gates = summarize(scored(record, outputs))

    assert gates["12"]["verdict"] == "unresolved"
    assert len(gates["12"]["failed"]) > 1
    assert gates["1"]["verdict"] == "pass"


def test_one_failure_is_unresolved_until_the_label_is_confirmed(record) -> None:
    output = output_for(record, "seed-001")
    output["action_status"] = "no_action_triggered"
    results = scored(record, {"seed-001": output})

    assert summarize(results)["1"]["verdict"] == "unresolved"
    confirmed = summarize(results, frozenset({"seed-001"}))
    assert confirmed["1"]["verdict"] == "fail"


def test_one_needless_escalation_stays_within_budget(record) -> None:
    output = output_for(record, "seed-001")
    output["action_status"] = "needs_review"

    assert summarize(scored(record, {"seed-001": output}))["12"]["verdict"] == "pass"


def test_hand_gates_wait_for_review_and_gate_14_is_not_exercised(record) -> None:
    gates = summarize(scored(record))

    assert gates["5"]["verdict"] == gates["11"]["verdict"] == "pending_hand_review"
    assert gates["14"]["verdict"] == "not_exercised"


def completed_review(record, gate_5="absent", confirmed=True) -> tuple[dict, dict]:
    results = scored(record)
    report = {"run_id": "s1-test", "gate_version": 1, "gates": summarize(results)}
    review = hand_review_template(results)
    review["reviewer"] = "owner"
    review["reviewer_confirmed"] = confirmed
    for entry in review["units"].values():
        entry["gate_5"]["result"] = gate_5
        if entry["gate_11"]["result"] == "":
            entry["gate_11"]["result"] = "consistent"
    return report, review


def test_clean_review_concludes_go(record) -> None:
    report, review = completed_review(record)

    verdict = conclude(report, review)

    assert verdict["decision"] == "go"
    assert verdict["provisional"] is False


def test_unconfirmed_reviewer_makes_the_decision_provisional(record) -> None:
    report, review = completed_review(record, confirmed=False)

    assert conclude(report, review)["provisional"] is True


def test_forbidden_claim_found_by_hand_blocks_go(record) -> None:
    report, review = completed_review(record, gate_5="present")

    assert conclude(report, review)["decision"] == "unresolved"
    confirmed = conclude(report, review, frozenset(S1))
    assert confirmed["decision"] == "fix_or_switch"


def test_aggregate_failure_with_confirmed_labels_concludes_constrain(record) -> None:
    report, review = completed_review(record)
    for name in ("seed-001", "seed-006"):
        report["gates"]["12"]["failed"].append(name)
    report["gates"]["12"]["verdict"] = "fail"

    assert conclude(report, review)["decision"] == "constrain"


def test_incomplete_review_is_refused(record) -> None:
    report, review = completed_review(record)
    review["units"]["seed-001"]["gate_5"]["result"] = ""

    with pytest.raises(ValueError, match="seed-001 gate_5"):
        conclude(report, review)
