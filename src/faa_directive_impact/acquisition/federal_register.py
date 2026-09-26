"""Federal Register and GovInfo representation requests for one document."""

import re
from dataclasses import dataclass
from pathlib import PurePosixPath
from typing import Any, TypeGuard
from urllib.parse import urlparse

from faa_directive_impact.acquisition.retrieval import (
    ExpectedArtifact,
    RepresentationRequest,
)

API_BASE_URL = "https://www.federalregister.gov/api/v1"
DOCUMENT_NUMBER_PATTERN = re.compile(r"^\d{4}-\d{5}$")
PUBLICATION_DATE_PATTERN = re.compile(r"^\d{4}-\d{2}-\d{2}$")
GRAPHIC_IDENTIFIER_PATTERN = re.compile(r"^[A-Za-z0-9][A-Za-z0-9._-]*$")
DOCUMENT_NAMESPACE = "federal_register_document_number"
GOVINFO_NAMESPACE = "govinfo_package_granule"
# See REDISTRIBUTION.md. Text is a U.S. Government work; a figure may reproduce
# third-party material, so graphics are reviewed per document.
TEXT_REDISTRIBUTION = (
    "permitted",
    "U.S. Government work, 17 U.S.C. 105; GovInfo policy permits reprinting "
    "with credit to the issuing agency (FAA). See REDISTRIBUTION.md.",
)
GRAPHIC_REDISTRIBUTION = (
    "review_required",
    "Document graphics may reproduce third-party copyrighted material; "
    "reviewed per document. See REDISTRIBUTION.md.",
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
    unresolved: list[ExpectedArtifact]


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
        redistribution_status=TEXT_REDISTRIBUTION[0],
        redistribution_basis=TEXT_REDISTRIBUTION[1],
    )


def resolve_representations(
    api_record: dict[str, Any], document_number: str, run_id: str
) -> ResolvedRepresentations:
    """Resolve every expected representation URL from an API JSON record.

    A representation whose URL is absent or unusable is reported in
    ``unresolved`` rather than guessed.
    """
    _require_document_number(document_number)
    requests: list[RepresentationRequest] = []
    unresolved: list[ExpectedArtifact] = []
    publication_date = api_record.get("publication_date")
    granule = (
        f"FR-{publication_date}/{document_number}"
        if isinstance(publication_date, str)
        and PUBLICATION_DATE_PATTERN.fullmatch(publication_date)
        else None
    )

    for field, system, role, authority, file_name in _DOCUMENT_REPRESENTATIONS:
        url = api_record.get(field)
        if system == "govinfo" and granule is not None:
            namespace, identity = GOVINFO_NAMESPACE, granule
        else:
            namespace, identity = DOCUMENT_NAMESPACE, document_number
        if not _is_https_url(url) or (system == "govinfo" and granule is None):
            unresolved.append(ExpectedArtifact(namespace, identity, role))
            continue
        if system == "govinfo":
            parent = (DOCUMENT_NAMESPACE, document_number)
            directory = f"raw/govinfo/{document_number}/{run_id}"
        else:
            parent = None
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
                redistribution_status=TEXT_REDISTRIBUTION[0],
                redistribution_basis=TEXT_REDISTRIBUTION[1],
                parent_identity=parent,
            )
        )

    images = api_record.get("images") or {}
    if not isinstance(images, dict):
        unresolved.append(
            ExpectedArtifact(DOCUMENT_NAMESPACE, document_number, "original_graphic")
        )
        images = {}
    for identifier in sorted(images):
        sizes = images[identifier]
        url = sizes.get("original_size") if isinstance(sizes, dict) else None
        if not GRAPHIC_IDENTIFIER_PATTERN.fullmatch(identifier) or not _is_https_url(
            url
        ):
            unresolved.append(
                ExpectedArtifact(
                    DOCUMENT_NAMESPACE, document_number, "original_graphic", identifier
                )
            )
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
                redistribution_status=GRAPHIC_REDISTRIBUTION[0],
                redistribution_basis=GRAPHIC_REDISTRIBUTION[1],
                parent_identity=(DOCUMENT_NAMESPACE, document_number),
                source_graphic_identifier=identifier,
            )
        )
    return ResolvedRepresentations(requests, unresolved)


def expected_without_metadata(document_number: str) -> list[ExpectedArtifact]:
    """Return the fixed expected matrix when the API record is unusable.

    GovInfo granule identity needs the publication date, so these cells fall
    back to the Federal Register document identity. Graphics cannot be
    enumerated without the record.
    """
    return [
        ExpectedArtifact(DOCUMENT_NAMESPACE, document_number, role)
        for _, _, role, _, _ in _DOCUMENT_REPRESENTATIONS
    ]


def _require_document_number(document_number: str) -> None:
    if not DOCUMENT_NUMBER_PATTERN.fullmatch(document_number):
        raise ValueError(f"invalid Federal Register document number: {document_number}")


def _url_extension(url: str) -> str:
    suffix = PurePosixPath(urlparse(url).path).suffix.lstrip(".").lower()
    return suffix if suffix.isalnum() and len(suffix) <= 5 else "bin"


def _is_https_url(value: Any) -> TypeGuard[str]:
    return isinstance(value, str) and value.startswith("https://")


FAA_DOCKET_PATTERN = re.compile(r"^Docket No\. (FAA-\d{4}-\d+)$")
AIRWORTHINESS_DIRECTIVE_PATTERN = re.compile(r"^AD (\d{4}-\d{2}-\d{2})$")


def faa_docket_numbers(api_record: dict[str, Any]) -> set[str]:
    """Return FAA docket numbers the record lists, such as ``FAA-2025-0926``."""
    return _docket_matches(api_record, FAA_DOCKET_PATTERN)


def airworthiness_directive_numbers(api_record: dict[str, Any]) -> set[str]:
    """Return AD numbers the record lists, such as ``2025-19-13``."""
    return _docket_matches(api_record, AIRWORTHINESS_DIRECTIVE_PATTERN)


def _docket_matches(api_record: dict[str, Any], pattern: re.Pattern) -> set[str]:
    docket_ids = api_record.get("docket_ids")
    if not isinstance(docket_ids, list):
        return set()
    return {
        match.group(1)
        for entry in docket_ids
        if isinstance(entry, str) and (match := pattern.fullmatch(entry.strip()))
    }
