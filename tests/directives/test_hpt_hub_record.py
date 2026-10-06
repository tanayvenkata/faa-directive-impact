from pathlib import Path

import pytest

from faa_directive_impact.directives.hpt_hub_record import (
    SourceMismatch,
    build_record,
    canonical_json,
    record_hash,
)

REPO = Path(__file__).resolve().parents[2]
XML = REPO / "tests/fixtures/federal-register/2025-18469/full-text.xml"
GENERATION = REPO / "generations/gen-20260926T215105Z-7fe9da08"


@pytest.fixture(scope="module")
def record():
    return build_record(XML.read_bytes(), GENERATION)


def test_record_indexes_every_regulatory_paragraph_with_case_style_ids(
    record,
) -> None:
    assert [p["id"] for p in record["paragraphs"]] == [
        "(a)", "(b)", "(c)", "(d)", "(e)", "(f)", "(g)", "(h)", "(i)",
        "(i)(1)", "(i)(2)", "(i)(2)(i)", "(i)(2)(ii)",
        "(j)", "(j)(1)", "(j)(2)", "(k)", "(l)",
    ]  # fmt: skip
    paragraphs = {p["id"]: p for p in record["paragraphs"]}
    assert paragraphs["(h)"]["heading"] == "Installation Prohibition"
    assert paragraphs["(i)(2)"]["text"].startswith("(2) An “engine shop visit”")


def test_record_reads_dates_models_window_and_table_from_text(record) -> None:
    assert record["effective_date"] == "2025-10-29"
    assert len(record["applicable_models"]) == 10
    assert "V2500-A1" not in record["applicable_models"]
    assert record["grace_flight_cycles_after_effective_date"] == 100
    rows = record["table_1"]["rows"]
    assert len(rows) == 8
    assert rows[0] == {
        "component": "HPT 1st-stage hub",
        "part_number": "2A5001",
        "serial_number": "PKLBSK9287",
        "removal_limit_cycles_since_new": 100,
    }


def test_record_names_its_source_and_hashes_itself(record) -> None:
    assert record["source"]["generation_id"] == GENERATION.name
    assert record["record_sha256"] == record_hash(record)


def test_rebuilding_from_the_same_bytes_is_byte_identical(record) -> None:
    again = build_record(XML.read_bytes(), GENERATION)

    assert canonical_json(again) == canonical_json(record)


def test_builder_refuses_bytes_that_do_not_match_the_receipt() -> None:
    altered = XML.read_bytes().replace(b"PKLBSK9287", b"PKLBSK9288")

    with pytest.raises(SourceMismatch):
        build_record(altered, GENERATION)
