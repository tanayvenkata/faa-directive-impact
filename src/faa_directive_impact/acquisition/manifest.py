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
from faa_directive_impact.schema_validation import validate_raw_generation_manifest

MANIFEST_SCHEMA_VERSION = "1.1.0"
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
    """Return a schema-valid manifest; completeness decides eligibility.

    Eligibility here means only that every expected artifact is present. The
    A6 validation gate adds format and identity checks to that decision.
    """
    expected = []
    for document in documents:
        for cell in document.expected:
            entry = cell.as_record()
            entry["required"] = True
            expected.append(entry)
    missing = [entry for document in documents for entry in document.missing]
    complete = not missing and not any(document.problems for document in documents)
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
        "dependencies": drs_dependencies(documents),
        "missing_artifacts": missing,
        "completeness_status": "complete" if complete else "incomplete",
        "eligible_for_normalization": complete,
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
