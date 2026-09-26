"""End-to-end offline lifecycle of acquiring the HPT hub pair.

Per-behavior tests live beside each module. This suite drives the real CLI
across several runs against one storage root and asserts the cross-cutting
guarantees: idempotent reruns, preserved changes, fail-closed partial
generations, and untouched prior artifacts.
"""

import hashlib
import json
from pathlib import Path

import httpx
import pytest
from source_fakes import document_pages, serve

from faa_directive_impact import cli
from faa_directive_impact.acquisition import retrieval
from faa_directive_impact.acquisition.storage import RawStorage

PROPOSAL, FINAL = "2025-10764", "2025-18469"
FINAL_XML = f"https://www.federalregister.gov/documents/full_text/{FINAL}.xml"
FINAL_PDF = "https://www.govinfo.gov/content/pkg/FR-2025-09-24/pdf/2025-18469.pdf"


def pair() -> dict[str, bytes | None]:
    return {
        **document_pages(
            PROPOSAL,
            "Proposed Rule",
            "2025-06-13",
            ("Docket No. FAA-2025-0926", "Project Identifier AD-2025-00200-E"),
        ),
        **document_pages(
            FINAL,
            "Rule",
            "2025-09-24",
            ("Docket No. FAA-2025-0926", "AD 2025-19-13"),
        ),
    }


class Harness:
    def __init__(
        self, root: Path, monkeypatch: pytest.MonkeyPatch, capsys: pytest.CaptureFixture
    ) -> None:
        self.root = root
        self.monkeypatch = monkeypatch
        self.capsys = capsys

    def acquire(self, pages: dict[str, bytes | None]) -> tuple[int, dict]:
        self.monkeypatch.setattr(
            cli,
            "build_client",
            lambda timeout: retrieval.build_client(
                timeout, transport=httpx.MockTransport(serve(pages))
            ),
        )
        self.capsys.readouterr()
        code = cli.main(
            [
                "acquire",
                PROPOSAL,
                FINAL,
                "--storage-root",
                str(self.root),
                "--corpus-track",
                "frozen_evaluation",
            ]
        )
        return code, json.loads(self.capsys.readouterr().out)

    def manifest(self, summary: dict) -> dict:
        return json.loads((self.root / summary["manifest"]).read_text())

    def raw_snapshot(self) -> dict[str, tuple[str, int]]:
        """Map every raw artifact to its hash and permission bits."""
        return {
            str(path.relative_to(self.root)): (
                hashlib.sha256(path.read_bytes()).hexdigest(),
                path.stat().st_mode & 0o777,
            )
            for path in sorted((self.root / "raw").rglob("*"))
            if path.is_file()
        }


@pytest.fixture
def harness(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch, capsys: pytest.CaptureFixture
) -> Harness:
    return Harness(tmp_path, monkeypatch, capsys)


def statuses(summary: dict) -> set[str]:
    return {version["status"] for version in summary["versions"]}


def test_unchanged_rerun_of_the_pair_is_idempotent(harness: Harness) -> None:
    first_code, first = harness.acquire(pair())
    second_code, second = harness.acquire(pair())

    assert (first_code, second_code) == (cli.EXIT_OK, cli.EXIT_OK)
    assert statuses(first) == {"new"}
    assert statuses(second) == {"unchanged"}
    assert len(second["versions"]) == 12
    for summary in (first, second):
        manifest = harness.manifest(summary)
        assert manifest["eligible_for_normalization"] is True
        assert len(manifest["relationships"]) == 1


def test_changed_representation_is_preserved_and_flagged(harness: Harness) -> None:
    harness.acquire(pair())
    before = harness.raw_snapshot()
    pages = pair()
    pages[FINAL_XML] = (pages[FINAL_XML] or b"").replace(b"Contact", b"Please contact")

    code, summary = harness.acquire(pages)

    assert code == cli.EXIT_NEEDS_REVIEW
    changed = [v for v in summary["versions"] if v["status"] == "changed"]
    assert [
        (v["representation_role"], v["source_document_identity"]["value"])
        for v in changed
    ] == [("full_text_xml", FINAL)]
    after = harness.raw_snapshot()
    assert all(after[path] == state for path, state in before.items())
    assert harness.manifest(summary)["eligible_for_normalization"] is True


def test_partial_pair_fails_the_gate_without_touching_prior_artifacts(
    harness: Harness,
) -> None:
    harness.acquire(pair())
    before = harness.raw_snapshot()
    pages = pair()
    pages[FINAL_PDF] = None

    code, summary = harness.acquire(pages)

    assert code == cli.EXIT_FAILED
    manifest = harness.manifest(summary)
    assert manifest["completeness_status"] == "incomplete"
    assert manifest["eligible_for_normalization"] is False
    after = harness.raw_snapshot()
    assert all(after[path] == state for path, state in before.items())
    assert all(mode == 0o444 for _, mode in after.values())


def test_invalid_candidate_is_rejected_and_next_good_run_recovers(
    harness: Harness,
) -> None:
    harness.acquire(pair())
    pages = pair()
    pages[FINAL_PDF] = b"<html>maintenance page</html>"

    failed_code, failed = harness.acquire(pages)
    recovered_code, recovered = harness.acquire(pair())

    assert failed_code == cli.EXIT_FAILED
    assert harness.manifest(failed)["completeness_status"] == "complete"
    assert harness.manifest(failed)["eligible_for_normalization"] is False
    assert {c["reason_code"] for c in failed["failed_checks"]} >= {
        "media_type_mismatch",
        "unreadable_pdf",
    }
    assert recovered_code == cli.EXIT_OK
    assert statuses(recovered) == {"unchanged"}


def test_receipt_write_failure_aborts_without_a_manifest(harness: Harness) -> None:
    original = RawStorage.write_json

    def fail_on_receipts(self: RawStorage, relative_path: str, record: dict):
        if relative_path.startswith("receipts/") and "2025-18469" in json.dumps(record):
            raise OSError("disk full")
        return original(self, relative_path, record)

    harness.monkeypatch.setattr(RawStorage, "write_json", fail_on_receipts)

    with pytest.raises(OSError):
        harness.acquire(pair())

    # The run leaves at most an orphaned artifact: no manifest claims it, and
    # without a receipt it never becomes a logical version.
    assert not (harness.root / "manifests").exists()
    harness.monkeypatch.setattr(RawStorage, "write_json", original)
    code, summary = harness.acquire(pair())
    assert code == cli.EXIT_OK
    final_statuses = {
        v["status"]
        for v in summary["versions"]
        if v["source_document_identity"]["value"].endswith(FINAL)
    }
    assert final_statuses == {"new"}


def test_live_network_is_blocked_in_the_suite() -> None:
    with retrieval.build_client() as client, pytest.raises(AssertionError):
        client.get("https://www.federalregister.gov/api/v1/documents/x.json")
