"""Screen the demo fleet: retrieve each engine's directives, then screen them.

For every engine, candidate retrieval (``retrieval.search``, ROADMAP step 7)
finds the directives it might fall under in the frozen retrieval corpus, as
of the engine's snapshot date. Each candidate final rule is then screened by
what covers it:

- **AD 2025-19-13**: the S1 rules on the normalized record kept with the S1
  run.
- **A directive with a reference rule record** (every in-scope V2500
  directive, ``evaluation/coverage/reference/``): the rule interpreter on
  that record.
- **Any other candidate**: no rule record exists, so it is listed for a
  person to read, with the identifier that retrieved it.

Whether a directive is ``evaluated`` is set in one place,
``EVALUATED_DIRECTIVES``. The fleet's queues come from evaluated directives
only (ROADMAP, "Directive Coverage State"): a ``not_yet_evaluated`` result is
shown beside the queue, never inside it. A superseded directive is shown as
superseded, not queued.

Beside the outcomes, the screen says what keeps engines in review: per
directive and fleet-wide, the unavailable documents (incorporated service
information, or tables printed only as images) and the other missing facts,
counted over engines whose screen is ``needs_review``.
"""

import hashlib
import json
import re
from dataclasses import asdict
from datetime import date
from typing import Any

from faa_directive_impact.impact.hpt_hub_rules import QUEUES, Screen, screen
from faa_directive_impact.retrieval.search import RETRIEVER_VERSION, retrieve
from faa_directive_impact.rules.interpreter import INTERPRETER_VERSION, screen_rules

SCREEN_VERSION = 4
EVALUATED = "evaluated"
NOT_YET_EVALUATED = "not_yet_evaluated"
POTENTIALLY_AFFECTED = "potentially_affected"
NEEDS_REVIEW = "needs_review"
NO_ACTION = "no_action_or_not_applicable"
QUEUE_ORDER = (POTENTIALLY_AFFECTED, NEEDS_REVIEW, NO_ACTION)
UNKNOWN = "unknown"
# AD 2025-19-13 keeps the S1 rules baseline as its screener.
S1_DOCUMENT = "2025-18469"
# The single place that says which directives are evaluated (ROADMAP,
# "Directive Coverage State"; evaluation/coverage/PREREGISTRATION.md, "What
# Evaluated Means Here"). Only these set the fleet's queues.
EVALUATED_DIRECTIVES = frozenset({S1_DOCUMENT})

# Where each directive's rule record is read from. A directive absent here
# uses its reference record; an evaluated directive can point at its reviewed
# draft instead (for example ``evaluation/coverage/reviewed/<doc>.json``).
REFERENCE_RECORD_DIRECTORY = "evaluation/coverage/reference"
RULE_RECORD_PATHS: dict[str, str] = {}


def rule_record_path(document: str) -> str:
    """The repository path of the rule record the screen reads for ``document``."""
    return RULE_RECORD_PATHS.get(
        document, f"{REFERENCE_RECORD_DIRECTORY}/{document}.json"
    )


# How the review of each evaluated directive was done, shown beside its
# coverage badge. An evaluated directive with no entry here is a Claude
# stand-in review (``label_review``) with a Claude subagent as the independent
# check; a directive that is not evaluated has none.
CLAUDE_STAND_IN = {
    "label_review": "claude_stand_in",
    "independent_check": "claude_subagent",
}
REVIEW_PROVENANCE: dict[str, dict[str, str]] = {
    S1_DOCUMENT: {
        "rules": "hand-written (S1)",
        "hand_gates": "judged by Claude only",
    },
}


def review_provenance(
    document: str, evaluated: frozenset[str]
) -> dict[str, str] | None:
    if document not in evaluated:
        return None
    return REVIEW_PROVENANCE.get(document, CLAUDE_STAND_IN)


IMAGE = "image_only_figure"
E5_MODEL = "V2531-E5"
# Service documents named in dependency titles, so a document cited by several
# directives (or several tables of one) is counted once per engine.
SERVICE_DOCUMENT = re.compile(
    r"(?P<nmsb>(?:Alert )?NMSB V2500-[A-Z0-9]+-72-A?\d{4})"
    r"|(?:P&W |PW )?SI No\. (?P<si>\d+F-\d+)"
)
ALTERNATIVES = re.compile(r",? (?:and|or) (?=(?:IAE|PW|P&W) )")


