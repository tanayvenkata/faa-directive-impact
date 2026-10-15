"""Screen the demo fleet: retrieve each engine's directives, then screen them.

For every engine, candidate retrieval (``retrieval.search``, ROADMAP step 7)
finds the directives it might fall under in the frozen retrieval corpus, as
of the engine's snapshot date. Each candidate final rule is then screened by
what covers it:

- **AD 2025-19-13** (``evaluated``): the S1 rules on the normalized record
  kept with the S1 run.
- **A directive with a rule record** (AD 2026-17-03): the rule interpreter on
  its hand-written reference record. ``not_yet_evaluated``: its seed labels
  are Claude drafts no person has confirmed.
- **Any other candidate**: no rule record exists, so it is listed for a
  person to read, with the identifier that retrieved it. ``not_yet_evaluated``.

The fleet's queues come from evaluated directives only (ROADMAP, "Directive
Coverage State"): a ``not_yet_evaluated`` result is shown beside the queue,
never inside it. A superseded directive is shown as superseded, not queued.
"""

import hashlib
import json
from dataclasses import asdict
from datetime import date
from typing import Any

from faa_directive_impact.impact.hpt_hub_rules import QUEUES, Screen, screen
from faa_directive_impact.retrieval.search import RETRIEVER_VERSION, retrieve
from faa_directive_impact.rules.interpreter import INTERPRETER_VERSION, screen_rules

SCREEN_VERSION = 2
EVALUATED = "evaluated"
NOT_YET_EVALUATED = "not_yet_evaluated"
POTENTIALLY_AFFECTED = "potentially_affected"
NEEDS_REVIEW = "needs_review"
NO_ACTION = "no_action_or_not_applicable"
QUEUE_ORDER = (POTENTIALLY_AFFECTED, NEEDS_REVIEW, NO_ACTION)
UNKNOWN = "unknown"


def screen_fleet(
    fleet: dict[str, Any],
    hpt_hub_record: dict[str, Any],
    rule_records: dict[str, dict[str, Any]],
    corpus: dict[str, Any],
) -> dict[str, Any]:
    """Return per-engine candidates and screens, and per-directive totals."""
    records = {record["document"]: record for record in corpus["records"]}
    evaluated_document = hpt_hub_record["document"]
    engines = []
    for asset in fleet["engines"]:
        as_of = date.fromisoformat(
            asset.get("evaluation_case", {}).get("as_of")
            or asset["engine"]["snapshot_at"]
        )
        candidates = retrieve(corpus["records"], asset, as_of)
        screens = {}
        for candidate in candidates:
            document = candidate["document"]
            record = records[document]
            if record["kind"] != "final_rule":
                continue  # Proposals are not in force; corrections ride with finals.
            superseded_by = _superseded_by(record, records, as_of)
            if superseded_by:
                screens[document] = _superseded(document, superseded_by)
            elif document == evaluated_document:
                screens[document] = _entry(
                    screen(hpt_hub_record, asset, as_of), EVALUATED
                )
            elif document in rule_records:
                screens[document] = _entry(
                    screen_rules(rule_records[document], asset, as_of),
                    NOT_YET_EVALUATED,
                )
            else:
                screens[document] = _unread(candidate)
        engines.append(
            {
                "asset": asset,
                "as_of": as_of.isoformat(),
                "candidates": [
                    {key: c[key] for key in ("document", "kind", "via", "matches")}
                    for c in candidates
                ],
                "screens": screens,
                "evaluated_queue": _evaluated_queue(asset, screens),
                "not_yet_evaluated": sorted(
                    (
                        document
                        for document, entry in screens.items()
                        if entry["coverage_state"] == NOT_YET_EVALUATED
                        and entry["queue"] != NO_ACTION
                    ),
                    key=lambda document: (
                        screens[document]["via"] != "part_number",
                        document,
                    ),
                ),
            }
        )
    directives = _directives(engines, records, evaluated_document, rule_records)
    counts = {
        queue: sum(1 for e in engines if e["evaluated_queue"] == queue)
        for queue in QUEUE_ORDER
    }
    return {
        "screen_version": SCREEN_VERSION,
        "retriever": RETRIEVER_VERSION,
        "interpreter_version": INTERPRETER_VERSION,
        "corpus_generation": corpus["generation_id"],
        "fleet_version": fleet["fleet_version"],
        "fleet_sha256": _sha256(fleet),
        "evaluated_directive": evaluated_document,
        "evaluated_counts": counts,
        "directives": directives,
        "engines": engines,
    }


