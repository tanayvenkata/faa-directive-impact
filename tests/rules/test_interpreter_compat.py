"""Interpreter v2 leaves every version 1 output unchanged.

Preregistration (evaluation/coverage/PREREGISTRATION.md, "Rules"): S1's
outputs, the B3 v1 replays, and the current AD 2026-17-03 fleet screens must
not change. S1 does not import the interpreter, but a fresh S1 run is still
compared byte for byte with the committed run's outputs.json.
"""

import json
from datetime import UTC, date, datetime
from pathlib import Path

import pytest

from faa_directive_impact.evaluation.s1_run import run_s1
from faa_directive_impact.evaluation.seed import load_seed_cases
from faa_directive_impact.rules.interpreter import INTERPRETER_VERSION, screen_rules

REPO = Path(__file__).resolve().parents[2]
GOLDEN = REPO / "tests/fixtures/rules/interpreter-v1-outputs.json"
S1_RUN = REPO / "evaluation/runs/s1-20261006T223638Z-6a301b1"
B3_RUNS = sorted((REPO / "evaluation/runs").glob("b3-opus-5-5-high-r*"))
# The pre-v2 demo fleet's engines and their interpreter v1 outputs, frozen
# so the demo fleet can be regenerated without touching this check. When it
# was frozen, the live fleet screen matched the committed v1 screen (sha256
# 8eea7041..., version field removed).
FLEET_V1 = REPO / "tests/fixtures/rules/fleet-v1-screens.json"


def seed_cases() -> dict[str, dict]:
    return {
        c.record["case_id"]: c.record
        for c in load_seed_cases(REPO / "evaluation/seed/cases")
    }


def as_of(case: dict) -> date:
    return date.fromisoformat(case["source_snapshot"]["as_of"])


def plain(screen) -> dict:
    return json.loads(json.dumps(screen.to_dict()))


def test_version_is_three() -> None:
    assert INTERPRETER_VERSION == 3  # v1 records are unaffected (golden file)


def test_v1_reference_records_give_byte_identical_outputs_on_every_seed_asset() -> None:
    golden = json.loads(GOLDEN.read_text())
    cases = seed_cases()
    references = {
        p.stem: json.loads(p.read_text())
        for p in (REPO / "evaluation/b3/reference").glob("*.json")
    }
    assert len(golden) == len(cases) * len(references)
    for key, expected in golden.items():
        case_id, document = key.split("/")
        case = cases[case_id]
        got = plain(
            screen_rules(references[document], case["asset_snapshot"], as_of(case))
        )
        assert got == expected, key


@pytest.mark.parametrize("run", B3_RUNS, ids=lambda p: p.name)
def test_b3_v1_drafts_replay_to_the_recorded_outputs(run: Path) -> None:
    cases = seed_cases()
    recorded = json.loads((run / "units.json").read_text())
    assert recorded
    for unit in recorded:
        draft = json.loads(
            (run / "extractions" / f"{unit['directive']}.json").read_text()
        )
        case = cases[unit["unit"].split("/")[0]]
        got = plain(screen_rules(draft, case["asset_snapshot"], as_of(case)))
        assert got == unit["output"], (run.name, unit["unit"])


def test_frozen_fleet_engines_give_byte_identical_v1_outputs() -> None:
    frozen = json.loads(FLEET_V1.read_text())
    references = {
        p.stem: json.loads(p.read_text())
        for p in (REPO / "evaluation/b3/reference").glob("*.json")
    }
    assert len(frozen["engines"]) == 200
    for engine in frozen["engines"]:
        as_of = date.fromisoformat(engine["as_of"])
        for document, expected in engine["v1_outputs"].items():
            got = plain(screen_rules(references[document], engine["asset"], as_of))
            assert got == expected, (engine["asset"]["engine"]["asset_id"], document)


def test_s1_outputs_are_byte_identical_to_the_committed_run(tmp_path: Path) -> None:
    started = datetime(2026, 10, 15, 12, 0, tzinfo=UTC)
    directory = run_s1(REPO, tmp_path, started, "0" * 40, dirty=False)
    assert (directory / "outputs.json").read_bytes() == (
        S1_RUN / "outputs.json"
    ).read_bytes()
