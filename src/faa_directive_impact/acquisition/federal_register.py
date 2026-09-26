"""Federal Register and GovInfo representation requests for one document."""

import re
from dataclasses import dataclass
from pathlib import PurePosixPath
from typing import Any, TypeGuard
from urllib.parse import urlparse

from faa_directive_impact.acquisition.retrieval import RepresentationRequest

API_BASE_URL = "https://www.federalregister.gov/api/v1"
DOCUMENT_NUMBER_PATTERN = re.compile(r"^\d{4}-\d{5}$")
PUBLICATION_DATE_PATTERN = re.compile(r"^\d{4}-\d{2}-\d{2}$")
GRAPHIC_IDENTIFIER_PATTERN = re.compile(r"^[A-Za-z0-9][A-Za-z0-9._-]*$")
DOCUMENT_NAMESPACE = "federal_register_document_number"
GOVINFO_NAMESPACE = "govinfo_package_granule"
REDISTRIBUTION_BASIS = (
    "Federal Register publication of a U.S. Government work; retention and "
    "redistribution decision pending the Reproducible checkpoint review."
)

# (API field, source system, representation role, authority role, file name)
_DOCUMENT_REPRESENTATIONS = (
    (
        "full_text_xml_url",
        "federal_register",
        "full_text_xml",
        "structured_parsing_input",
        "full-text.xml",
    ),
    (
        "body_html_url",
        "federal_register",
        "full_text_html",
        "evidence_projection",
        "full-text.html",
    ),
    (
        "raw_text_url",
        "federal_register",
        "plain_text",
        "evidence_projection",
        "full-text.txt",
    ),
    ("pdf_url", "govinfo", "official_pdf", "official_edition", "official.pdf"),
    ("mods_url", "govinfo", "mods_xml", "bibliographic_metadata", "mods.xml"),
)


@dataclass(frozen=True)
class ResolvedRepresentations:
    """Requests resolved from API metadata, plus what could not be resolved."""

    requests: list[RepresentationRequest]
    missing: list[str]


def api_json_request(document_number: str, run_id: str) -> RepresentationRequest:
    """Request the complete API JSON record for one Federal Register document.

    No ``fields[]`` filter is applied; representation discovery needs the full
    record.
    """
    _require_document_number(document_number)
    return RepresentationRequest(
        source_system="federal_register",
        identity_namespace=DOCUMENT_NAMESPACE,
        identity_value=document_number,
        representation_role="api_json",
        authority_role="discovery_metadata",
        url=f"{API_BASE_URL}/documents/{document_number}.json",
        relative_path=f"raw/federal-register/{document_number}/{run_id}/api.json",
        redistribution_status="review_required",
        redistribution_basis=REDISTRIBUTION_BASIS,
    )


def resolve_representations(
    api_record: dict[str, Any], document_number: str, run_id: str
) -> ResolvedRepresentations:
    """Resolve every expected representation URL from an API JSON record.

    A representation whose URL is absent or unusable is reported in
    ``missing`` rather than guessed.
    """
    _require_document_number(document_number)
    requests: list[RepresentationRequest] = []
    missing: list[str] = []
    publication_date = api_record.get("publication_date")
    granule = (
        f"FR-{publication_date}/{document_number}"
        if isinstance(publication_date, str)
        and PUBLICATION_DATE_PATTERN.fullmatch(publication_date)
        else None
    )

    for field, system, role, authority, file_name in _DOCUMENT_REPRESENTATIONS:
        url = api_record.get(field)
        if not _is_https_url(url):
            missing.append(role)
            continue
        if system == "govinfo":
            if granule is None:
                missing.append(role)
                continue
            namespace, identity = GOVINFO_NAMESPACE, granule
            parent = (DOCUMENT_NAMESPACE, document_number)
            directory = f"raw/govinfo/{document_number}/{run_id}"
        else:
            namespace, identity, parent = DOCUMENT_NAMESPACE, document_number, None
            directory = f"raw/federal-register/{document_number}/{run_id}"
        requests.append(
            RepresentationRequest(
                source_system=system,
                identity_namespace=namespace,
                identity_value=identity,
                representation_role=role,
                authority_role=authority,
                url=url,
                relative_path=f"{directory}/{file_name}",
                redistribution_status="review_required",
                redistribution_basis=REDISTRIBUTION_BASIS,
                parent_identity=parent,
            )
        )

    images = api_record.get("images") or {}
    if not isinstance(images, dict):
        missing.append("original_graphic:images")
        images = {}
    for identifier in sorted(images):
        sizes = images[identifier]
        url = sizes.get("original_size") if isinstance(sizes, dict) else None
        if not GRAPHIC_IDENTIFIER_PATTERN.fullmatch(identifier) or not _is_https_url(
            url
        ):
            missing.append(f"original_graphic:{identifier}")
            continue
        extension = _url_extension(url)
        requests.append(
            RepresentationRequest(
                source_system="federal_register",
                identity_namespace=DOCUMENT_NAMESPACE,
                identity_value=document_number,
                representation_role="original_graphic",
                authority_role="document_graphic",
                url=url,
                relative_path=(
                    f"raw/federal-register/{document_number}/{run_id}/figures/"
                    f"{identifier}_original.{extension}"
                ),
                redistribution_status="review_required",
                redistribution_basis=REDISTRIBUTION_BASIS,
                parent_identity=(DOCUMENT_NAMESPACE, document_number),
                source_graphic_identifier=identifier,
            )
        )
    return ResolvedRepresentations(requests, missing)


def _require_document_number(document_number: str) -> None:
    if not DOCUMENT_NUMBER_PATTERN.fullmatch(document_number):
        raise ValueError(f"invalid Federal Register document number: {document_number}")


def _url_extension(url: str) -> str:
    suffix = PurePosixPath(urlparse(url).path).suffix.lstrip(".").lower()
    return suffix if suffix.isalnum() and len(suffix) <= 5 else "bin"


def _is_https_url(value: Any) -> TypeGuard[str]:
    return isinstance(value, str) and value.startswith("https://")
