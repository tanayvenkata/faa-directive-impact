from datetime import UTC, datetime
from itertools import count
from pathlib import Path

import httpx
from source_fakes import api_url, document_pages, edit_api_record

from faa_directive_impact.acquisition.document import acquire_document
from faa_directive_impact.acquisition.retrieval import AcquisitionContext, build_client
from faa_directive_impact.acquisition.storage import RawStorage
from faa_directive_impact.acquisition.versions import VersionIndex
from faa_directive_impact.schema_validation import validate_artifact_receipt

DOC = "2021-14268"
FIXED_TIME = datetime(2026, 9, 26, 12, 0, 0, tzinfo=UTC)
_ids = count()


def site() -> dict[str, bytes | None]:
    return document_pages(DOC, publication_date="2021-07-02", images=("ER02JY21.001",))


def xml_url(pages: dict) -> str:
    return next(url for url in pages if url.endswith(f"full_text/{DOC}.xml"))


def image_url(pages: dict) -> str:
    return next(url for url in pages if url.endswith("_original_size.png"))


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


def failed_checks(result) -> list[dict]:
    return [
        record
        for validation in result.validations
        for record in validation.records()
        if record["outcome"] == "failed"
    ]


def test_first_run_acquires_and_validates_every_representation(
    tmp_path: Path,
) -> None:
    result = run(tmp_path, site())

    assert not result.failed, failed_checks(result)
    assert len(result.receipts) == 7
    assert len(result.validations) == 7
    assert set(statuses(result).values()) == {"new"}
    for receipt in result.receipts:
        validate_artifact_receipt(receipt)
        assert (tmp_path / receipt["artifact"]["relative_path"]).is_file()
    assert result.incorporated_material is not None
    assert result.incorporated_material.paragraph == "l"


def test_unchanged_rerun_adds_no_logical_version(tmp_path: Path) -> None:
    run(tmp_path, site())
    pages = site()
    edit_api_record(pages, DOC, page_views={"count": 500})

    rerun = run(tmp_path, pages)

    assert not rerun.failed
    assert not rerun.needs_review
    assert set(statuses(rerun).values()) == {"unchanged"}


def test_changed_bytes_are_preserved_and_flagged(tmp_path: Path) -> None:
    first = run(tmp_path, site())
    pages = site()
    pages[xml_url(pages)] = (pages[xml_url(pages)] or b"").replace(
        b"Contact the FAA.", b"Contact the FAA office."
    )

    second = run(tmp_path, pages)

    assert second.needs_review
    assert statuses(second)["full_text_xml"] == "changed"
    assert statuses(second)["official_pdf"] == "unchanged"
    old_xml, new_xml = (
        next(r for r in result.receipts if r["representation_role"] == "full_text_xml")
        for result in (first, second)
    )
    old_bytes = (tmp_path / old_xml["artifact"]["relative_path"]).read_bytes()
    new_bytes = (tmp_path / new_xml["artifact"]["relative_path"]).read_bytes()
    assert b"office" not in old_bytes
    assert b"office" in new_bytes


def test_missing_referenced_image_fails_the_document(tmp_path: Path) -> None:
    pages = site()
    pages[image_url(pages)] = None

    result = run(tmp_path, pages)

    assert result.failed
    image_receipt = next(
        r for r in result.receipts if r["representation_role"] == "original_graphic"
    )
    assert image_receipt["failure"]["reason_code"] == "not_found"
    assert image_receipt["source_graphic_identifier"] == "ER02JY21.001"


def test_api_record_for_another_document_stops_resolution(tmp_path: Path) -> None:
    pages = site()
    edit_api_record(pages, DOC, document_number="2025-10764")

    result = run(tmp_path, pages)

    assert result.problems == ["api_json_invalid"]
    assert len(result.receipts) == 1
    assert [f["reason_code"] for f in failed_checks(result)] == ["identity_mismatch"]


def test_unreadable_api_json_stops_resolution(tmp_path: Path) -> None:
    pages = site()
    pages[api_url(DOC)] = b"{oops"

    result = run(tmp_path, pages)

    assert result.problems == ["api_json_invalid"]
    assert result.failed


def test_failed_receipts_do_not_count_as_versions(tmp_path: Path) -> None:
    pages = site()
    pages[xml_url(pages)] = None
    run(tmp_path, pages)

    later = run(tmp_path, site())

    assert statuses(later)["full_text_xml"] == "new"


def test_invalid_artifact_does_not_become_a_version(tmp_path: Path) -> None:
    pages = site()
    pages[xml_url(pages)] = b"<RULE><unclosed></RULE>"

    result = run(tmp_path, pages)

    assert result.failed
    assert "full_text_xml" not in statuses(result)
