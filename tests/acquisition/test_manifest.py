import json
from datetime import UTC, datetime
from itertools import count
from pathlib import Path
from typing import Any

import httpx
import pytest
from fakes import api_url, document_pages, edit_api_record
from jsonschema import ValidationError

from faa_directive_impact.acquisition.document import acquire_document
from faa_directive_impact.acquisition.manifest import (
    build_manifest,
    build_validation_report,
)
from faa_directive_impact.acquisition.retrieval import AcquisitionContext, build_client
from faa_directive_impact.acquisition.storage import RawStorage
from faa_directive_impact.acquisition.versions import VersionIndex
from faa_directive_impact.schema_validation import validate_raw_generation_manifest

PROPOSAL, FINAL = "2025-10764", "2025-18469"
FINAL_PDF = "https://www.govinfo.gov/content/pkg/FR-2025-09-24/pdf/2025-18469.pdf"
FIXED_TIME = datetime(2026, 9, 26, 12, 0, 0, tzinfo=UTC)
_ids = count()


def graphic_url(identifier: str) -> str:
    return (
        f"https://img.federalregister.gov/{identifier}/{identifier}_original_size.png"
    )


def pair_pages(**final_overrides: Any) -> dict[str, bytes | None]:
    final: dict[str, Any] = {
        "document_type": "Rule",
        "publication_date": "2025-09-24",
        "docket_ids": ("Docket No. FAA-2025-0926", "AD 2025-19-13"),
    }
    final.update(final_overrides)
    return {
        **document_pages(
            PROPOSAL,
            "Proposed Rule",
            "2025-06-13",
            ("Docket No. FAA-2025-0926", "Project Identifier AD-2025-00200-E"),
        ),
        **document_pages(FINAL, **final),
    }


def generate(tmp_path: Path, pages: dict[str, bytes | None]) -> dict:
    return generate_with_report(tmp_path, pages)[0]


def generate_with_report(
    tmp_path: Path, pages: dict[str, bytes | None]
) -> tuple[dict, dict]:
    def handler(request: httpx.Request) -> httpx.Response:
        body = pages.get(str(request.url))
        return (
            httpx.Response(404) if body is None else httpx.Response(200, content=body)
        )

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
        documents = [
            acquire_document(context, number, versions) for number in (PROPOSAL, FINAL)
        ]
    manifest = build_manifest(
        generation_id=f"generation-{run_id}",
        created_at=FIXED_TIME,
        corpus_track="frozen_evaluation",
        run_id=run_id,
        documents=documents,
    )
    report = build_validation_report(
        generation_id=f"generation-{run_id}", created_at=FIXED_TIME, documents=documents
    )
    return manifest, report


def cell_key(entry: dict) -> tuple:
    identity = entry["source_document_identity"]
    return (
        identity["namespace"],
        identity["value"],
        entry["representation_role"],
        entry.get("source_graphic_identifier"),
    )


def test_complete_pair_is_eligible_with_relationship(tmp_path: Path) -> None:
    manifest = generate(tmp_path, pair_pages())

    assert manifest["completeness_status"] == "complete"
    assert manifest["eligible_for_normalization"] is True
    assert len(manifest["expected_artifacts"]) == 12
    (relationship,) = manifest["relationships"]
    assert relationship["relationship_type"] == "proposal_final"
    assert relationship["from_identity"]["value"] == PROPOSAL
    assert relationship["to_identity"]["value"] == FINAL
    assert relationship["confidence_class"] == "identifier_join"
    assert len(relationship["evidence_receipt_ids"]) == 2


def test_final_rule_records_deferred_drs_dependency(tmp_path: Path) -> None:
    manifest = generate(tmp_path, pair_pages())

    drs = [
        d for d in manifest["dependencies"] if d["dependency_type"] == "source_access"
    ]
    (dependency,) = drs
    assert dependency["name"] == "FAA DRS record for AD 2025-19-13"
    assert dependency["availability_status"] == "deferred_access_verification"


def test_every_expected_cell_has_a_receipt_file_or_missing_entry(
    tmp_path: Path,
) -> None:
    pages = pair_pages()
    pages[FINAL_PDF] = None

    manifest = generate(tmp_path, pages)

    receipts = [
        json.loads((tmp_path / ref["receipt_relative_path"]).read_text())
        for ref in manifest["receipt_references"]
    ]
    acquired = {cell_key(r) for r in receipts if r["acquisition_status"] == "succeeded"}
    missing = {cell_key(entry) for entry in manifest["missing_artifacts"]}
    for cell in manifest["expected_artifacts"]:
        assert (cell_key(cell) in acquired) != (cell_key(cell) in missing)


def test_failed_representation_makes_generation_ineligible(tmp_path: Path) -> None:
    pages = pair_pages()
    pages[FINAL_PDF] = None

    manifest = generate(tmp_path, pages)

    assert manifest["completeness_status"] == "incomplete"
    assert manifest["eligible_for_normalization"] is False
    (missing,) = manifest["missing_artifacts"]
    assert missing["representation_role"] == "official_pdf"
    assert missing["reason_code"] == "acquisition_failed"
    assert "receipt_id" in missing


