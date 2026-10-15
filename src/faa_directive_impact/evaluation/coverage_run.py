"""Score rule records on the coverage units under the frozen gates.

``evaluation/coverage/PREREGISTRATION.md`` scores every in-scope V2500
directive except AD 2025-19-13 (which keeps S1) on its coverage cases and the
seed cases for it, with the same gate code S1, B2, and B3 use
(``s1_scoring.score_unit`` and ``summarize``). A set of rule records (the
hand-written references, raw drafts, or reviewed drafts) is screened by the
rule interpreter and scored per directive. Gates 5 and 11 are judged by hand
and stay pending here.
"""

import json
from dataclasses import dataclass
from datetime import UTC, date, datetime
from pathlib import Path
from typing import Any

from defusedxml import ElementTree

from faa_directive_impact.directives.source_text import documents_for, load_generation
from faa_directive_impact.evaluation.b2_run import CitationIndex, index_paragraphs
from faa_directive_impact.evaluation.s1_scoring import (
    Unit,
    score_unit,
    summarize,
    units,
)
from faa_directive_impact.evaluation.seed import load_seed_cases
from faa_directive_impact.rules.interpreter import INTERPRETER_VERSION, screen_rules
from faa_directive_impact.rules.serial_guard import invented_identifiers

GENERATION_ID = "gen-20261015T175844Z-57440372"
COVERAGE_CASES = Path("evaluation/coverage/cases")
SEED_CASES = Path("evaluation/seed/cases")
REFERENCE_DIR = Path("evaluation/coverage/reference")
CORPUS = Path("evaluation/retrieval/corpus.json")
# AD 2025-19-13 keeps S1 and its own evaluation; the proposal is not in force.
EXCLUDED = frozenset({"2025-18469", "2025-20088"})


@dataclass(frozen=True)
class CoverageUnit:
    unit: Unit
    directive: str
    as_of: date
    index: CitationIndex


def prepare(repo: Path, storage_root: Path) -> list[CoverageUnit]:
    """Every coverage unit, and every seed unit of a covered directive."""
    documents, relationships = load_generation(
        repo / "generations" / GENERATION_ID, storage_root
    )
    paragraphs = {
        number: index_paragraphs(ElementTree.fromstring(document.xml))
        for number, document in documents.items()
    }
    records = [c.record for c in load_seed_cases(repo / COVERAGE_CASES)]
    records += [c.record for c in load_seed_cases(repo / SEED_CASES)]
    references = {path.stem for path in (repo / REFERENCE_DIR).glob("*.json")}
    prepared = []
    for unit in units(records):
        directive = unit.expected["directive"]
        if directive in EXCLUDED or directive not in references:
            continue
        if unit.record["case_id"].startswith("seed-") and directive not in documents:
            continue
        as_of = date.fromisoformat(unit.record["source_snapshot"]["as_of"])
        index = CitationIndex({})
        for document in documents_for(directive, as_of, documents, relationships):
            index.add_document(
                document.number, paragraphs[document.number], document.text
            )
        prepared.append(CoverageUnit(unit, directive, as_of, index))
    return prepared


def load_records(directory: Path) -> dict[str, dict[str, Any]]:
    return {
        path.stem: json.loads(path.read_text(encoding="utf-8"))
        for path in sorted(directory.glob("*.json"))
    }


def score_records(
    records: dict[str, dict[str, Any]],
    items: list[CoverageUnit],
    corpus: dict[str, Any],
) -> dict[str, Any]:
    """Screen every unit with its directive's record and roll up per directive."""
    guard = {
        directive: invented_identifiers(record, corpus)
        for directive, record in records.items()
    }
    scored: dict[str, list[dict[str, Any]]] = {}
    for item in items:
        record = records.get(item.directive)
        output, error = None, None
        if record is None:
            error = "no rule record"
        elif guard[item.directive]:
            error = f"serial guard: {guard[item.directive]}"
        else:
            try:
                output = screen_rules(
                    record, item.unit.record["asset_snapshot"], item.as_of
                ).to_dict()
            except Exception as failure:  # the failure is this unit's answer
                error = f"interpreter: {type(failure).__name__}: {failure}"
        gates = score_unit(item.unit, output, item.index)
        scored.setdefault(item.directive, []).append(
            {
                "unit": item.unit.name,
                "severity": item.unit.record["severity"],
                "gates": gates,
                "expected": [
                    item.unit.expected["applicability"],
                    item.unit.expected.get("action_status"),
                ],
                "output": [output["applicability"], output["action_status"]]
                if output
                else None,
                "error": error,
                "failed": sorted(
                    (g for g, r in gates.items() if not r.get("passed", True)),
                    key=int,
                ),
            }
        )
    directives = {}
    for directive, results in sorted(scored.items()):
        verdicts = summarize(results)
        mechanical = {
            n: v["verdict"]
            for n, v in verdicts.items()
            if v["verdict"] not in ("pending_hand_review", "not_exercised")
        }
        directives[directive] = {
            "units": len(results),
            "serial_guard": guard.get(directive, ["no rule record"]),
            "mechanical_verdicts": mechanical,
            "mechanical_pass": all(v == "pass" for v in mechanical.values()),
            "gates": verdicts,
            "results": results,
        }
    return {
        "interpreter_version": INTERPRETER_VERSION,
        "generation_id": GENERATION_ID,
        "directives": directives,
    }


def write_run(
    repo: Path, runs_root: Path, storage_root: Path, label: str, records_dir: Path
) -> Path:
    items = prepare(repo, storage_root)
    corpus = json.loads((repo / CORPUS).read_text(encoding="utf-8"))
    result = score_records(load_records(records_dir), items, corpus)
    stamp = datetime.now(UTC).strftime("%Y%m%dT%H%M%SZ")
    directory = runs_root / f"coverage-{label}-{stamp}"
    directory.mkdir(parents=True, exist_ok=False)
    result["records"] = str(records_dir)
    result["created_at_utc"] = stamp
    (directory / "report.json").write_text(
        json.dumps(result, indent=2, sort_keys=True, default=str) + "\n",
        encoding="utf-8",
    )
    (directory / "report.md").write_text(_markdown(result, label), encoding="utf-8")
    return directory


def _markdown(result: dict[str, Any], label: str) -> str:
    lines = [
        f"# Coverage run: {label}",
        "",
        f"- Records: `{result['records']}`; interpreter v{result['interpreter_version']}",
        f"- Source generation: `{result['generation_id']}`",
        "- Gates 5 and 11 are judged by hand and are pending here.",
        "",
        "| Directive | Units | Serial guard | Mechanical gates | Failed units |",
        "|---|---|---|---|---|",
    ]
    for directive, row in result["directives"].items():
        failed = [r for r in row["results"] if r["failed"]]
        detail = "; ".join(
            f"{r['unit']} ({', '.join(r['failed'])}): expected "
            f"{'/'.join(str(x) for x in r['expected'])}, got "
            f"{'/'.join(str(x) for x in r['output']) if r['output'] else r['error']}"
            for r in failed
        )
        lines.append(
            f"| {directive} | {row['units']} | "
            f"{'ok' if not row['serial_guard'] else 'FAIL'} | "
            f"{'pass' if row['mechanical_pass'] else 'fail'} | {detail or '—'} |"
        )
    return "\n".join(lines) + "\n"