def screen_fleet(
    fleet: dict[str, Any],
    hpt_hub_record: dict[str, Any],
    rule_records: dict[str, dict[str, Any]],
    corpus: dict[str, Any],
    evaluated: frozenset[str] = EVALUATED_DIRECTIVES,
    rule_sources: dict[str, str] | None = None,
) -> dict[str, Any]:
    """Return per-engine candidates and screens, and per-directive totals."""
    records = {record["document"]: record for record in corpus["records"]}
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
            state = EVALUATED if document in evaluated else NOT_YET_EVALUATED
            superseded_by = _superseded_by(record, records, as_of)
            if superseded_by:
                screens[document] = _superseded(document, superseded_by)
            elif document == S1_DOCUMENT:
                screens[document] = _entry(screen(hpt_hub_record, asset, as_of), state)
            elif document in rule_records:
                screens[document] = _entry(
                    screen_rules(rule_records[document], asset, as_of), state
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
        "evaluated_directives": sorted(evaluated),
        "evaluated_counts": counts,
        "directives": _directives(
            engines, records, evaluated, rule_records, rule_sources or {}
        ),
        "blocking_documents": _blocking_documents(engines, rule_records),
        "missing_fact_kinds": _missing_fact_kinds(engines, rule_records),
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


# What blocks decisions ------------------------------------------------------


def _dependency(fact: str, rule_record: dict[str, Any] | None) -> dict[str, Any] | None:
    """The record dependency a missing fact names, matched on its full title.

    A fact names a dependency as its title followed by `` (`` and a reason.
    Some titles are prefixes of others (one table, or that table "or" another
    document), so the longest title that matches wins.
    """
    if rule_record is None:
        return None
    matches = [
        d for d in rule_record["dependencies"] if fact.startswith(d["title"] + " (")
    ]
    return max(matches, key=lambda d: len(d["title"]), default=None)


def _service_documents(title: str, model: str) -> list[str]:
    """The service documents a dependency title names that bear on ``model``.

    A document marked for the V2531-E5, or an E5 bulletin, is not counted
    against an A5 or D5 engine.
    """
    found = []
    for segment in ALTERNATIVES.split(title):
        for match in SERVICE_DOCUMENT.finditer(segment):
            if match.group("nmsb"):
                name = f"IAE {match.group('nmsb')}"
                e5_only = "-E5-" in name
            else:
                name = f"P&W SI No. {match.group('si')}"
                e5_only = f"({E5_MODEL})" in segment
            if e5_only and model != E5_MODEL:
                continue
            if name not in found:
                found.append(name)
    return found


def _blockers(
    entry: dict[str, Any], rule_record: dict[str, Any] | None, model: str, ad: str
) -> tuple[list[tuple[str, str]], list[str]]:
    """A review screen's blocking documents (name, kind) and its other facts."""
    documents: list[tuple[str, str]] = []
    others: list[str] = []
    for fact in entry["missing_facts"]:
        dependency = _dependency(fact, rule_record)
        if dependency is None:
            others.append(_fact_pattern(fact))
            continue
        if dependency["kind"] == IMAGE:
            name = f"{ad}: {dependency['title'].split(' (image')[0]}"
            documents.append((name, "printed only as an image in the directive"))
        else:
            for name in _service_documents(dependency["title"], model) or [
                dependency["title"]
            ]:
                documents.append((name, "incorporated by reference, not available"))
    return list(dict.fromkeys(documents)), list(dict.fromkeys(others))


def _fact_pattern(fact: str) -> str:
    """A missing fact with its event date generalized, so engines can be counted."""
    return re.sub(r"^events\[[^\]]+\]", "events[...]", fact)


def _fact_kind(fact: str) -> str:
    if fact.startswith("ad_records["):
        return "operator AD status record"
    if fact.startswith("amoc_claims["):
        return "approval of a claimed AMOC"
    if fact.startswith("operator."):
        return "operator program fact"
    if fact.startswith(("engine.", "installed_components", "events[")):
        return "engine record field"
    return "condition no engine record field holds"


def _review_screens(
    engines: list[dict[str, Any]],
) -> list[tuple[dict[str, Any], str, dict[str, Any]]]:
    return [
        (engine, document, entry)
        for engine in engines
        for document, entry in sorted(engine["screens"].items())
        if entry["queue"] == NEEDS_REVIEW
    ]


def _blocking_documents(
    engines: list[dict[str, Any]], rule_records: dict[str, dict[str, Any]]
) -> list[dict[str, Any]]:
    """Each unavailable document, with the engines it leaves in review."""
    blocked: dict[tuple[str, str], dict[str, set[str]]] = {}
    for engine, document, entry in _review_screens(engines):
        record = rule_records.get(document)
        if record is None:
            continue
        documents, _ = _blockers(
            entry,
            record,
            engine["asset"]["engine"]["engine_model"],
            record["ad_number"],
        )
        for key in documents:
            seen = blocked.setdefault(key, {"engines": set(), "directives": set()})
            seen["engines"].add(engine["asset"]["engine"]["asset_id"])
            seen["directives"].add(record["ad_number"])
    rows = [
        {
            "document": name,
            "kind": kind,
            "engines": len(seen["engines"]),
            "directives": sorted(seen["directives"]),
        }
        for (name, kind), seen in blocked.items()
    ]
    return sorted(rows, key=lambda r: (-r["engines"], r["document"]))


def _missing_fact_kinds(
    engines: list[dict[str, Any]], rule_records: dict[str, dict[str, Any]]
) -> list[dict[str, Any]]:
    """Engines in review on any directive for want of each kind of fact."""
    kinds: dict[str, set[str]] = {}
    for engine, document, entry in _review_screens(engines):
        record = rule_records.get(document)
        documents, others = _blockers(
            entry,
            record,
            engine["asset"]["engine"]["engine_model"],
            record["ad_number"] if record else document,
        )
        asset_id = engine["asset"]["engine"]["asset_id"]
        if documents:
            kinds.setdefault("unavailable document", set()).add(asset_id)
        for fact in others:
            kinds.setdefault(_fact_kind(fact), set()).add(asset_id)
        if entry["screener"] == "none":
            kinds.setdefault("no rule record (a person reads it)", set()).add(asset_id)
    rows = [{"kind": kind, "engines": len(ids)} for kind, ids in kinds.items()]
    return sorted(rows, key=lambda r: (-r["engines"], r["kind"]))


def _directives(
    engines: list[dict[str, Any]],
    records: dict[str, dict[str, Any]],
    evaluated: frozenset[str],
    rule_records: dict[str, dict[str, Any]],
    rule_sources: dict[str, str],
) -> list[dict[str, Any]]:
    """Every directive screened for at least one engine, with fleet totals."""
    documents = sorted({d for engine in engines for d in engine["screens"]})
    rows = []
    for document in documents:
        record = records[document]
        rule_record = rule_records.get(document)
        screened = [
            (engine, engine["screens"][document])
            for engine in engines
            if document in engine["screens"]
        ]
        entries = [entry for _, entry in screened]
        blocking: dict[tuple[str, str], int] = {}
        facts: dict[str, int] = {}
        for engine, entry in screened:
            if entry["queue"] != NEEDS_REVIEW:
                continue
            found, others = _blockers(
                entry,
                rule_record,
                engine["asset"]["engine"]["engine_model"],
                record.get("ad_number") or document,
            )
            for key in found:
                blocking[key] = blocking.get(key, 0) + 1
            for fact in others:
                facts[fact] = facts.get(fact, 0) + 1
        rows.append(
            {
                "document": document,
                "ad_number": record.get("ad_number"),
                "title": record["title"],
                "publication_date": record["publication_date"],
                "effective_date": record["effective_date"],
                "coverage_state": EVALUATED
                if document in evaluated
                else NOT_YET_EVALUATED,
                "screener": "S1 rules"
                if document == S1_DOCUMENT
                else "rule interpreter on a reference rule record"
                if rule_record is not None
                else "none: listed for a person to read",
                "review_provenance": review_provenance(document, evaluated),
                "rule_record_source": rule_sources.get(document),
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
                "outcomes": _outcomes(entries),
                "blocking_documents": [
                    {"document": name, "kind": kind, "engines": n}
                    for (name, kind), n in sorted(
                        blocking.items(), key=lambda item: (-item[1], item[0])
                    )
                ],
                "missing_facts": [
                    {"fact": fact, "kind": _fact_kind(fact), "engines": n}
                    for fact, n in sorted(facts.items(), key=lambda i: (-i[1], i[0]))
                ],
            }
        )
    order = {EVALUATED: 0, NOT_YET_EVALUATED: 1}
    return sorted(
        rows,
        key=lambda r: (
            order[r["coverage_state"]],
            r["document"] not in rule_records and r["document"] != S1_DOCUMENT,
            -r["by_part_number"],
            r["document"],
        ),
    )


def _outcomes(entries: list[dict[str, Any]]) -> dict[str, int]:
    """Counts of each applicability and action status the screens gave."""
    counts: dict[str, int] = {}
    for entry in entries:
        key = entry["action_status"] or entry["applicability"]
        counts[key] = counts.get(key, 0) + 1
    return dict(sorted(counts.items()))


def _sha256(value: Any) -> str:
    text = json.dumps(value, sort_keys=True, separators=(",", ":"))
    return hashlib.sha256(text.encode()).hexdigest()
