import json
from datetime import UTC, datetime
from itertools import count
from pathlib import Path

import httpx

from faa_directive_impact.acquisition.document import acquire_document
from faa_directive_impact.acquisition.retrieval import AcquisitionContext, build_client
from faa_directive_impact.acquisition.storage import RawStorage
from faa_directive_impact.acquisition.versions import VersionIndex
from faa_directive_impact.schema_validation import validate_artifact_receipt

DOC = "2021-14268"
XML_URL = "https://www.federalregister.gov/x/2021-14268.xml"
IMAGE_URL = (
    "https://img.federalregister.gov/ER02JY21.001/ER02JY21.001_original_size.png"
)
FIXED_TIME = datetime(2026, 9, 26, 12, 0, 0, tzinfo=UTC)
_ids = count()


def api_body(page_views: int = 1, document_number: str = DOC) -> bytes:
    return json.dumps(
        {
            "document_number": document_number,
            "publication_date": "2021-07-02",
            "full_text_xml_url": XML_URL,
            "body_html_url": "https://www.federalregister.gov/h/2021-14268.html",
            "raw_text_url": "https://www.federalregister.gov/t/2021-14268.txt",
            "pdf_url": "https://www.govinfo.gov/content/pkg/FR-2021-07-02/pdf/2021-14268.pdf",
            "mods_url": "https://www.govinfo.gov/metadata/granule/FR-2021-07-02/2021-14268/mods.xml",
            "images": {"ER02JY21.001": {"original_size": IMAGE_URL}},
            "page_views": {"count": page_views},
        }
    ).encode()


def site(
    page_views: int = 1,
    xml: bytes = b"<RULE>v1</RULE>",
    overrides: dict[str, bytes | None] | None = None,
) -> dict[str, bytes | None]:
    pages: dict[str, bytes | None] = {
        f"https://www.federalregister.gov/api/v1/documents/{DOC}.json": api_body(
            page_views
        ),
        XML_URL: xml,
        "https://www.federalregister.gov/h/2021-14268.html": b"<html>v1</html>",
        "https://www.federalregister.gov/t/2021-14268.txt": b"text v1",
        "https://www.govinfo.gov/content/pkg/FR-2021-07-02/pdf/2021-14268.pdf": (
            b"%PDF-1.7 v1"
        ),
        "https://www.govinfo.gov/metadata/granule/FR-2021-07-02/2021-14268/mods.xml": (
            b"<mods/>"
        ),
        IMAGE_URL: b"\x89PNG\r\n\x1a\nv1",
    }
    pages.update(overrides or {})
    return pages


def run(tmp_path: Path, pages: dict[str, bytes | None]):
    def handler(request: httpx.Request) -> httpx.Response:
        body = pages.get(str(request.url))
        if body is None:
            return httpx.Response(404)
        return httpx.Response(200, content=body)

    run_id = f"run-{next(_ids):04d}"
    storage = RawStorage(tmp_path)
    versions = VersionIndex.from_receipts(storage.root)
    with build_client(transport=httpx.MockTransport(handler)) as client:
        context = AcquisitionContext(
            run_id=run_id,
            storage=storage,
            client=client,
            clock=lambda: FIXED_TIME,
            new_id=lambda prefix, at: f"{prefix}-{next(_ids):06d}",
        )
        return acquire_document(context, DOC, versions)


def statuses(result) -> dict[str, str]:
    return {version.key[3]: version.status for version in result.versions}


def test_first_run_acquires_every_representation_as_new(tmp_path: Path) -> None:
    result = run(tmp_path, site())

    assert not result.failed
    assert len(result.receipts) == 7
    assert set(statuses(result).values()) == {"new"}
    for receipt in result.receipts:
        validate_artifact_receipt(receipt)
        artifact = tmp_path / receipt["artifact"]["relative_path"]
        assert artifact.is_file()


def test_unchanged_rerun_adds_no_logical_version(tmp_path: Path) -> None:
    run(tmp_path, site(page_views=1))

    rerun = run(tmp_path, site(page_views=500))

    assert not rerun.failed
    assert not rerun.needs_review
    assert set(statuses(rerun).values()) == {"unchanged"}


def test_changed_bytes_are_preserved_and_flagged(tmp_path: Path) -> None:
    first = run(tmp_path, site())

    second = run(tmp_path, site(xml=b"<RULE>v2</RULE>"))

    assert second.needs_review
    assert statuses(second)["full_text_xml"] == "changed"
    assert statuses(second)["official_pdf"] == "unchanged"
    old_xml, new_xml = (
        next(r for r in result.receipts if r["representation_role"] == "full_text_xml")
        for result in (first, second)
    )
    assert (tmp_path / old_xml["artifact"]["relative_path"]).read_bytes() == (
        b"<RULE>v1</RULE>"
    )
    assert (tmp_path / new_xml["artifact"]["relative_path"]).read_bytes() == (
        b"<RULE>v2</RULE>"
    )


def test_missing_referenced_image_fails_the_document(tmp_path: Path) -> None:
    result = run(tmp_path, site(overrides={IMAGE_URL: None}))

    assert result.failed
    image_receipt = next(
        r for r in result.receipts if r["representation_role"] == "original_graphic"
    )
    assert image_receipt["failure"]["reason_code"] == "not_found"
    assert image_receipt["source_graphic_identifier"] == "ER02JY21.001"


def test_api_record_for_another_document_stops_resolution(tmp_path: Path) -> None:
    pages = site(
        overrides={
            f"https://www.federalregister.gov/api/v1/documents/{DOC}.json": api_body(
                document_number="2025-10764"
            )
        }
    )

    result = run(tmp_path, pages)

    assert result.problems == ["api_json_identity_mismatch"]
    assert len(result.receipts) == 1


def test_unreadable_api_json_stops_resolution(tmp_path: Path) -> None:
    pages = site(
        overrides={
            f"https://www.federalregister.gov/api/v1/documents/{DOC}.json": b"{oops"
        }
    )

    result = run(tmp_path, pages)

    assert result.problems == ["api_json_unreadable"]
    assert result.failed


def test_failed_receipts_do_not_count_as_versions(tmp_path: Path) -> None:
    run(tmp_path, site(overrides={XML_URL: None}))

    later = run(tmp_path, site())

    assert statuses(later)["full_text_xml"] == "new"
