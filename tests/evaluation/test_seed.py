from pathlib import Path

import pytest
import yaml

from faa_directive_impact.evaluation.seed import check_seed_cases, load_seed_cases

REPO = Path(__file__).resolve().parents[2]
CASES = REPO / "evaluation" / "seed" / "cases"
GENERATIONS = REPO / "generations"


def test_committed_seed_cases_are_consistent() -> None:
    cases = load_seed_cases(CASES)

    assert cases
    assert check_seed_cases(cases, GENERATIONS) == []


def rewrite(tmp_path: Path, name: str, **changes) -> Path:
    record = yaml.safe_load((CASES / "seed-001.yaml").read_text())
    record.update(changes)
    directory = tmp_path / "cases"
    directory.mkdir(exist_ok=True)
    (directory / name).write_text(yaml.safe_dump(record))
    return directory


@pytest.mark.parametrize(
    ("name", "changes", "problem"),
    [
        ("seed-999.yaml", {}, "file name does not match"),
        (
            "seed-001.yaml",
            {"directive_candidates": ["2099-00001"]},
            "not in the source generation",
        ),
        (
            "seed-001.yaml",
            {
                "source_snapshot": {
                    "generation_id": "gen-unknown",
                    "as_of": "2026-09-26",
                }
            },
            "not an accepted generation",
        ),
    ],
)
def test_inconsistent_cases_are_reported(
    tmp_path: Path, name: str, changes: dict, problem: str
) -> None:
    directory = rewrite(tmp_path, name, **changes)

    problems = check_seed_cases(load_seed_cases(directory), GENERATIONS)

    assert any(problem in message for message in problems), problems


def test_expert_required_case_must_route_to_review(tmp_path: Path) -> None:
    record = yaml.safe_load((CASES / "seed-001.yaml").read_text())
    record["label"]["provenance"] = "expert_required"
    directory = tmp_path / "cases"
    directory.mkdir()
    (directory / "seed-001.yaml").write_text(yaml.safe_dump(record))

    problems = check_seed_cases(load_seed_cases(directory), GENERATIONS)

    assert problems and "needs_review" in problems[0]
