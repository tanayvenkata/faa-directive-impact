"""Run the S1 rules baseline end to end and write a kept run directory.

One run builds the normalized record from the frozen XML, screens every seed
engine against AD 2025-19-13, scores the 18 S1 units under the frozen gates,
and writes everything to ``evaluation/runs/<run-id>/``:

- ``normalized-record.json``: the derived record the rules read;
- ``outputs.json``: each unit's structured screen;
- ``report.json`` and ``report.md``: gate results, disclosures, known gaps;
- ``hand-review.md`` and ``hand-review.yaml``: the sheet for gates 5 and 11;
- ``queues.html``: the static three-queue page.

``conclude_run`` later folds the completed hand review into ``verdict.json``
and ``verdict.md``. Runs are never overwritten.
"""

import json
import re
from datetime import date, datetime
from pathlib import Path
from typing import Any

import yaml

from faa_directive_impact.directives.hpt_hub_record import (
    build_record,
    canonical_json,
)
from faa_directive_impact.evaluation.s1_scoring import (
    GATE_NAMES,
    GATE_VERSION,
    STANDING_FORBIDDEN,
    Unit,
    conclude,
    hand_review_template,
    score_unit,
    summarize,
    units,
)
from faa_directive_impact.evaluation.seed import load_seed_cases
from faa_directive_impact.impact.hpt_hub_rules import screen
from faa_directive_impact.impact.queue_page import render_page

GENERATION_ID = "gen-20260926T215105Z-7fe9da08"
SOURCE_XML = Path("tests/fixtures/federal-register/2025-18469/full-text.xml")
LABEL_CHECKS = Path("evaluation/seed/critique/s1-label-checks.yaml")
ORACLE_DISCLOSURE = (
    "The S1 rules port the logic of `evaluation/hpt_hub_reference.py`, the "
    "reference derivation written alongside the seed labels by the same "
    "author, and add citations and wording. A test asserts the two agree on "
    "every S1 unit. Agreement with the labels therefore shows that the rules "
    "reproduce one reading of AD 2025-19-13 consistently. It does not show "
    "that the reading is correct. Practitioner review (issue #9) is the "
    "independent check."
)
SAMPLE_CAVEAT = (
    "Eighteen units cannot support a statistical claim. With zero failures in "
    "18 units, the rough 95% upper bound on the true failure rate is about "
    "17% (3/18); for the ten gate 1 units it is about 30%. Results are exact "
    "counts on this disclosed suite, not rates. Protected gates are "
    "tripwires, not statistical demonstrations."
)


def run_s1(
    repo: Path, runs_root: Path, started_at: datetime, commit: str, dirty: bool
) -> Path:
    """Execute one S1 run and return its directory."""
    record = build_record(
        (repo / SOURCE_XML).read_bytes(), repo / "generations" / GENERATION_ID
    )
    cases = [case.record for case in load_seed_cases(repo / "evaluation/seed/cases")]
    all_units = units(cases)
    confirmed = _confirmed_labels(repo / LABEL_CHECKS)

    scored, outputs, screened = [], {}, []
    for unit in all_units:
        if not unit.in_s1:
            continue
        as_of = unit.record["source_snapshot"]["as_of"]
        result = screen(
            record, unit.record["asset_snapshot"], date.fromisoformat(as_of)
        ).to_dict()
        outputs[unit.name] = result
        screened.append(
            {
                "case": unit.name,
                "as_of": as_of,
                "engine": unit.record["asset_snapshot"]["engine"],
                "screen": result,
            }
        )
        scored.append(
            {
                "unit": unit.name,
                "slice": unit.record["slice"],
                "severity": unit.record["severity"],
                "has_action_timing": "action_timing" in unit.expected,
                "gates": score_unit(unit, result, record),
            }
        )

    run_id = f"s1-{started_at.strftime('%Y%m%dT%H%M%SZ')}-{commit[:7]}"
    directory = runs_root / run_id
    directory.mkdir(parents=True, exist_ok=False)
    gates = summarize(scored, confirmed)
    report = {
        "run_id": run_id,
        "system": "S1 rules baseline (hpt_hub_rules)",
        "gate_version": GATE_VERSION,
        "started_at": started_at.isoformat(),
        "git_commit": commit,
        "worktree_dirty": dirty,
        "generation_id": GENERATION_ID,
        "source_sha256": record["source"]["sha256"],
        "normalized_record_sha256": record["record_sha256"],
        "normalizer_version": record["normalizer_version"],
        "oracle_disclosure": ORACLE_DISCLOSURE,
        "sample_caveat": SAMPLE_CAVEAT,
        "units_scored": len(scored),
        "units_not_yet_evaluated": [u.name for u in all_units if not u.in_s1],
        "confirmed_labels": sorted(confirmed),
        "gates": gates,
        "units": scored,
    }
    meta = {"run_id": run_id, "gate_version": GATE_VERSION, "commit": commit[:7]}
    known_gaps = _gates_section(repo / "evaluation/GATES.md", "Known Gaps")

    _write(directory / "normalized-record.json", canonical_json(record))
    _write(directory / "outputs.json", canonical_json(outputs))
    _write(directory / "report.json", canonical_json(report))
    _write(directory / "report.md", report_markdown(report, known_gaps))
    _write(
        directory / "hand-review.md",
        hand_review_markdown(all_units, outputs, scored, record),
    )
    _write(
        directory / "hand-review.yaml",
        yaml.safe_dump(hand_review_template(scored), sort_keys=False, width=88),
    )
    _write(directory / "queues.html", render_page(screened, record, meta))
    return directory


