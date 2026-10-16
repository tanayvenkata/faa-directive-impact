import json
from pathlib import Path

import pytest

from faa_directive_impact.fleet.build import FLEET_REPLAY_FILE, compute_replay, dump
from faa_directive_impact.fleet.replay import (
    REPLAY_DATES,
    REPLAY_DIRECTIVE,
    engine_as_of,
)

REPO = Path(__file__).resolve().parents[2]


def _fleet():
    return json.loads((REPO / "demo/fleet.json").read_text(encoding="utf-8"))


def _replay():
    if not hasattr(_replay, "value"):
        _replay.value = compute_replay(REPO, _fleet())
    return _replay.value


def engine(**component):
    return {
        "engine": {
            "asset_id": "SYN-TEST",
            "snapshot_at": "2026-10-12",
            "engine_cycle_readings": [
                {"at": "2025-10-29", "engine_flight_cycles": 14715},
                {"at": "2026-10-12", "engine_flight_cycles": 16143},
            ],
        },
        "events": [
            {"at": "2025-01-05", "event_type": "shop_visit_induction"},
            {"at": "2026-03-01", "event_type": "shop_visit_induction"},
        ],
        "installed_components": [
            {
                "component_name": "HPT 1st-stage hub",
                "installed_at": "2025-10-15",
                "cycles_since_new": 4191,
                "cycles_since_new_readings": [
                    {"at": "2025-10-29", "cycles_since_new": 2763},
                    {"at": "2026-09-24", "cycles_since_new": 4117},
                ],
                **component,
            }
        ],
    }


def test_engine_as_of_keeps_only_what_was_known_then():
    rolled = engine_as_of(engine(), "2025-10-29")

    assert rolled["engine"]["snapshot_at"] == "2025-10-29"
    assert [e["at"] for e in rolled["events"]] == ["2025-01-05"]
    assert [r["at"] for r in rolled["engine"]["engine_cycle_readings"]] == [
        "2025-10-29"
    ]
    hub = rolled["installed_components"][0]
    assert hub["cycles_since_new"] == 2763
    assert [r["at"] for r in hub["cycles_since_new_readings"]] == ["2025-10-29"]


def test_component_cycles_are_unknown_before_their_first_reading():
    hub = engine_as_of(engine(), "2025-10-28")["installed_components"][0]

    assert hub["cycles_since_new"] is None


def test_engine_as_of_refuses_a_part_installed_after_the_date():
    with pytest.raises(ValueError, match="installed after"):
        engine_as_of(engine(installed_at="2026-02-16"), "2025-10-29")


def test_committed_replay_matches_a_fresh_regeneration():
    assert (REPO / FLEET_REPLAY_FILE).read_text(encoding="utf-8") == dump(_replay())


def test_replay_leaves_out_exactly_the_engines_it_cannot_roll_back():
    replay = _replay()
    generated = [e for e in _fleet()["engines"] if "evaluation_case" not in e]
    late = {
        e["engine"]["asset_id"]
        for e in generated
        if any(
            (c.get("installed_at") or "") > REPLAY_DATES[0]
            for c in e["installed_components"]
        )
    }
    assert set(replay["left_out"]) == late
    assert replay["replayed_engines"] == len(generated) - len(late)
    for day in REPLAY_DATES:
        engines = replay["states"][day]["engines"]
        assert len(engines) == replay["replayed_engines"]
        assert not late & set(engines)


def test_nothing_is_queued_before_the_directive_takes_effect():
    replay = _replay()
    before = replay["states"][REPLAY_DATES[0]]["engines"].values()
    assert {e["queue"] for e in before} == {"no_action_or_not_applicable"}
    assert all("does not take effect until" in e["summary"] for e in before)


def test_every_moved_engine_is_queued_on_the_effective_date():
    replay = _replay()
    after = replay["states"][REPLAY_DATES[1]]["engines"]
    assert replay["directive"] == REPLAY_DIRECTIVE
    assert replay["moved"]
    for asset_id in replay["moved"]:
        assert after[asset_id]["queue"] in ("potentially_affected", "needs_review")
    unmoved = set(after) - set(replay["moved"])
    assert {after[a]["queue"] for a in unmoved} == {"no_action_or_not_applicable"}
