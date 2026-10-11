"""Offline syncs of the discovery corpus against a fake Federal Register."""

import json

import httpx
import pytest
from discovery_fakes import IAE, Harness, seed_corpus

from faa_directive_impact.acquisition.retrieval import build_client
from faa_directive_impact.discovery import sync as sync_module
from faa_directive_impact.discovery.state import (
    StorageRootRefused,
    read_active,
    read_attempts,
    read_decisions,
    require_discovery_root,
)
from faa_directive_impact.discovery.sync import RollbackError, rollback, run_sync


@pytest.fixture
def harness(tmp_path) -> Harness:
    return Harness(tmp_path / "discovery")


def test_first_sync_promotes_with_coverage_states_and_links(harness):
    attempt = harness.sync(seed_corpus())

    assert attempt["outcome"] == "promoted", attempt["failures"]
    active = read_active(harness.root)
    assert active["generation_id"] == attempt["generation_id"]
    assert active["previous_generation_id"] is None
    assert active["checkpoint"] == "2026-09-12"
    generation = harness.generation(attempt)
    records = harness.records(generation)
    assert {n: r["coverage_state"] for n, r in records.items()} == {
        "2025-18469": "evaluated",
        "2026-16954": "not_yet_evaluated",
        "2026-18423": "not_yet_evaluated",
        "2026-18500": "outside_supported_scope",
        "2026-18600": "outside_supported_scope",
    }
    assert records["2026-18600"]["scope"]["basis"] == "title"
    assert records["2026-18500"]["scope"]["basis"] == "applicability_paragraph"
    assert "full_text_xml" in records["2026-16954"]["evidence"]
    assert "full_text_xml" not in records["2026-18600"]["evidence"]
    [link] = generation["relationships"]
    assert link["relationship_type"] == "corrects"
    assert link["from_identity"]["value"] == "2026-18423"
    assert link["to_identity"]["value"] == "2026-16954"
    assert link["confidence_class"] == "identifier_join"
    assert generation["validation"]["status"] == "passed"
    assert generation["corpus_track"] == "refreshable_discovery"
    assert any(
        d["name"].startswith("IAE NMSB") and d["availability_status"] == "unavailable"
        for d in generation["dependencies"]
    )
    [decision] = read_decisions(harness.root)
    assert decision["receipt_type"] == "promotion"
    assert attempt["counts"]["new"] == 5 and attempt["counts"]["read_in_full"] == 4


def test_rerun_with_the_same_responses_changes_nothing(harness):
    corpus = seed_corpus()
    first = harness.sync(corpus)
    generations = sorted((harness.root / "generations").iterdir())

    second = harness.sync(corpus)

    assert second["outcome"] == "no_change"
    # The search re-reads the week before the checkpoint (2026-09-12).
    assert {k: v for k, v in second["counts"].items() if v} == {
        "searched": 3,
        "unchanged": 3,
    }
    assert read_active(harness.root)["generation_id"] == first["generation_id"]
    assert sorted((harness.root / "generations").iterdir()) == generations
    assert len(read_attempts(harness.root)) == 2


def test_checkpoint_window_is_searched_again_and_deduplicated(harness):
    corpus = seed_corpus()
    first = harness.sync(corpus)
    corpus.add("2026-18700", "2026-09-12", ad_number="2026-18-30")
    corpus.add("2026-18800", "2026-09-15", ad_number="2026-19-01")

    second = harness.sync(corpus)

    assert second["outcome"] == "promoted", second["failures"]
    assert second["since"] == "2026-09-05"  # checkpoint less the lookback
    assert second["counts"]["unchanged"] == 3
    assert second["new_documents"] == ["2026-18700", "2026-18800"]
    generation = harness.generation(second)
    numbers = [r["document_number"] for r in generation["records"]]
    assert len(numbers) == len(set(numbers)) == 7
    assert generation["previous_generation_id"] == first["generation_id"]
    assert read_active(harness.root)["checkpoint"] == "2026-09-15"


def test_unexpected_metadata_change_rejects_and_keeps_active(harness):
    corpus = seed_corpus()
    first = harness.sync(corpus)
    corpus.entries[-1]["title"] = "Airworthiness Directives; Airbus SAS Airplanes v2"
    corpus.add("2026-18800", "2026-09-15", ad_number="2026-19-01")

    rejected = harness.sync(corpus)

    assert rejected["outcome"] == "rejected"
    assert any("2026-18600" in failure for failure in rejected["failures"])
    active = read_active(harness.root)
    assert active["generation_id"] == first["generation_id"]
    assert active["checkpoint"] == "2026-09-12"
    decision = read_decisions(harness.root)[-1]
    assert decision["receipt_type"] == "rejection"
    assert decision["previous_generation_id"] == first["generation_id"]
    assert decision["reasons"]

    accepted = harness.sync(corpus, accept_changed=frozenset({"2026-18600"}))

    assert accepted["outcome"] == "promoted", accepted["failures"]
    record = harness.records(harness.generation(accepted))["2026-18600"]
    assert [v.get("change") for v in record["versions"]] == [
        None,
        "accepted_by_operator",
    ]
    original = harness.records(harness.generation(first))["2026-18600"]
    assert original["title"] == "Airworthiness Directives; Airbus SAS Airplanes"


