"""Summarize B2 repeats per model, next to S1, from the kept run reports.

Only runs of the given prompt version are summarized. Each failure is
reported as a count out of the repeats, and units whose answer changed
between repeats are listed, because a model that answers differently on
identical input is itself a finding.
"""

import json
from collections import defaultdict
from pathlib import Path
from typing import Any

from faa_directive_impact.evaluation.s1_scoring import GATE_NAMES, PROTECTED

MECHANICAL = ("1", "2", "3", "4", "6", "7", "8", "9", "10", "12", "13")


def load_runs(runs_root: Path, prompt_version: str) -> dict[str, list[dict]]:
    by_model: dict[str, list[dict]] = defaultdict(list)
    for path in sorted(runs_root.glob("b2-*/report.json")):
        report = json.loads(path.read_text(encoding="utf-8"))
        if report.get("prompt_version") != prompt_version:
            continue
        outputs = json.loads((path.parent / "outputs.json").read_text("utf-8"))
        report["outputs"] = outputs
        by_model[f"{report['model']} @ {report['effort']}"].append(report)
    for runs in by_model.values():
        runs.sort(key=lambda report: report["repeat"])
    return dict(by_model)


def summarize_model(runs: list[dict]) -> dict[str, Any]:
    names = [unit["unit"] for unit in runs[0]["units"]]
    directive = {unit["unit"]: unit["directive"] for unit in runs[0]["units"]}
    failures: dict[str, dict[str, int]] = {name: {} for name in names}
    answers: dict[str, set[str]] = {name: set() for name in names}
    for run in runs:
        for unit in run["units"]:
            for gate, result in unit["gates"].items():
                if gate in MECHANICAL and not result["passed"]:
                    failures[unit["unit"]][gate] = (
                        failures[unit["unit"]].get(gate, 0) + 1
                    )
            output = run["outputs"][unit["unit"]]["output"]
            answers[unit["unit"]].add(
                "no_answer"
                if output is None
                else f"{output['applicability']}/{output['action_status']}"
            )
    cost = sum(run["usage"]["cost_usd"] for run in runs)
    units_per_run = len(names)
    return {
        "model": runs[0]["model"],
        "effort": runs[0]["effort"],
        "repeats": len(runs),
        "run_ids": [run["run_id"] for run in runs],
        "cost_usd": round(cost, 4),
        "cost_usd_per_unit": round(cost / (units_per_run * len(runs)), 5),
        "mean_latency_seconds": round(
            sum(run["usage"]["mean_latency_seconds"] for run in runs) / len(runs), 1
        ),
        "failures": {name: gates for name, gates in failures.items() if gates},
        "unstable_units": sorted(
            name for name, seen in answers.items() if len(seen) > 1
        ),
        "answers": {name: sorted(seen) for name, seen in answers.items()},
        "directive": directive,
    }


def summary_markdown(summaries: list[dict], prompt_version: str) -> str:
    lines = [
        "# B2 Summary",
        "",
        f"Prompt version `{prompt_version}`. Mechanical gates only; gates 5 and "
        "11 are on each run's hand-review sheet. S1 (hand-written rules) passes "
        "every mechanical gate on the 18 AD 2025-19-13 units.",
        "",
        "| Model | Effort | Repeats | Cost | Cost per engine check | Mean latency |",
        "|---|---|---|---|---|---|",
    ]
    for s in summaries:
        lines.append(
            f"| `{s['model']}` | {s['effort']} | {s['repeats']} | ${s['cost_usd']} "
            f"| ${s['cost_usd_per_unit']} | {s['mean_latency_seconds']} s (batch) |"
        )
    for s in summaries:
        k = s["repeats"]
        lines += [
            "",
            f"## `{s['model']}` at {s['effort']} effort",
            "",
            "Failures per unit, as runs failing out of "
            f"{k}. Protected gates are marked *.",
            "",
            f"| Unit | Directive | Failed gates (runs out of {k}) | Answers seen |",
            "|---|---|---|---|",
        ]
        for name, gates in s["failures"].items():
            shown = ", ".join(
                f"{g}{'*' if g in PROTECTED else ''} ({n}/{k})"
                for g, n in sorted(gates.items(), key=lambda item: int(item[0]))
            )
            lines.append(
                f"| {name} | {s['directive'][name]} | {shown} | "
                f"{'; '.join(s['answers'][name])} |"
            )
        lines += [
            "",
            "Units whose answer changed between repeats: "
            + (", ".join(s["unstable_units"]) or "none")
            + ".",
        ]
    lines += [
        "",
        "Gate names: " + "; ".join(f"{n} {GATE_NAMES[n]}" for n in MECHANICAL) + ".",
        "",
    ]
    return "\n".join(lines)
