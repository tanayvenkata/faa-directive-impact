"""Draft every in-scope directive's rule record with prompt v2, and record it.

``plumbing`` is the format-only check made before the prompt is frozen: it
drafts one directive outside the evaluation (a CFM International AD from the
retrieval corpus's distractors) and checks only that the answer parses and
validates. ``draft_all`` is the one recorded drafting run the
pre-registration calls for. Every call is saved, so a run can be re-read
without calling the model.
"""

import json
from datetime import UTC, date, datetime
from pathlib import Path
from typing import Any

from jsonschema import Draft202012Validator

from faa_directive_impact.directives.source_text import documents_for, load_generation
from faa_directive_impact.evaluation.coverage_prompt import (
    PROMPT_VERSION,
    RULE_SCHEMA,
    build_request,
)
from faa_directive_impact.evaluation.coverage_run import GENERATION_ID, REFERENCE_DIR
from faa_directive_impact.llm.client import ModelResponse, call_batch, record
from faa_directive_impact.rules.serial_guard import invented_identifiers

PLUMBING_DIRECTIVE = "2025-02204"  # CFM LEAP-1A; a distractor, never scored
THREAD_AS_OF = date(2026, 10, 15)
MODEL = "claude-opus-5-5"
EFFORT = "high"
MAX_TOKENS = 64000


def directives(repo: Path) -> list[str]:
    """Every directive with a coverage reference record."""
    return sorted(path.stem for path in (repo / REFERENCE_DIR).glob("*.json"))


def requests_for(repo: Path, storage_root: Path, numbers: list[str]) -> list[Any]:
    documents, relationships = load_generation(
        repo / "generations" / GENERATION_ID, storage_root
    )
    return [
        build_request(
            MODEL,
            EFFORT,
            number,
            documents_for(number, THREAD_AS_OF, documents, relationships),
            MAX_TOKENS,
        )
        for number in numbers
    ]


def check(response: ModelResponse, corpus: dict[str, Any]) -> dict[str, Any]:
    answer = response.answer
    if answer is None:
        return {"valid": False, "problems": [f"no JSON (stop {response.stop_reason})"]}
    errors = [e.message for e in Draft202012Validator(RULE_SCHEMA).iter_errors(answer)]
    if errors:
        return {"valid": False, "problems": errors[:10]}
    invented = invented_identifiers(answer, corpus)
    return {
        "valid": not invented,
        "problems": [f"serial guard: {item}" for item in invented],
    }


def run(
    repo: Path,
    runs_root: Path,
    storage_root: Path,
    label: str,
    numbers: list[str],
    client: Any = None,
    batch_id: str | None = None,
    stamp: str | None = None,
) -> Path:
    """Draft ``numbers`` in one batch, or collect an already submitted batch.

    The batch id is written to ``batch.json`` the moment the batch exists, so
    an interrupted run can be collected later with ``batch_id`` (and the
    original ``stamp``) instead of being drafted a second time.
    """
    stamp = stamp or datetime.now(UTC).strftime("%Y%m%dT%H%M%SZ")
    directory = runs_root / f"coverage-{label}-{stamp}"
    directory.mkdir(parents=True, exist_ok=True)
    if any(directory.iterdir()) and batch_id is None:
        raise FileExistsError(f"{directory} already holds a run")
    requests = requests_for(repo, storage_root, numbers)
    if client is None:
        import anthropic

        client = anthropic.Anthropic()

    def save_batch(submitted: str, collected_later: bool) -> None:
        (directory / "batch.json").write_text(
            json.dumps(
                {"batch_id": submitted, "collected_later": collected_later},
                indent=2,
                sort_keys=True,
            )
            + "\n",
            encoding="utf-8",
        )

    if batch_id is not None:
        save_batch(batch_id, collected_later=True)
    by_key = call_batch(
        client,
        requests,
        batch_id=batch_id,
        on_submit=lambda submitted: save_batch(submitted, collected_later=False),
    )
    corpus = json.loads(
        (repo / "evaluation/retrieval/corpus.json").read_text(encoding="utf-8")
    )
    summary = {
        "label": label,
        "model": MODEL,
        "effort": EFFORT,
        "max_tokens": MAX_TOKENS,
        "prompt_version": PROMPT_VERSION,
        "generation_id": GENERATION_ID,
        "created_at_utc": stamp,
        "drafts": {},
        "cost_usd": 0.0,
    }
    for number, request in zip(numbers, requests, strict=True):
        response = by_key[request.key()]
        record(directory / "calls", request, response)
        result = check(response, corpus)
        summary["drafts"][number] = {
            **result,
            "stop_reason": response.stop_reason,
            "cost_usd": response.cost_usd,
            "output_tokens": response.usage.get("output_tokens"),
        }
        summary["cost_usd"] = round(summary["cost_usd"] + response.cost_usd, 4)
        if response.answer is not None:
            (directory / "drafts").mkdir(exist_ok=True)
            (directory / "drafts" / f"{number}.json").write_text(
                json.dumps(response.answer, indent=2, sort_keys=True) + "\n",
                encoding="utf-8",
            )
    (directory / "summary.json").write_text(
        json.dumps(summary, indent=2, sort_keys=True) + "\n", encoding="utf-8"
    )
    return directory
