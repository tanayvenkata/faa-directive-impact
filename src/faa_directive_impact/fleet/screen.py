"""Screen the demo fleet against each directive and record two releases.

Two directives are screened, each by the screener that covers it:

- **AD 2025-19-13** (``evaluated``): the S1 rules on the normalized record kept
  with the S1 run. This is the directive the evaluation covers.
- **AD 2026-17-03** (``not_yet_evaluated``): the general rule interpreter on
  its hand-written reference rule record (B3). Its seed labels are Claude
  drafts no person has confirmed, so its results never count as evaluated.

The fleet view replays two releases of the rule set: the first with AD
2025-19-13 alone, the second with AD 2026-17-03 added. Both are computed here
from the same fleet; the page only renders them.
"""

import hashlib
import json
from dataclasses import asdict
from datetime import date
from typing import Any

from faa_directive_impact.impact.hpt_hub_rules import QUEUES, Screen, screen
from faa_directive_impact.rules.interpreter import (
    INTERPRETER_VERSION,
    screen_rules,
)

SCREEN_VERSION = 1
EVALUATED = "evaluated"
NOT_YET_EVALUATED = "not_yet_evaluated"
POTENTIALLY_AFFECTED = "potentially_affected"
NEEDS_REVIEW = "needs_review"
NO_ACTION = "no_action_or_not_applicable"
QUEUE_ORDER = (POTENTIALLY_AFFECTED, NEEDS_REVIEW, NO_ACTION)


def screen_fleet(
    fleet: dict[str, Any],
    hpt_hub_record: dict[str, Any],
    hpc_blade_rules: dict[str, Any],
) -> dict[str, Any]:
    """Return per-engine screens and the two releases' queues."""
    directives = [
        {
            "document": hpt_hub_record["document"],
            "ad_number": hpt_hub_record["ad_number"],
            "effective_date": hpt_hub_record["effective_date"],
            "coverage_state": EVALUATED,
            "screener": f"S1 rules ({hpt_hub_record['normalizer']} "
            f"v{hpt_hub_record['normalizer_version']})",
            "record_sha256": hpt_hub_record["record_sha256"],
        },
        {
            "document": hpc_blade_rules["final_rule_document"],
            "ad_number": hpc_blade_rules["ad_number"],
            "effective_date": hpc_blade_rules["effective_date"]["date"],
            "coverage_state": NOT_YET_EVALUATED,
            "screener": f"rule interpreter v{INTERPRETER_VERSION} on the reference "
            "rule record",
            "record_sha256": _sha256(hpc_blade_rules),
        },
    ]
    engines = []
    for asset in fleet["engines"]:
        as_of = date.fromisoformat(
            asset.get("evaluation_case", {}).get("as_of")
            or asset["engine"]["snapshot_at"]
        )
        screens = {
            directives[0]["document"]: _entry(screen(hpt_hub_record, asset, as_of)),
            directives[1]["document"]: _entry(
                screen_rules(hpc_blade_rules, asset, as_of)
            ),
        }
        engines.append({"asset": asset, "as_of": as_of.isoformat(), "screens": screens})
    releases = [
        _release("r1", "AD 2025-19-13 only", [directives[0]["document"]], engines),
        _release(
            "r2",
            "AD 2026-17-03 added",
            [d["document"] for d in directives],
            engines,
        ),
    ]
    return {
        "screen_version": SCREEN_VERSION,
        "fleet_version": fleet["fleet_version"],
        "fleet_sha256": _sha256(fleet),
        "directives": directives,
        "engines": engines,
        "releases": releases,
    }


def _entry(result: Screen) -> dict[str, Any]:
    status = result.action_status or result.applicability
    data = asdict(result)
    return {
        "queue": QUEUES[status],
        "applicability": result.applicability,
        "action_status": result.action_status,
        "summary": result.summary,
        "timing": result.timing,
        "missing_facts": result.missing_facts,
        "notes": result.notes,
        "citations": data["citations"],
        "computed": result.computed,
    }


def _release(
    release_id: str, label: str, documents: list[str], engines: list[dict[str, Any]]
) -> dict[str, Any]:
    """An engine's queue is the most urgent across the release's directives."""
    queues = {}
    for engine in engines:
        own = [engine["screens"][document]["queue"] for document in documents]
        queues[engine["asset"]["engine"]["asset_id"]] = min(own, key=QUEUE_ORDER.index)
    counts = {queue: list(queues.values()).count(queue) for queue in QUEUE_ORDER}
    return {
        "release_id": release_id,
        "label": label,
        "directives": documents,
        "queues": queues,
        "counts": counts,
    }


def _sha256(value: Any) -> str:
    text = json.dumps(value, sort_keys=True, separators=(",", ":"))
    return hashlib.sha256(text.encode()).hexdigest()
