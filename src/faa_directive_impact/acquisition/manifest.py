"""Build the raw-generation manifest for one acquisition run."""

from datetime import datetime
from importlib.metadata import version
from itertools import product
from typing import Any

from faa_directive_impact.acquisition.document import DocumentAcquisition
from faa_directive_impact.acquisition.federal_register import (
    DOCUMENT_NAMESPACE,
    airworthiness_directive_numbers,
    faa_docket_numbers,
)
from faa_directive_impact.acquisition.retrieval import format_utc, receipt_path
from faa_directive_impact.schema_validation import (
    validate_raw_generation_manifest,
    validate_validation_report,
)

MANIFEST_SCHEMA_VERSION = "1.1.0"
VALIDATION_SCHEMA_VERSION = "1.0.0"
PROPOSED_RULE = "Proposed Rule"
FINAL_RULE = "Rule"


def build_manifest(
    *,
    generation_id: str,
    created_at: datetime,
    corpus_track: str,
    run_id: str,
    documents: list[DocumentAcquisition],
) -> dict[str, Any]:
    """Return a schema-valid manifest.

    A generation is eligible for normalization only when every expected
    artifact is present and every retained artifact passed validation.
    """
    expected = []
    for document in documents:
        for cell in document.expected:
            entry = cell.as_record()
            entry["required"] = True
            expected.append(entry)
    missing = [entry for document in documents for entry in document.missing]
    complete = not missing and not any(document.problems for document in documents)
    validated = all(document.validated for document in documents)
    manifest = {
        "schema_version": MANIFEST_SCHEMA_VERSION,
        "generation_id": generation_id,
        "created_at_utc": format_utc(created_at),
        "creating_process": {
            "name": "faa-directive-impact",
            "version": version("faa-directive-impact"),
        },
        "corpus_track": corpus_track,
        "acquisition_run_ids": [run_id],
        "expected_artifacts": expected,
        "receipt_references": [
            {
                "receipt_id": receipt["receipt_id"],
                "receipt_relative_path": receipt_path(run_id, receipt["receipt_id"]),
            }
            for document in documents
            for receipt in document.receipts
        ],
        "relationships": proposal_final_relationships(documents),
        "dependencies": incorporated_material_dependencies(documents)
        + drs_dependencies(documents),
        "missing_artifacts": missing,
        "completeness_status": "complete" if complete else "incomplete",
        "eligible_for_normalization": complete and validated,
    }
    validate_raw_generation_manifest(manifest)
    return manifest


def proposal_final_relationships(
    documents: list[DocumentAcquisition],
) -> list[dict[str, Any]]:
    """Link a proposed rule to a final rule that shares an FAA docket number.

    The API does not assert this link directly, so it is an identifier join
    supported by both API JSON receipts, not a source assertion.
    """
    usable = [
        (document, document.api_record)
        for document in documents
        if document.api_record is not None
    ]
    relationships = []
    for (proposal, proposal_record), (final, final_record) in product(usable, usable):
        if (
            proposal_record.get("type") != PROPOSED_RULE
            or final_record.get("type") != FINAL_RULE
            or not faa_docket_numbers(proposal_record)
            & faa_docket_numbers(final_record)
            or str(proposal_record.get("publication_date"))
            > str(final_record.get("publication_date"))
        ):
            continue
        relationships.append(
            {
                "relationship_type": "proposal_final",
                "from_identity": _identity(proposal.document_number),
                "to_identity": _identity(final.document_number),
                "evidence_receipt_ids": [proposal.api_receipt_id, final.api_receipt_id],
                "confidence_class": "identifier_join",
            }
        )
    return relationships


def incorporated_material_dependencies(
    documents: list[DocumentAcquisition],
) -> list[dict[str, Any]]:
    """Record what each directive states about incorporated material.

    Listed material is recorded as unavailable: acquisition never fetches
    manufacturer documents. "None" is recorded explicitly as not required.
    """
    dependencies = []
    for document in documents:
        material = document.incorporated_material
        receipt_id = document.incorporated_material_receipt_id
        if material is None or not material.determined or receipt_id is None:
            continue
        if not material.required:
            dependencies.append(
                {
                    "name": (
                        f"Material incorporated by reference in "
                        f"{document.document_number} paragraph ({material.paragraph})"
                    ),
                    "dependency_type": "incorporated_material",
                    "availability_status": "not_required",
                    "evidence_receipt_ids": [receipt_id],
                }
            )
        for item in material.items:
            dependencies.append(
                {
                    "name": item,
                    "dependency_type": "incorporated_material",
                    "availability_status": "unavailable",
                    "evidence_receipt_ids": [receipt_id],
                }
            )
    return dependencies


def build_validation_report(
    *, generation_id: str, created_at: datetime, documents: list[DocumentAcquisition]
) -> dict[str, Any]:
    """Return the schema-valid findings for every retained artifact."""
    findings = [
        record
        for document in documents
        for validation in document.validations
        for record in validation.records()
    ]
    passed = all(finding["outcome"] == "passed" for finding in findings)
    report = {
        "schema_version": VALIDATION_SCHEMA_VERSION,
        "generation_id": generation_id,
        "created_at_utc": format_utc(created_at),
        "status": "passed" if passed else "failed",
        "findings": findings,
    }
    validate_validation_report(report)
    return report


def drs_dependencies(documents: list[DocumentAcquisition]) -> list[dict[str, Any]]:
    """Record FAA DRS corroboration for each final AD as not yet verifiable."""
    dependencies = []
    for document in documents:
        record = document.api_record
        if not record or record.get("type") != FINAL_RULE:
            continue
        for number in sorted(airworthiness_directive_numbers(record)):
            dependencies.append(
                {
                    "name": f"FAA DRS record for AD {number}",
                    "dependency_type": "source_access",
                    "availability_status": "deferred_access_verification",
                    "evidence_receipt_ids": [document.api_receipt_id],
                }
            )
    return dependencies


def _identity(document_number: str) -> dict[str, str]:
    return {"namespace": DOCUMENT_NAMESPACE, "value": document_number}