def _evaluated_queue(asset: dict[str, Any], screens: dict[str, Any]) -> str:
    """The engine's queue under evaluated directives only."""
    model = asset.get("engine", {}).get("engine_model")
    if not isinstance(model, str) or not model.strip() or model.lower() == UNKNOWN:
        # Without a model, retrieval cannot rule a directive out.
        return NEEDS_REVIEW
    own = [
        entry["queue"]
        for entry in screens.values()
        if entry["coverage_state"] == EVALUATED
    ]
    return min(own, key=QUEUE_ORDER.index) if own else NO_ACTION


def _entry(result: Screen, coverage_state: str) -> dict[str, Any]:
    status = result.action_status or result.applicability
    return {
        "coverage_state": coverage_state,
        "screener": "rules",
        "queue": QUEUES[status],
        "applicability": result.applicability,
        "action_status": result.action_status,
        "summary": result.summary,
        "timing": result.timing,
        "missing_facts": result.missing_facts,
        "notes": result.notes,
        "citations": asdict(result)["citations"],
        "computed": result.computed,
        "via": None,
    }


def _unread(candidate: dict[str, Any]) -> dict[str, Any]:
    tokens = ", ".join(match["token"] for match in candidate["matches"])
    if candidate["via"] == "part_number":
        why = f"an installed part number ({tokens}) appears in its text"
    else:
        why = f"paragraph (c) lists the engine model ({tokens})"
    return {
        "coverage_state": NOT_YET_EVALUATED,
        "screener": "none",
        "queue": NEEDS_REVIEW,
        "applicability": "candidate",
        "action_status": None,
        "summary": f"Retrieved because {why}. No rule record exists for this "
        "directive yet, so a person reads it to decide.",
        "timing": None,
        "missing_facts": [],
        "notes": [],
        "citations": [
            {
                "document": candidate["document"],
                "paragraph": paragraph,
                "locator": match["token"],
                "supports": "why it was retrieved",
            }
            for match in candidate["matches"]
            for paragraph in match.get("paragraphs", [])
        ],
        "computed": {},
        "via": candidate["via"],
    }


def _superseded(document: str, superseded_by: str) -> dict[str, Any]:
    return {
        "coverage_state": NOT_YET_EVALUATED,
        "screener": "none",
        "queue": NO_ACTION,
        "applicability": "superseded",
        "action_status": None,
        "summary": f"Superseded by {superseded_by}, which is screened in its place.",
        "timing": None,
        "missing_facts": [],
        "notes": [],
        "citations": [],
        "computed": {},
        "via": None,
    }


def _superseded_by(
    record: dict[str, Any], records: dict[str, dict[str, Any]], as_of: date
) -> str | None:
    for link in record["relationships"]:
        later = records.get(link["document"])
        if (
            link["type"] == "supersedes"
            and link["direction"] == "from"
            and later is not None
            and date.fromisoformat(later["publication_date"]) <= as_of
        ):
            return later.get("ad_number") or later["document"]
    return None


def _directives(
    engines: list[dict[str, Any]],
    records: dict[str, dict[str, Any]],
    evaluated_document: str,
    rule_records: dict[str, dict[str, Any]],
) -> list[dict[str, Any]]:
    """Every directive screened for at least one engine, with fleet totals."""
    documents = sorted({d for engine in engines for d in engine["screens"]})
    rows = []
    for document in documents:
        record = records[document]
        entries = [e["screens"][document] for e in engines if document in e["screens"]]
        rows.append(
            {
                "document": document,
                "ad_number": record.get("ad_number"),
                "title": record["title"],
                "publication_date": record["publication_date"],
                "effective_date": record["effective_date"],
                "coverage_state": EVALUATED
                if document == evaluated_document
                else NOT_YET_EVALUATED,
                "screener": "S1 rules"
                if document == evaluated_document
                else "rule interpreter on a reference rule record"
                if document in rule_records
                else "none: listed for a person to read",
                "engines": len(entries),
                "by_part_number": sum(
                    1
                    for engine in engines
                    for candidate in engine["candidates"]
                    if candidate["document"] == document
                    and candidate["via"] == "part_number"
                ),
                "superseded": sum(
                    1 for e in entries if e["applicability"] == "superseded"
                ),
                "queues": {
                    queue: sum(1 for e in entries if e["queue"] == queue)
                    for queue in QUEUE_ORDER
                },
            }
        )
    order = {EVALUATED: 0, NOT_YET_EVALUATED: 1}
    return sorted(
        rows,
        key=lambda r: (
            order[r["coverage_state"]],
            r["document"] not in rule_records,
            -r["by_part_number"],
            r["document"],
        ),
    )


def _sha256(value: Any) -> str:
    text = json.dumps(value, sort_keys=True, separators=(",", ":"))
    return hashlib.sha256(text.encode()).hexdigest()
