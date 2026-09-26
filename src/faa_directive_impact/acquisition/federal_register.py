"""Federal Register representation requests."""

import re

from faa_directive_impact.acquisition.retrieval import RepresentationRequest

API_BASE_URL = "https://www.federalregister.gov/api/v1"
DOCUMENT_NUMBER_PATTERN = re.compile(r"^\d{4}-\d{5}$")
REDISTRIBUTION_BASIS = (
    "Federal Register publication of a U.S. Government work; retention and "
    "redistribution decision pending the Reproducible checkpoint review."
)


def api_json_request(document_number: str, run_id: str) -> RepresentationRequest:
    """Request the complete API JSON record for one Federal Register document.

    No ``fields[]`` filter is applied; later representation discovery needs
    the full record.
    """
    if not DOCUMENT_NUMBER_PATTERN.fullmatch(document_number):
        raise ValueError(f"invalid Federal Register document number: {document_number}")
    return RepresentationRequest(
        source_system="federal_register",
        identity_namespace="federal_register_document_number",
        identity_value=document_number,
        representation_role="api_json",
        authority_role="discovery_metadata",
        url=f"{API_BASE_URL}/documents/{document_number}.json",
        relative_path=f"raw/federal-register/{document_number}/{run_id}/api.json",
        redistribution_status="review_required",
        redistribution_basis=REDISTRIBUTION_BASIS,
    )