def test_a_new_correction_on_an_original_is_an_expected_change(harness):
    corpus = seed_corpus()
    harness.sync(corpus)
    original = next(e for e in corpus.entries if e["document_number"] == "2026-18600")
    original["corrections"] = [
        "https://www.federalregister.gov/api/v1/documents/C1-2026-18600"
    ]

    attempt = harness.sync(corpus)

    assert attempt["outcome"] == "promoted", attempt["failures"]
    record = harness.records(harness.generation(attempt))["2026-18600"]
    assert record["versions"][-1]["change"] == "corrections_added"


def test_partial_acquisition_failure_rejects(harness):
    corpus = seed_corpus()
    pdf = next(url for url in corpus.pages if url.endswith("2026-16954.pdf"))
    corpus.pages[pdf] = None

    attempt = harness.sync(corpus)

    assert attempt["outcome"] == "rejected"
    assert attempt["counts"]["failed"] == 1
    assert any("2026-16954" in failure for failure in attempt["failures"])
    assert read_active(harness.root) is None
    assert read_decisions(harness.root)[-1]["receipt_type"] == "rejection"


def test_failed_search_rejects_and_keeps_active(harness):
    corpus = seed_corpus()
    first = harness.sync(corpus)
    handler = lambda request: httpx.Response(503)  # noqa: E731
    with build_client(transport=httpx.MockTransport(handler)) as client:
        attempt = run_sync(harness.root, client, clock=harness.clock)

    assert attempt["outcome"] == "rejected"
    assert read_active(harness.root)["generation_id"] == first["generation_id"]


def test_unclassifiable_iae_directive_is_quarantined_not_in_scope(harness):
    corpus = seed_corpus()
    corpus.add("2026-18900", "2026-09-12", IAE, "2026-18-40", None)

    attempt = harness.sync(corpus)

    assert attempt["outcome"] == "promoted", attempt["failures"]
    generation = harness.generation(attempt)
    assert "2026-18900" not in harness.records(generation)
    [held] = generation["review"]
    assert held["document_number"] == "2026-18900"
    assert held["coverage_state"] == "outside_supported_scope"
    assert attempt["counts"]["quarantined"] == 1


def test_rollback_returns_to_the_previous_generation(harness):
    corpus = seed_corpus()
    first = harness.sync(corpus)
    corpus.add("2026-18800", "2026-09-15", ad_number="2026-19-01")
    second = harness.sync(corpus)

    pointer = rollback(harness.root, clock=harness.clock)

    assert pointer["generation_id"] == first["generation_id"]
    assert read_active(harness.root)["checkpoint"] == "2026-09-12"
    decision = read_decisions(harness.root)[-1]
    assert decision["receipt_type"] == "rollback"
    assert decision["previous_generation_id"] == second["generation_id"]
    with pytest.raises(RollbackError):
        rollback(harness.root, clock=harness.clock)

    again = harness.sync(corpus)

    assert again["outcome"] == "promoted"
    assert again["new_documents"] == ["2026-18800"]


def test_rollback_refuses_a_generation_that_was_never_promoted(harness):
    corpus = seed_corpus()
    harness.sync(corpus)
    corpus.entries[-1]["title"] = "changed"
    rejected = harness.sync(corpus)

    with pytest.raises(RollbackError):
        rollback(harness.root, to_generation=rejected["generation_id"])


def test_a_crash_is_still_logged(harness, monkeypatch):
    def explode(*args, **kwargs):
        raise RuntimeError("boom")

    monkeypatch.setattr(sync_module, "search_directives", explode)

    attempt = harness.sync(seed_corpus())

    assert attempt["outcome"] == "error"
    assert read_attempts(harness.root)[-1]["failures"] == ["RuntimeError: boom"]


def test_sync_writes_only_under_its_root(tmp_path, harness):
    harness.sync(seed_corpus())

    assert sorted(p.name for p in tmp_path.iterdir()) == ["discovery"]
    for path in harness.root.rglob("*.json"):
        json.loads(path.read_text())


@pytest.mark.parametrize(
    "parts",
    [("data", "seed-frozen"), ("data", "frozen-evaluation", "x"), ("generations",)],
)
def test_frozen_roots_are_refused(tmp_path, parts):
    with pytest.raises(StorageRootRefused):
        require_discovery_root(tmp_path.joinpath(*parts))


def test_a_directory_holding_frozen_corpora_is_refused(tmp_path):
    (tmp_path / "data" / "seed-frozen").mkdir(parents=True)

    with pytest.raises(StorageRootRefused):
        require_discovery_root(tmp_path / "data")
    assert require_discovery_root(tmp_path / "data" / "discovery")


def test_federal_register_corrections_link_by_correction_of(harness):
    corpus = seed_corpus()
    republished = corpus.add("R1-2026-18600", "2026-09-12", ad_number="2026-18-20")
    republished["correction_of"] = (
        "https://www.federalregister.gov/api/v1/documents/2026-18600"
    )
    corpus.add("C1-2026-16954", "2026-09-12", IAE, "2026-17-03")

    attempt = harness.sync(corpus)

    assert attempt["outcome"] == "promoted", attempt["failures"]
    generation = harness.generation(attempt)
    assert harness.records(generation)["R1-2026-18600"]["kind"] == "correction"
    assert {
        (r["from_identity"]["value"], r["to_identity"]["value"], r["confidence_class"])
        for r in generation["relationships"]
    } == {
        ("2026-18423", "2026-16954", "identifier_join"),
        ("R1-2026-18600", "2026-18600", "source_asserted"),
    }
    [held] = generation["review"]
    assert held["document_number"] == "C1-2026-16954"
