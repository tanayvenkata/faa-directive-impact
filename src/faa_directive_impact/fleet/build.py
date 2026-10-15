"""Read the fleet's inputs from the repository and write its recorded outputs.

``write_fleet`` regenerates ``demo/fleet.json`` and ``demo/fleet-screen.json``
offline from committed inputs only: the seed cases, the retrieval corpus, the
normalized record kept with the S1 run, and the reference rule records. CI
renders the page from the committed screen and never regenerates it.
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
RETRIEVAL_CORPUS = Path("evaluation/retrieval/corpus.json")
# Directives with a rule record the interpreter can apply. Each is
# not_yet_evaluated: its seed labels are Claude drafts.
RULE_RECORDS = {"2026-16954": Path("evaluation/b3/reference/2026-16954.json")}
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
        _read(repo / HPT_HUB_RECORD),
        {document: _read(repo / path) for document, path in RULE_RECORDS.items()},
        _read(repo / RETRIEVAL_CORPUS),
    )
    return fleet, screened


def _read(path: Path) -> Any:
    return json.loads(path.read_text(encoding="utf-8"))


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
