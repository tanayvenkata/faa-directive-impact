import json
from pathlib import Path

from faa_directive_impact.fleet.build import (
    FLEET_FILE,
    FLEET_SCREEN_FILE,
    compute_fleet,
    dump,
)
from faa_directive_impact.fleet.generate import build_fleet
from faa_directive_impact.fleet.page import render_fleet_page
from faa_directive_impact.fleet.screen import (
    EVALUATED,
    NO_ACTION,
    NOT_YET_EVALUATED,
    QUEUE_ORDER,
)

REPO = Path(__file__).resolve().parents[2]


def _computed():
    if not hasattr(_computed, "value"):
        _computed.value = compute_fleet(REPO)
    return _computed.value


def test_committed_fleet_matches_a_fresh_regeneration():
    fleet, screened = _computed()
    assert (REPO / FLEET_FILE).read_text(encoding="utf-8") == dump(fleet)
    assert (REPO / FLEET_SCREEN_FILE).read_text(encoding="utf-8") == dump(screened)


def test_fleet_generation_is_deterministic():
    assert build_fleet([]) == build_fleet([])
    assert build_fleet([], random_seed=1) != build_fleet([], random_seed=2)


def test_fleet_has_about_two_hundred_synthetic_engines():
    fleet, _ = _computed()
    ids = [engine["engine"]["asset_id"] for engine in fleet["engines"]]
    assert 100 <= len(ids) <= 300
    assert len(set(ids)) == len(ids)
    assert all(asset_id.startswith("SYN-") for asset_id in ids)


def test_seed_assets_are_embedded_unchanged_and_tagged():
    import yaml

    fleet, _ = _computed()
    embedded = {
        engine["evaluation_case"]["case_id"]: engine
        for engine in fleet["engines"]
        if "evaluation_case" in engine
    }
    assert embedded
    for case_id, engine in embedded.items():
        case = yaml.safe_load(
            (REPO / "evaluation/seed/cases" / f"{case_id}.yaml").read_text()
        )
        asset = {k: v for k, v in engine.items() if k != "evaluation_case"}
        assert asset == case["asset_snapshot"]


def test_unknown_hub_serial_goes_to_needs_review():
    _, screened = _computed()
    unknown = [
        engine
        for engine in screened["engines"]
        if "evaluation_case" not in engine["asset"]
        and any(
            c["component_name"].startswith("HPT") and c["serial_number"] == "unknown"
            for c in engine["asset"]["installed_components"]
        )
    ]
    assert unknown
    for engine in unknown:
        assert engine["screens"]["2025-18469"]["queue"] == "needs_review"


def test_only_evaluated_directives_set_the_queue():
    _, screened = _computed()
    assert screened["evaluated_directive"] == "2025-18469"
    for engine in screened["engines"]:
        evaluated = [
            entry["queue"]
            for entry in engine["screens"].values()
            if entry["coverage_state"] == EVALUATED
        ]
        expected = min(evaluated, key=QUEUE_ORDER.index) if evaluated else NO_ACTION
        assert engine["evaluated_queue"] == expected
    counts = screened["evaluated_counts"]
    assert sum(counts.values()) == len(screened["engines"])


def test_candidates_come_from_retrieval_and_unread_ones_need_review():
    _, screened = _computed()
    states = {d["document"]: d["coverage_state"] for d in screened["directives"]}
    assert states["2025-18469"] == EVALUATED
    assert states["2026-16954"] == NOT_YET_EVALUATED
    assert len(states) > 2
    for engine in screened["engines"]:
        retrieved = {c["document"] for c in engine["candidates"]}
        assert set(engine["screens"]) <= retrieved
        for entry in engine["screens"].values():
            if entry["screener"] == "none" and entry["applicability"] == "candidate":
                assert entry["queue"] == "needs_review"


def test_superseded_directive_is_not_queued_for_review():
    _, screened = _computed()
    for engine in screened["engines"]:
        superseded = engine["screens"].get("2021-11960")
        if superseded:
            assert superseded["applicability"] == "superseded"
            assert "2021-11960" not in engine["not_yet_evaluated"]


def test_page_embeds_the_recorded_screen_safely():
    _, screened = _computed()
    page = render_fleet_page(screened)
    assert page.startswith("<!doctype html>")
    assert "__" not in page.split('<script id="fleet-data"')[0]
    data = page.split('type="application/json">')[1].split("</script>")[0]
    assert json.loads(data)["counts"] == screened["evaluated_counts"]
    assert "Screening tool, not a compliance determination" in page
