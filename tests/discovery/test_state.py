import os

import pytest
from discovery_fakes import Harness, seed_corpus

from faa_directive_impact.acquisition.storage import RawStorage
from faa_directive_impact.discovery.state import (
    SNAPSHOT_EVERY,
    RecordStoreError,
    generation_path,
    read_active,
    read_generation,
    read_json,
    record_path,
    write_active,
    write_generation,
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


def record(number: str, published: str, title: str = "AD") -> dict:
    return {"document_number": number, "publication_date": published, "title": title}


def generation(generation_id: str, previous: str | None, records: list) -> dict:
    return {
        "generation_id": generation_id,
        "previous_generation_id": previous,
        "records": records,
        "review": [],
    }


def test_a_later_generation_stores_only_its_changes(tmp_path):
    storage = RawStorage(tmp_path)
    first = [record("2025-00001", "2025-01-02"), record("2025-00002", "2025-01-03")]
    write_generation(storage, generation("gen-1", None, first))
    second = [
        first[0],
        record("2025-00002", "2025-01-03", "changed"),
        record("2025-00003", "2025-01-04"),
    ]
    write_generation(storage, generation("gen-2", "gen-1", second))

    stored = read_json(tmp_path / generation_path("gen-2"))
    assert stored["delta_from"] == "gen-1"
    assert [r["document_number"] for r in stored["records"]["set"]] == [
        "2025-00002",
        "2025-00003",
    ]
    assert read_generation(tmp_path, "gen-2")["records"] == second
    assert "delta_from" not in read_generation(tmp_path, "gen-2")


def test_a_removed_record_is_gone_after_the_delta(tmp_path):
    storage = RawStorage(tmp_path)
    first = [record("2025-00001", "2025-01-02"), record("2025-00002", "2025-01-03")]
    write_generation(storage, generation("gen-1", None, first))
    write_generation(storage, generation("gen-2", "gen-1", first[:1]))

    assert read_generation(tmp_path, "gen-2")["records"] == first[:1]
    assert read_generation(tmp_path, "gen-1")["records"] == first


def test_a_full_snapshot_bounds_the_delta_chain(tmp_path):
    storage = RawStorage(tmp_path)
    records = [record("2025-00001", "2025-01-02")]
    write_generation(storage, generation("gen-0", None, records))
    for index in range(1, SNAPSHOT_EVERY + 1):
        records = records + [record(f"2025-{index + 1:05d}", "2025-01-03")]
        write_generation(
            storage, generation(f"gen-{index}", f"gen-{index - 1}", records)
        )

    deltas = [
        "delta_from" in read_json(tmp_path / generation_path(f"gen-{i}"))
        for i in range(SNAPSHOT_EVERY + 1)
    ]
    assert deltas[0] is False and deltas[SNAPSHOT_EVERY] is False
    assert all(deltas[1:SNAPSHOT_EVERY])
    assert read_generation(tmp_path, f"gen-{SNAPSHOT_EVERY}")["records"] == records
