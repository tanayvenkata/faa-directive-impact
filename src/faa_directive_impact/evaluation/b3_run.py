"""Run B3: a model drafts each directive's rule record; score it two ways.

One run makes one call per directive (AD 2025-19-13 and AD 2026-17-03), each
given the directive's whole thread as published by the latest scored question
date. Every call is recorded under ``calls/`` so the run can be re-scored
without the model.

Scoring:

1. Field accuracy: each drafted field against the hand-written reference
   record (``evaluation/b3/reference/``), plus whether the draft flags the
   reference's ambiguities (``b3_fields``).
2. End to end: the same interpreter screens every unit of those directives
   from the drafted record and from the reference record, and both are scored
   under the frozen gates. A gate that fails with the draft but passes with
   the reference is an extraction error; a gate that fails with both is a
   limit of the interpreter or the rule vocabulary, not of the draft.

The run writes ``extractions/``, ``fields.json``, ``units.json``,
``report.json``, ``report.md``, and ``proofread.md``. Runs are never
overwritten.
"""

import json
from dataclasses import dataclass
from datetime import date, datetime
from pathlib import Path
from typing import Any

from jsonschema import Draft202012Validator

from faa_directive_impact.directives.source_text import (
    SourceDocument,
    documents_for,
    load_generation,
)
from faa_directive_impact.evaluation.b2_run import B2Unit, prepare, usage_totals
from faa_directive_impact.evaluation.b3_fields import compare
from faa_directive_impact.evaluation.b3_prompt import (
    PROMPT_VERSION,
    RULE_SCHEMA,
    build_request,
)
from faa_directive_impact.evaluation.s1_run import GENERATION_ID
from faa_directive_impact.evaluation.s1_scoring import (
    GATE_NAMES,
    GATE_VERSION,
    PROTECTED,
    score_unit,
)
from faa_directive_impact.llm.client import (
    LiveModel,
    ModelRequest,
    ModelResponse,
    ReplayModel,
    call_batch,
    record,
)
from faa_directive_impact.rules.interpreter import INTERPRETER_VERSION, screen_rules

DIRECTIVES = ("2025-18469", "2026-16954")
REFERENCE_DIR = Path("evaluation/b3/reference")
CLAIM_NOTE = (
    "The evaluated claim stays AD 2025-19-13. AD 2026-17-03 results are "
    "reported separately; its labels and reference record are Claude drafts "
    "awaiting owner confirmation, and they do not widen the claim."
)
REFERENCE_NOTE = (
    "The reference records were written by the same author as the seed labels "
    "(Claude), so field accuracy measures agreement with one reading, as S1 "
    "does. The interpreter applies no adjudication: where the readings of AD "
    "2025-19-13 (g) diverge (seed-005), it routes to review even with the "
    "reference record, so that unit fails gates 8 and 12 for every system "
    "here and is not counted against a draft."
)


@dataclass(frozen=True)
class Thread:
    directive: str
    documents: tuple[SourceDocument, ...]
    units: tuple[B2Unit, ...]


def prepare_threads(repo: Path, storage_root: Path) -> list[Thread]:
    """Each directive with its thread documents and its scored units."""
    documents, relationships = load_generation(
        repo / "generations" / GENERATION_ID, storage_root
    )
    items = prepare(repo, storage_root)
    threads = []
    for directive in DIRECTIVES:
        units = tuple(i for i in items if i.unit.expected["directive"] == directive)
        latest = max(item.as_of for item in units)
        given = documents_for(directive, latest, documents, relationships)
        threads.append(Thread(directive, tuple(given), units))
    return threads


def request_for(
    thread: Thread, model: str, effort: str, max_tokens: int = 32000
) -> ModelRequest:
    return build_request(
        model, effort, thread.directive, list(thread.documents), max_tokens
    )


def load_references(repo: Path) -> dict[str, dict[str, Any]]:
    return {
        directive: json.loads(
            (repo / REFERENCE_DIR / f"{directive}.json").read_text(encoding="utf-8")
        )
        for directive in DIRECTIVES
    }


def run_b3(
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
    max_tokens: int = 32000,
) -> Path:
    """Draft each directive's rule record with one model, record, and score."""
    threads = prepare_threads(repo, storage_root)
    name = model.removeprefix("claude-")
    stamp = started_at.strftime("%Y%m%dT%H%M%SZ")
    directory = runs_root / f"b3-{name}-{effort}-r{repeat}-{stamp}-{commit[:7]}"
    directory.mkdir(parents=True, exist_ok=False)
    requests = [request_for(t, model, effort, max_tokens) for t in threads]

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
        record(directory / "calls", request, response)

    meta = {
        "run_id": directory.name,
        "system": "B3 model-drafted rules, interpreted",
        "model": model,
        "effort": effort,
        "max_tokens": max_tokens,
        "repeat": repeat,
        "mode": mode,
        "prompt_version": PROMPT_VERSION,
        "interpreter_version": INTERPRETER_VERSION,
        "gate_version": GATE_VERSION,
        "started_at": started_at.isoformat(),
        "git_commit": commit,
        "worktree_dirty": dirty,
        "generation_id": GENERATION_ID,
    }
    write_results(repo, directory, meta, threads, responses)
    return directory


