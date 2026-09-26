import pytest

from faa_directive_impact.acquisition.federal_register import (
    airworthiness_directive_numbers,
    api_json_request,
    faa_docket_numbers,
    resolve_representations,
)

RUN_ID = "run-1"


def api_record(**overrides: object) -> dict:
    record = {
        "document_number": "2021-14268",
        "publication_date": "2021-07-02",
        "full_text_xml_url": "https://www.federalregister.gov/x/2021-14268.xml",
        "body_html_url": "https://www.federalregister.gov/h/2021-14268.html",
        "raw_text_url": "https://www.federalregister.gov/t/2021-14268.txt",
        "pdf_url": "https://www.govinfo.gov/content/pkg/FR-2021-07-02/pdf/2021-14268.pdf",
        "mods_url": "https://www.govinfo.gov/metadata/granule/FR-2021-07-02/2021-14268/mods.xml",
        "images": {
            "ER02JY21.001": {
                "large": "https://img.federalregister.gov/ER02JY21.001/ER02JY21.001_large.png",
                "original_size": "https://img.federalregister.gov/ER02JY21.001/ER02JY21.001_original_size.png",
            }
        },
    }
    record.update(overrides)
    return record


def unresolved_roles(resolved) -> set[str]:
    return {cell.representation_role for cell in resolved.unresolved}


def by_role(resolved) -> dict:
    return {request.representation_role: request for request in resolved.requests}


def test_resolves_all_expected_representations() -> None:
    resolved = resolve_representations(api_record(), "2021-14268", RUN_ID)

    roles = by_role(resolved)
    assert set(roles) == {
        "full_text_xml",
        "full_text_html",
        "plain_text",
        "official_pdf",
        "mods_xml",
        "original_graphic",
    }
    assert resolved.unresolved == []
    assert roles["full_text_xml"].authority_role == "structured_parsing_input"
    assert roles["official_pdf"].source_system == "govinfo"
    assert roles["official_pdf"].identity_value == "FR-2021-07-02/2021-14268"
    assert roles["official_pdf"].parent_identity == (
        "federal_register_document_number",
        "2021-14268",
    )
    assert roles["official_pdf"].relative_path == (
        "raw/govinfo/2021-14268/run-1/official.pdf"
    )


def test_graphics_use_original_size_not_large() -> None:
    graphic = by_role(resolve_representations(api_record(), "2021-14268", RUN_ID))[
        "original_graphic"
    ]

    assert graphic.url.endswith("_original_size.png")
    assert graphic.source_graphic_identifier == "ER02JY21.001"
    assert graphic.relative_path == (
        "raw/federal-register/2021-14268/run-1/figures/ER02JY21.001_original.png"
    )


def test_absent_url_is_reported_missing_not_guessed() -> None:
    resolved = resolve_representations(
        api_record(full_text_xml_url=None, pdf_url="http://insecure.test/a.pdf"),
        "2021-14268",
        RUN_ID,
    )

    assert unresolved_roles(resolved) == {"full_text_xml", "official_pdf"}
    assert "full_text_xml" not in by_role(resolved)


def test_unsafe_graphic_identifier_is_reported_missing() -> None:
    images = {"../escape": {"original_size": "https://img.test/a.png"}}

    resolved = resolve_representations(api_record(images=images), "2021-14268", RUN_ID)

    (cell,) = resolved.unresolved
    assert cell.representation_role == "original_graphic"
    assert cell.source_graphic_identifier == "../escape"


def test_govinfo_needs_a_publication_date() -> None:
    resolved = resolve_representations(
        api_record(publication_date=None), "2021-14268", RUN_ID
    )

    assert {"official_pdf", "mods_xml"} <= unresolved_roles(resolved)


def test_document_number_is_validated() -> None:
    with pytest.raises(ValueError):
        api_json_request("../2025-10764", RUN_ID)


def test_docket_and_directive_numbers_come_from_docket_ids() -> None:
    record = {
        "docket_ids": [
            "Docket No. FAA-2025-0926",
            "Project Identifier AD-2025-00200-E",
            "Amendment 39-23153",
            "AD 2025-19-13",
        ]
    }

    assert faa_docket_numbers(record) == {"FAA-2025-0926"}
    assert airworthiness_directive_numbers(record) == {"2025-19-13"}
    assert faa_docket_numbers({"docket_ids": None}) == set()


def test_text_is_redistributable_but_graphics_need_review() -> None:
    roles = by_role(resolve_representations(api_record(), "2021-14268", RUN_ID))

    assert roles["official_pdf"].redistribution_status == "permitted"
    assert roles["full_text_xml"].redistribution_status == "permitted"
    assert roles["original_graphic"].redistribution_status == "review_required"
    assert api_json_request("2021-14268", RUN_ID).redistribution_status == "permitted"
