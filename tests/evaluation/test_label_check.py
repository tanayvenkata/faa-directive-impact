from pathlib import Path

import yaml

from faa_directive_impact.evaluation.label_check import blind_case, compare

SEED = Path(__file__).resolve().parents[2] / "evaluation/seed/cases/seed-003.yaml"


def test_blind_case_hides_the_answer_and_its_explanation():
    record = yaml.safe_load(SEED.read_text())
    blind = blind_case(record)
    text = str(blind)
    assert "expected" not in blind and "forbidden_claims" not in blind
    assert "rationale" not in blind["label"]
    assert record["expected"][0]["reason"] not in text
    assert blind["asset_snapshot"] == record["asset_snapshot"]


def test_compare_reports_each_differing_field():
    record = yaml.safe_load(SEED.read_text())
    same = [
        {
            "directive": "2025-18469",
            "applicability": "applies",
            "action_status": "needs_review",
            "required_missing_facts": ["serial"],
        }
    ]
    assert compare(record, same) == []
    different = [{**same[0], "action_status": "action_required"}]
    [row] = compare(record, different)
    assert row["field"] == "action_status"
    assert compare(record, [])[0]["field"] == "outcome"
