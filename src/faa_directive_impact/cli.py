"""Command-line entry point for acquisition runs."""

import argparse
import json
import sys
from pathlib import Path

from faa_directive_impact.acquisition.document import acquire_document
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


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(prog="faa-directive-impact")
    commands = parser.add_subparsers(dest="command", required=True)
    acquire = commands.add_parser(
        "acquire",
        help="Acquire every expected representation of Federal Register documents.",
    )
    acquire.add_argument("document_numbers", nargs="+", help="for example 2025-10764")
    acquire.add_argument("--storage-root", type=Path, required=True)
    acquire.add_argument("--timeout", type=float, default=DEFAULT_TIMEOUT_SECONDS)
    args = parser.parse_args(argv)

    storage = RawStorage(args.storage_root)
    run_id = random_id("run", utc_now())
    versions = VersionIndex.from_receipts(storage.root, exclude_run_id=run_id)
    with build_client(args.timeout) as client:
        context = AcquisitionContext(
            run_id=run_id,
            storage=storage,
            client=client,
            clock=utc_now,
            new_id=random_id,
        )
        results = [
            acquire_document(context, number, versions)
            for number in args.document_numbers
        ]

    report = {
        "acquisition_run_id": run_id,
        "documents": [result.as_record() for result in results],
    }
    storage.write_json(f"runs/{run_id}/report.json", report)
    json.dump(report, sys.stdout, indent=2, sort_keys=True)
    print()

    if any(result.failed for result in results):
        return EXIT_FAILED
    if any(result.needs_review for result in results):
        return EXIT_NEEDS_REVIEW
    return EXIT_OK


if __name__ == "__main__":
    raise SystemExit(main())
