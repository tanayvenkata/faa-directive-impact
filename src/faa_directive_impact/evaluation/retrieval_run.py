"""Score a retriever on the seed cases under the step 7 pre-registration.

Gate 14 is ``GATES.md`` v1's candidate recall; M1 to M3 are report-only
(``evaluation/retrieval/PREREGISTRATION.md``). A run is written to its own
directory with every case's full candidate list, so it can be re-read without
re-running.
"""

import json
import statistics
from datetime import UTC, date, datetime
from pathlib import Path
from typing import Any

from faa_directive_impact.evaluation.seed import load_seed_cases
from faa_directive_impact.impact.hpt_hub_rules import SUPPORTED_ENGINE_MODELS
from faa_directive_impact.retrieval.search import RETRIEVER_VERSION, retrieve

CORPUS_FILE = Path("evaluation/retrieval/corpus.json")
SELECTION_FILE = Path("evaluation/retrieval/corpus-selection.json")
DISTRACTOR_GROUPS = ("iae_out", "cfm", "pw")
PROTECTED_OUTCOMES = ("action_required", "action_required_on_event", "needs_review")


def score_retrieval(repo: Path) -> dict[str, Any]:
    corpus = json.loads((repo / CORPUS_FILE).read_text(encoding="utf-8"))
    records = corpus["records"]
    selection = json.loads((repo / SELECTION_FILE).read_text(encoding="utf-8"))
    distractors = {
        number: group for group in DISTRACTOR_GROUPS for number in selection[group]
    }
    by_number = {record["document"]: record for record in records}
    cases: list[dict[str, Any]] = []
    for case in load_seed_cases(repo / "evaluation/seed/cases"):
        record = case.record
        asset = record["asset_snapshot"]
        as_of = date.fromisoformat(record["source_snapshot"]["as_of"])
        found = retrieve(records, asset, as_of)
        surfaced = {candidate["document"] for candidate in found}
        expected = {item["directive"]: item for item in record["expected"]}
        in_family = asset["engine"].get("engine_model") in SUPPORTED_ENGINE_MODELS
        misses = []
        for directive in record["directive_candidates"]:
            if directive in surfaced:
                continue
            outcome = _outcome(expected.get(directive))
            misses.append(
                {
                    "directive": directive,
                    "expected_outcome": outcome,
                    "in_corpus": directive in by_number,
                    "protected": outcome in PROTECTED_OUTCOMES,
                }
            )
        wanted = len(record["directive_candidates"])
        cases.append(
            {
                "case_id": record["case_id"],
                "as_of": as_of.isoformat(),
                "engine_model": asset["engine"].get("engine_model"),
                "in_family": in_family,
                "directive_candidates": record["directive_candidates"],
                "recall": f"{wanted - len(misses)}/{wanted}",
                "misses": misses,
                "distractors_surfaced": sorted(
                    f"{number} ({distractors[number]})"
                    for number in surfaced
                    if number in distractors
                )
                if in_family
                else [],
                "part_number_only": sorted(
                    candidate["document"]
                    for candidate in found
                    if candidate["via"] == "part_number"
                    and asset["engine"].get("engine_model", "").upper()
                    not in by_number[candidate["document"]]["applicability_models"]
                ),
                "candidates": found,
            }
        )
    protected = [
        f"{case['case_id']}/{miss['directive']}"
        for case in cases
        for miss in case["misses"]
        if miss["protected"]
    ]
    sizes = [len(case["candidates"]) for case in cases]
    return {
        "retriever": RETRIEVER_VERSION,
        "corpus_generation": corpus["generation_id"],
        "corpus_documents": len(records),
        "created_at_utc": datetime.now(UTC).strftime("%Y-%m-%dT%H:%M:%SZ"),
        "gate_14": {
            "verdict": "fail" if protected else "pass",
            "protected_failures": protected,
            "candidates_surfaced": sum(
                len(c["directive_candidates"]) - len(c["misses"]) for c in cases
            ),
            "candidates_expected": sum(len(c["directive_candidates"]) for c in cases),
            "unprotected_misses": [
                f"{case['case_id']}/{miss['directive']} ({miss['expected_outcome']})"
                for case in cases
                for miss in case["misses"]
                if not miss["protected"]
            ],
        },
        "m1_distractors_for_in_family_engines": sum(
            len(case["distractors_surfaced"]) for case in cases
        ),
        "m2_part_number_only": sum(len(case["part_number_only"]) for case in cases),
        "m3_candidate_set_size": {
            "median": statistics.median(sizes),
            "max": max(sizes),
        },
        "cases": cases,
    }


def write_retrieval_run(repo: Path, runs_root: Path) -> Path:
    result = score_retrieval(repo)
    stamp = result["created_at_utc"].replace("-", "").replace(":", "")
    directory = runs_root / f"retrieval-{RETRIEVER_VERSION.lower()}-{stamp}"
    directory.mkdir(parents=True, exist_ok=False)
    (directory / "report.json").write_text(
        json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8"
    )
    (directory / "report.md").write_text(_markdown(result), encoding="utf-8")
    return directory


def _outcome(expected: dict[str, Any] | None) -> str:
    if expected is None:
        return "no expected outcome"
    return expected.get("action_status") or expected["applicability"]


def _markdown(result: dict[str, Any]) -> str:
    gate = result["gate_14"]
    lines = [
        f"# Retrieval run: {result['retriever']}",
        "",
        f"- Corpus: `{result['corpus_generation']}`, "
        f"{result['corpus_documents']} documents",
        f"- Created: {result['created_at_utc']}",
        "",
        "| Measure | Result |",
        "|---|---|",
        f"| Gate 14 (protected) | **{gate['verdict']}**: "
        f"{gate['candidates_surfaced']}/{gate['candidates_expected']} candidates "
        f"surfaced; protected failures: "
        f"{', '.join(gate['protected_failures']) or 'none'} |",
        f"| Unprotected misses | {', '.join(gate['unprotected_misses']) or 'none'} |",
        f"| M1 distractors for in-family engines | "
        f"{result['m1_distractors_for_in_family_engines']} |",
        f"| M2 part-number-only candidates | {result['m2_part_number_only']} |",
        f"| M3 candidate-set size | median {result['m3_candidate_set_size']['median']}, "
        f"max {result['m3_candidate_set_size']['max']} |",
        "",
        "## Cases",
        "",
        "| Case | Engine | As of | Recall | Misses | Candidates |",
        "|---|---|---|---|---|---|",
    ]
    for case in result["cases"]:
        misses = ", ".join(
            f"{m['directive']} ({m['expected_outcome']})" for m in case["misses"]
        )
        lines.append(
            f"| {case['case_id']} | {case['engine_model']} | {case['as_of']} | "
            f"{case['recall']} | {misses or '—'} | {len(case['candidates'])} |"
        )
    return "\n".join(lines) + "\n"