def replay_results(repo: Path, storage_root: Path, directory: Path) -> dict[str, Any]:
    """Re-score a recorded run without calling the model."""
    meta = json.loads((directory / "report.json").read_text(encoding="utf-8"))["meta"]
    threads = prepare_threads(repo, storage_root)
    replay = ReplayModel(directory / "calls")
    responses = [
        replay.call(request_for(t, meta["model"], meta["effort"], meta["max_tokens"]))
        for t in threads
    ]
    return score(repo, threads, responses)


def valid_draft(response: ModelResponse) -> dict[str, Any] | None:
    answer = response.answer
    if answer is None or list(Draft202012Validator(RULE_SCHEMA).iter_errors(answer)):
        return None
    return answer


def screen_unit(
    rules: dict[str, Any] | None, item: B2Unit
) -> tuple[dict[str, Any] | None, str | None]:
    """The interpreter's output for one unit, or None with the reason."""
    if rules is None:
        return None, "no valid rule record"
    try:
        screened = screen_rules(rules, item.unit.record["asset_snapshot"], item.as_of)
    except (KeyError, TypeError, ValueError) as error:
        return None, f"interpreter rejected the record: {type(error).__name__}: {error}"
    return screened.to_dict(), None


def score(
    repo: Path, threads: list[Thread], responses: list[ModelResponse]
) -> dict[str, Any]:
    references = load_references(repo)
    fields, units = {}, []
    for thread, response in zip(threads, responses, strict=True):
        draft = valid_draft(response)
        reference = references[thread.directive]
        fields[thread.directive] = (
            compare(draft, reference) if draft is not None else {"no_answer": True}
        )
        for item in thread.units:
            drafted, error = screen_unit(draft, item)
            referenced, _ = screen_unit(reference, item)
            gates = score_unit(item.unit, drafted, item.index)
            reference_gates = score_unit(item.unit, referenced, item.index)
            failed = _failed(gates)
            reference_failed = _failed(reference_gates)
            units.append(
                {
                    "unit": item.unit.name,
                    "directive": thread.directive,
                    "expected": [
                        item.unit.expected["applicability"],
                        item.unit.expected.get("action_status"),
                    ],
                    "drafted": [drafted["applicability"], drafted["action_status"]]
                    if drafted
                    else None,
                    "reference": [
                        referenced["applicability"],
                        referenced["action_status"],
                    ]
                    if referenced
                    else None,
                    "error": error,
                    "failed": failed,
                    "reference_failed": reference_failed,
                    "extraction_errors": [
                        g for g in failed if g not in reference_failed
                    ],
                    "details": {g: gates[g].get("detail", "") for g in failed},
                    "output": drafted,
                }
            )
    return {"fields": fields, "units": units, "summary": summarize(fields, units)}


def summarize(fields: dict[str, Any], units: list[dict[str, Any]]) -> dict[str, Any]:
    per_directive = {}
    for directive in DIRECTIVES:
        mine = [u for u in units if u["directive"] == directive]
        result = fields[directive]
        per_directive[directive] = {
            "field_accuracy": None if result.get("no_answer") else result["accuracy"],
            "fields_correct": None if result.get("no_answer") else result["correct"],
            "fields": None if result.get("no_answer") else result["fields"],
            "ambiguities_flagged": None
            if result.get("no_answer")
            else sum(a["flagged"] for a in result["ambiguities"]["expected"]),
            "ambiguities_expected": None
            if result.get("no_answer")
            else len(result["ambiguities"]["expected"]),
            "units": len(mine),
            "units_with_extraction_errors": sum(
                bool(u["extraction_errors"]) for u in mine
            ),
            "protected_extraction_errors": sum(
                g in PROTECTED for u in mine for g in u["extraction_errors"]
            ),
            "reference_protected_failures": sum(
                g in PROTECTED for u in mine for g in u["reference_failed"]
            ),
        }
    return per_directive


