import hashlib
import json
from collections.abc import Callable, Iterator
from datetime import UTC, datetime
from pathlib import Path

import httpx
import pytest

from faa_directive_impact.acquisition.federal_register import api_json_request
from faa_directive_impact.acquisition.retrieval import (
    AcquisitionContext,
    build_client,
    detect_media_type,
    retrieve,
)
from faa_directive_impact.acquisition.storage import STAGING_DIRECTORY, RawStorage
from faa_directive_impact.schema_validation import validate_artifact_receipt

RUN_ID = "run-20260926T120000Z-00000000"
API_URL = "https://www.federalregister.gov/api/v1/documents/2025-10764.json"
API_BODY = b'{"document_number": "2025-10764", "type": "Proposed Rule"}'
FIXED_TIME = datetime(2026, 9, 26, 12, 0, 0, tzinfo=UTC)


def acquire(
    tmp_path: Path,
    handler: Callable[[httpx.Request], httpx.Response],
    first_id: int = 0,
) -> dict:
    counter = iter(range(first_id, first_id + 1000))
    with build_client(transport=httpx.MockTransport(handler)) as client:
        context = AcquisitionContext(
            run_id=RUN_ID,
            storage=RawStorage(tmp_path),
            client=client,
            clock=lambda: FIXED_TIME,
            new_id=lambda prefix, at: f"{prefix}-{next(counter):04d}",
        )
        return retrieve(context, api_json_request("2025-10764", RUN_ID))


def stored_receipt(tmp_path: Path, receipt: dict) -> dict:
    path = tmp_path / "receipts" / RUN_ID / f"{receipt['receipt_id']}.json"
    return json.loads(path.read_text())


def raw_files(tmp_path: Path) -> list[Path]:
    return [path for path in (tmp_path / "raw").rglob("*") if path.is_file()]


def assert_no_staging_leftovers(tmp_path: Path) -> None:
    assert list((tmp_path / STAGING_DIRECTORY).iterdir()) == []


def test_success_retains_exact_bytes_with_valid_receipt(tmp_path: Path) -> None:
    def handler(request: httpx.Request) -> httpx.Response:
        return httpx.Response(
            200,
            content=API_BODY,
            headers={"content-type": "application/json; charset=utf-8", "etag": "x"},
        )

    receipt = acquire(tmp_path, handler)

    assert receipt["acquisition_status"] == "succeeded"
    artifact = receipt["artifact"]
    stored = tmp_path / artifact["relative_path"]
    assert stored.read_bytes() == API_BODY
    assert artifact["sha256"] == hashlib.sha256(API_BODY).hexdigest()
    assert artifact["byte_length"] == len(API_BODY)
    assert artifact["declared_media_type"] == "application/json"
    assert artifact["detected_media_type"] == "application/json"
    assert receipt["response"]["headers"]["etag"] == "x"
    assert receipt["authority_role"] == "discovery_metadata"
    assert stored.stat().st_mode & 0o222 == 0
    assert stored_receipt(tmp_path, receipt) == receipt
    validate_artifact_receipt(stored_receipt(tmp_path, receipt))
    assert_no_staging_leftovers(tmp_path)


def test_request_identifies_project_without_credentials(tmp_path: Path) -> None:
    seen: list[httpx.Request] = []

    def handler(request: httpx.Request) -> httpx.Response:
        seen.append(request)
        return httpx.Response(200, content=API_BODY, headers={"set-cookie": "s=1"})

    receipt = acquire(tmp_path, handler)

    (request,) = seen
    assert request.headers["user-agent"].startswith("faa-directive-impact/")
    assert request.headers["accept-encoding"] == "identity"
    assert "authorization" not in request.headers
    assert "cookie" not in request.headers
    serialized = json.dumps(receipt).lower()
    assert "cookie" not in serialized
    assert "authorization" not in serialized


def test_redirect_records_resolved_url(tmp_path: Path) -> None:
    final_url = "https://www.federalregister.gov/api/v1/documents/2025-10764.json?v=2"

    def handler(request: httpx.Request) -> httpx.Response:
        if str(request.url) == API_URL:
            return httpx.Response(301, headers={"location": final_url})
        return httpx.Response(200, content=API_BODY)

    receipt = acquire(tmp_path, handler)

    assert receipt["acquisition_status"] == "succeeded"
    assert receipt["request"]["requested_url"] == API_URL
    assert receipt["request"]["resolved_url"] == final_url


