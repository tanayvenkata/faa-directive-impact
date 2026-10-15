"""The serial guard rejects identifiers a directive's own text does not print."""

import copy
import json
from pathlib import Path

import pytest

from faa_directive_impact.rules.serial_guard import (
    IDENTIFIER_KEYS,
    invented_identifiers,
    record_identifiers,
)
from faa_directive_impact.schema_validation import load_schema

REPO = Path(__file__).resolve().parents[2]
CORPUS = json.loads((REPO / "evaluation/retrieval/corpus.json").read_text())
COVERAGE = {
    p.stem: json.loads(p.read_text())
    for p in sorted((REPO / "evaluation/coverage/reference").glob("*.json"))
}
B3 = {
    p.stem: json.loads(p.read_text())
    for p in sorted((REPO / "evaluation/b3/reference").glob("*.json"))
}


@pytest.mark.parametrize("document", sorted(COVERAGE))
def test_every_coverage_reference_prints_only_its_own_identifiers(document) -> None:
    assert invented_identifiers(COVERAGE[document], CORPUS) == []


@pytest.mark.parametrize("document", sorted(B3))
def test_the_v1_references_pass_too(document) -> None:
    assert invented_identifiers(B3[document], CORPUS) == []


def test_a_transposed_digit_is_rejected() -> None:
    record = copy.deepcopy(COVERAGE["2019-19412"])
    record["parts"][0]["listed"][0]["serial_number"] = "MAP04285"
    assert invented_identifiers(record, CORPUS) == [
        ("parts[0].listed[0].serial_number", "MAP04285")
    ]


def test_a_real_serial_from_another_directive_is_rejected() -> None:
    record = copy.deepcopy(COVERAGE["2020-07627"])
    record["parts"][1]["listed"].append(
        {
            "part_number": "2A5001",
            "serial_number": "PKLBSK9287",
            "cycles_since_new_limit": None,
        }
    )  # listed in AD 2025-19-13, not in AD 2020-07-51
    assert invented_identifiers(record, CORPUS) == [
        ("parts[1].listed[3].serial_number", "PKLBSK9287")
    ]


def test_engine_serial_bounds_and_exclusions_are_checked() -> None:
    record = copy.deepcopy(COVERAGE["2015-12068"])
    condition = record["applicability"]["engine_serials"][0]
    condition["ranges"][0]["last"] = "V13191"
    condition["excluded"].append("V16708")
    assert {value for _, value in invented_identifiers(record, CORPUS)} == {
        "V13191",
        "V16708",
    }


def test_an_invented_part_number_is_rejected() -> None:
    record = copy.deepcopy(COVERAGE["2013-08448"])
    record["parts"][0]["part_numbers"] = ["2A2074-02"]
    assert ("parts[0].part_numbers[0]", "2A2074-02") in invented_identifiers(
        record, CORPUS
    )


def test_a_document_missing_from_the_corpus_confirms_nothing() -> None:
    record = copy.deepcopy(COVERAGE["2019-19412"])
    record["final_rule_document"] = record["governing_document"]["document"] = (
        "1999-99999"
    )
    assert len(invented_identifiers(record, CORPUS)) == len(
        list(record_identifiers(record))
    )


def test_every_identifier_field_of_schema_v2_is_walked() -> None:
    """A new schema field holding serials or part numbers must use a guarded name."""
    names: set[str] = set()

    def walk(node):
        if isinstance(node, dict):
            for key, value in node.get("properties", {}).items():
                names.add(key)
                walk(value)
            for value in node.values():
                if isinstance(value, (dict, list)):
                    walk(value)
        elif isinstance(node, list):
            for item in node:
                walk(item)

    walk(load_schema("rule-record-v2.schema.json"))
    suspicious = {
        n
        for n in names
        if any(word in n for word in ("serial", "part_number", "models"))
    }
    assert suspicious <= IDENTIFIER_KEYS | {
        "engine_serials",
        "serials",
        "models_paragraph",
    }
