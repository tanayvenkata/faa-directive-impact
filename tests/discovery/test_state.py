import os

import pytest
from discovery_fakes import Harness, seed_corpus

from faa_directive_impact.discovery.state import (
    RecordStoreError,
    read_active,
    read_generation,
    record_path,
    write_active,
)


def test_active_pointer_is_replaced_whole(tmp_path):
    write_active(tmp_path, {"generation_id": "gen-1", "checkpoint": "2026-09-01"})
    write_active(tmp_path, {"generation_id": "gen-2", "checkpoint": "2026-09-02"})

    assert read_active(tmp_path)["generation_id"] == "gen-2"
    assert sorted(os.listdir(tmp_path)) == ["active.json"]


def test_unchanged_records_are_stored_once_across_generations(tmp_path):
    harness = Harness(tmp_path / "discovery")
    corpus = seed_corpus()
    harness.sync(corpus)
    stored = set((harness.root / "records").rglob("*.json"))
    corpus.add("2026-18800", "2026-09-15", ad_number="2026-19-01")

    second = harness.sync(corpus)

    added = set((harness.root / "records").rglob("*.json")) - stored
    assert len(added) == 1
    assert len(harness.generation(second)["records"]) == 6


def test_an_altered_record_is_refused(tmp_path):
    harness = Harness(tmp_path / "discovery")
    attempt = harness.sync(seed_corpus())
    raw = (
        harness.root / "generations" / f"{attempt['generation_id']}.json"
    ).read_text()
    digest = raw.split('"record_sha256": "')[1].split('"')[0]
    path = harness.root / record_path(digest)
    path.chmod(0o644)
    path.write_text(path.read_text().replace("Airworthiness", "Airworthy"))

    with pytest.raises(RecordStoreError):
        read_generation(harness.root, attempt["generation_id"])
