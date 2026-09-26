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


HPT_CASES = [
    case
    for case in load_seed_cases(REPO / "evaluation/seed/cases")
    if case.record["directive_candidates"] == [DIRECTIVE]
]


@pytest.mark.parametrize("case", HPT_CASES, ids=lambda case: case.record["case_id"])
def test_seed_label_matches_reference_derivation(case, facts) -> None:
    (expected,) = case.record["expected"]
    derivation = derive(case.record["asset_snapshot"], facts)

    assert derivation.classification == expected["classification"]
    assert set(expected.get("required_missing_facts", [])) >= set(
        derivation.missing_facts
    )
    computed = expected.get("computed", {})
    if "latest_engine_flight_cycles" in computed:
        assert (
            derivation.latest_engine_flight_cycles
            == computed["latest_engine_flight_cycles"]
        )
    if "component_cycles_remaining" in computed:
        assert (
            derivation.component_cycles_remaining
            == computed["component_cycles_remaining"]
        )
    if "readings" in computed:
        assert derivation.readings == computed["readings"]
    if case.record["label"]["provenance"] == "expert_required":
        assert derivation.readings_diverge
