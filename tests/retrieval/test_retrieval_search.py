from datetime import date

from defusedxml import ElementTree

from faa_directive_impact.retrieval.corpus import (
    applicability_models,
    identifiers,
    regulatory_identifiers,
)
from faa_directive_impact.retrieval.search import VIA_MODEL, VIA_PART_NUMBER, retrieve

XML = b"""<RULE><PREAMB><P>Discussion mentions P/N 9Z9999.</P></PREAMB>
<HD>(a) Effective Date</HD><P>This AD is effective October 29, 2025.</P>
<HD>(c) Applicability</HD>
<P>This AD applies to IAE Model V2522-A5 and V2527- A5 engines with a
3rd stage blade, part number (P/N) 6A8353.</P>
<HD>(g) Required Actions</HD><P>Replace P/N 6A8353 with P/N 6C8368.</P>
<GPOTABLE><ROW><ENT>2A5001</ENT><ENT>PKLBST5011</ENT></ROW></GPOTABLE>
</RULE>"""


def _record(number, published, models, identifiers_by_paragraph, links=()):
    return {
        "document": number,
        "kind": "final_rule",
        "title": number,
        "publication_date": published,
        "applicability_models": models,
        "identifiers": identifiers_by_paragraph,
        "relationships": list(links),
    }


def _asset(model, *parts):
    return {
        "engine": {"engine_model": model},
        "installed_components": [{"part_number": part} for part in parts],
    }


def test_regulatory_identifiers_skip_the_preamble_and_read_tables():
    root = ElementTree.fromstring(XML)
    tokens = regulatory_identifiers(root)
    assert "9Z9999" not in tokens
    assert tokens["6A8353"] == ["(c)", "(g)"]
    assert tokens["2A5001"] == ["(g)"]
    assert "V2527-A5" in applicability_models(root)


def test_identifiers_need_a_digit_and_four_characters():
    assert identifiers("P/N ABCD or 12 or 2A5001") == {"2A5001"}


def test_model_match_and_part_number_match_are_both_candidates():
    records = [
        _record("A", "2025-01-01", ["V2527-A5"], {}),
        _record("B", "2025-01-01", ["CFM56-5B4/3"], {"2A5001": ["(g)"]}),
        _record("C", "2025-01-01", ["CFM56-5B4/3"], {}),
    ]
    found = retrieve(records, _asset("V2527-A5", "2A5001"), date(2025, 6, 1))
    assert [(c["document"], c["via"]) for c in found] == [
        ("B", VIA_PART_NUMBER),
        ("A", VIA_MODEL),
    ]


def test_documents_published_after_the_as_of_date_are_not_retrieved():
    records = [_record("A", "2026-08-20", ["V2527-A5"], {})]
    assert retrieve(records, _asset("V2527-A5"), date(2026, 8, 19)) == []


def test_a_retrieved_final_brings_its_published_correction():
    final = _record(
        "F", "2026-08-20", ["V2527-A5"], {},
        [{"type": "corrects", "direction": "from", "document": "K"}],
    )  # fmt: skip
    correction = _record(
        "K", "2026-09-10", [], {},
        [{"type": "corrects", "direction": "to", "document": "F"}],
    )  # fmt: skip
    found = retrieve([final, correction], _asset("V2527-A5"), date(2026, 10, 1))
    assert {c["document"] for c in found} == {"F", "K"}
    assert (
        retrieve([final, correction], _asset("V2527-A5"), date(2026, 9, 1))[0][
            "document"
        ]
        == "F"
    )


def test_unknown_or_malformed_query_fields_never_crash():
    records = [_record("A", "2025-01-01", ["V2527-A5"], {"2A5001": ["(g)"]})]
    assert (
        retrieve(records, {"engine": {}, "installed_components": []}, date(2025, 6, 1))
        == []
    )
    asset = {
        "engine": {"engine_model": None},
        "installed_components": [{"part_number": "unknown"}, {"part_number": 7}, {}],
    }
    assert retrieve(records, asset, date(2025, 6, 1)) == []
