"""Odd engine records fed to both screens: never a crash, never a clear.

A malformed record must go to needs_review with the bad fields named; it
must never land in the no-action queue. Both screens are run on the same
records: S1 (``screen``) and the rule interpreter (``screen_rules``) on the
hand-written AD 2025-19-13 and AD 2026-17-03 rule records.
"""

import copy
import json
from collections.abc import Callable
from datetime import date
from pathlib import Path

import pytest

from faa_directive_impact.directives.hpt_hub_record import build_record
from faa_directive_impact.evaluation.seed import load_seed_cases
from faa_directive_impact.impact.hpt_hub_rules import (
    engine_record_problems,
    screen,
)
from faa_directive_impact.rules.interpreter import screen_rules

REPO = Path(__file__).resolve().parents[2]
XML = REPO / "tests/fixtures/federal-register/2025-18469/full-text.xml"
GENERATION = REPO / "generations/gen-20260926T215105Z-7fe9da08"
REFERENCE = REPO / "evaluation/b3/reference"
HUB_RULES = json.loads((REFERENCE / "2025-18469.json").read_text())
BLADE_RULES = json.loads((REFERENCE / "2026-16954.json").read_text())
AS_OF = date(2026, 10, 5)
RECORD = build_record(XML.read_bytes(), GENERATION)
CASES = [case.record for case in load_seed_cases(REPO / "evaluation/seed/cases")]


def screens(asset: dict) -> list:
    """The asset through every screen: S1 and the interpreter on both ADs."""
    return [
        screen(RECORD, asset, AS_OF),
        screen_rules(HUB_RULES, asset, AS_OF),
        screen_rules(BLADE_RULES, asset, AS_OF),
    ]


def seed_asset(status: str) -> dict:
    """A seed engine that S1 screens to ``status`` on 2026-10-05."""
    for case in CASES:
        asset = case["asset_snapshot"]
        if screen(RECORD, asset, AS_OF).action_status == status:
            return copy.deepcopy(asset)
    raise AssertionError(f"no seed engine screens to {status}")


MATCHED = seed_asset("action_required")
CLEAR = seed_asset("no_action_triggered")


def hub(asset: dict) -> dict:
    """The installed component S1 matched (or the first one)."""
    result = screen(RECORD, asset, AS_OF)
    names = [h.position for h in result.hubs if h.outcome == "matched"]
    return next(
        c
        for c in asset["installed_components"]
        if not names or c["component_name"] == names[0]
    )


def set_hub(key: str, value) -> Callable[[dict], None]:
    def mutate(asset: dict) -> None:
        hub(asset)[key] = value

    return mutate


def lookalike_serial(asset: dict) -> None:
    # Cyrillic capital A (U+0410) or a fullwidth digit in place of the first
    # ASCII letter or digit: it looks the same and matches no table row.
    component = hub(asset)
    serial = component["serial_number"]
    for index, char in enumerate(serial):
        if char == "A":
            swapped = "А"
        elif char.isdigit():
            swapped = chr(0xFF10 + int(char))
        else:
            continue
        component["serial_number"] = serial[:index] + swapped + serial[index + 1 :]
        return
    raise AssertionError("no character to swap")


def duplicate_position_unlisted_last(asset: dict) -> None:
    component = hub(asset)
    asset["installed_components"].append(
        {**component, "part_number": "9Z9999", "serial_number": "ZZZ00001"}
    )


def set_engine(key: str, value) -> Callable[[dict], None]:
    def mutate(asset: dict) -> None:
        asset["engine"][key] = value

    return mutate


def drop(*path: str) -> Callable[[dict], None]:
    def mutate(asset: dict) -> None:
        target = asset
        for key in path[:-1]:
            target = target[key]
        target.pop(path[-1], None)

    return mutate


def put(key: str, value) -> Callable[[dict], None]:
    def mutate(asset: dict) -> None:
        asset[key] = value

    return mutate


MALFORMED: dict[str, Callable[[dict], None]] = {
    "engine_missing": drop("engine"),
    "engine_not_object": put("engine", "V2527-A5"),
    "engine_model_missing": drop("engine", "engine_model"),
    "engine_model_number": set_engine("engine_model", 2527),
    "engine_model_list": set_engine("engine_model", ["V2527-A5"]),
    "engine_model_empty": set_engine("engine_model", ""),
    "engine_model_fullwidth": set_engine("engine_model", "Ｖ2527-A5"),
    "engine_model_en_dash": set_engine("engine_model", "V2527–A5"),
    "engine_readings_bad_date": set_engine(
        "engine_cycle_readings", [{"at": "15/09/2025", "engine_flight_cycles": 1}]
    ),
    "engine_readings_string_count": set_engine(
        "engine_cycle_readings", [{"at": "2025-10-29", "engine_flight_cycles": "9"}]
    ),
    "components_missing": drop("installed_components"),
    "components_not_list": put("installed_components", {"a": 1}),
    "component_not_object": put("installed_components", ["HPT stage 1 hub"]),
    "part_number_null": set_hub("part_number", None),
    "part_number_number": set_hub("part_number", 2_000_000),
    "part_number_empty": set_hub("part_number", ""),
    "serial_number_null": set_hub("serial_number", None),
    "serial_number_number": set_hub("serial_number", 12345),
    "serial_number_lookalike": lookalike_serial,
    "duplicate_position": duplicate_position_unlisted_last,
    "cycles_boolean": set_hub("cycles_since_new", True),
    "cycles_negative": set_hub("cycles_since_new", -5),
    "cycles_infinite_float": set_hub("cycles_since_new", float("inf")),
    "cycles_word": set_hub("cycles_since_new", "lots"),
    "hub_readings_not_list": set_hub("cycles_since_new_readings", "none"),
    "events_not_list": put("events", "none"),
    "event_bad_date": put(
        "events", [{"event_type": "shop_visit_induction", "at": "yesterday"}]
    ),
    "event_answers_not_map": put(
        "events",
        [
            {
                "event_type": "shop_visit_induction",
                "at": "2026-01-01",
                "qualifies_as_engine_shop_visit": "yes",
            }
        ],
    ),
    "amoc_ad_number": put("amoc_claims", [{"ad": 5}]),
    "ad_record_not_object": put("ad_records", ["complied"]),
}


