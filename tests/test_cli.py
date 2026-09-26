import json
from pathlib import Path

import httpx
import pytest

from faa_directive_impact import cli
from faa_directive_impact.acquisition import retrieval
from faa_directive_impact.schema_validation import validate_raw_generation_manifest

DOC = "2025-10764"
API_URL = f"https://www.federalregister.gov/api/v1/documents/{DOC}.json"
REPRESENTATION_URLS = {
    "full_text_xml_url": "https://www.federalregister.gov/x/2025-10764.xml",
    "body_html_url": "https://www.federalregister.gov/h/2025-10764.html",
    "raw_text_url": "https://www.federalregister.gov/t/2025-10764.txt",
    "pdf_url": "https://www.govinfo.gov/p/2025-10764.pdf",
    "mods_url": "https://www.govinfo.gov/m/2025-10764/mods.xml",
}
XML_URL = REPRESENTATION_URLS["full_text_xml_url"]


def serve(monkeypatch: pytest.MonkeyPatch, pages: dict[str, bytes]) -> None:
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


def site(xml: bytes = b"<RULE>v1</RULE>", omit: str | None = None) -> dict:
    record = {"document_number": DOC, "publication_date": "2025-06-13"}
    record.update(REPRESENTATION_URLS)
    if omit:
        del record[omit]
    pages = {url: b"body" for url in REPRESENTATION_URLS.values()}
    pages[XML_URL] = xml
    pages[API_URL] = json.dumps(record).encode()
    return pages


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


def test_complete_run_exits_ok_and_stores_valid_manifest(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch, capsys: pytest.CaptureFixture
) -> None:
    serve(monkeypatch, site())

    assert acquire(tmp_path) == cli.EXIT_OK

    summary = json.loads(capsys.readouterr().out)
    manifest = json.loads((tmp_path / summary["manifest"]).read_text())
    validate_raw_generation_manifest(manifest)
    assert manifest["completeness_status"] == "complete"
    assert manifest["corpus_track"] == "frozen_evaluation"
    assert not (tmp_path / "runs").exists()


def test_missing_representation_exits_failed(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    serve(monkeypatch, site(omit="pdf_url"))

    assert acquire(tmp_path) == cli.EXIT_FAILED


def test_changed_content_exits_for_review(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    serve(monkeypatch, site(xml=b"<RULE>v1</RULE>"))
    assert acquire(tmp_path) == cli.EXIT_OK

    serve(monkeypatch, site(xml=b"<RULE>v2</RULE>"))

    assert acquire(tmp_path) == cli.EXIT_NEEDS_REVIEW
