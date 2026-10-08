import json
from pathlib import Path

from faa_directive_impact.evaluation.b2_summary import (
    load_runs,
    summarize_model,
    summary_markdown,
)


def write_run(root: Path, repeat: int, status: str, gate_1_passed: bool) -> None:
    directory = root / f"b2-test-r{repeat}"
    directory.mkdir()
    gates = {n: {"passed": True} for n in ("1", "6", "10")}
    gates["1"]["passed"] = gate_1_passed
    report = {
        "run_id": directory.name,
        "model": "claude-test",
        "effort": "medium",
        "repeat": repeat,
        "prompt_version": "v-test",
        "usage": {"cost_usd": 0.5, "mean_latency_seconds": 10},
        "units": [{"unit": "seed-013", "directive": "2026-16954", "gates": gates}],
    }
    outputs = {
        "seed-013": {"output": {"applicability": "applies", "action_status": status}}
    }
    (directory / "report.json").write_text(json.dumps(report))
    (directory / "outputs.json").write_text(json.dumps(outputs))


def test_failures_are_counted_across_repeats_and_changes_flagged(tmp_path) -> None:
    write_run(tmp_path, 1, "no_action_triggered", gate_1_passed=False)
    write_run(tmp_path, 2, "action_required_on_event", gate_1_passed=True)
    write_run(tmp_path, 3, "no_action_triggered", gate_1_passed=False)

    runs = load_runs(tmp_path, "v-test")
    summary = summarize_model(runs["claude-test @ medium cap 16000"])

    assert summary["repeats"] == 3
    assert summary["failures"] == {"seed-013": {"1": 2}}
    assert summary["unstable_units"] == ["seed-013"]
    assert summary["cost_usd"] == 1.5
    assert "1* (2/3)" in summary_markdown([summary], "v-test")


def test_other_prompt_versions_are_left_out(tmp_path) -> None:
    write_run(tmp_path, 1, "no_action_triggered", gate_1_passed=True)

    assert load_runs(tmp_path, "another-version") == {}
