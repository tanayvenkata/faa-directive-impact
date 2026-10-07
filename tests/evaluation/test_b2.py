"""B2 prompt freeze, answer conversion, and scoring of model answers."""

import copy
from datetime import date
from pathlib import Path

import pytest
from defusedxml import ElementTree

from faa_directive_impact.directives.hpt_hub_record import (
    build_record,
    index_paragraphs,
)
from faa_directive_impact.evaluation.b2_prompt import (
    INSTRUCTIONS,
    PROMPT_VERSION,
    question,
)
from faa_directive_impact.evaluation.b2_run import adapt
from faa_directive_impact.evaluation.s1_scoring import (
    CitationIndex,
    score_unit,
    units,
)
from faa_directive_impact.evaluation.seed import load_seed_cases

REPO = Path(__file__).resolve().parents[2]
XML = REPO / "tests/fixtures/federal-register/2025-18469/full-text.xml"
GENERATION = REPO / "generations/gen-20260926T215105Z-7fe9da08"
UNITS = {
    u.name: u
    for u in units([c.record for c in load_seed_cases(REPO / "evaluation/seed/cases")])
}

# Every frozen prompt version, oldest first. Changing the instructions or the
# answer schema changes the hash; a new version needs a stated reason and new
# runs, never a quiet edit. The current prompt must be the last entry.
FROZEN_PROMPT_VERSIONS = {
    "b73f8e333bee": "v1, frozen 2026-10-07 after plumbing b2-plumbing-20261007T230103Z",
    "e0a54c1578a5": (
        "v2, format only, after v1's first scored runs: citation document is the "
        "number alone, missing facts split into record_path and description, "
        "listed S/N may be null for part-number-only listings"
    ),
}


def test_prompt_is_frozen() -> None:
    assert PROMPT_VERSION == list(FROZEN_PROMPT_VERSIONS)[-1]


def test_prompt_never_contains_labels_or_adjudications() -> None:
    for unit in UNITS.values():
        text = INSTRUCTIONS + question(
            unit.expected["directive"],
            date.fromisoformat(unit.record["source_snapshot"]["as_of"]),
            unit.record["asset_snapshot"],
        )
        assert unit.record["title"] not in text
        assert unit.expected["reason"] not in text
        assert unit.record["label"]["rationale"] not in text
        for claim in unit.record["forbidden_claims"]:
            assert claim not in text
    assert "faa-informal" not in INSTRUCTIONS
    assert "adjudicat" not in INSTRUCTIONS.lower()


@pytest.fixture(scope="module")
def index() -> CitationIndex:
    record = build_record(XML.read_bytes(), GENERATION)
    index = CitationIndex({})
    index.add_document(
        "2025-18469", index_paragraphs(ElementTree.fromstring(XML.read_bytes()))
    )
    index.tables["2025-18469"] = ("(g)", record["table_1"]["rows"])
    return index


def answer(**changes) -> dict:
    """A model answer for seed-001 that matches the label."""
    base = {
        "applicability": "applies",
        "action_status": "action_required",
        "authority_state": "in_force",
        "summary": "Listed hub installed; removal required.",
        "timing": "Remove at the next engine shop visit, by counter 45,050.",
        "latest_engine_flight_cycles": 45050,
        "component_cycles_remaining": 2400,
        "alternative_readings": [],
        "missing_facts": [],
        "continuing_obligations": [{"paragraph": "(h)", "text": "Do not install."}],
        "matched_parts": [
            {
                "component_name": "HPT 1st-stage hub",
                "installed_part_number": "2A5001",
                "installed_serial_number": "PKLBST5011",
                "listed_part_number": "2A5001",
                "listed_serial_number": "PKLBST5011",
            }
        ],
        "citations": [
            {"document": "2025-18469", "paragraph": p, "locator": None, "supports": ""}
            for p in ("(c)", "(g)", "(i)(2)")
        ],
        "notes": [],
    }
    base.update(changes)
    return base


def failed(unit: str, output, index) -> set[str]:
    gates = score_unit(UNITS[unit], output, index)
    return {n for n, g in gates.items() if not g["passed"]}


def test_correct_answer_passes_every_mechanical_gate(index) -> None:
    assert failed("seed-001", adapt(answer()), index) == set()


def test_answer_converts_to_the_rules_output_shape() -> None:
    output = adapt(answer(action_status="none", applicability="does_not_apply"))

    assert output["action_status"] is None
    assert output["hubs"][0]["table_row"]["serial_number"] == "PKLBST5011"
    assert output["computed"] == {
        "latest_engine_flight_cycles": 45050,
        "component_cycles_remaining": 2400,
    }


def test_alternative_readings_become_computed_readings() -> None:
    readings = [
        {"name": "A", "latest_engine_flight_cycles": 18100, "explanation": ""},
        {"name": "B", "latest_engine_flight_cycles": 18040, "explanation": ""},
    ]

    output = adapt(answer(alternative_readings=readings))

    assert output["computed"]["readings"] == {"A": 18100, "B": 18040}


