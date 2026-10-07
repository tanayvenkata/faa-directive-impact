"""B2: screen every seed unit with a model reading the directive text directly.

One run is one model, one effort level, and one repeat. It writes a kept
directory under ``evaluation/runs/``:

- ``calls/``: every request and response, replayable without the model;
- ``outputs.json``: each unit's answer converted to the shape the S1 rules
  produce, so the same scorer applies;
- ``report.json`` and ``report.md``: tokens, cost, gate results on the 18
  AD 2025-19-13 units next to S1, and on all 33 units;
- ``hand-review.md`` and ``hand-review.yaml``: the sheet for gates 5 and 11
  and anything the scorer cannot settle by itself.

Repeats are separate runs, because identical requests share a recording key.
"""

import json
from dataclasses import dataclass
from datetime import date, datetime
from pathlib import Path
from typing import Any

import yaml
from defusedxml import ElementTree
from jsonschema import Draft202012Validator

from faa_directive_impact.directives.hpt_hub_record import (
    build_record,
    canonical_json,
    index_paragraphs,
)
from faa_directive_impact.directives.source_text import (
    SourceDocument,
    documents_for,
    load_generation,
)
from faa_directive_impact.evaluation.b2_prompt import (
    ANSWER_SCHEMAS,
    PROMPT_VERSION,
    build_request,
)
from faa_directive_impact.evaluation.s1_run import (
    GENERATION_ID,
    SOURCE_XML,
    _gates_section,
)
from faa_directive_impact.evaluation.s1_scoring import (
    GATE_NAMES,
    GATE_VERSION,
    PROTECTED,
    S1_DIRECTIVE,
    STANDING_FORBIDDEN,
    CitationIndex,
    Unit,
    hand_review_template,
    score_unit,
    summarize,
    units,
)
from faa_directive_impact.evaluation.seed import load_seed_cases
from faa_directive_impact.llm.client import (
    LiveModel,
    ModelRequest,
    ModelResponse,
    call_batch,
    record,
)

META_KEYS = (
    "run_id", "system", "model", "effort", "repeat", "mode", "prompt_version",
    "gate_version", "started_at", "git_commit", "worktree_dirty", "generation_id",
)  # fmt: skip
QUEUES = {
    "action_required": "potentially_affected",
    "action_required_on_event": "potentially_affected",
    "needs_review": "needs_review",
    "no_action_triggered": "no_action_or_not_applicable",
    "does_not_apply": "no_action_or_not_applicable",
    "outside_supported_scope": "no_action_or_not_applicable",
    "unknown": "needs_review",
}
PROMPT_DISCLOSURE = (
    "The prompt contains: the outcome vocabulary and record conventions from "
    "evaluation/seed/README.md (including that operator AD records and AMOC "
    "claims are claims to check, not evidence), the list of supported engine "
    "models, the missing-fact path format, the answer format, and each "
    "document's type, publication date, and Federal Register effective date "
    "alongside its text. Documents are rendered from the XML with image "
    "placeholders, and each unit gets its directive plus the related "
    "documents published by its question date. The prompt never contains a "
    "case's title, slice, label, rationale, forbidden claims, notes, or any "
    "adjudication."
)
EXPECTED_OUT_OF_TEXT = (
    "Seed-005's expected timing follows informal FAA correspondence "
    "(faa-informal-2026-10-05) that is not in the directive text, and its "
    "expected `computed.readings` includes an `FAA` reading. A system reading "
    "only the text is expected to miss it on gate 8. That is a limit of the "
    "text, not a model error, and it was written here before the run."
)
NO_ANSWER_RULE = (
    "A unit with no usable answer (a refusal, a non-JSON response, or JSON "
    "that does not match the answer schema) fails every gate it is covered "
    "by, because no safe output was produced. Only transport errors are "
    "retried, by the SDK; answers are never retried for content."
)


@dataclass(frozen=True)
class B2Unit:
    unit: Unit
    as_of: date
    documents: tuple[SourceDocument, ...]
    index: CitationIndex


def prepare(repo: Path, storage_root: Path) -> list[B2Unit]:
    """Every seed unit with its documents and citation index."""
    generation_dir = repo / "generations" / GENERATION_ID
    s1_record = build_record((repo / SOURCE_XML).read_bytes(), generation_dir)
    documents, relationships = load_generation(generation_dir, storage_root)
    paragraphs = {
        number: index_paragraphs(ElementTree.fromstring(document.xml))
        for number, document in documents.items()
    }
    cases = [case.record for case in load_seed_cases(repo / "evaluation/seed/cases")]
    prepared = []
    for unit in units(cases):
        as_of = date.fromisoformat(unit.record["source_snapshot"]["as_of"])
        given = documents_for(
            unit.expected["directive"], as_of, documents, relationships
        )
        index = CitationIndex({})
        for document in given:
            index.add_document(
                document.number, paragraphs[document.number], document.text
            )
        if s1_record["document"] in index.paragraphs:
            table = s1_record["table_1"]
            index.tables[s1_record["document"]] = (table["paragraph"], table["rows"])
        prepared.append(B2Unit(unit, as_of, tuple(given), index))
    return prepared


