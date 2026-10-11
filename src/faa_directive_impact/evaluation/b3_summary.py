"""Summarize B3 repeats under the rules pre-registered in evaluation/b3/PREREGISTRATION.md.

Reads each run's ``fields.json``, ``units.json``, and ``report.json``; never
changes a run. It splits field accuracy into data fields and vocabulary
fields, and splits end-to-end extraction errors into safe escalations (the
interpreter declined an action it does not support and the unit went to
review; never gate 1) and substantive errors.
"""

import json
from pathlib import Path
from typing import Any

from faa_directive_impact.evaluation.b3_run import DIRECTIVES
from faa_directive_impact.evaluation.s1_scoring import PROTECTED

VOCABULARY_SUFFIXES = (".applies_to", ".trigger", ".combination")
DECLINED = "is not evaluated: this interpreter does not support"


def load_runs(runs_root: Path, prompt_version: str) -> list[dict[str, Any]]:
    runs = []
    for directory in sorted(runs_root.glob("b3-*-r*")):
        report_path = directory / "report.json"
        if not report_path.is_file():
            continue
        report = json.loads(report_path.read_text(encoding="utf-8"))
        if report["meta"]["prompt_version"] != prompt_version:
            continue
        runs.append(
            {
                "directory": directory.name,
                "report": report,
                "fields": json.loads((directory / "fields.json").read_text()),
                "units": json.loads((directory / "units.json").read_text()),
            }
        )
    return runs


def classify_unit(unit: dict[str, Any]) -> dict[str, list[str]]:
    declined = bool(unit["output"]) and any(
        DECLINED in note for note in unit["output"]["notes"]
    )
    safe = [g for g in unit["extraction_errors"] if declined and g != "1"]
    return {
        "safe_escalation": safe,
        "substantive": [g for g in unit["extraction_errors"] if g not in safe],
    }


def summarize_run(run: dict[str, Any]) -> dict[str, Any]:
    per_directive = {}
    for directive in DIRECTIVES:
        fields = run["fields"][directive]
        units = [u for u in run["units"] if u["directive"] == directive]
        classes = [classify_unit(u) for u in units]
        if fields.get("no_answer"):
            data = vocabulary = None
            flagged = None
        else:
            vocab = [
                c for c in fields["checks"] if c["field"].endswith(VOCABULARY_SUFFIXES)
            ]
            data_checks = [c for c in fields["checks"] if c not in vocab]
            data = [sum(c["correct"] for c in data_checks), len(data_checks)]
            vocabulary = [sum(c["correct"] for c in vocab), len(vocab)]
            expected = fields["ambiguities"]["expected"]
            flagged = [sum(a["flagged"] for a in expected), len(expected)]
        per_directive[directive] = {
            "data_fields": data,
            "vocabulary_fields": vocabulary,
            "ambiguities_flagged": flagged,
            "field_errors": []
            if fields.get("no_answer")
            else [c["field"] for c in fields["checks"] if not c["correct"]],
            "units": len(units),
            "units_safe_escalation": sum(bool(c["safe_escalation"]) for c in classes),
            "units_substantive": sum(bool(c["substantive"]) for c in classes),
            "protected_substantive": sum(
                g in PROTECTED for c in classes for g in c["substantive"]
            ),
            "false_clears": sum("1" in u["failed"] for u in units),
            "absolute_protected_failures": sum(
                g in PROTECTED for u in units for g in u["failed"]
            ),
        }
    return {
        "run": run["directory"],
        "cost_usd": run["report"]["usage"]["cost_usd"],
        "directives": per_directive,
    }


def summary_markdown(summaries: list[dict[str, Any]], prompt_version: str) -> str:
    lines = [
        "# B3 Summary",
        "",
        f"Prompt `{prompt_version}`; classes as pre-registered in "
        "`evaluation/b3/PREREGISTRATION.md`. Fractions are correct/total.",
        "",
        "| Run | Directive | Data fields | Vocabulary fields | Ambiguities flagged "
        "| Units with safe escalation | Units with substantive errors | Protected "
        "substantive | False clears | Absolute protected failures | Cost |",
        "|---|---|---|---|---|---|---|---|---|---|---|",
    ]

    def frac(value: list[int] | None) -> str:
        return "no answer" if value is None else f"{value[0]}/{value[1]}"

    for summary in summaries:
        for directive, s in summary["directives"].items():
            lines.append(
                f"| {summary['run']} | {directive} | {frac(s['data_fields'])} | "
                f"{frac(s['vocabulary_fields'])} | {frac(s['ambiguities_flagged'])} | "
                f"{s['units_safe_escalation']}/{s['units']} | "
                f"{s['units_substantive']}/{s['units']} | {s['protected_substantive']} | "
                f"{s['false_clears']} | {s['absolute_protected_failures']} | "
                f"${summary['cost_usd']:.4f} |"
            )
    lines += ["", "## Field errors", ""]
    for summary in summaries:
        for directive, s in summary["directives"].items():
            if s["field_errors"]:
                lines.append(
                    f"- {summary['run']} {directive}: "
                    + ", ".join(f"`{f}`" for f in s["field_errors"])
                )
    return "\n".join(lines) + "\n"
