"""Command-line entry point for acquisition and S1 baseline runs."""

import argparse
import json
import subprocess
import sys
from datetime import UTC, date, datetime
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
    b2_conclude = commands.add_parser(
        "b2-conclude", help="Fold a completed hand review into a B2 run's verdict."
    )
    b2_conclude.add_argument("run_directory", type=Path)
    b3_plumbing = commands.add_parser(
        "b3-plumbing",
        help="One format-only rule-drafting call on an unscored directive.",
    )
    b3_plumbing.add_argument("--model", default="claude-haiku-5-5")
    b3_plumbing.add_argument("--effort", default="medium")
    b3_run = commands.add_parser(
        "b3-run", help="Draft each B3 directive's rule record with a model; score it."
    )
    b3_run.add_argument("--model", required=True)
    b3_run.add_argument("--effort", default="high")
    b3_run.add_argument("--repeat", type=int, default=1)
    b3_run.add_argument("--mode", choices=("live", "batch"), default="batch")
    b3_run.add_argument("--max-tokens", type=int, default=32000)
    b3_replay = commands.add_parser(
        "b3-replay",
        help="Re-score a recorded B3 run offline; finish its report if missing.",
    )
    b3_replay.add_argument("run_directory", type=Path)
    b3_summary = commands.add_parser(
        "b3-summary", help="Summarize B3 repeats under the pre-registered rules."
    )
    b3_summary.add_argument("--runs-root", type=Path, default=Path("evaluation/runs"))
    b3_summary.add_argument(
        "--output", type=Path, default=Path("evaluation/b3-summary")
    )
    for sub in (b2_plumbing, b2_run, b3_plumbing, b3_run, b3_replay):
        sub.add_argument("--repo", type=Path, default=Path("."))
        sub.add_argument("--storage-root", type=Path, default=Path("data/seed-frozen"))
        sub.add_argument("--runs-root", type=Path, default=Path("evaluation/runs"))
    _add_discovery_commands(commands)
    fleet_build = commands.add_parser(
        "fleet-build",
        help="Offline: regenerate the demo fleet and its recorded screens.",
    )
    fleet_build.add_argument("--repo", type=Path, default=Path("."))
    fleet_site = commands.add_parser(
        "fleet-site", help="Offline: write the fleet view from the recorded screens."
    )
    fleet_site.add_argument("--repo", type=Path, default=Path("."))
    fleet_site.add_argument("--output", type=Path, default=Path("site"))
    retrieval_corpus = commands.add_parser(
        "retrieval-corpus",
        help="Offline: normalize a frozen generation into retrieval records.",
    )
    retrieval_corpus.add_argument("generation_dir", type=Path)
    retrieval_corpus.add_argument("--storage-root", type=Path, required=True)
    retrieval_corpus.add_argument(
        "--output", type=Path, default=Path("evaluation/retrieval/corpus.json")
    )
    retrieval_run = commands.add_parser(
        "retrieval-run", help="Offline: score the retriever on the seed cases."
    )
    retrieval_run.add_argument("--repo", type=Path, default=Path("."))
    retrieval_run.add_argument(
        "--runs-root", type=Path, default=Path("evaluation/runs")
    )
    coverage_run = commands.add_parser(
        "coverage-run",
        help="Offline: score a set of rule records on the coverage units.",
    )
    coverage_run.add_argument("label")
    coverage_run.add_argument("records_dir", type=Path)
    coverage_run.add_argument("--repo", type=Path, default=Path("."))
    coverage_run.add_argument("--runs-root", type=Path, default=Path("evaluation/runs"))
    coverage_run.add_argument(
        "--storage-root", type=Path, default=Path("data/retrieval-frozen")
    )
    coverage_drafts = commands.add_parser(
        "coverage-drafts",
        help="Live: draft every coverage directive with prompt v2 (one batch), "
        "or collect a batch already submitted.",
    )
    coverage_drafts.add_argument("label")
    coverage_drafts.add_argument("--repo", type=Path, default=Path("."))
    coverage_drafts.add_argument(
        "--runs-root", type=Path, default=Path("evaluation/runs")
    )
    coverage_drafts.add_argument(
        "--storage-root", type=Path, default=Path("data/retrieval-frozen")
    )
    coverage_drafts.add_argument("--batch-id", help="collect this submitted batch")
    coverage_drafts.add_argument("--stamp", help="the run's original UTC stamp")
    args = parser.parse_args(argv)

    if args.command == "coverage-drafts":
        from faa_directive_impact.evaluation.coverage_drafts import directives, run

        print(
            run(
                args.repo,
                args.runs_root,
                args.storage_root,
                args.label,
                directives(args.repo),
                batch_id=args.batch_id,
                stamp=args.stamp,
            )
        )
        return EXIT_OK

    if args.command == "coverage-run":
        from faa_directive_impact.evaluation.coverage_run import write_run

        print(
            write_run(
                args.repo,
                args.runs_root,
                args.storage_root,
                args.label,
                args.records_dir,
            )
        )
        return EXIT_OK

    if args.command == "retrieval-corpus":
        from faa_directive_impact.retrieval.corpus import normalize_generation

        records = normalize_generation(args.generation_dir, args.storage_root)
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(
            json.dumps(
                {"generation_id": args.generation_dir.name, "records": records},
                indent=2,
                sort_keys=True,
                ensure_ascii=False,
            )
            + "\n",
            encoding="utf-8",
        )
        print(f"{len(records)} records -> {args.output}")
        return EXIT_OK

    if args.command == "retrieval-run":
        from faa_directive_impact.evaluation.retrieval_run import write_retrieval_run

        print(write_retrieval_run(args.repo, args.runs_root))
        return EXIT_OK

    if args.command == "fleet-build":
        from faa_directive_impact.fleet.build import write_fleet

        for path in write_fleet(args.repo):
            print(path)
        return EXIT_OK

    if args.command == "fleet-site":
        from faa_directive_impact.fleet.build import (
            FLEET_FILE,
            FLEET_REPLAY_FILE,
            FLEET_SCREEN_FILE,
        )
        from faa_directive_impact.fleet.page import build_fleet_page

        screened, replay, fleet = (
            json.loads((args.repo / path).read_text(encoding="utf-8"))
            for path in (FLEET_SCREEN_FILE, FLEET_REPLAY_FILE, FLEET_FILE)
        )
        print(build_fleet_page(screened, args.output, replay=replay, fleet=fleet))
        return EXIT_OK

    if args.command.startswith("discovery-"):
        return _run_discovery_command(args)

    if args.command == "b2-conclude":
        from faa_directive_impact.evaluation.b2_run import conclude_b2

        verdicts = conclude_b2(args.run_directory)
        for scope, result in verdicts.items():
            failing = {
                n: g["failed"] for n, g in result["gates"].items() if g.get("failed")
            }
            print(
                scope, "provisional" if result["provisional"] else "confirmed", failing
            )
        return EXIT_OK
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
    if args.command == "b3-plumbing":
        from faa_directive_impact.evaluation.b3_plumbing import (
            run_plumbing as run_b3_plumbing,
        )

        stamp = datetime.now(UTC).strftime("%Y%m%dT%H%M%SZ")
        directory = args.runs_root / f"b3-plumbing-{stamp}"
        results = run_b3_plumbing(
            args.repo.resolve(), args.storage_root, directory, args.model, args.effort
        )
        print(json.dumps(results, indent=2))
        print(directory)
        return EXIT_OK
    if args.command == "b3-summary":
        from faa_directive_impact.evaluation.b3_prompt import (
            PROMPT_VERSION as B3_PROMPT_VERSION,
        )
        from faa_directive_impact.evaluation.b3_summary import (
            load_runs as load_b3_runs,
        )
        from faa_directive_impact.evaluation.b3_summary import (
            summarize_run,
        )
        from faa_directive_impact.evaluation.b3_summary import (
            summary_markdown as b3_summary_markdown,
        )

        summaries = [
            summarize_run(run)
            for run in load_b3_runs(args.runs_root, B3_PROMPT_VERSION)
        ]
        args.output.with_suffix(".json").write_text(
            json.dumps(summaries, indent=2, sort_keys=True) + "\n", encoding="utf-8"
        )
        args.output.with_suffix(".md").write_text(
            b3_summary_markdown(summaries, B3_PROMPT_VERSION), encoding="utf-8"
        )
        print(args.output.with_suffix(".md"))
        return EXIT_OK
    if args.command == "b3-replay":
        from faa_directive_impact.evaluation.b3_run import replay_results

        results = replay_results(
            args.repo.resolve(), args.storage_root, args.run_directory
        )
        print(json.dumps(results["summary"], indent=2))
        return EXIT_OK
    if args.command == "b3-run":
        from faa_directive_impact.evaluation.b3_run import run_b3

        commit, dirty = _git_state(args.repo)
        directory = run_b3(
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


# Discovery corpus (ROADMAP step 6): daily sync, rollback, and freshness page.
DISCOVERY_STORAGE_ROOT = Path("data/discovery")


def _add_discovery_commands(commands: argparse._SubParsersAction) -> None:
    sync = commands.add_parser(
        "discovery-sync",
        help="Live network call: search for new FAA ADs, then promote or reject.",
    )
    sync.add_argument(
        "--start-date",
        type=date.fromisoformat,
        default=None,
        help="first-sync search start (YYYY-MM-DD); later syncs use the checkpoint",
    )
    sync.add_argument(
        "--accept-changed",
        nargs="*",
        default=[],
        metavar="DOCUMENT",
        help="documents whose changed metadata was investigated and accepted",
    )
    sync.add_argument(
        "--reread",
        nargs="*",
        default=[],
        metavar="DOCUMENT",
        help="IAE directives already in the corpus to acquire and classify again",
    )
    sync.add_argument("--timeout", type=float, default=DEFAULT_TIMEOUT_SECONDS)
    rollback = commands.add_parser(
        "discovery-rollback",
        help="Point the active discovery generation back at an earlier one.",
    )
    rollback.add_argument("--to", dest="to_generation", default=None)
    site = commands.add_parser(
        "discovery-site", help="Write the static freshness page for the corpus."
    )
    site.add_argument("--output", type=Path, default=Path("site"))
    site.add_argument("--runs-root", type=Path, default=Path("evaluation/runs"))
    for sub in (sync, rollback, site):
        sub.add_argument("--storage-root", type=Path, default=DISCOVERY_STORAGE_ROOT)


def _run_discovery_command(args: argparse.Namespace) -> int:
    from faa_directive_impact.discovery.state import StorageRootRefused
    from faa_directive_impact.discovery.sync import (
        DEFAULT_START_DATE,
        SUCCESSFUL_OUTCOMES,
        RollbackError,
        rollback,
        run_sync,
    )

    try:
        if args.command == "discovery-site":
            from faa_directive_impact.discovery.site import (
                build_site,
                latest_s1_queues,
            )

            root = args.storage_root.resolve()
            print(build_site(root, args.output, latest_s1_queues(args.runs_root)))
            return EXIT_OK
        if args.command == "discovery-rollback":
            try:
                pointer = rollback(args.storage_root, to_generation=args.to_generation)
            except RollbackError as error:
                print(f"rollback refused: {error}")
                return EXIT_FAILED
            print(json.dumps(pointer, indent=2, sort_keys=True))
            return EXIT_OK
        with build_client(args.timeout) as client:
            attempt = run_sync(
                args.storage_root,
                client,
                start_date=args.start_date or DEFAULT_START_DATE,
                accept_changed=frozenset(args.accept_changed),
                reread=frozenset(args.reread),
            )
    except StorageRootRefused as error:
        print(error)
        return EXIT_FAILED
    attempt.pop("traceback", None)
    json.dump(attempt, sys.stdout, indent=2, sort_keys=True)
    print()
    return EXIT_OK if attempt["outcome"] in SUCCESSFUL_OUTCOMES else EXIT_FAILED


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
