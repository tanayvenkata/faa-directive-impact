"""Validate retained artifacts before a generation may advance.

Each check returns a finding with a bounded reason code on failure. Checks
inspect only what acquisition needs to trust the bytes: integrity, format,
identity, and declared dependencies. They never interpret directive meaning.
"""

import hashlib
import io
import json
import logging
from collections.abc import Callable
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any
from xml.etree.ElementTree import Element

from defusedxml import ElementTree as SafeElementTree
from pypdf import PdfReader

from faa_directive_impact.acquisition.incorporation import (
    IncorporatedMaterial,
    read_incorporated_material,
)
from faa_directive_impact.acquisition.retrieval import detect_media_type

REQUIRED_API_FIELDS = ("document_number", "type", "publication_date")
MARKUP_MEDIA_TYPES = ("text/html", "application/xml")
EXPECTED_MEDIA_TYPES = {
    "api_json": ("application/json",),
    "full_text_xml": ("application/xml",),
    "full_text_html": MARKUP_MEDIA_TYPES,
    "mods_xml": ("application/xml",),
    "official_pdf": ("application/pdf",),
    "original_graphic": ("image/png", "image/jpeg", "image/gif"),
}

DASHES = str.maketrans(dict.fromkeys("\u2010\u2011\u2012\u2013\u2014\u2212", "-"))

# pypdf logs recoverable structure problems as warnings; findings carry them.
logging.getLogger("pypdf").setLevel(logging.ERROR)


@dataclass(frozen=True)
class Finding:
    check: str
    passed: bool
    detail: str
    reason_code: str | None = None


@dataclass
class ArtifactValidation:
    """Findings for one receipt plus anything later stages need from it."""

    receipt: dict[str, Any]
    findings: list[Finding] = field(default_factory=list)
    api_record: dict[str, Any] | None = None
    incorporated_material: IncorporatedMaterial | None = None

    @property
    def passed(self) -> bool:
        return all(finding.passed for finding in self.findings)

    def records(self) -> list[dict[str, Any]]:
        receipt = self.receipt
        base: dict[str, Any] = {
            "receipt_id": receipt["receipt_id"],
            "source_document_identity": receipt["source_document_identity"],
            "representation_role": receipt["representation_role"],
        }
        if "source_graphic_identifier" in receipt:
            base["source_graphic_identifier"] = receipt["source_graphic_identifier"]
        records = []
        for finding in self.findings:
            record = {
                **base,
                "check": finding.check,
                "outcome": "passed" if finding.passed else "failed",
                "detail": finding.detail,
            }
            if finding.reason_code:
                record["reason_code"] = finding.reason_code
            records.append(record)
        return records


def validate_artifact(
    receipt: dict[str, Any],
    storage_root: Path,
    document_number: str,
    api_record: dict[str, Any] | None = None,
) -> ArtifactValidation:
    """Run every check that applies to one successful receipt.

    ``api_record`` supplies expected graphic metadata and GovInfo identity for
    representations resolved from it.
    """
    result = ArtifactValidation(receipt)
    artifact = receipt["artifact"]
    try:
        body = (storage_root / artifact["relative_path"]).read_bytes()
    except OSError as error:
        result.findings.append(
            Finding("readable", False, str(error), "unreadable_artifact")
        )
        return result

    actual = hashlib.sha256(body).hexdigest()
    result.findings.append(
        Finding("sha256", True, "matches receipt")
        if actual == artifact["sha256"] and len(body) == artifact["byte_length"]
        else Finding(
            "sha256", False, f"retained bytes hash to {actual}", "integrity_mismatch"
        )
    )

    role = receipt["representation_role"]
    expected_media = EXPECTED_MEDIA_TYPES.get(role)
    if expected_media is not None:
        detected = detect_media_type(body[:1024])
        result.findings.append(
            Finding("media_type", True, detected)
            if detected in expected_media
            else Finding(
                "media_type",
                False,
                f"detected {detected}, expected one of {', '.join(expected_media)}",
                "media_type_mismatch",
            )
        )

    checker = _ROLE_CHECKS.get(role)
    if checker is not None:
        checker(result, body, document_number, api_record)
    return result


def _check_api_json(
    result: ArtifactValidation,
    body: bytes,
    document_number: str,
    api_record: dict[str, Any] | None,
) -> None:
    try:
        record = json.loads(body)
    except ValueError as error:
        result.findings.append(
            Finding("json_wellformed", False, str(error), "malformed_json")
        )
        return
    if not isinstance(record, dict):
        result.findings.append(
            Finding("json_wellformed", False, "not a JSON object", "malformed_json")
        )
        return
    result.findings.append(Finding("json_wellformed", True, "parsed"))
    absent = [name for name in REQUIRED_API_FIELDS if not record.get(name)]
    result.findings.append(
        Finding("required_fields", True, "present")
        if not absent
        else Finding(
            "required_fields",
            False,
            f"missing {', '.join(absent)}",
            "missing_required_field",
        )
    )
    _identity_finding(
        result, record.get("document_number") == document_number, document_number
    )
    result.api_record = record