def conclude_run(repo: Path, directory: Path) -> dict[str, Any]:
    """Fold the completed hand review into the run's verdict files."""
    report = json.loads((directory / "report.json").read_text(encoding="utf-8"))
    review = yaml.safe_load((directory / "hand-review.yaml").read_text("utf-8"))
    verdict = conclude(report, review, _confirmed_labels(repo / LABEL_CHECKS))
    _write(directory / "verdict.json", canonical_json(verdict))
    _write(directory / "verdict.md", verdict_markdown(verdict))
    return verdict


def report_markdown(report: dict[str, Any], known_gaps: str) -> str:
    lines = [
        f"# S1 Run {report['run_id']}",
        "",
        "| Field | Value |",
        "|---|---|",
        f"| System | {report['system']} |",
        f"| Gate version | {report['gate_version']} |",
        f"| Git commit | `{report['git_commit']}` |",
        f"| Uncommitted changes at run time | {report['worktree_dirty']} |",
        f"| Source generation | `{report['generation_id']}` |",
        f"| Source XML SHA-256 | `{report['source_sha256']}` |",
        f"| Normalized record SHA-256 | `{report['normalized_record_sha256']}` |",
        f"| Units scored | {report['units_scored']} |",
        "",
        "## Read This First",
        "",
        report["oracle_disclosure"],
        "",
        report["sample_caveat"],
        "",
        "Gates 5 and 11 are checked by hand on `hand-review.md`. Until that "
        "review is recorded in `verdict.md`, the go / constrain / switch "
        "decision is not made.",
        "",
        "## Gates",
        "",
        "| # | Gate | Verdict | Covered S1 units | Failed |",
        "|---|---|---|---|---|",
    ]
    for number, gate in report["gates"].items():
        covered = gate.get("covered")
        failed = gate.get("failed", [])
        lines.append(
            f"| {number} | {GATE_NAMES[number]} | {gate['verdict']} | "
            f"{len(covered) if covered is not None else '—'} | "
            f"{', '.join(failed) if failed else '—'} |"
        )
    lines += [
        "",
        "Gate 10 is scored here on its citation part only: each required "
        "(document, paragraph) pair must be cited, and every clear must cite "
        "its clearing paragraph. Locators are listed on the hand-review sheet.",
        "",
        "## Units",
        "",
        "| Unit | Slice | Severity | Failed gates |",
        "|---|---|---|---|",
    ]
    for unit in report["units"]:
        failed = [n for n, g in unit["gates"].items() if not g["passed"]]
        lines.append(
            f"| {unit['unit']} | {unit['slice']} | {unit['severity']} | "
            f"{', '.join(failed) or '—'} |"
        )
    lines += ["", "## Failure Taxonomy (mechanical gates)", ""]
    failures = [
        (unit["unit"], n, g["detail"])
        for unit in report["units"]
        for n, g in unit["gates"].items()
        if not g["passed"]
    ]
    if failures:
        lines += ["| Unit | Gate | Detail |", "|---|---|---|"]
        lines += [f"| {u} | {n} | {d} |" for u, n, d in failures]
    else:
        lines.append(
            "No mechanical gate failed on any S1 unit. This is expected: the "
            "rules port the reference derivation that already agrees with "
            "every label (see Read This First)."
        )
    lines += [
        "",
        "## Not Yet Evaluated",
        "",
        "S1 covers only AD 2025-19-13. These units are neither passes nor "
        "failures: " + ", ".join(report["units_not_yet_evaluated"]) + ".",
        "",
        "## Known Gaps (from GATES.md)",
        "",
        "A pass says nothing about these risks.",
        "",
        known_gaps.strip(),
        "",
    ]
    return "\n".join(lines)


