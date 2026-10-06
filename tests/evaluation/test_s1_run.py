import json
from datetime import UTC, datetime
from pathlib import Path

import pytest
import yaml

from faa_directive_impact.evaluation.s1_run import conclude_run, run_s1

REPO = Path(__file__).resolve().parents[2]
STARTED = datetime(2026, 10, 6, 12, 0, tzinfo=UTC)
COMMIT = "0123456789abcdef0123456789abcdef01234567"


@pytest.fixture
def run_directory(tmp_path: Path) -> Path:
    return run_s1(REPO, tmp_path, STARTED, COMMIT, dirty=False)


def test_run_writes_every_artifact_under_its_id(run_directory: Path) -> None:
    assert run_directory.name == "s1-20261006T120000Z-0123456"
    assert sorted(p.name for p in run_directory.iterdir()) == [
        "hand-review.md",
        "hand-review.yaml",
        "normalized-record.json",
        "outputs.json",
        "queues.html",
        "report.json",
        "report.md",
    ]


def test_report_records_provenance_and_disclosures(run_directory: Path) -> None:
    report = json.loads((run_directory / "report.json").read_text())

    assert report["gate_version"] == 1
    assert report["git_commit"] == COMMIT
    assert report["generation_id"] == "gen-20260926T215105Z-7fe9da08"
    assert report["units_scored"] == 18
    assert len(report["units_not_yet_evaluated"]) == 15
    assert "one reading" in report["oracle_disclosure"]
    markdown = (run_directory / "report.md").read_text()
    assert "## Known Gaps (from GATES.md)" in markdown
    assert "Thin slices." in markdown


def test_run_is_never_overwritten(tmp_path: Path) -> None:
    run_s1(REPO, tmp_path, STARTED, COMMIT, dirty=False)

    with pytest.raises(FileExistsError):
        run_s1(REPO, tmp_path, STARTED, COMMIT, dirty=False)


def test_conclude_reads_the_completed_review(run_directory: Path) -> None:
    path = run_directory / "hand-review.yaml"
    review = yaml.safe_load(path.read_text())
    review["reviewer"] = "test"
    for entry in review["units"].values():
        entry["gate_5"]["result"] = "absent"
        if entry["gate_11"]["result"] == "":
            entry["gate_11"]["result"] = "consistent"
    path.write_text(yaml.safe_dump(review))

    verdict = conclude_run(REPO, run_directory)

    assert verdict["decision"] == "go"
    assert verdict["provisional"] is True
    markdown = (run_directory / "verdict.md").read_text()
    assert "PROVISIONAL" in markdown
    assert markdown.index("| 2 | No scope leak") < markdown.index("| 10 | Required")
