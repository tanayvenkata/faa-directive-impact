"""Command-line entry point for acquisition and S1 baseline runs."""

import argparse
import json
import subprocess
import sys
from datetime import UTC, datetime
from pathlib import Path

from faa_directive_impact.acquisition.document import acquire_document
from faa_directive_impact.acquisition.manifest import (
    build_manifest,
    build_validation_report,
)
from faa_directive_impact.acquisition.packaging import package_generation
from faa_directive_impact.acquisition.retrieval import (
    DEFAULT_TIMEOUT_SECONDS,
    AcquisitionContext,
    build_client,
    random_id,
    utc_now,
)
from faa_directive_impact.acquisition.storage import RawStorage
from faa_directive_impact.acquisition.versions import VersionIndex
from faa_directive_impact.evaluation.s1_run import conclude_run, run_s1

EXIT_OK = 0
EXIT_FAILED = 1
EXIT_NEEDS_REVIEW = 2
CORPUS_TRACKS = ("frozen_evaluation", "refreshable_discovery")


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(prog="faa-directive-impact")
    commands = parser.add_subparsers(dest="command", required=True)
    acquire = commands.add_parser(
        "acquire",
        help="Acquire Federal Register documents as one raw generation.",
    )
    acquire.add_argument("document_numbers", nargs="+", help="for example 2025-10764")
    acquire.add_argument("--storage-root", type=Path, required=True)
    acquire.add_argument("--corpus-track", choices=CORPUS_TRACKS, required=True)
    acquire.add_argument("--timeout", type=float, default=DEFAULT_TIMEOUT_SECONDS)
    package = commands.add_parser(
        "package-generation",
        help="Write a deterministic archive of a generation's raw artifacts.",
    )
    package.add_argument("generation_id")
    package.add_argument("--storage-root", type=Path, required=True)
    package.add_argument("--output", type=Path, required=True)
    s1_run = commands.add_parser(
        "s1-run",
        help="Run the S1 rules baseline offline and write a kept run directory.",
    )
    s1_run.add_argument("--repo", type=Path, default=Path("."))
    s1_run.add_argument("--runs-root", type=Path, default=Path("evaluation/runs"))
    s1_conclude = commands.add_parser(
        "s1-conclude",
        help="Fold a completed hand review into an S1 run's verdict.",
    )
    s1_conclude.add_argument("run_directory", type=Path)
    s1_conclude.add_argument("--repo", type=Path, default=Path("."))
    llm_check = commands.add_parser(
        "llm-check",
        help="Make one tiny model call to confirm credentials (costs < $0.01).",
    )
    llm_check.add_argument("--model", default="claude-haiku-5-5")
    b2_plumbing = commands.add_parser(
        "b2-plumbing",
        help="Two format-only model calls on a synthetic engine (a few cents).",
    )
    b2_plumbing.add_argument("--model", default="claude-haiku-5-5")
    b2_plumbing.add_argument("--effort", default="medium")
    b2_run = commands.add_parser(
        "b2-run", help="Screen every seed unit with a model reading the text."
    )
    b2_run.add_argument("--model", required=True)
    b2_run.add_argument("--effort", default="medium")
    b2_run.add_argument("--repeat", type=int, default=1)
    b2_run.add_argument("--mode", choices=("live", "batch"), default="batch")
    b2_run.add_argument("--max-tokens", type=int, default=16000)
    b2_summary = commands.add_parser(
        "b2-summary", help="Summarize B2 repeats per model for the current prompt."
    )
    b2_summary.add_argument("--runs-root", type=Path, default=Path("evaluation/runs"))
    b2_summary.add_argument(
        "--output", type=Path, default=Path("evaluation/b2-summary")
    )
    for sub in (b2_plumbing, b2_run):
        sub.add_argument("--repo", type=Path, default=Path("."))
        sub.add_argument("--storage-root", type=Path, default=Path("data/seed-frozen"))
        sub.add_argument("--runs-root", type=Path, default=Path("evaluation/runs"))
    args = parser.parse_args(argv)

    if args.command == "b2-summary":
        from faa_directive_impact.evaluation.b2_prompt import PROMPT_VERSION
        from faa_directive_impact.evaluation.b2_summary import (
            load_runs,
            summarize_model,
            summary_markdown,
        )

        runs = load_runs(args.runs_root, PROMPT_VERSION)
        summaries = [summarize_model(model_runs) for model_runs in runs.values()]
        args.output.with_suffix(".json").write_text(
            json.dumps(summaries, indent=2, sort_keys=True) + "\n", encoding="utf-8"
        )
        args.output.with_suffix(".md").write_text(
            summary_markdown(summaries, PROMPT_VERSION), encoding="utf-8"
        )
        print(args.output.with_suffix(".md"))
        return EXIT_OK
    if args.command == "b2-plumbing":
        from faa_directive_impact.evaluation.b2_plumbing import run_plumbing

        stamp = datetime.now(UTC).strftime("%Y%m%dT%H%M%SZ")
        directory = args.runs_root / f"b2-plumbing-{stamp}"
        results = run_plumbing(
            args.repo.resolve(), args.storage_root, directory, args.model, args.effort
        )
        print(json.dumps(results, indent=2))
        print(directory)
        return EXIT_OK
    if args.command == "b2-run":
        from faa_directive_impact.evaluation.b2_run import run_b2

        commit, dirty = _git_state(args.repo)
        directory = run_b2(
            args.repo.resolve(),
            args.runs_root,
            args.storage_root,
            args.model,
            args.effort,
            args.repeat,
            args.mode,
            datetime.now(UTC),
            commit,
            dirty,
            max_tokens=args.max_tokens,
        )
        print(directory)
        return EXIT_OK
    if args.command == "llm-check":
        return _llm_check(args.model)

    if args.command == "s1-run":
        commit, dirty = _git_state(args.repo)
        directory = run_s1(
            args.repo.resolve(), args.runs_root, datetime.now(UTC), commit, dirty
        )
        print(directory)
        return EXIT_OK
    if args.command == "s1-conclude":
        verdict = conclude_run(args.repo.resolve(), args.run_directory)
        print(f"{verdict['decision']} (provisional: {verdict['provisional']})")
        return EXIT_OK
    if args.command == "package-generation":
        archive = package_generation(
            args.storage_root.resolve(), args.generation_id, args.output
        )
        print(archive)
        return EXIT_OK

    storage = RawStorage(args.storage_root)
    started_at = utc_now()
    run_id = random_id("run", started_at)
    versions = VersionIndex.from_receipts(storage.root, exclude_run_id=run_id)
    with build_client(args.timeout) as client:
        context = AcquisitionContext(
            run_id=run_id,
            storage=storage,
            client=client,
            clock=utc_now,
            new_id=random_id,
        )
        documents = [
            acquire_document(context, number, versions)
            for number in args.document_numbers
        ]

    generation_id = f"gen-{run_id.removeprefix('run-')}"
    created_at = utc_now()
    manifest = build_manifest(
        generation_id=generation_id,
        created_at=created_at,
        corpus_track=args.corpus_track,
        run_id=run_id,
        documents=documents,
    )
    manifest_path = f"manifests/raw-generation-{generation_id}.json"
    validation_path = f"validation/{generation_id}.json"
    storage.write_json(
        validation_path,
        build_validation_report(
            generation_id=generation_id, created_at=created_at, documents=documents
        ),
    )
    storage.write_json(manifest_path, manifest)

    # Version outcomes are derived from receipts, so they are reported, not stored.
    summary = {
        "manifest": manifest_path,
        "validation_report": validation_path,
        "failed_checks": [
            record
            for doc in documents
            for validation in doc.validations
            for record in validation.records()
            if record["outcome"] == "failed"
        ],
        "completeness_status": manifest["completeness_status"],
        "eligible_for_normalization": manifest["eligible_for_normalization"],
        "missing_artifacts": manifest["missing_artifacts"],
        "problems": {doc.document_number: doc.problems for doc in documents},
        "versions": [
            version.as_record() for doc in documents for version in doc.versions
        ],
    }
    json.dump(summary, sys.stdout, indent=2, sort_keys=True)
    print()

    if not manifest["eligible_for_normalization"]:
        return EXIT_FAILED
    if any(doc.needs_review for doc in documents):
        return EXIT_NEEDS_REVIEW
    return EXIT_OK