def test_unavailable_api_record_marks_every_cell_missing(tmp_path: Path) -> None:
    pages = pair_pages()
    pages[api_url(FINAL)] = None

    manifest = generate(tmp_path, pages)

    final_missing = [
        entry
        for entry in manifest["missing_artifacts"]
        if entry["source_document_identity"]["value"] == FINAL
    ]
    assert len(final_missing) == 6
    assert {entry["reason_code"] for entry in final_missing} == {"acquisition_failed"}
    assert manifest["relationships"] == []
    assert all(
        FINAL not in dependency["name"] and "2025-19-13" not in dependency["name"]
        for dependency in manifest["dependencies"]
    )


def test_url_absent_from_record_is_not_published(tmp_path: Path) -> None:
    pages = pair_pages()
    edit_api_record(pages, FINAL, raw_text_url=None)

    manifest = generate(tmp_path, pages)

    (missing,) = manifest["missing_artifacts"]
    assert missing["representation_role"] == "plain_text"
    assert missing["reason_code"] == "not_published"


@pytest.mark.parametrize(
    "overrides",
    [
        {"docket_ids": ("Docket No. FAA-2099-0001",)},
        {"publication_date": "2025-01-01"},
        {"document_type": "Proposed Rule"},
    ],
)
def test_no_relationship_without_shared_docket_and_order(
    tmp_path: Path, overrides: dict
) -> None:
    manifest = generate(tmp_path, pair_pages(**overrides))

    assert manifest["relationships"] == []


def test_graphics_are_expected_artifacts(tmp_path: Path) -> None:
    manifest = generate(tmp_path, pair_pages(images=("ER24SE25.000",)))

    graphics = [
        cell
        for cell in manifest["expected_artifacts"]
        if cell["representation_role"] == "original_graphic"
    ]
    assert [cell["source_graphic_identifier"] for cell in graphics] == ["ER24SE25.000"]
    assert manifest["completeness_status"] == "complete"


def test_manifest_contains_no_credentials(tmp_path: Path) -> None:
    serialized = json.dumps(generate(tmp_path, pair_pages())).lower()

    assert "cookie" not in serialized
    assert "authorization" not in serialized


def test_incomplete_manifest_cannot_claim_eligibility(tmp_path: Path) -> None:
    pages = pair_pages()
    pages[FINAL_PDF] = None
    manifest = generate(tmp_path, pages)

    manifest["eligible_for_normalization"] = True

    with pytest.raises(ValidationError):
        validate_raw_generation_manifest(manifest)


def test_missing_graphic_is_identified(tmp_path: Path) -> None:
    pages = pair_pages(images=("ER24SE25.000", "ER24SE25.001"))
    pages[graphic_url("ER24SE25.001")] = None

    manifest = generate(tmp_path, pages)

    (missing,) = manifest["missing_artifacts"]
    assert missing["representation_role"] == "original_graphic"
    assert missing["source_graphic_identifier"] == "ER24SE25.001"


def test_unresolved_graphic_is_identified_without_a_receipt(tmp_path: Path) -> None:
    pages = pair_pages(images=("ER24SE25.000",))
    edit_api_record(
        pages, FINAL, images={"ER24SE25.000": {"large": "https://img.test/large.png"}}
    )

    manifest = generate(tmp_path, pages)

    (missing,) = manifest["missing_artifacts"]
    assert missing["source_graphic_identifier"] == "ER24SE25.000"
    assert missing["reason_code"] == "not_published"
    assert "receipt_id" not in missing


def test_stated_none_is_recorded_as_not_required(tmp_path: Path) -> None:
    manifest = generate(tmp_path, pair_pages())

    incorporated = [
        d
        for d in manifest["dependencies"]
        if d["dependency_type"] == "incorporated_material"
    ]
    assert {d["name"] for d in incorporated} == {
        f"Material incorporated by reference in {PROPOSAL} paragraph (l)",
        f"Material incorporated by reference in {FINAL} paragraph (l)",
    }
    assert {d["availability_status"] for d in incorporated} == {"not_required"}


def test_listed_material_is_recorded_as_unavailable(tmp_path: Path) -> None:
    bulletin = "IAE NMSB V2500-E5-72-0015, dated December 15, 2020."

    manifest = generate(tmp_path, pair_pages(incorporated=(bulletin,)))

    (listed,) = [d for d in manifest["dependencies"] if d["name"] == bulletin]
    assert listed["availability_status"] == "unavailable"
    assert manifest["eligible_for_normalization"] is True


def test_invalid_artifact_makes_complete_generation_ineligible(
    tmp_path: Path,
) -> None:
    pages = pair_pages()
    pages[FINAL_PDF] = b"%PDF-1.7 truncated"

    manifest, report = generate_with_report(tmp_path, pages)

    assert manifest["completeness_status"] == "complete"
    assert manifest["eligible_for_normalization"] is False
    assert report["status"] == "failed"
    (failure,) = [f for f in report["findings"] if f["outcome"] == "failed"]
    assert failure["reason_code"] == "unreadable_pdf"
    assert failure["source_document_identity"]["value"] == "FR-2025-09-24/2025-18469"
    assert failure["representation_role"] == "official_pdf"


def test_valid_pair_produces_passing_report(tmp_path: Path) -> None:
    _, report = generate_with_report(tmp_path, pair_pages())

    assert report["status"] == "passed"
    checks = {(f["representation_role"], f["check"]) for f in report["findings"]}
    assert ("official_pdf", "pdf_readable") in checks
    assert ("full_text_xml", "incorporated_material") in checks
    assert ("mods_xml", "govinfo_identity") in checks
