"""Acquire and validate every expected representation of one document."""

from dataclasses import dataclass, field
from typing import Any

from faa_directive_impact.acquisition.directive_sections import IncorporatedMaterial
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
from faa_directive_impact.acquisition.validation import (
    ArtifactValidation,
    validate_artifact,
)
from faa_directive_impact.acquisition.versions import VersionIndex, VersionObservation


@dataclass
class DocumentAcquisition:
    """Expected cells, receipts, gaps, validation, and version outcomes."""

    document_number: str
    run_id: str
    api_record: dict[str, Any] | None = None
    api_receipt_id: str | None = None
    expected: list[ExpectedArtifact] = field(default_factory=list)
    receipts: list[dict[str, Any]] = field(default_factory=list)
    missing: list[dict[str, Any]] = field(default_factory=list)
    problems: list[str] = field(default_factory=list)
    validations: list[ArtifactValidation] = field(default_factory=list)
    versions: list[VersionObservation] = field(default_factory=list)
    incorporated_material: IncorporatedMaterial | None = None
    replaced_ads: tuple[str, ...] = ()
    full_text_xml_receipt_id: str | None = None

    @property
    def validated(self) -> bool:
        return all(validation.passed for validation in self.validations)

    @property
    def failed(self) -> bool:
        return bool(self.missing or self.problems) or not self.validated

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

    Each retained artifact is validated immediately; only artifacts that pass
    become logical versions. Nothing is inferred when the API record is
    unavailable or fails validation: every expected cell is recorded as missing
    against the API receipt and the document stops there.
    """
    result = DocumentAcquisition(document_number, context.run_id)
    api_request = api_json_request(document_number, context.run_id)
    api_receipt = retrieve(context, api_request)
    result.receipts.append(api_receipt)
    result.api_receipt_id = api_receipt["receipt_id"]
    result.expected.append(api_request.expected)

    api_validation = None
    if api_receipt["acquisition_status"] == "succeeded":
        api_validation = _validate(context, result, api_receipt, versions)
    api_record = api_validation.api_record if api_validation else None
    if api_validation is None or not api_validation.passed or api_record is None:
        result.problems.append(
            "api_json_unavailable" if api_validation is None else "api_json_invalid"
        )
        result.expected.extend(expected_without_metadata(document_number))
        for cell in result.expected:
            result.mark_missing(cell, "acquisition_failed", result.api_receipt_id)
        return result

    result.api_record = api_record
    resolved = resolve_representations(api_record, document_number, context.run_id)
    for cell in resolved.unresolved:
        result.expected.append(cell)
        result.mark_missing(cell, "not_published", None)
    for request in resolved.requests:
        result.expected.append(request.expected)
        receipt = retrieve(context, request)
        result.receipts.append(receipt)
        if receipt["acquisition_status"] != "succeeded":
            result.mark_missing(
                request.expected, "acquisition_failed", receipt["receipt_id"]
            )
            continue
        validation = _validate(context, result, receipt, versions)
        if receipt["representation_role"] == "full_text_xml":
            result.incorporated_material = validation.incorporated_material
            result.replaced_ads = validation.replaced_ads
            result.full_text_xml_receipt_id = receipt["receipt_id"]
    return result


def _validate(
    context: AcquisitionContext,
    result: DocumentAcquisition,
    receipt: dict[str, Any],
    versions: VersionIndex,
) -> ArtifactValidation:
    validation = validate_artifact(
        receipt, context.storage.root, result.document_number, result.api_record
    )
    result.validations.append(validation)
    if validation.passed:
        result.versions.append(versions.observe(receipt))
    return validation
