import json
from pathlib import Path

import httpx
import pytest
from source_fakes import api_url, document_pages

from faa_directive_impact import cli
from faa_directive_impact.acquisition import retrieval
from faa_directive_impact.schema_validation import (
    validate_raw_generation_manifest,
    validate_validation_report,
)

DOC = "2025-10764"
XML_URL = f"https://www.federalregister.gov/documents/full_text/{DOC}.xml"


def serve(monkeypatch: pytest.MonkeyPatch, pages: dict[str, bytes | None]) -> None:
    def handler(request: httpx.Request) -> httpx.Response:
        body = pages.get(str(request.url))
        return (
            httpx.Response(404) if body is None else httpx.Response(200, content=body)
        )

    monkeypatch.setattr(
        cli,
        "build_client",
        lambda timeout: retrieval.build_client(
            timeout, transport=httpx.MockTransport(handler)
        ),
    )


def site() -> dict[str, bytes | None]:
    return document_pages(DOC, "Proposed Rule", "2025-06-13")


def acquire(tmp_path: Path) -> int:
    return cli.main(
        [
            "acquire",
            DOC,
            "--storage-root",
            str(tmp_path),
            "--corpus-track",
            "frozen_evaluation",
        ]
    )


def test_complete_run_exits_ok_and_stores_valid_records(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch, capsys: pytest.CaptureFixture
) -> None:
    serve(monkeypatch, site())

    assert acquire(tmp_path) == cli.EXIT_OK

    summary = json.loads(capsys.readouterr().out)
    manifest = json.loads((tmp_path / summary["manifest"]).read_text())
    report = json.loads((tmp_path / summary["validation_report"]).read_text())
    validate_raw_generation_manifest(manifest)
    validate_validation_report(report)
    assert manifest["eligible_for_normalization"] is True
    assert report["status"] == "passed"
    assert report["generation_id"] == manifest["generation_id"]


def test_missing_representation_exits_failed(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    pages = site()
    pages[XML_URL] = None
    serve(monkeypatch, pages)

    assert acquire(tmp_path) == cli.EXIT_FAILED


def test_invalid_artifact_exits_failed_and_is_not_indexed(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch, capsys: pytest.CaptureFixture
) -> None:
    pages = site()
    record = json.loads(pages[api_url(DOC)] or b"")
    record["document_number"] = "2025-18469"
    pages[api_url(DOC)] = json.dumps(record).encode()
    serve(monkeypatch, pages)
    assert acquire(tmp_path) == cli.EXIT_FAILED
    capsys.readouterr()

    serve(monkeypatch, site())
    assert acquire(tmp_path) == cli.EXIT_OK

    summary = json.loads(capsys.readouterr().out)
    api_versions = [
        v for v in summary["versions"] if v["representation_role"] == "api_json"
    ]
    assert [v["status"] for v in api_versions] == ["new"]


def test_changed_content_exits_for_review(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    serve(monkeypatch, site())
    assert acquire(tmp_path) == cli.EXIT_OK

    pages = site()
    pages[XML_URL] = (pages[XML_URL] or b"").replace(b"Contact", b"Please contact")
    serve(monkeypatch, pages)

    assert acquire(tmp_path) == cli.EXIT_NEEDS_REVIEW
