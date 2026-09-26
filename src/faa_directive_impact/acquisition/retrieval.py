"""Retrieve one official-source representation into raw storage with a receipt.

Every attempt, successful or not, yields a schema-valid artifact receipt.
Directive meaning is never inspected here.
"""

import secrets
from collections.abc import Callable
from dataclasses import dataclass
from datetime import UTC, datetime
from typing import Any

import httpx

from faa_directive_impact.acquisition.storage import RawStorage, StoragePathError
from faa_directive_impact.schema_validation import validate_artifact_receipt

RECEIPT_SCHEMA_VERSION = "1.0.0"
USER_AGENT = (
    "faa-directive-impact/0.1 (+https://github.com/tanayvenkata/faa-directive-impact)"
)
DEFAULT_TIMEOUT_SECONDS = 30.0
MAX_FAILURE_DETAIL = 2000

Clock = Callable[[], datetime]
IdFactory = Callable[[str, datetime], str]


@dataclass(frozen=True)
class RepresentationRequest:
    """What to fetch, where to keep it, and how the source classifies it."""

    source_system: str
    identity_namespace: str
    identity_value: str
    representation_role: str
    authority_role: str
    url: str
    relative_path: str
    redistribution_status: str
    redistribution_basis: str
    parent_identity: tuple[str, str] | None = None
    source_graphic_identifier: str | None = None


@dataclass(frozen=True)
class AcquisitionContext:
    """Per-run settings shared by every retrieval in one acquisition run."""

    run_id: str
    storage: RawStorage
    client: httpx.Client
    clock: Clock
    new_id: IdFactory


def utc_now() -> datetime:
    return datetime.now(UTC)


def random_id(prefix: str, at: datetime) -> str:
    """Return an opaque ID that sorts by UTC time."""
    return f"{prefix}-{at.strftime('%Y%m%dT%H%M%SZ')}-{secrets.token_hex(4)}"


def build_client(
    timeout_seconds: float = DEFAULT_TIMEOUT_SECONDS,
    transport: httpx.BaseTransport | None = None,
) -> httpx.Client:
    """Return an HTTP client that identifies the project and sends no credentials.

    ``transport`` lets tests substitute an offline transport.
    """
    return httpx.Client(
        headers={"User-Agent": USER_AGENT, "Accept-Encoding": "identity"},
        timeout=timeout_seconds,
        follow_redirects=True,
        transport=transport,
    )


class _AcquisitionFailure(Exception):
    def __init__(
        self, reason_code: str, detail: str, response: dict[str, Any] | None = None
    ) -> None:
        super().__init__(detail)
        self.reason_code = reason_code
        self.detail = detail[:MAX_FAILURE_DETAIL]
        self.response = response


def retrieve(context: AcquisitionContext, spec: RepresentationRequest) -> dict:
    """Fetch ``spec`` and publish its bytes and receipt; return the receipt."""
    started_at = context.clock()
    retrieval_id = context.new_id("retrieval", started_at)
    receipt: dict[str, Any] = {
        "schema_version": RECEIPT_SCHEMA_VERSION,
        "receipt_id": f"receipt-{retrieval_id.removeprefix('retrieval-')}",
        "acquisition_run_id": context.run_id,
        "retrieval_id": retrieval_id,
        "source_system": spec.source_system,
        "source_document_identity": {
            "namespace": spec.identity_namespace,
            "value": spec.identity_value,
        },
        "representation_role": spec.representation_role,
        "request": {"method": "GET", "requested_url": spec.url},
        "authority_role": spec.authority_role,
        "redistribution": {
            "status": spec.redistribution_status,
            "basis": spec.redistribution_basis,
        },
    }
    if spec.parent_identity is not None:
        namespace, value = spec.parent_identity
        receipt["parent_document_identity"] = {"namespace": namespace, "value": value}
    if spec.source_graphic_identifier is not None:
        receipt["source_graphic_identifier"] = spec.source_graphic_identifier
    try:
        response_record, resolved_url, artifact = _download(context, spec)
    except _AcquisitionFailure as failure:
        receipt["acquisition_status"] = "failed"
        receipt["failure"] = {
            "reason_code": failure.reason_code,
            "detail": failure.detail,
        }
        if failure.response is not None:
            receipt["response"] = failure.response
    else:
        receipt["acquisition_status"] = "succeeded"
        receipt["request"]["resolved_url"] = resolved_url
        receipt["response"] = response_record
        receipt["artifact"] = artifact
    receipt["retrieved_at_utc"] = _format_utc(context.clock())

    validate_artifact_receipt(receipt)
    context.storage.write_json(
        f"receipts/{context.run_id}/{receipt['receipt_id']}.json", receipt
    )
    return receipt


