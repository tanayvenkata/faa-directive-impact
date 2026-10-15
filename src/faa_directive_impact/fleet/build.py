"""Read the fleet's inputs from the repository and write its recorded outputs.

``write_fleet`` regenerates ``demo/fleet.json`` and ``demo/fleet-screen.json``
offline from committed inputs only: the seed cases, the normalized record kept
with the S1 run, and the AD 2026-17-03 reference rule record. CI renders the
page from the committed screen and never regenerates it.
"""

import json
from pathlib import Path
from typing import Any

import yaml

from faa_directive_impact.fleet.generate import build_fleet
from faa_directive_impact.fleet.screen import screen_fleet

SEED_CASES = Path("evaluation/seed/cases")
HPT_HUB_RECORD = Path(
    "evaluation/runs/s1-20261006T223638Z-6a301b1/normalized-record.json"
)
HPC_BLADE_RULES = Path("evaluation/b3/reference/2026-16954.json")
FLEET_FILE = Path("demo/fleet.json")
FLEET_SCREEN_FILE = Path("demo/fleet-screen.json")


def compute_fleet(repo: Path) -> tuple[dict[str, Any], dict[str, Any]]:
    cases = [
        yaml.safe_load(path.read_text(encoding="utf-8"))
        for path in sorted((repo / SEED_CASES).glob("seed-*.yaml"))
    ]
    fleet = build_fleet(cases)
    screened = screen_fleet(
        fleet,
        json.loads((repo / HPT_HUB_RECORD).read_text(encoding="utf-8")),
        json.loads((repo / HPC_BLADE_RULES).read_text(encoding="utf-8")),
    )
    return fleet, screened


def dump(value: Any) -> str:
    return json.dumps(value, indent=2, sort_keys=True, ensure_ascii=False) + "\n"


def write_fleet(repo: Path) -> list[Path]:
    fleet, screened = compute_fleet(repo)
    written = []
    for path, value in ((FLEET_FILE, fleet), (FLEET_SCREEN_FILE, screened)):
        target = repo / path
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text(dump(value), encoding="utf-8")
        written.append(target)
    return written
