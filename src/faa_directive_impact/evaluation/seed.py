"""Load feasibility seed cases and check them against their source snapshot."""

import json
from dataclasses import dataclass
from pathlib import Path
from typing import Any

import yaml
from jsonschema import Draft202012Validator, FormatChecker

from faa_directive_impact.schema_validation import load_schema


@dataclass(frozen=True)
class SeedCase:
    path: Path
    record: dict[str, Any]


def load_seed_cases(case_directory: Path) -> list[SeedCase]:
    """Read every ``seed-*.yaml`` case in filename order."""
    return [
        SeedCase(path, yaml.safe_load(path.read_text(encoding="utf-8")))
        for path in sorted(case_directory.glob("seed-*.yaml"))
    ]


def check_seed_cases(cases: list[SeedCase], generations_root: Path) -> list[str]:
    """Return every problem found; an empty list means the seed is consistent.

    Beyond the schema, each case must name its file after its ID, cite only
    documents present in its accepted source generation, and expect outcomes
    only for directives it lists as candidates.
    """
    validator = Draft202012Validator(
        load_schema("seed-case.schema.json"), format_checker=FormatChecker()
    )
    problems: list[str] = []
    seen: dict[str, Path] = {}
    for case in cases:
        name = case.path.name
        errors = sorted(validator.iter_errors(case.record), key=str)
        if errors:
            problems.extend(f"{name}: {error.message}" for error in errors)
            continue
        record = case.record
        case_id = record["case_id"]
        if name != f"{case_id}.yaml":
            problems.append(f"{name}: file name does not match case_id {case_id}")
        if case_id in seen:
            problems.append(f"{name}: duplicate case_id also in {seen[case_id].name}")
        seen[case_id] = case.path

        documents = _generation_documents(
            generations_root, record["source_snapshot"]["generation_id"]
        )
        if documents is None:
            problems.append(f"{name}: source generation is not an accepted generation")
            continue
        candidates = set(record["directive_candidates"])
        cited = candidates | {
            evidence["document"]
            for outcome in record["expected"]
            for evidence in outcome["required_evidence"]
        }
        problems.extend(
            f"{name}: document {number} is not in the source generation"
            for number in sorted(cited - documents)
        )
        problems.extend(
            f"{name}: expected outcome for non-candidate {outcome['directive']}"
            for outcome in record["expected"]
            if outcome["directive"] not in candidates
        )
    return problems


def _generation_documents(
    generations_root: Path, generation_id: str
) -> set[str] | None:
    manifest_path = (
        generations_root
        / generation_id
        / "manifests"
        / f"raw-generation-{generation_id}.json"
    )
    if not (generations_root / generation_id / "DECISION.md").is_file():
        return None
    if not manifest_path.is_file():
        return None
    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    return {
        artifact["source_document_identity"]["value"]
        for artifact in manifest["expected_artifacts"]
        if artifact["source_document_identity"]["namespace"]
        == "federal_register_document_number"
    }