def request_for(item: B2Unit, model: str, effort: str) -> ModelRequest:
    return build_request(
        model,
        effort,
        item.unit.expected["directive"],
        item.as_of,
        item.unit.record["asset_snapshot"],
        list(item.documents),
    )


def adapt(
    answer: dict[str, Any] | None, prompt_version: str = PROMPT_VERSION
) -> dict[str, Any] | None:
    """Convert a valid answer into the output shape the S1 rules produce.

    The answer is validated against the schema of the prompt version that
    produced it. Missing facts are scored by their record paths; their
    descriptions go to the hand-review sheet.
    """
    schema = ANSWER_SCHEMAS[prompt_version]
    if answer is None or list(Draft202012Validator(schema).iter_errors(answer)):
        return None
    facts = [
        {"record_path": fact, "description": fact} if isinstance(fact, str) else fact
        for fact in answer["missing_facts"]
    ]
    status = None if answer["action_status"] == "none" else answer["action_status"]
    computed: dict[str, Any] = {}
    for key in ("latest_engine_flight_cycles", "component_cycles_remaining"):
        if answer[key] is not None:
            computed[key] = answer[key]
    if answer["alternative_readings"]:
        computed["readings"] = {
            reading["name"]: reading["latest_engine_flight_cycles"]
            for reading in answer["alternative_readings"]
        }
    return {
        "applicability": answer["applicability"],
        "action_status": status,
        "authority_state": answer["authority_state"],
        "computed": computed,
        "missing_facts": [f["record_path"] for f in facts if f["record_path"]],
        "missing_fact_descriptions": [f["description"] for f in facts],
        "continuing_obligations": answer["continuing_obligations"],
        "citations": answer["citations"],
        "hubs": [
            {
                "position": part["component_name"],
                "outcome": "matched",
                "part_number": part["installed_part_number"],
                "serial_number": part["installed_serial_number"],
                "table_row": {
                    "part_number": part["listed_part_number"],
                    "serial_number": part["listed_serial_number"],
                },
                "statement": (
                    f"{part['component_name']} P/N {part['installed_part_number']} "
                    f"S/N {part['installed_serial_number']} matched listed P/N "
                    f"{part['listed_part_number']} S/N {part['listed_serial_number']}"
                ),
            }
            for part in answer["matched_parts"]
        ],
        "summary": answer["summary"],
        "timing": answer["timing"],
        "notes": answer["notes"],
        "queue": QUEUES.get(status or answer["applicability"], "needs_review"),
    }


def run_b2(
    repo: Path,
    runs_root: Path,
    storage_root: Path,
    model: str,
    effort: str,
    repeat: int,
    mode: str,
    started_at: datetime,
    commit: str,
    dirty: bool,
    client: Any = None,
) -> Path:
    """Run one model over every unit, record the calls, and score them."""
    items = prepare(repo, storage_root)
    name = model.removeprefix("claude-")
    stamp = started_at.strftime("%Y%m%dT%H%M%SZ")
    directory = runs_root / f"b2-{name}-{effort}-r{repeat}-{stamp}-{commit[:7]}"
    directory.mkdir(parents=True, exist_ok=False)
    calls = directory / "calls"
    requests = [request_for(item, model, effort) for item in items]

    if client is None:
        import anthropic

        client = anthropic.Anthropic()
    if mode == "batch":
        by_key = call_batch(client, requests)
        responses = [by_key[request.key()] for request in requests]
    elif mode == "live":
        live = LiveModel(client)
        responses = [live.call(request) for request in requests]
    else:
        raise ValueError(f"unknown mode {mode!r}")
    for request, response in zip(requests, responses, strict=True):
        record(calls, request, response)

    meta = {
        "run_id": directory.name,
        "system": "B2 full-context model",
        "model": model,
        "effort": effort,
        "repeat": repeat,
        "mode": mode,
        "prompt_version": PROMPT_VERSION,
        "gate_version": GATE_VERSION,
        "started_at": started_at.isoformat(),
        "git_commit": commit,
        "worktree_dirty": dirty,
        "generation_id": GENERATION_ID,
    }
    write_results(repo, directory, meta, items, requests, responses)
    return directory


