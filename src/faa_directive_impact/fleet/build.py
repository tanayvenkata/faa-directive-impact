"""Read the fleet's inputs from the repository and write its recorded outputs.

``write_fleet`` regenerates ``demo/fleet.json`` and ``demo/fleet-screen.json``
offline from committed inputs only: the seed cases, the Registry summary, the
retrieval corpus, the normalized record kept with the S1 run, and the
reference rule records. CI renders the page from the committed screen and
never regenerates it.
"""

import json
from pathlib import Path
from typing import Any

import yaml

from faa_directive_impact.fleet.generate import build_fleet
from faa_directive_impact.fleet.screen import S1_DOCUMENT, screen_fleet

SEED_CASES = Path("evaluation/seed/cases")
REGISTRY_FILE = Path("demo/registry-v2500.json")
HPT_HUB_RECORD = Path(
    "evaluation/runs/s1-20261006T223638Z-6a301b1/normalized-record.json"
)
RETRIEVAL_CORPUS = Path("evaluation/retrieval/corpus.json")
# One rule record per in-scope directive (evaluation/coverage/PREREGISTRATION.md,
# deviation 2). AD 2025-19-13 is screened by S1; its record here only gives
# the fleet generator its applicability and effective date.
RULE_RECORDS = Path("evaluation/coverage/reference")
FLEET_FILE = Path("demo/fleet.json")
FLEET_SCREEN_FILE = Path("demo/fleet-screen.json")


def load_inputs(repo: Path) -> dict[str, Any]:
    return {
        "cases": [
            yaml.safe_load(path.read_text(encoding="utf-8"))
            for path in sorted((repo / SEED_CASES).glob("seed-*.yaml"))
        ],
        "registry": _read(repo / REGISTRY_FILE),
        "corpus": _read(repo / RETRIEVAL_CORPUS),
        "references": {
            path.stem: _read(path)
            for path in sorted((repo / RULE_RECORDS).glob("*.json"))
        },
        "hpt_hub_record": _read(repo / HPT_HUB_RECORD),
    }


def corpus_identifiers(corpus: dict[str, Any]) -> set[str]:
    """Every identifier printed in any directive of the retrieval corpus."""
    return {token for record in corpus["records"] for token in record["identifiers"]}


def compute_fleet(repo: Path) -> tuple[dict[str, Any], dict[str, Any]]:
    inputs = load_inputs(repo)
    fleet = build_fleet(
        inputs["cases"],
        inputs["registry"],
        list(inputs["references"].values()),
        corpus_identifiers(inputs["corpus"]),
    )
    screened = screen_fleet(
        fleet,
        inputs["hpt_hub_record"],
        {
            document: record
            for document, record in inputs["references"].items()
            if document != S1_DOCUMENT
        },
        inputs["corpus"],
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