@pytest.mark.parametrize("base", ["matched", "clear"])
@pytest.mark.parametrize("name", sorted(MALFORMED))
def test_malformed_engine_record_goes_to_review_in_every_screen(name, base):
    asset = copy.deepcopy(MATCHED if base == "matched" else CLEAR)
    MALFORMED[name](asset)

    problems = engine_record_problems(asset)
    results = screens(asset)

    assert problems, name
    for result in results:
        assert result.action_status == "needs_review", (name, result.summary)
        assert result.queue == "needs_review"
        assert result.missing_facts
        assert "malformed" in result.summary
        result.to_dict()  # serializes for the fleet and the run records


@pytest.mark.parametrize("base", [MATCHED, CLEAR])
def test_well_formed_seed_engines_raise_no_problems(base):
    assert engine_record_problems(base) == []


def test_every_seed_engine_is_well_formed():
    assert {
        case["case_id"]: engine_record_problems(case["asset_snapshot"])
        for case in CASES
        if engine_record_problems(case["asset_snapshot"])
    } == {}


def test_every_demo_fleet_engine_is_well_formed():
    fleet = json.loads((REPO / "demo/fleet.json").read_text())
    engines = fleet["engines"] if isinstance(fleet, dict) else fleet
    assets = [e.get("asset", e) for e in engines]
    assert assets
    assert [a["engine"]["asset_id"] for a in assets if engine_record_problems(a)] == []


def test_huge_cycle_counts_screen_without_error():
    asset = copy.deepcopy(MATCHED)
    hub(asset)["cycles_since_new"] = 10**30
    for reading in asset["engine"].get("engine_cycle_readings", []):
        reading["engine_flight_cycles"] += 10**30

    results = screens(asset)

    assert results[0].action_status in ("action_required", "needs_review")
    assert results[0].hubs


def test_empty_component_list_is_review_not_clear():
    asset = copy.deepcopy(CLEAR)
    asset["installed_components"] = []

    for result in screens(asset)[:2]:
        assert result.action_status == "needs_review"


def test_unicode_in_free_text_is_accepted():
    asset = copy.deepcopy(CLEAR)
    asset["engine"]["aircraft_tail_id"] = "N-✈-ÄÖ"
    asset.setdefault("events", []).append(
        {"event_type": "repair", "at": "2026-01-01", "detail": "Réparé ✓ 修理"}
    )

    assert engine_record_problems(asset) == []
    assert screen(RECORD, asset, AS_OF).action_status == "no_action_triggered"


def test_a_snapshot_without_events_screens_in_s1():
    # ``events`` is optional in the seed-case schema; S1 once read it
    # unconditionally once the AD was in force.
    asset = copy.deepcopy(MATCHED)
    asset.pop("events", None)

    result = screen(RECORD, asset, AS_OF)

    assert result.applicability == "applies"
    assert result.action_status in ("action_required", "needs_review")


def test_an_unsupported_model_written_plainly_is_still_outside_scope():
    asset = copy.deepcopy(CLEAR)
    asset["engine"]["engine_model"] = "PW1127G-JM"

    assert engine_record_problems(asset) == []
    assert screen(RECORD, asset, AS_OF).applicability == "outside_supported_scope"


# Version 2 rule records (evaluation/coverage/reference) get the same inputs.
COVERAGE_RULES = {
    path.stem: json.loads(path.read_text())
    for path in sorted((REPO / "evaluation/coverage/reference").glob("*.json"))
}


@pytest.mark.parametrize("base", ["matched", "clear"])
@pytest.mark.parametrize("name", sorted(MALFORMED))
def test_malformed_engine_record_goes_to_review_under_every_v2_record(name, base):
    asset = copy.deepcopy(MATCHED if base == "matched" else CLEAR)
    MALFORMED[name](asset)
    for document, rules in COVERAGE_RULES.items():
        result = screen_rules(rules, asset, AS_OF)
        assert result.action_status == "needs_review", (name, document)
        assert result.queue == "needs_review"
        assert "malformed" in result.summary
        result.to_dict()


@pytest.mark.parametrize("document", sorted(COVERAGE_RULES))
def test_odd_but_well_formed_engines_screen_under_every_v2_record(document):
    rules = COVERAGE_RULES[document]
    empty = copy.deepcopy(MATCHED)
    empty["installed_components"] = []
    huge = copy.deepcopy(MATCHED)
    hub(huge)["cycles_since_new"] = 10**30
    for reading in huge["engine"].get("engine_cycle_readings", []):
        reading["engine_flight_cycles"] += 10**30
    no_events = copy.deepcopy(MATCHED)
    no_events.pop("events", None)
    for asset in (empty, huge, no_events):
        result = screen_rules(rules, asset, AS_OF)
        assert result.queue  # every outcome maps to a queue
        result.to_dict()
    # An empty component list never clears a directive that names parts.
    if rules["applicability"]["parts"]:
        assert screen_rules(rules, empty, AS_OF).action_status in (
            "needs_review",
            None,  # superseded or outside the listed models
        )