def write_results(
    repo: Path,
    directory: Path,
    meta: dict[str, Any],
    items: list[B2Unit],
    requests: list[ModelRequest],
    responses: list[ModelResponse],
) -> dict[str, Any]:
    """Score recorded responses and write outputs, report, and review sheet."""
    outputs, scored = {}, []
    for item, request, response in zip(items, requests, responses, strict=True):
        output = adapt(response.answer, meta["prompt_version"])
        error = response.error or (
            "answer does not match the answer schema"
            if output is None and response.answer is not None
            else None
        )
        outputs[item.unit.name] = {
            "request_key": request.key(),
            "output": output,
            "error": error,
            "usage": response.usage,
            "cost_usd": response.cost_usd,
            "latency_seconds": response.latency_seconds,
        }
        scored.append(
            {
                "unit": item.unit.name,
                "directive": item.unit.expected["directive"],
                "slice": item.unit.record["slice"],
                "severity": item.unit.record["severity"],
                "has_action_timing": "action_timing" in item.unit.expected,
                "no_answer": output is None,
                "gates": score_unit(item.unit, output, item.index),
            }
        )

    s1_units = [s for s in scored if s["directive"] == S1_DIRECTIVE]
    report = {
        **meta,
        "prompt_disclosure": PROMPT_DISCLOSURE,
        "no_answer_rule": NO_ANSWER_RULE,
        "expected_out_of_text": EXPECTED_OUT_OF_TEXT,
        "usage": usage_totals(responses),
        "units_scored": len(scored),
        "no_answer_units": [s["unit"] for s in scored if s["no_answer"]],
        "gates_s1_units": summarize(s1_units),
        "gates_all_units": summarize(scored),
        "units": scored,
    }
    known_gaps = _gates_section(repo / "evaluation/GATES.md", "Known Gaps")
    (directory / "outputs.json").write_text(canonical_json(outputs), "utf-8")
    (directory / "report.json").write_text(canonical_json(report), "utf-8")
    (directory / "report.md").write_text(report_markdown(report, known_gaps), "utf-8")
    (directory / "hand-review.md").write_text(
        hand_review_markdown(items, outputs, scored), "utf-8"
    )
    (directory / "hand-review.yaml").write_text(
        yaml.safe_dump(hand_review_template(scored), sort_keys=False, width=88),
        "utf-8",
    )
    return report


def usage_totals(responses: list[ModelResponse]) -> dict[str, Any]:
    keys = (
        "input_tokens",
        "cache_creation_input_tokens",
        "cache_read_input_tokens",
        "output_tokens",
    )
    totals = {key: sum(r.usage.get(key) or 0 for r in responses) for key in keys}
    cost = round(sum(r.cost_usd for r in responses), 4)
    latencies = [r.latency_seconds for r in responses]
    return {
        **totals,
        "calls": len(responses),
        "cost_usd": cost,
        "cost_usd_per_unit": round(cost / len(responses), 5) if responses else 0,
        "mean_latency_seconds": round(sum(latencies) / len(latencies), 2)
        if latencies
        else 0,
    }


