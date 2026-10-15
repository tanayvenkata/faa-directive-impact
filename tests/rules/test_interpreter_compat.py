"""Interpreter v2 leaves every version 1 output unchanged.

Preregistration (evaluation/coverage/PREREGISTRATION.md, "Rules"): S1's
outputs, the B3 v1 replays, and the current AD 2026-17-03 fleet screens must
not change. S1 does not import the interpreter, but a fresh S1 run is still
compared byte for byte with the committed run's outputs.json.
"""

import hashlib
import json
from datetime import UTC, date, datetime
from pathlib import Path

import pytest

from faa_directive_impact.evaluation.s1_run import run_s1
from faa_directive_impact.evaluation.seed import load_seed_cases
from faa_directive_impact.fleet.build import compute_fleet, dump
from faa_directive_impact.rules.interpreter import INTERPRETER_VERSION, screen_rules

REPO = Path(__file__).resolve().parents[2]
GOLDEN = REPO / "tests/fixtures/rules/interpreter-v1-outputs.json"
S1_RUN = REPO / "evaluation/runs/s1-20261006T223638Z-6a301b1"
B3_RUNS = sorted((REPO / "evaluation/runs").glob("b3-opus-5-5-high-r*"))
# sha256 of demo/fleet-screen.json as committed before interpreter v2, with
# its "interpreter_version" field removed (that field is the only change).
FLEET_SCREEN_V1_SHA256 = (
    "8eea704142a18bbe9a4076d8f3ef29b8a5780448af7df00269ed57a15f5b1043"
)


def seed_cases() -> dict[str, dict]:
    return {
        c.record["case_id"]: c.record
        for c in load_seed_cases(REPO / "evaluation/seed/cases")
    }


def as_of(case: dict) -> date:
    return date.fromisoformat(case["source_snapshot"]["as_of"])


def plain(screen) -> dict:
    return json.loads(json.dumps(screen.to_dict()))


def test_version_is_two() -> None:
    assert INTERPRETER_VERSION == 2


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


def test_fleet_screens_are_unchanged_apart_from_the_version_field() -> None:
    _, screened = compute_fleet(REPO)
    assert screened.pop("interpreter_version") == INTERPRETER_VERSION
    digest = hashlib.sha256(dump(screened).encode("utf-8")).hexdigest()
    assert digest == FLEET_SCREEN_V1_SHA256


def test_s1_outputs_are_byte_identical_to_the_committed_run(tmp_path: Path) -> None:
    started = datetime(2026, 10, 15, 12, 0, tzinfo=UTC)
    directory = run_s1(REPO, tmp_path, started, "0" * 40, dirty=False)
    assert (directory / "outputs.json").read_bytes() == (
        S1_RUN / "outputs.json"
    ).read_bytes()
