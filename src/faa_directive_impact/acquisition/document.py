"""Acquire every expected representation of one Federal Register document."""

import json
from dataclasses import dataclass, field
from typing import Any

from faa_directive_impact.acquisition.federal_register import (
    api_json_request,
    expected_without_metadata,
    resolve_representations,
)
from faa_directive_impact.acquisition.retrieval import (
    AcquisitionContext,
    ExpectedArtifact,
    retrieve,
)
from faa_directive_impact.acquisition.versions import VersionIndex, VersionObservation


@dataclass
class DocumentAcquisition:
    """Expected cells, receipts, gaps, and version outcomes for one document."""

    document_number: str
    run_id: str
    api_record: dict[str, Any] | None = None
    api_receipt_id: str | None = None
    expected: list[ExpectedArtifact] = field(default_factory=list)
    receipts: list[dict[str, Any]] = field(default_factory=list)
    missing: list[dict[str, Any]] = field(default_factory=list)
    problems: list[str] = field(default_factory=list)
    versions: list[VersionObservation] = field(default_factory=list)

    @property
    def failed(self) -> bool:
        return bool(self.missing or self.problems)

    @property
    def needs_review(self) -> bool:
        return any(version.status == "changed" for version in self.versions)

    def mark_missing(
        self, cell: ExpectedArtifact, reason_code: str, receipt_id: str | None
    ) -> None:
        entry = cell.as_record()
        entry["reason_code"] = reason_code
        if receipt_id is not None:
            entry["receipt_id"] = receipt_id
        self.missing.append(entry)


def acquire_document(
    context: AcquisitionContext, document_number: str, versions: VersionIndex
) -> DocumentAcquisition:
    """Fetch API JSON, resolve representations from it, and fetch each one.

    Nothing is inferred when the API record is unavailable, unreadable, or
    describes a different document: every expected cell is recorded as missing
    against the API receipt and the document stops there.
    """
    result = DocumentAcquisition(document_number, context.run_id)
    api_request = api_json_request(document_number, context.run_id)
    api_receipt = retrieve(context, api_request)
    result.receipts.append(api_receipt)
    result.api_receipt_id = api_receipt["receipt_id"]
    result.expected.append(api_request.expected)

    problem = _api_problem(context, api_receipt, document_number)
    if problem is not None:
        result.problems.append(problem)
        result.expected.extend(expected_without_metadata(document_number))
        for cell in result.expected:
            result.mark_missing(cell, "acquisition_failed", result.api_receipt_id)
        return result

    result.api_record = _read_api_record(context, api_receipt)
    result.versions.append(versions.observe(api_receipt))
    resolved = resolve_representations(
        result.api_record, document_number, context.run_id
    )
    for cell in resolved.unresolved:
        result.expected.append(cell)
        result.mark_missing(cell, "not_published", None)
    for request in resolved.requests:
        result.expected.append(request.expected)
        receipt = retrieve(context, request)
        result.receipts.append(receipt)
        if receipt["acquisition_status"] == "succeeded":
            result.versions.append(versions.observe(receipt))
        else:
            result.mark_missing(
                request.expected, "acquisition_failed", receipt["receipt_id"]
            )
    return result


def _api_problem(
    context: AcquisitionContext, receipt: dict[str, Any], document_number: str
) -> str | None:
    if receipt["acquisition_status"] != "succeeded":
        return "api_json_unavailable"
    try:
        record = _read_api_record(context, receipt)
    except ValueError:
        return "api_json_unreadable"
    if record.get("document_number") != document_number:
        return "api_json_identity_mismatch"
    return None


def _read_api_record(
    context: AcquisitionContext, receipt: dict[str, Any]
) -> dict[str, Any]:
    path = context.storage.resolve(receipt["artifact"]["relative_path"])
    record = json.loads(path.read_bytes())
    if not isinstance(record, dict):
        raise ValueError("API JSON record is not an object")
    return record