def _llm_check(model: str) -> int:
    from faa_directive_impact.llm.client import LiveModel, ModelRequest

    request = ModelRequest(
        model=model,
        instructions="Answer in the requested JSON format.",
        document="This is a connectivity check.",
        question="Is this a connectivity check?",
        output_schema={
            "type": "object",
            "properties": {"answer": {"type": "boolean"}},
            "required": ["answer"],
            "additionalProperties": False,
        },
        effort="low",
        max_tokens=1024,
    )
    import anthropic

    try:
        response = LiveModel().call(request)
    except anthropic.AuthenticationError:
        print("The API key was rejected. Check ANTHROPIC_API_KEY in .env.")
        return EXIT_FAILED
    except anthropic.APIStatusError as exc:
        print(f"The API refused the call ({exc.status_code}): {exc.message}")
        return EXIT_FAILED
    except anthropic.APIConnectionError:
        print("Could not reach the API. Check the network connection.")
        return EXIT_FAILED
    print(
        json.dumps(
            {
                "model": response.model,
                "answer": response.answer,
                "error": response.error,
                "usage": response.usage,
                "cost_usd": response.cost_usd,
            },
            indent=2,
        )
    )
    return EXIT_OK if response.answer is not None else EXIT_FAILED


def _git_state(repo: Path) -> tuple[str, bool]:
    """Return the HEAD commit and whether the worktree has uncommitted changes."""

    def git(*args: str) -> str:
        return subprocess.run(
            ["git", *args], cwd=repo, check=True, capture_output=True, text=True
        ).stdout.strip()

    return git("rev-parse", "HEAD"), bool(git("status", "--porcelain"))


if __name__ == "__main__":
    raise SystemExit(main())
