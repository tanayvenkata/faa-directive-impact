"""Command-line entry point for acquisition runs."""

import argparse
import json
import sys
from pathlib import Path

from faa_directive_impact.acquisition.federal_register import api_json_request
from faa_directive_impact.acquisition.retrieval import (
    DEFAULT_TIMEOUT_SECONDS,
    AcquisitionContext,
    build_client,
    random_id,
    retrieve,
    utc_now,
)
from faa_directive_impact.acquisition.storage import RawStorage


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(prog="faa-directive-impact")
    commands = parser.add_subparsers(dest="command", required=True)
    acquire = commands.add_parser(
        "acquire-api-json",
        help="Acquire Federal Register API JSON for one document.",
    )
    acquire.add_argument("document_number", help="for example 2025-10764")
    acquire.add_argument("--storage-root", type=Path, required=True)
    acquire.add_argument("--timeout", type=float, default=DEFAULT_TIMEOUT_SECONDS)
    args = parser.parse_args(argv)

    run_id = random_id("run", utc_now())
    with build_client(args.timeout) as client:
        context = AcquisitionContext(
            run_id=run_id,
            storage=RawStorage(args.storage_root),
            client=client,
            clock=utc_now,
            new_id=random_id,
        )
        receipt = retrieve(context, api_json_request(args.document_number, run_id))

    json.dump(receipt, sys.stdout, indent=2, sort_keys=True)
    print()
    return 0 if receipt["acquisition_status"] == "succeeded" else 1


if __name__ == "__main__":
    raise SystemExit(main())
