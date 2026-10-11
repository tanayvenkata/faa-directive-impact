from source_fakes import directive_xml

from faa_directive_impact.discovery.scope import (
    EVALUATED,
    NOT_YET_EVALUATED,
    OUTSIDE_SUPPORTED_SCOPE,
    classify_applicability,
    names_international_aero_engines,
)

FAMILY = (
    "This AD applies to International Aero Engines AG (IAE AG) Model V2522-A5, "
    "V2524-A5, V2525-D5, V2527E-A5, V2531-E5, and V2533-A5 engines."
)


def classify(number: str, applicability: str | None):
    return classify_applicability(
        directive_xml(number, applicability=applicability), number
    )


def test_iae_family_directive_is_not_yet_evaluated():
    decision = classify("2026-16954", FAMILY)

    assert decision.coverage_state == NOT_YET_EVALUATED
    assert not decision.needs_review
    assert "V2527E-A5" in decision.models and "V2531-E5" in decision.models


def test_only_the_evaluated_document_is_evaluated():
    assert classify("2025-18469", FAMILY).coverage_state == EVALUATED


def test_iae_llc_engines_are_outside_scope_from_paragraph_c():
    decision = classify(
        "2026-20000",
        "This AD applies to International Aero Engines, LLC (IAE LLC) Model "
        "PW1124G1-JM, PW1127G-JM, and PW1133G-JM engines.",
    )

    assert decision.coverage_state == OUTSIDE_SUPPORTED_SCOPE
    assert not decision.needs_review


def test_mixed_v2500_variants_go_to_review_not_scope():
    decision = classify(
        "2026-20001",
        "This AD applies to IAE Model V2500-A1, V2527-A5, and V2530-A5 engines.",
    )

    assert decision.coverage_state == OUTSIDE_SUPPORTED_SCOPE
    assert decision.needs_review
    assert "V2500-A1" in decision.detail


def test_missing_applicability_paragraph_goes_to_review():
    decision = classify("2026-20002", None)

    assert decision.needs_review
    assert decision.coverage_state == OUTSIDE_SUPPORTED_SCOPE


def test_hyphen_split_by_a_space_still_reads_as_the_model():
    decision = classify(
        "2026-20003", "This AD applies to IAE AG Model V2524- A5 and V2522-A5 engines."
    )

    assert decision.coverage_state == NOT_YET_EVALUATED
    assert decision.models == ("V2522-A5", "V2524-A5")


def test_unparseable_xml_goes_to_review():
    decision = classify_applicability(b"<RULE><unclosed></RULE>", "2026-20004")

    assert decision.needs_review


def test_title_decides_only_what_is_read_in_full():
    assert names_international_aero_engines(
        "Airworthiness Directives; International Aero Engines AG Engines"
    )
    assert not names_international_aero_engines(
        "Airworthiness Directives; Airbus SAS Airplanes"
    )
