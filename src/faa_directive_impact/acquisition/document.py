"""Acquire every expected representation of one Federal Register document."""

import json
from dataclasses import dataclass, field
from typing import Any

from faa_directive_impact.acquisition.federal_register import (
    api_json_request,
    resolve_representations,
)
from faa_directive_impact.acquisition.retrieval import AcquisitionContext, retrieve
from faa_directive_impact.acquisition.versions import VersionIndex, VersionObservation


@dataclass
class DocumentAcquisition:
    """Receipts, unresolved representations, and version outcomes for one run."""

    document_number: str
    run_id: str
    receipts: list[dict[str, Any]] = field(default_factory=list)
    missing: list[str] = field(default_factory=list)
    problems: list[str] = field(default_factory=list)
    versions: list[VersionObservation] = field(default_factory=list)

    @property
    def failed(self) -> bool:
        return bool(self.missing or self.problems) or any(
            receipt["acquisition_status"] != "succeeded" for receipt in self.receipts
        )

    @property
    def needs_review(self) -> bool:
        return any(version.status == "changed" for version in self.versions)

    def as_record(self) -> dict[str, Any]:
        return {
            "document_number": self.document_number,
            "acquisition_run_id": self.run_id,
            "receipt_ids": [receipt["receipt_id"] for receipt in self.receipts],
            "failed_receipt_ids": [
                receipt["receipt_id"]
                for receipt in self.receipts
                if receipt["acquisition_status"] != "succeeded"
            ],
            "missing_representations": self.missing,
            "problems": self.problems,
            "versions": [version.as_record() for version in self.versions],
            "needs_review": self.needs_review,
        }


def acquire_document(
    context: AcquisitionContext, document_number: str, versions: VersionIndex
) -> DocumentAcquisition:
    """Fetch API JSON, resolve representations from it, and fetch each one.

    Nothing is inferred when the API record is unavailable, unreadable, or
    describes a different document; the run records the problem and stops.
    """
    result = DocumentAcquisition(document_number, context.run_id)
    api_receipt = retrieve(context, api_json_request(document_number, context.run_id))
    result.receipts.append(api_receipt)
    if api_receipt["acquisition_status"] != "succeeded":
        result.problems.append("api_json_unavailable")
        return result

    api_path = context.storage.resolve(api_receipt["artifact"]["relative_path"])
    try:
        api_record = json.loads(api_path.read_bytes())
    except ValueError:
        result.problems.append("api_json_unreadable")
        return result
    if not isinstance(api_record, dict):
        result.problems.append("api_json_unreadable")
        return result
    if api_record.get("document_number") != document_number:
        result.problems.append("api_json_identity_mismatch")
        return result

    result.versions.append(versions.observe(api_receipt))
    resolved = resolve_representations(api_record, document_number, context.run_id)
    result.missing.extend(resolved.missing)
    for request in resolved.requests:
        receipt = retrieve(context, request)
        result.receipts.append(receipt)
        if receipt["acquisition_status"] == "succeeded":
            result.versions.append(versions.observe(receipt))
    return result
