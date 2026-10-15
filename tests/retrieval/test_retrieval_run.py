from pathlib import Path

from faa_directive_impact.evaluation.retrieval_run import score_retrieval

REPO = Path(__file__).resolve().parents[2]


def test_committed_corpus_passes_gate_14():
    result = score_retrieval(REPO)
    assert result["gate_14"]["verdict"] == "pass"
    assert result["gate_14"]["protected_failures"] == []


def test_no_true_distractor_reaches_an_in_family_engine():
    mislabeled = {"2012-12329", "2015-12068"}  # PREREGISTRATION.md, deviation 2
    result = score_retrieval(REPO)
    for case in result["cases"]:
        for label in case["distractors_surfaced"]:
            assert label.split()[0] in mislabeled