def test_redirect_to_plain_http_fails_without_artifact(tmp_path: Path) -> None:
    def handler(request: httpx.Request) -> httpx.Response:
        if request.url.scheme == "https":
            return httpx.Response(
                302, headers={"location": "http://example.test/doc.json"}
            )
        return httpx.Response(200, content=API_BODY)

    receipt = acquire(tmp_path, handler)

    assert receipt["acquisition_status"] == "failed"
    assert receipt["failure"]["reason_code"] == "redirect_error"
    assert raw_files(tmp_path) == []


def test_redirect_loop_fails_as_redirect_error(tmp_path: Path) -> None:
    def handler(request: httpx.Request) -> httpx.Response:
        return httpx.Response(302, headers={"location": API_URL})

    receipt = acquire(tmp_path, handler)

    assert receipt["failure"]["reason_code"] == "redirect_error"


@pytest.mark.parametrize(
    ("status_code", "reason_code"),
    [(404, "not_found"), (403, "access_denied"), (503, "http_error")],
)
def test_http_error_statuses_produce_failure_receipts(
    tmp_path: Path, status_code: int, reason_code: str
) -> None:
    def handler(request: httpx.Request) -> httpx.Response:
        return httpx.Response(status_code, content=b"error page")

    receipt = acquire(tmp_path, handler)

    assert receipt["acquisition_status"] == "failed"
    assert receipt["failure"]["reason_code"] == reason_code
    assert receipt["response"]["status_code"] == status_code
    assert "artifact" not in receipt
    assert raw_files(tmp_path) == []
    validate_artifact_receipt(stored_receipt(tmp_path, receipt))


def test_timeout_before_response_produces_failure_receipt(tmp_path: Path) -> None:
    def handler(request: httpx.Request) -> httpx.Response:
        raise httpx.ConnectTimeout("timed out", request=request)

    receipt = acquire(tmp_path, handler)

    assert receipt["failure"]["reason_code"] == "timeout"
    assert "response" not in receipt
    validate_artifact_receipt(stored_receipt(tmp_path, receipt))


def test_connection_error_produces_network_failure(tmp_path: Path) -> None:
    def handler(request: httpx.Request) -> httpx.Response:
        raise httpx.ConnectError("refused", request=request)

    receipt = acquire(tmp_path, handler)

    assert receipt["failure"]["reason_code"] == "network_error"


class InterruptedStream(httpx.SyncByteStream):
    def __iter__(self) -> Iterator[bytes]:
        yield API_BODY[:10]
        raise httpx.ReadError("connection reset mid-body")


def test_interrupted_body_publishes_nothing(tmp_path: Path) -> None:
    def handler(request: httpx.Request) -> httpx.Response:
        return httpx.Response(200, stream=InterruptedStream())

    receipt = acquire(tmp_path, handler)

    assert receipt["acquisition_status"] == "failed"
    assert receipt["failure"]["reason_code"] == "network_error"
    assert raw_files(tmp_path) == []
    assert_no_staging_leftovers(tmp_path)
    validate_artifact_receipt(stored_receipt(tmp_path, receipt))


def test_existing_artifact_is_never_overwritten(tmp_path: Path) -> None:
    def handler(request: httpx.Request) -> httpx.Response:
        return httpx.Response(200, content=API_BODY)

    first = acquire(tmp_path, handler)
    second = acquire(tmp_path, handler, first_id=100)

    assert first["acquisition_status"] == "succeeded"
    assert second["acquisition_status"] == "failed"
    assert second["failure"]["reason_code"] == "write_error"
    assert (tmp_path / first["artifact"]["relative_path"]).read_bytes() == API_BODY


@pytest.mark.parametrize(
    ("leading", "media_type"),
    [
        (b"%PDF-1.7", "application/pdf"),
        (b"\x89PNG\r\n\x1a\n", "image/png"),
        (b"<?xml version='1.0'?>", "application/xml"),
        (b"  <!DOCTYPE html>", "text/html"),
        (b'{"a": 1}', "application/json"),
        (b"plain", "application/octet-stream"),
    ],
)
def test_detect_media_type_from_leading_bytes(leading: bytes, media_type: str) -> None:
    assert detect_media_type(leading) == media_type