def hand_review_markdown(
    all_units: list[Unit],
    outputs: dict[str, Any],
    scored: list[dict[str, Any]],
    record: dict[str, Any],
) -> str:
    by_name = {u.name: u for u in all_units}
    rows = {r["serial_number"]: r for r in record["table_1"]["rows"]}
    lines = [
        "# S1 Hand-Review Sheet",
        "",
        "Record results in `hand-review.yaml`, then run "
        "`make s1-conclude RUN=<run directory>`.",
        "",
        "- **Gate 5:** read the output against every forbidden claim below, "
        "including the standing list. A field value that entails a claim "
        "counts as stating it. Record `absent` or `present` with a reason.",
        "- **Gate 11:** compare the stated timing with the expected timing. "
        "Record `contradicts` only for a wrong trigger, limit, or date.",
        "- **Locators:** each cited table row is printed beside the row it names.",
        "",
        "Standing forbidden claims, for every unit:",
        "",
    ]
    lines += [f"- {claim}" for claim in STANDING_FORBIDDEN]
    for item in scored:
        unit = by_name[item["unit"]]
        output = outputs[item["unit"]]
        expected = unit.expected
        lines += [
            "",
            f"## {item['unit']}: {unit.record['title']}",
            "",
            f"- **Fields:** applicability `{output['applicability']}`, "
            f"action_status `{output['action_status']}`, authority "
            f"`{output['authority_state']}`, queue `{output['queue']}`",
            f"- **Expected:** applicability `{expected['applicability']}`, "
            f"action_status `{expected.get('action_status')}`",
            f"- **Summary:** {output['summary']}",
        ]
        lines += [f"- **Hub finding:** {hub['statement']}" for hub in output["hubs"]]
        if output["timing"]:
            lines.append(f"- **Stated timing:** {output['timing']}")
        if "action_timing" in expected:
            lines.append(
                f"- **Expected timing:** {expected['action_timing']['description']}"
            )
        for fact in output["missing_facts"]:
            lines.append(f"- **Missing fact:** `{fact}`")
        lines += [f"- **Note:** {note}" for note in output["notes"]]
        lines += ["", "Forbidden claims for this case:", ""]
        lines += [f"- {claim}" for claim in unit.record["forbidden_claims"]]
        located = [c for c in output["citations"] if c["locator"]]
        if located:
            lines += ["", "Cited locators:", ""]
            for citation in located:
                row = None
                match = re.fullmatch(r"table 1 row S/N (\S+)", citation["locator"])
                if match:
                    row = rows.get(match.group(1))
                shown = (
                    f" → {row['component']} P/N {row['part_number']} S/N "
                    f"{row['serial_number']}, limit "
                    f"{row['removal_limit_cycles_since_new']:,} CSN"
                    if row
                    else ""
                )
                lines.append(f"- {citation['paragraph']} {citation['locator']}{shown}")
    lines.append("")
    return "\n".join(lines)


def verdict_markdown(verdict: dict[str, Any]) -> str:
    status = (
        "PROVISIONAL: the hand review is not yet confirmed by the project owner."
        if verdict["provisional"]
        else "Confirmed by the project owner."
    )
    lines = [
        f"# S1 Verdict for {verdict['run_id']}",
        "",
        f"**Decision: {verdict['decision']}.** {verdict['why']}",
        "",
        f"Reviewer: {verdict['reviewer']}. {status}",
        "",
        "| # | Gate | Verdict | Failed |",
        "|---|---|---|---|",
    ]
    for number, gate in verdict["gates"].items():
        failed = gate.get("failed", [])
        lines.append(
            f"| {number} | {GATE_NAMES[number]} | {gate['verdict']} | "
            f"{', '.join(failed) if failed else '—'} |"
        )
    lines.append("")
    return "\n".join(lines)


def _confirmed_labels(path: Path) -> frozenset[str]:
    """Units whose failing label was checked against the AD and upheld."""
    if not path.is_file():
        return frozenset()
    checks = yaml.safe_load(path.read_text(encoding="utf-8")) or []
    return frozenset(
        check["unit"] for check in checks if check["verdict"] == "label_correct"
    )


def _gates_section(path: Path, heading: str) -> str:
    text = path.read_text(encoding="utf-8")
    match = re.search(
        rf"^### {re.escape(heading)}\n(.*?)(?=^##)", text, re.MULTILINE | re.DOTALL
    )
    if match is None:
        raise ValueError(f"GATES.md has no '{heading}' section")
    return match.group(1)


def _write(path: Path, text: str) -> None:
    path.write_text(text, encoding="utf-8")
