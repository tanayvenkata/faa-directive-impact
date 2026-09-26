"""Command-line entry point for acquisition runs."""

import argparse
import json
import sys
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
    args = parser.parse_args(argv)

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


if __name__ == "__main__":
    raise SystemExit(main())