def report_markdown(report: dict[str, Any], known_gaps: str) -> str:
    usage = report["usage"]
    lines = [
        f"# B2 Run {report['run_id']}",
        "",
        "| Field | Value |",
        "|---|---|",
        f"| System | {report['system']} |",
        f"| Model | `{report['model']}`, effort `{report['effort']}` |",
        f"| Repeat | {report['repeat']} ({report['mode']}) |",
        f"| Prompt version | `{report['prompt_version']}` |",
        f"| Gate version | {report['gate_version']} |",
        f"| Git commit | `{report['git_commit']}` (dirty: {report['worktree_dirty']}) |",
        f"| Source generation | `{report['generation_id']}` |",
        f"| Units | {report['units_scored']}; no answer: "
        f"{len(report['no_answer_units'])} |",
        f"| Cost | ${usage['cost_usd']} total, ${usage['cost_usd_per_unit']} per unit |",
        f"| Tokens | input {usage['input_tokens']:,}, cache write "
        f"{usage['cache_creation_input_tokens']:,}, cache read "
        f"{usage['cache_read_input_tokens']:,}, output {usage['output_tokens']:,} |",
        f"| Mean latency | {usage['mean_latency_seconds']} s |",
        "",
        "## Method",
        "",
        report["prompt_disclosure"],
        "",
        report["no_answer_rule"],
        "",
        report["expected_out_of_text"],
        "",
        "Gates 5 and 11, missing facts described in words, and locators the "
        "index cannot resolve are on the hand-review sheet and pending here.",
        "",
    ]
    for title, key in (
        ("Gates on the 18 AD 2025-19-13 units (paired with S1)", "gates_s1_units"),
        ("Gates on all 33 units", "gates_all_units"),
    ):
        lines += [
            f"## {title}",
            "",
            "| # | Gate | Verdict | Covered | Failed |",
            "|---|---|---|---|---|",
        ]
        for number, gate in report[key].items():
            covered = gate.get("covered")
            failed = gate.get("failed", [])
            shown = ", ".join(failed) if failed else "—"
            if failed and gate.get("budget") and gate["verdict"] == "pass":
                shown += f" ({len(failed)} of {gate['budget']} allowed)"
            lines.append(
                f"| {number} | {GATE_NAMES[number]} | {gate['verdict']} | "
                f"{len(covered) if covered is not None else '—'} | {shown} |"
            )
        lines.append("")
    lines += [
        "## Units",
        "",
        "| Unit | Directive | Slice | Severity | Failed gates |",
        "|---|---|---|---|---|",
    ]
    for unit in report["units"]:
        failed = [n for n, g in unit["gates"].items() if not g["passed"]]
        flag = " (no answer)" if unit["no_answer"] else ""
        lines.append(
            f"| {unit['unit']} | {unit['directive']} | {unit['slice']} | "
            f"{unit['severity']} | {', '.join(failed) or '—'}{flag} |"
        )
    lines += ["", "## Failures (mechanical gates)", ""]
    failures = [
        (unit["unit"], n, g["detail"])
        for unit in report["units"]
        for n, g in unit["gates"].items()
        if not g["passed"]
    ]
    if failures:
        lines += ["| Unit | Gate | Detail |", "|---|---|---|"]
        lines += [
            f"| {u} | {n}{' (protected)' if n in PROTECTED else ''} | {d} |"
            for u, n, d in failures
        ]
    else:
        lines.append("No mechanical gate failed.")
    lines += ["", "## Known Gaps (from GATES.md)", "", known_gaps.strip(), ""]
    return "\n".join(lines)


def hand_review_markdown(
    items: list[B2Unit], outputs: dict[str, Any], scored: list[dict[str, Any]]
) -> str:
    lines = [
        "# B2 Hand-Review Sheet",
        "",
        "Record results in `hand-review.yaml`. For each unit: gate 5 (forbidden "
        "claims, including the standing list), gate 11 (stated timing against "
        "the expected timing), and, where listed, missing facts described in "
        "words and locators the index could not resolve.",
        "",
        "Standing forbidden claims, for every unit:",
        "",
    ]
    lines += [f"- {claim}" for claim in STANDING_FORBIDDEN]
    by_name = {s["unit"]: s for s in scored}
    for item in items:
        unit, name = item.unit, item.unit.name
        result = outputs[name]
        output = result["output"]
        expected = unit.expected
        lines += ["", f"## {name}: {unit.record['title']}", ""]
        if output is None:
            lines.append(f"- **No answer:** {result['error']}")
            continue
        lines += [
            f"- **Fields:** applicability `{output['applicability']}`, "
            f"action_status `{output['action_status']}`, authority "
            f"`{output['authority_state']}`",
            f"- **Expected:** applicability `{expected['applicability']}`, "
            f"action_status `{expected.get('action_status')}`",
            f"- **Summary:** {output['summary']}",
        ]
        if output["timing"]:
            lines.append(f"- **Stated timing:** {output['timing']}")
        if "action_timing" in expected:
            lines.append(
                f"- **Expected timing:** {expected['action_timing']['description']}"
            )
        lines += [
            f"- **Missing fact:** {fact}"
            for fact in output["missing_fact_descriptions"]
        ]
        lines += [f"- **Note:** {note}" for note in output["notes"]]
        gates = by_name[name]["gates"]
        for fact in gates["4"].get("hand_review_facts", []):
            lines.append(f"- **Expected missing fact (judge on meaning):** {fact}")
        for locator in gates["6"]["hand_review_locators"]:
            lines.append(f"- **Unresolved locator:** {locator}")
        lines += ["", "Forbidden claims for this case:", ""]
        lines += [f"- {claim}" for claim in unit.record["forbidden_claims"]]
    lines.append("")
    return "\n".join(lines)


def replay_results(repo: Path, storage_root: Path, directory: Path) -> dict[str, Any]:
    """Re-score a recorded run from its calls, without the model."""
    report = json.loads((directory / "report.json").read_text(encoding="utf-8"))
    items = prepare(repo, storage_root)
    requests = [request_for(item, report["model"], report["effort"]) for item in items]
    responses = []
    for request in requests:
        recorded = json.loads(
            (directory / "calls" / f"{request.key()}.json").read_text("utf-8")
        )
        responses.append(ModelResponse(**recorded["response"]))
    meta = {key: report[key] for key in META_KEYS}
    return write_results(repo, directory, meta, items, requests, responses)