def _download(
    context: AcquisitionContext, spec: RepresentationRequest
) -> tuple[dict[str, Any], str, dict[str, Any]]:
    try:
        with context.client.stream("GET", spec.url) as response:
            response_record = _response_record(response)
            resolved_url = str(response.url)
            if response.url.scheme != "https":
                raise _AcquisitionFailure(
                    "redirect_error",
                    f"resolved to non-HTTPS URL {resolved_url}",
                    response_record,
                )
            if not response.is_success:
                raise _AcquisitionFailure(
                    _status_reason(response.status_code),
                    f"HTTP {response.status_code} from {resolved_url}",
                    response_record,
                )
            with context.storage.stage() as writer:
                first_chunk = b""
                for chunk in response.iter_bytes():
                    if not first_chunk:
                        first_chunk = chunk
                    writer.write(chunk)
                published = context.storage.publish(writer, spec.relative_path)
    except _AcquisitionFailure:
        raise
    except httpx.TimeoutException as error:
        raise _AcquisitionFailure("timeout", _describe(error)) from error
    except httpx.TooManyRedirects as error:
        raise _AcquisitionFailure("redirect_error", _describe(error)) from error
    except httpx.TransportError as error:
        raise _AcquisitionFailure("network_error", _describe(error)) from error
    except (OSError, StoragePathError) as error:
        raise _AcquisitionFailure("write_error", _describe(error)) from error
    except Exception as error:
        raise _AcquisitionFailure("unexpected_error", _describe(error)) from error

    declared = _media_type(response_record["headers"].get("content_type"))
    artifact = {
        "relative_path": spec.relative_path,
        "byte_length": published.byte_length,
        "sha256": published.sha256,
        "declared_media_type": declared,
        "detected_media_type": detect_media_type(first_chunk),
    }
    return response_record, resolved_url, artifact


def detect_media_type(leading_bytes: bytes) -> str:
    """Classify content from its leading bytes only; A6 owns mismatch policy."""
    head = leading_bytes.lstrip()[:64]
    lowered = head.lower()
    if head.startswith(b"%PDF-"):
        return "application/pdf"
    if head.startswith(b"\x89PNG\r\n\x1a\n"):
        return "image/png"
    if head.startswith(b"\xff\xd8\xff"):
        return "image/jpeg"
    if head.startswith(b"GIF8"):
        return "image/gif"
    if lowered.startswith((b"<!doctype html", b"<html")):
        return "text/html"
    if head.startswith(b"<?xml") or head.startswith(b"<"):
        return "application/xml"
    if head.startswith((b"{", b"[")):
        return "application/json"
    return "application/octet-stream"


def _response_record(response: httpx.Response) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    for header, key in (
        ("content-type", "content_type"),
        ("etag", "etag"),
        ("last-modified", "last_modified"),
        ("content-disposition", "content_disposition"),
    ):
        value = response.headers.get(header)
        if value:
            headers[key] = value
    length = response.headers.get("content-length")
    if length and length.isdigit():
        headers["content_length"] = int(length)
    return {"status_code": response.status_code, "headers": headers}


def _status_reason(status_code: int) -> str:
    if status_code == 404:
        return "not_found"
    if status_code in (401, 403):
        return "access_denied"
    return "http_error"


def _media_type(content_type: str | None) -> str:
    if not content_type:
        return "application/octet-stream"
    return content_type.split(";", 1)[0].strip().lower() or "application/octet-stream"


def _describe(error: BaseException) -> str:
    return f"{type(error).__name__}: {error}" if str(error) else type(error).__name__


def _format_utc(moment: datetime) -> str:
    return moment.astimezone(UTC).strftime("%Y-%m-%dT%H:%M:%SZ")
