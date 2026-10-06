"""Re-derive every AD 2025-19-13 seed label from the frozen directive text."""

import hashlib
import json
from datetime import date
from pathlib import Path

import pytest
from defusedxml import ElementTree

from faa_directive_impact.evaluation.hpt_hub_reference import (
    derive,
    read_directive_facts,
)
from faa_directive_impact.evaluation.seed import load_seed_cases

REPO = Path(__file__).resolve().parents[2]
FIXTURE = REPO / "tests/fixtures/federal-register/2025-18469/full-text.xml"
GENERATION = REPO / "generations/gen-20260926T215105Z-7fe9da08"
DIRECTIVE = "2025-18469"


def receipt_hash() -> str:
    for path in (GENERATION / "receipts").glob("*/*.json"):
        receipt = json.loads(path.read_text())
        if (
            receipt["representation_role"] == "full_text_xml"
            and receipt["source_document_identity"]["value"] == DIRECTIVE
        ):
            return receipt["artifact"]["sha256"]
    raise AssertionError("no receipt for the directive XML")


@pytest.fixture(scope="module")
def facts():
    return read_directive_facts(ElementTree.fromstring(FIXTURE.read_bytes()))


def test_fixture_is_the_frozen_artifact() -> None:
    assert hashlib.sha256(FIXTURE.read_bytes()).hexdigest() == receipt_hash()


def test_directive_facts_are_read_from_text(facts) -> None:
    assert facts.effective_date == date(2025, 10, 29)
    assert len(facts.applicable_models) == 10
    assert len(facts.rows) == 8
    assert {row.part_number for row in facts.rows} == {"2A5001", "2A4802"}
    limits = {
        row.serial_number: row.removal_limit_cycles_since_new for row in facts.rows
    }
    assert limits["PKLBSK9287"] == 100
    assert limits["PKLBSR2100"] == 6000


HPT_OUTCOMES = [
    (case, outcome)
    for case in load_seed_cases(REPO / "evaluation/seed/cases")
    for outcome in case.record["expected"]
    if outcome["directive"] == DIRECTIVE
]


@pytest.mark.parametrize(
    ("case", "expected"),
    HPT_OUTCOMES,
    ids=[case.record["case_id"] for case, _ in HPT_OUTCOMES],
)
def test_seed_label_matches_reference_derivation(case, expected, facts) -> None:
    as_of = date.fromisoformat(case.record["source_snapshot"]["as_of"])
    derivation = derive(case.record["asset_snapshot"], facts, as_of)

    assert derivation.applicability == expected["applicability"]
    assert derivation.action_status == expected.get("action_status")
    assert derivation.authority_state == expected.get("authority_state", "in_force")
    assert sorted(derivation.missing_facts) == sorted(
        expected.get("required_missing_facts", [])
    )
    assert derivation.continuing_obligations == [
        obligation["paragraph"]
        for obligation in expected.get("continuing_obligations", [])
    ]
    computed = expected.get("computed", {})
    assert derivation.latest_engine_flight_cycles == computed.get(
        "latest_engine_flight_cycles"
    )
    assert derivation.component_cycles_remaining == computed.get(
        "component_cycles_remaining"
    )
    assert derivation.readings == computed.get("readings", {})
    label = case.record["label"]
    if label["provenance"] == "expert_required" and label["status"] != "adjudicated":
        assert derivation.readings_diverge
    if label["status"] == "adjudicated" and derivation.adjudications:
        assert set(derivation.adjudications) == {label["adjudication"]["id"]}


def first_stage_hub_engine(part_number: str, serial_number: str) -> dict:
    return {
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
    }


@pytest.mark.parametrize(
    ("part_number", "serial_number", "missing_fact"),
    [
        ("2A5001-01", "PKLBSK9287", "part_number"),
        ("2A4802", "PKLBSK9287", "part_number"),
        ("2a5001", "PKLBSK9287", "part_number"),
        ("2A5001", "pklbsk 9287", "serial_number"),
    ],
)
def test_listed_serial_under_variant_identity_needs_review(
    facts, part_number, serial_number, missing_fact
) -> None:
    derivation = derive(first_stage_hub_engine(part_number, serial_number), facts)

    assert derivation.action_status == "needs_review"
    assert derivation.missing_facts == [
        f"installed_components[HPT 1st-stage hub].{missing_fact}"
    ]


@pytest.mark.parametrize("serial_number", ["PKLBSK9288", "PKLBSK9287-R"])
def test_serial_that_only_resembles_a_listed_one_is_not_matched(
    facts, serial_number
) -> None:
    derivation = derive(first_stage_hub_engine("2A5001", serial_number), facts)

    assert derivation.action_status == "no_action_triggered"
    assert derivation.missing_facts == []
