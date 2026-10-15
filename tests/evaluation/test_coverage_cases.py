from pathlib import Path

from faa_directive_impact.evaluation.seed import check_seed_cases, load_seed_cases

REPO = Path(__file__).resolve().parents[2]
CASES = REPO / "evaluation" / "coverage" / "cases"
GENERATIONS = REPO / "generations"


def test_committed_coverage_cases_are_consistent() -> None:
    cases = load_seed_cases(CASES)
    assert check_seed_cases(cases, GENERATIONS) == []
    assert all(case.record["case_id"].startswith("cov-") for case in cases)
