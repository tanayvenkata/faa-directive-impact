"""The fleet page over the committed screen, replay, and fleet."""

import json
import re
from pathlib import Path

from faa_directive_impact.fleet.build import (
    FLEET_FILE,
    FLEET_REPLAY_FILE,
    FLEET_SCREEN_FILE,
)
from faa_directive_impact.fleet.page import (
    FORBIDDEN_WORDS,
    build_fleet_page,
    render_fleet_page,
)

REPO = Path(__file__).resolve().parents[2]


def _read(path):
    return json.loads((REPO / path).read_text(encoding="utf-8"))


def _page():
    if not hasattr(_page, "value"):
        replay, fleet = _read(FLEET_REPLAY_FILE), _read(FLEET_FILE)
        _page.value = (
            render_fleet_page(_read(FLEET_SCREEN_FILE), replay, fleet),
            replay,
            fleet,
        )
    return _page.value


def _data(page):
    return json.loads(page.split('type="application/json">')[1].split("</script>")[0])


def test_replay_counts_on_the_page_match_the_replay_file():
    page, replay, _ = _page()
    data = _data(page)
    states = {s["key"]: s for s in data["states"]}
    for day in replay["dates"]:
        recorded = replay["states"][day]["counts"]
        assert {k: v for k, v in states[day]["counts"].items() if v} == recorded
    assert sorted(data["movers"]) == replay["moved"]
    assert sum(not e["out"] for e in data["engines"]) == replay["replayed_engines"]
    assert sorted(e["id"] for e in data["engines"] if e["out"]) == replay["left_out"]
    # The headline is written from the recorded counts.
    effective = replay["states"][replay["dates"][-1]]["counts"]
    assert (effective["potentially_affected"], effective["needs_review"]) == (5, 10)
    assert "Five engines must lose a hub, ten need a person" in page
    assert "the screen found all five and no others" in page


def test_movers_are_sorted_by_recorded_cycles_remaining():
    page, replay, _ = _page()
    data = _data(page)
    last = replay["states"][replay["dates"][-1]]["engines"]
    affected = [m for m in data["movers"] if last[m]["queue"] == "potentially_affected"]
    assert data["movers"][: len(affected)] == affected
    remaining = [last[m]["computed"]["component_cycles_remaining"] for m in affected]
    assert remaining == sorted(remaining)
    engines = {e["id"]: e for e in data["engines"]}
    for asset_id in affected:
        assert (
            engines[asset_id]["st"][replay["dates"][-1]]["r"]
            == (last[asset_id]["computed"]["component_cycles_remaining"])
        )


def test_fixtures_are_never_in_the_fleet_tiles_or_movers():
    page, _, fleet = _page()
    data = _data(page)
    fixtures = {
        e["engine"]["asset_id"] for e in fleet["engines"] if "evaluation_case" in e
    }
    assert {f["id"] for f in data["fixtures"]} == fixtures
    assert not fixtures & {e["id"] for e in data["engines"]}
    assert not fixtures & set(data["movers"])
    assert len(data["engines"]) == len(fleet["engines"]) - len(fixtures)
    assert "reuse serial numbers listed in the directive" in " ".join(page.split())


def test_the_day_before_is_labelled_not_yet_in_force():
    page, replay, _ = _page()
    data = _data(page)
    before = data["states"][0]
    assert before["key"] == replay["dates"][0] and not before["in_force"]
    assert all(s["in_force"] for s in data["states"][1:])
    assert "Not yet in force" in page
    # Its recorded text already names the listed hub for the movers it flags.
    named = [
        e["id"]
        for e in data["engines"]
        if not e["out"] and e["st"][before["key"]]["t"] is not None
    ]
    assert named and set(named) <= set(data["movers"])


def test_no_forbidden_word_appears_on_the_page():
    page, _, _ = _page()
    text = page.lower()
    for word in FORBIDDEN_WORDS:
        assert not re.search(rf"\b{re.escape(word)}\b", text), word


def test_banner_says_it_is_a_replay_and_links_the_freshness_page():
    page, replay, _ = _page()
    assert "As-of replay, not live" in page
    assert '<a href="../">directive freshness page</a>' in page
    assert " ".join(replay["rules"].split()) in " ".join(page.split())
    assert "on 95 scored units" in " ".join(page.split())
    assert "across the fleet" not in page


def test_build_writes_the_page_under_fleet(tmp_path):
    replay, fleet = _read(FLEET_REPLAY_FILE), _read(FLEET_FILE)
    path = build_fleet_page(_read(FLEET_SCREEN_FILE), tmp_path, replay, fleet)
    assert path == tmp_path / "fleet" / "index.html"
    assert path.read_text(encoding="utf-8") == _page()[0]
