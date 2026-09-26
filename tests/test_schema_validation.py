from copy import deepcopy

import pytest
from jsonschema import ValidationError

from faa_directive_impact.schema_validation import (
    validate_artifact_receipt,
    validate_raw_generation_manifest,
)


@pytest.fixture
def successful_receipt() -> dict:
    return {
        "schema_version": "1.0.0",
        "receipt_id": "receipt-001",
        "acquisition_run_id": "run-001",
        "retrieval_id": "retrieval-001",
        "retrieved_at_utc": "2026-09-01T21:28:24Z",
        "source_system": "federal_register",
        "source_document_identity": {
            "namespace": "federal_register_document_number",
            "value": "2025-10764",
        },
        "representation_role": "full_text_xml",
        "request": {
            "method": "GET",
            "requested_url": "https://www.federalregister.gov/example.xml",
            "resolved_url": "https://www.federalregister.gov/example.xml",
        },
        "response": {
            "status_code": 200,
            "headers": {"content_type": "application/xml"},
        },
        "acquisition_status": "succeeded",
        "artifact": {
            "relative_path": "raw/2025-10764/full-text.xml",
            "byte_length": 20615,
            "sha256": "a" * 64,
            "declared_media_type": "application/xml",
            "detected_media_type": "application/xml",
        },
        "authority_role": "structured_parsing_input",
        "redistribution": {
            "status": "review_required",
            "basis": "Pending recorded source-specific review.",
        },
    }


def test_successful_receipt_requires_artifact(successful_receipt: dict) -> None:
    validate_artifact_receipt(successful_receipt)

    invalid = deepcopy(successful_receipt)
    del invalid["artifact"]

    with pytest.raises(ValidationError):
        validate_artifact_receipt(invalid)


def test_failed_receipt_requires_failure_and_forbids_artifact(
    successful_receipt: dict,
) -> None:
    failed = deepcopy(successful_receipt)
    failed["acquisition_status"] = "failed"
    failed["response"]["status_code"] = 404
    failed["failure"] = {"reason_code": "not_found", "detail": "Source returned 404."}
    del failed["artifact"]

    validate_artifact_receipt(failed)

    failed["artifact"] = successful_receipt["artifact"]
    with pytest.raises(ValidationError):
        validate_artifact_receipt(failed)


def test_network_failure_does_not_invent_http_response(
    successful_receipt: dict,
) -> None:
    failed = deepcopy(successful_receipt)
    failed["acquisition_status"] = "failed"
    failed["failure"] = {
        "reason_code": "network_error",
        "detail": "Connection failed before an HTTP response was received.",
    }
    del failed["artifact"]
    del failed["response"]
    del failed["request"]["resolved_url"]

    validate_artifact_receipt(failed)


def test_receipt_rejects_invalid_hash(successful_receipt: dict) -> None:
    invalid = deepcopy(successful_receipt)
    invalid["artifact"]["sha256"] = "not-a-sha256"

    with pytest.raises(ValidationError):
        validate_artifact_receipt(invalid)


def test_receipt_enforces_representation_semantics(successful_receipt: dict) -> None:
    invalid = deepcopy(successful_receipt)
    invalid["authority_role"] = "official_edition"

    with pytest.raises(ValidationError):
        validate_artifact_receipt(invalid)


def test_receipt_enforces_source_semantics(successful_receipt: dict) -> None:
    invalid = deepcopy(successful_receipt)
    invalid["source_system"] = "govinfo"

    with pytest.raises(ValidationError):
        validate_artifact_receipt(invalid)


def test_receipt_rejects_unsafe_relative_path(successful_receipt: dict) -> None:
    invalid = deepcopy(successful_receipt)
    invalid["artifact"]["relative_path"] = "raw/../outside.xml"

    with pytest.raises(ValidationError):
        validate_artifact_receipt(invalid)


def test_original_graphic_requires_parent_and_identifier(
    successful_receipt: dict,
) -> None:
    invalid = deepcopy(successful_receipt)
    invalid["representation_role"] = "original_graphic"
    invalid["authority_role"] = "document_graphic"

    with pytest.raises(ValidationError):
        validate_artifact_receipt(invalid)


def test_incomplete_manifest_cannot_enter_normalization() -> None:
    manifest = {
        "schema_version": "1.1.0",
        "generation_id": "raw-generation-001",
        "created_at_utc": "2026-09-01T22:00:00Z",
        "corpus_track": "frozen_evaluation",
        "acquisition_run_ids": ["run-001"],
        "expected_artifacts": [
            {
                "source_document_identity": {
                    "namespace": "federal_register_document_number",
                    "value": "2025-10764",
                },
                "representation_role": "full_text_xml",
                "required": True,
            }
        ],
        "receipt_references": [],
        "relationships": [],
        "dependencies": [],
        "missing_artifacts": [
            {
                "source_document_identity": {
                    "namespace": "federal_register_document_number",
                    "value": "2025-10764",
                },
                "representation_role": "full_text_xml",
                "reason_code": "acquisition_failed",
            }
        ],
        "completeness_status": "incomplete",
        "eligible_for_normalization": False,
    }
    validate_raw_generation_manifest(manifest)

    manifest["eligible_for_normalization"] = True
    with pytest.raises(ValidationError):
        validate_raw_generation_manifest(manifest)
