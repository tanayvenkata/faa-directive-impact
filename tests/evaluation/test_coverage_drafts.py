import json
from pathlib import Path

import pytest

from faa_directive_impact.evaluation import coverage_drafts


class Interrupted(Exception):
    pass


class DyingBatches:
    """Accepts the batch, then the process dies while waiting."""

    def create(self, requests):
        return type("Batch", (), {"id": "msgbatch_1"})()

    def retrieve(self, batch_id):
        raise Interrupted


def test_interrupted_drafting_run_keeps_its_batch_id(tmp_path, monkeypatch) -> None:
    monkeypatch.setattr(
        coverage_drafts,
        "requests_for",
        lambda repo, storage_root, numbers: [
            type("Request", (), {"key": lambda self: "k1", "params": lambda self: {}})()
        ],
    )
    client = type("C", (), {"messages": type("M", (), {"batches": DyingBatches()})()})()

    with pytest.raises(Interrupted):
        coverage_drafts.run(
            Path("."), tmp_path, tmp_path, "drafts", ["2025-18469"], client, stamp="S"
        )

    saved = json.loads((tmp_path / "coverage-drafts-S" / "batch.json").read_text())
    assert saved == {"batch_id": "msgbatch_1", "collected_later": False}


def test_drafting_run_refuses_to_redraft_into_a_used_directory(tmp_path) -> None:
    used = tmp_path / "coverage-drafts-S"
    used.mkdir()
    (used / "batch.json").write_text("{}")

    with pytest.raises(FileExistsError):
        coverage_drafts.run(Path("."), tmp_path, tmp_path, "drafts", [], stamp="S")
