import hashlib
import json
from pathlib import Path

import pytest
from fakes import directive_xml, graphic_bytes, make_pdf

from faa_directive_impact.acquisition.validation import validate_artifact

DOC = "2025-18469"
PDF_URL = "https://www.govinfo.gov/content/pkg/FR-2025-09-24/pdf/2025-18469.pdf"


def store(
    tmp_path: Path,
    role: str,
    body: bytes,
    *,
    identity: str = DOC,
    resolved_url: str = "https://www.federalregister.gov/x",
    graphic: str | None = None,
) -> dict:
    relative = f"raw/{role}"
    (tmp_path / "raw").mkdir(exist_ok=True)
    (tmp_path / relative).write_bytes(body)
    receipt = {
        "receipt_id": f"receipt-{role}",
        "source_document_identity": {
            "namespace": "federal_register_document_number",
            "value": identity,
        },
        "representation_role": role,
        "request": {
            "method": "GET",
            "requested_url": resolved_url,
            "resolved_url": resolved_url,
        },
        "artifact": {
            "relative_path": relative,
            "byte_length": len(body),
            "sha256": hashlib.sha256(body).hexdigest(),
        },
    }
    if graphic:
        receipt["source_graphic_identifier"] = graphic
    return receipt


def failures(validation) -> dict[str, str]:
    return {
        finding.check: finding.reason_code
        for finding in validation.findings
        if not finding.passed
    }


def api_body(**changes) -> bytes:
    record = {"document_number": DOC, "type": "Rule", "publication_date": "2025-09-24"}
    record.update(changes)
    return json.dumps(record).encode()


def test_additive_api_fields_pass(tmp_path: Path) -> None:
    receipt = store(tmp_path, "api_json", api_body(brand_new_field={"x": 1}))

    assert failures(validate_artifact(receipt, tmp_path, DOC)) == {}


@pytest.mark.parametrize(
    ("body", "check", "reason"),
    [
        (b"{not json", "json_wellformed", "malformed_json"),
        (api_body(type=None), "required_fields", "missing_required_field"),
        (
            api_body(document_number="2025-10764"),
            "document_identity",
            "identity_mismatch",
        ),
    ],
)
def test_api_json_failures(
    tmp_path: Path, body: bytes, check: str, reason: str
) -> None:
    receipt = store(tmp_path, "api_json", body)

    assert failures(validate_artifact(receipt, tmp_path, DOC))[check] == reason


def test_tampered_bytes_fail_integrity(tmp_path: Path) -> None:
    receipt = store(tmp_path, "api_json", api_body())
    (tmp_path / receipt["artifact"]["relative_path"]).write_bytes(api_body(x=1))

    assert failures(validate_artifact(receipt, tmp_path, DOC))["sha256"] == (
        "integrity_mismatch"
    )


def test_deleted_artifact_is_unreadable(tmp_path: Path) -> None:
    receipt = store(tmp_path, "api_json", api_body())
    (tmp_path / receipt["artifact"]["relative_path"]).unlink()

    assert failures(validate_artifact(receipt, tmp_path, DOC)) == {
        "readable": "unreadable_artifact"
    }


def test_xml_failures(tmp_path: Path) -> None:
    malformed = store(tmp_path, "full_text_xml", b"<RULE><P></RULE>")
    assert failures(validate_artifact(malformed, tmp_path, DOC))["xml_wellformed"] == (
        "malformed_xml"
    )

    other = store(tmp_path, "full_text_xml", directive_xml("2025-10764"))
    assert failures(validate_artifact(other, tmp_path, DOC)) == {
        "document_identity": "identity_mismatch"
    }


def test_xml_entity_expansion_is_rejected(tmp_path: Path) -> None:
    hostile = (
        b'<?xml version="1.0"?><!DOCTYPE r [<!ENTITY a "aaaa">'
        b'<!ENTITY b "&a;&a;&a;&a;">]><RULE>&b;</RULE>'
    )
    receipt = store(tmp_path, "full_text_xml", hostile)

    assert failures(validate_artifact(receipt, tmp_path, DOC))["xml_wellformed"] == (
        "malformed_xml"
    )


def test_missing_incorporation_paragraph_is_undetermined(tmp_path: Path) -> None:
    body = f"<RULE><FRDOC>[FR Doc. {DOC} Filed]</FRDOC></RULE>".encode()
    receipt = store(tmp_path, "full_text_xml", body)

    assert failures(validate_artifact(receipt, tmp_path, DOC)) == {
        "incorporated_material": "incorporated_material_undetermined"
    }


def test_pdf_checks(tmp_path: Path) -> None:
    good = store(
        tmp_path,
        "official_pdf",
        make_pdf("[FR Doc. 2025\u201318469 Filed 9\u201323\u201325]"),
        identity=f"FR-2025-09-24/{DOC}",
        resolved_url=PDF_URL,
    )
    assert failures(validate_artifact(good, tmp_path, DOC)) == {}

    neighbour_only = store(
        tmp_path,
        "official_pdf",
        make_pdf("[FR Doc. 2025\u201318528 Filed] see 2025-18469"),
        identity=f"FR-2025-09-24/{DOC}",
        resolved_url=PDF_URL,
    )
    assert failures(validate_artifact(neighbour_only, tmp_path, DOC)) == {
        "document_identity": "identity_mismatch"
    }

    truncated = store(
        tmp_path,
        "official_pdf",
        b"%PDF-1.7\n1 0 obj",
        identity=f"FR-2025-09-24/{DOC}",
        resolved_url=PDF_URL,
    )
    assert failures(validate_artifact(truncated, tmp_path, DOC)) == {
        "pdf_readable": "unreadable_pdf"
    }


def test_html_served_as_pdf_fails_media_type(tmp_path: Path) -> None:
    receipt = store(
        tmp_path,
        "official_pdf",
        b"<html>maintenance</html>",
        identity=f"FR-2025-09-24/{DOC}",
        resolved_url=PDF_URL,
    )

    assert failures(validate_artifact(receipt, tmp_path, DOC))["media_type"] == (
        "media_type_mismatch"
    )


def test_govinfo_granule_must_match_served_url(tmp_path: Path) -> None:
    receipt = store(
        tmp_path,
        "official_pdf",
        make_pdf(f"[FR Doc. {DOC} Filed]"),
        identity=f"FR-2025-01-01/{DOC}",
        resolved_url=PDF_URL,
    )

    assert failures(validate_artifact(receipt, tmp_path, DOC)) == {
        "govinfo_identity": "govinfo_identity_mismatch"
    }


def test_undecodable_text_fails(tmp_path: Path) -> None:
    receipt = store(tmp_path, "plain_text", b"\xff\xfe FR Doc")

    assert failures(validate_artifact(receipt, tmp_path, DOC)) == {
        "text_decodable": "undecodable_text"
    }


def test_graphic_must_match_source_metadata(tmp_path: Path) -> None:
    body = graphic_bytes("ER24SE25.000")
    receipt = store(tmp_path, "original_graphic", body, graphic="ER24SE25.000")
    api_record = {
        "images_metadata": {
            "ER24SE25.000": {"original_size": {"size": len(body), "sha": "0" * 32}}
        }
    }

    assert failures(validate_artifact(receipt, tmp_path, DOC, api_record)) == {
        "graphic_metadata": "graphic_metadata_mismatch"
    }
