"""Screen the fleet as of past dates: the replay behind the fleet page.

The daily sync began on 2026-10-11, after both evaluated directives took
effect, so the system never watched one go live. The replay re-screens the
generated engines as they stood on a past date: real screen output, but a
replay, and the page says so.

The rules are today's (the S1 record and the rule records as committed), so
the replay applies them to the fleet as it stood, including FAA
correspondence received later. An engine's state as of a date keeps only
what was known then. Events,
engine cycle readings, and component cycle readings after the date are
dropped, and each component's ``cycles_since_new`` becomes its latest
reading on or before the date (unknown if there is none). A component
installed after the date cannot be rolled back, because the fleet does not
record what it replaced, so the replay refuses rather than guess.

Evaluation-case engines are left out: each keeps its own case date and is a
test fixture, not part of the fleet's history.
"""

import copy
from collections import Counter
from typing import Any

from faa_directive_impact.fleet.screen import S1_DOCUMENT, screen_fleet

# AD 2025-19-13 took effect on 2025-10-29: the day before, and the day itself.
REPLAY_DIRECTIVE = S1_DOCUMENT
REPLAY_DATES = ("2025-10-28", "2025-10-29")
SCREEN_FIELDS = (
    "applicability",
    "action_status",
    "queue",
    "summary",
    "timing",
    "missing_facts",
    "citations",
    "hubs",
)


def engine_as_of(engine: dict[str, Any], day: str) -> dict[str, Any]:
    """The engine record as it stood on ``day`` (ISO date)."""
    rolled = copy.deepcopy(engine)
    rolled["engine"]["snapshot_at"] = day
    rolled["events"] = [
        event for event in rolled.get("events", []) if (event.get("at") or "") <= day
    ]
    rolled["engine"]["engine_cycle_readings"] = [
        reading
        for reading in rolled["engine"].get("engine_cycle_readings", [])
        if reading["at"] <= day
    ]
    for component in rolled.get("installed_components", []):
        if (component.get("installed_at") or "") > day:
            raise ValueError(
                f"{rolled['engine']['asset_id']}: {component.get('component_name')} "
                f"was installed after {day}; the part it replaced is not recorded"
            )
        if "cycles_since_new_readings" in component:
            readings = [
                reading
                for reading in component["cycles_since_new_readings"]
                if reading["at"] <= day
            ]
            component["cycles_since_new_readings"] = readings
            component["cycles_since_new"] = (
                readings[-1]["cycles_since_new"] if readings else None
            )
    return rolled


def replay_fleet(
    fleet: dict[str, Any],
    hpt_hub_record: dict[str, Any],
    rule_records: dict[str, dict[str, Any]],
    corpus: dict[str, Any],
    rule_sources: dict[str, str] | None = None,
) -> dict[str, Any]:
    """Screen the generated engines as of each replay date.

    Engines with a component installed after the first replay date cannot
    be rolled back, so they are left out and listed under ``left_out``.
    """
    generated = [e for e in fleet["engines"] if "evaluation_case" not in e]
    first_day = REPLAY_DATES[0]
    left_out = sorted(
        e["engine"]["asset_id"]
        for e in generated
        if any(
            (c.get("installed_at") or "") > first_day
            for c in e.get("installed_components", [])
        )
    )
    replayable = [e for e in generated if e["engine"]["asset_id"] not in left_out]
    states = {}
    for day in REPLAY_DATES:
        snapshot = {**fleet, "engines": [engine_as_of(e, day) for e in replayable]}
        screened = screen_fleet(
            snapshot, hpt_hub_record, rule_records, corpus, rule_sources=rule_sources
        )
        engines = {}
        for entry in screened["engines"]:
            screen = entry["screens"].get(REPLAY_DIRECTIVE)
            if screen is None:
                continue
            engines[entry["asset"]["engine"]["asset_id"]] = {
                field: screen.get(field) for field in SCREEN_FIELDS
            }
        states[day] = {
            "counts": dict(
                sorted(Counter(e["queue"] for e in engines.values()).items())
            ),
            "engines": engines,
        }
    first, last = REPLAY_DATES
    moved = sorted(
        engine
        for engine, screen in states[last]["engines"].items()
        if states[first]["engines"].get(engine, {}).get("queue") != screen["queue"]
    )
    return {
        "directive": REPLAY_DIRECTIVE,
        "dates": list(REPLAY_DATES),
        "generated_engines": len(generated),
        "replayed_engines": len(replayable),
        "kind": "as-of replay, not a live event",
        "rules": (
            "The fleet's state as of each date, screened with today's rules, "
            "including FAA correspondence received after that date. It shows "
            "what today's screen says about the fleet as it stood then, not "
            "what a screen would have said at the time."
        ),
        "left_out": left_out,
        "left_out_reason": (
            f"A life-limited part was replaced after {first_day}; the fleet does "
            "not record the part it replaced, so the engine's state then is unknown."
        ),
        "moved": moved,
        "states": states,
    }