def _check_full_text_xml(
    result: ArtifactValidation,
    body: bytes,
    document_number: str,
    api_record: dict[str, Any] | None,
) -> None:
    root = _parse_xml(result, body)
    if root is None:
        return
    frdoc = " ".join("".join(element.itertext()) for element in root.iter("FRDOC"))
    _identity_finding(
        result, f"FR Doc. {document_number} " in f"{frdoc} ", document_number
    )
    material = read_incorporated_material(root)
    result.incorporated_material = material
    if not material.determined:
        result.findings.append(
            Finding(
                "incorporated_material",
                False,
                "no Material Incorporated by Reference paragraph found",
                "incorporated_material_undetermined",
            )
        )
    else:
        stated = f"{len(material.items)} item(s)" if material.required else "None"
        result.findings.append(
            Finding(
                "incorporated_material",
                True,
                f"paragraph ({material.paragraph}) states {stated}",
            )
        )


def _check_mods_xml(
    result: ArtifactValidation,
    body: bytes,
    document_number: str,
    api_record: dict[str, Any] | None,
) -> None:
    if _parse_xml(result, body) is None:
        return
    _identity_finding(result, document_number.encode() in body, document_number)
    _govinfo_identity_finding(result)


def _check_text_representation(
    result: ArtifactValidation,
    body: bytes,
    document_number: str,
    api_record: dict[str, Any] | None,
) -> None:
    try:
        text = body.decode("utf-8")
    except UnicodeDecodeError as error:
        result.findings.append(
            Finding("text_decodable", False, str(error), "undecodable_text")
        )
        return
    result.findings.append(Finding("text_decodable", True, "utf-8"))
    _identity_finding(result, document_number in text, document_number)


def _check_official_pdf(
    result: ArtifactValidation,
    body: bytes,
    document_number: str,
    api_record: dict[str, Any] | None,
) -> None:
    try:
        reader = PdfReader(io.BytesIO(body))
        pages = len(reader.pages)
        text = "".join(page.extract_text() or "" for page in reader.pages)
    except Exception as error:  # pypdf raises many types for damaged files
        result.findings.append(
            Finding("pdf_readable", False, f"{type(error).__name__}", "unreadable_pdf")
        )
        return
    if pages == 0:
        result.findings.append(
            Finding("pdf_readable", False, "no pages", "unreadable_pdf")
        )
        return
    result.findings.append(Finding("pdf_readable", True, f"{pages} page(s)"))
    # The official edition typesets "2025–10764" with an en dash, and a page can
    # also carry a neighbouring document's "FR Doc." line.
    normalized = text.translate(DASHES)
    _identity_finding(
        result, f"FR Doc. {document_number} " in normalized, document_number
    )
    _govinfo_identity_finding(result)


def _check_original_graphic(
    result: ArtifactValidation,
    body: bytes,
    document_number: str,
    api_record: dict[str, Any] | None,
) -> None:
    identifier = result.receipt.get("source_graphic_identifier")
    metadata = ((api_record or {}).get("images_metadata") or {}).get(identifier or "")
    original = metadata.get("original_size") if isinstance(metadata, dict) else None
    if not isinstance(original, dict):
        result.findings.append(
            Finding("graphic_metadata", True, "no source metadata to compare")
        )
        return
    problems = []
    expected_size = original.get("size")
    if isinstance(expected_size, int) and expected_size != len(body):
        problems.append(f"size {len(body)} != {expected_size}")
    expected_md5 = original.get("sha")
    actual_md5 = hashlib.md5(body, usedforsecurity=False).hexdigest()
    if isinstance(expected_md5, str) and expected_md5 != actual_md5:
        problems.append(f"md5 {actual_md5} != {expected_md5}")
    result.findings.append(
        Finding("graphic_metadata", True, "size and md5 match source metadata")
        if not problems
        else Finding(
            "graphic_metadata", False, "; ".join(problems), "graphic_metadata_mismatch"
        )
    )


_ROLE_CHECKS: dict[str, Callable[..., None]] = {
    "api_json": _check_api_json,
    "full_text_xml": _check_full_text_xml,
    "full_text_html": _check_text_representation,
    "plain_text": _check_text_representation,
    "mods_xml": _check_mods_xml,
    "official_pdf": _check_official_pdf,
    "original_graphic": _check_original_graphic,
}


def _parse_xml(result: ArtifactValidation, body: bytes) -> Element | None:
    try:
        root = SafeElementTree.fromstring(body)
    except Exception as error:  # defusedxml raises parse and security errors
        result.findings.append(
            Finding("xml_wellformed", False, str(error)[:500], "malformed_xml")
        )
        return None
    result.findings.append(Finding("xml_wellformed", True, "parsed"))
    return root


def _identity_finding(
    result: ArtifactValidation, agrees: bool, document_number: str
) -> None:
    result.findings.append(
        Finding("document_identity", True, f"names {document_number}")
        if agrees
        else Finding(
            "document_identity",
            False,
            f"does not identify {document_number}",
            "identity_mismatch",
        )
    )


def _govinfo_identity_finding(result: ArtifactValidation) -> None:
    """The constructed granule must appear in the URL GovInfo actually served."""
    receipt = result.receipt
    package, _, granule = receipt["source_document_identity"]["value"].partition("/")
    resolved = receipt["request"].get("resolved_url", "")
    agrees = f"/{package}/" in resolved and granule in resolved
    result.findings.append(
        Finding("govinfo_identity", True, "granule matches served URL")
        if agrees
        else Finding(
            "govinfo_identity",
            False,
            f"{package}/{granule} not in {resolved}",
            "govinfo_identity_mismatch",
        )
    )