def write_results(
    repo: Path,
    directory: Path,
    meta: dict[str, Any],
    threads: list[Thread],
    responses: list[ModelResponse],
) -> None:
    results = score(repo, threads, responses)
    extractions = directory / "extractions"
    extractions.mkdir(exist_ok=True)
    for thread, response in zip(threads, responses, strict=True):
        (extractions / f"{thread.directive}.json").write_text(
            json.dumps(response.answer, indent=2, ensure_ascii=False) + "\n",
            encoding="utf-8",
        )
    report = {
        "meta": meta,
        "usage": usage_totals(responses),
        "summary": results["summary"],
        "disclosures": [CLAIM_NOTE, REFERENCE_NOTE],
    }
    _write_json(directory / "report.json", report)
    _write_json(directory / "fields.json", results["fields"])
    _write_json(directory / "units.json", results["units"])
    (directory / "report.md").write_text(
        report_markdown(report, results), encoding="utf-8"
    )
    (directory / "proofread.md").write_text(
        proofread_markdown(meta, threads, responses), encoding="utf-8"
    )


def report_markdown(report: dict[str, Any], results: dict[str, Any]) -> str:
    meta, usage = report["meta"], report["usage"]
    lines = [
        f"# B3 run {meta['run_id']}",
        "",
        f"Model `{meta['model']}` at {meta['effort']} effort, repeat "
        f"{meta['repeat']}; prompt `{meta['prompt_version']}`, interpreter "
        f"v{meta['interpreter_version']}, gates v{meta['gate_version']}. Cost "
        f"${usage['cost_usd']:.4f}.",
        "",
        "| Directive | Field accuracy | Ambiguities flagged | Units | Units with "
        "extraction errors | Protected extraction errors |",
        "|---|---|---|---|---|---|",
    ]
    for directive, s in report["summary"].items():
        accuracy = (
            "no answer"
            if s["field_accuracy"] is None
            else f"{s['fields_correct']}/{s['fields']}"
        )
        flagged = (
            "–"
            if s["ambiguities_flagged"] is None
            else f"{s['ambiguities_flagged']}/{s['ambiguities_expected']}"
        )
        lines.append(
            f"| {directive} | {accuracy} | {flagged} | {s['units']} | "
            f"{s['units_with_extraction_errors']} | {s['protected_extraction_errors']} |"
        )
    lines += ["", "## Field errors", ""]
    for directive, result in results["fields"].items():
        if result.get("no_answer"):
            lines.append(f"- {directive}: no valid rule record.")
            continue
        for check in result["checks"]:
            if not check["correct"]:
                lines.append(
                    f"- {directive} `{check['field']}`: expected "
                    f"`{json.dumps(check['expected'])}`, drafted "
                    f"`{json.dumps(check['drafted'])}`"
                )
        for extra in result["ambiguities"]["additional"]:
            lines.append(
                f"- {directive}: additional ambiguity on {extra['paragraph']} "
                "(for the proofreader)"
            )
    lines += [
        "",
        "## Units",
        "",
        "| Unit | Expected | Drafted | Reference | "
        "Extraction errors | Also fail with reference |",
        "|---|---|---|---|---|---|",
    ]
    for unit in results["units"]:
        lines.append(
            f"| {unit['unit']} | {'/'.join(map(str, unit['expected']))} | "
            f"{'/'.join(map(str, unit['drafted'])) if unit['drafted'] else unit['error']} | "
            f"{'/'.join(map(str, unit['reference']))} | "
            f"{', '.join(unit['extraction_errors']) or '–'} | "
            f"{', '.join(unit['reference_failed']) or '–'} |"
        )
    lines += ["", "Gates: " + "; ".join(f"{k} {v}" for k, v in GATE_NAMES.items()), ""]
    lines += [f"- {note}" for note in report["disclosures"]]
    return "\n".join(lines) + "\n"


def proofread_markdown(
    meta: dict[str, Any], threads: list[Thread], responses: list[ModelResponse]
) -> str:
    """The sheet a person proofreads against the AD text, with a timer."""
    lines = [
        f"# Proofread: B3 drafted rule records ({meta['run_id']})",
        "",
        "Start a timer. For each directive, read the drafted record below against "
        "the AD text and mark every field that is wrong or unsupported. Do not "
        "look at the reference records or the field scores first. Record the "
        "minutes per directive in `proofread.yaml`.",
        "",
    ]
    for thread, response in zip(threads, responses, strict=True):
        documents = ", ".join(d.number for d in thread.documents)
        lines += [
            f"## {thread.directive} (documents given: {documents})",
            "",
            "```json",
            json.dumps(response.answer, indent=2, ensure_ascii=False),
            "```",
            "",
        ]
    return "\n".join(lines)


def _failed(gates: dict[str, dict[str, Any]]) -> list[str]:
    return [g for g, r in gates.items() if r["covered"] and not r["passed"]]


def _write_json(path: Path, value: Any) -> None:
    path.write_text(
        json.dumps(value, indent=2, ensure_ascii=False) + "\n", encoding="utf-8"
    )


def thread_as_of(thread: Thread) -> date:
    return max(item.as_of for item in thread.units)