def test_answer_outside_the_schema_is_no_answer(index) -> None:
    broken = answer()
    del broken["citations"]

    assert adapt(broken) is None
    assert {"1", "8", "10", "12"} <= failed("seed-001", None, index)


def test_no_answer_fails_only_gates_the_unit_is_covered_by(index) -> None:
    gates = score_unit(UNITS["seed-001"], None, index)

    assert gates["2"]["passed"] is True
    assert gates["1"]["passed"] is False
    assert gates["1"]["detail"] == "no_answer"


def test_citation_to_a_document_not_given_is_fabricated(index) -> None:
    cites = answer()["citations"] + [
        {"document": "2026-16954", "paragraph": "(c)", "locator": None, "supports": ""}
    ]

    assert "6" in failed("seed-001", adapt(answer(citations=cites)), index)


def test_preamble_citation_and_quoted_locator_resolve(index) -> None:
    cites = answer()["citations"] + [
        {"document": "2025-18469", "paragraph": "preamble", "locator": None,
         "supports": ""},
        {"document": "2025-18469", "paragraph": "(g)",
         "locator": "Table 1, S/N PKLBST5011", "supports": ""},
    ]  # fmt: skip

    assert failed("seed-001", adapt(answer(citations=cites)), index) == set()


def test_locator_naming_an_unlisted_serial_goes_to_hand_review(index) -> None:
    cites = answer()["citations"] + [
        {"document": "2025-18469", "paragraph": "(g)",
         "locator": "row for S/N PKLBSX9999", "supports": ""},
    ]  # fmt: skip
    gates = score_unit(UNITS["seed-001"], adapt(answer(citations=cites)), index)

    assert gates["6"]["hand_review_locators"] == [
        "2025-18469 (g) row for S/N PKLBSX9999"
    ]


def test_described_missing_facts_go_to_hand_review() -> None:
    gates = score_unit(UNITS["seed-021"], None, CitationIndex({}))

    assert len(gates["4"]["hand_review_facts"]) == 2
    assert all("incorporated material" in f for f in gates["4"]["hand_review_facts"])


def test_clear_for_other_directives_needs_a_regulatory_paragraph() -> None:
    unit = UNITS["seed-023/2025-17066"]
    index = CitationIndex({"2025-17066": {"(g)(1)(i)": "", "preamble": ""}})
    output = adapt(
        answer(
            action_status="no_action_triggered",
            latest_engine_flight_cycles=None,
            component_cycles_remaining=None,
            matched_parts=[],
            citations=[
                {"document": "2025-17066", "paragraph": "preamble",
                 "locator": None, "supports": ""}
            ],
        )
    )  # fmt: skip
    only_preamble = score_unit(unit, output, index)
    cited = copy.deepcopy(output)
    cited["citations"].append(
        {"document": "2025-17066", "paragraph": "(g)(1)(i)", "locator": None,
         "supports": ""}
    )  # fmt: skip

    assert only_preamble["10"]["uncited_clear"] is True
    assert score_unit(unit, cited, index)["10"]["uncited_clear"] is False


def test_version_1_answers_are_scored_under_their_own_schema() -> None:
    v1 = answer(missing_facts=["installed_components[HPT 1st-stage hub].serial_number"])

    assert adapt(v1) is None
    output = adapt(v1, "b73f8e333bee")
    assert output["missing_facts"] == [
        "installed_components[HPT 1st-stage hub].serial_number"
    ]


def test_missing_fact_paths_are_scored_and_descriptions_kept(index) -> None:
    facts = [
        {
            "record_path": "installed_components[HPT 1st-stage hub].serial_number",
            "description": "The hub's S/N is unknown.",
        },
        {"record_path": None, "description": "A document was not provided."},
    ]

    output = adapt(answer(missing_facts=facts))

    assert output["missing_facts"] == [facts[0]["record_path"]]
    assert output["missing_fact_descriptions"] == [f["description"] for f in facts]


def test_citation_document_must_be_a_bare_number() -> None:
    cites = [
        {"document": "Federal Register 2025-18469", "paragraph": "(c)",
         "locator": None, "supports": ""}
    ]  # fmt: skip

    assert adapt(answer(citations=cites)) is None


def test_part_number_only_listing_matches_on_part_number(index) -> None:
    unit = UNITS["seed-023/2026-16954"]
    parts = [
        {
            "component_name": "3rd stage HPC rotor blade set",
            "installed_part_number": "6A8688",
            "installed_serial_number": "not tracked at set level",
            "listed_part_number": "6A8688",
            "listed_serial_number": None,
        }
    ]
    output = adapt(answer(matched_parts=parts))

    assert score_unit(unit, output, CitationIndex({}))["9"]["passed"] is True
