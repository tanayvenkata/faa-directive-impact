# FAA Directive Impact

This project is building a continuously refreshable, evidence-backed FAA
directive-impact system. The first supported evaluation boundary is the
International Aero Engines V2500-A5/D5/E5 family.

The active milestone is immutable official-source acquisition. Application,
retrieval, and agent work remain deferred until the acquisition and evaluation
contracts are proven.

## Current Flow

```text
official acquisition
→ immutable raw generation
→ versioned normalization
→ candidate retrieval indexes
→ evaluation gates
→ explicit promotion or rejection
```

See [`ROADMAP.md`](ROADMAP.md) and
[`ACQUISITION_MILESTONE.md`](ACQUISITION_MILESTONE.md) for scope.

## Requirements

- Python 3.12 or later
- [uv](https://docs.astral.sh/uv/)

Python 3.12 is the compatibility floor; development may use a newer supported
Python version. The lockfile records exact development dependencies.

## Development Commands

Run these commands from the repository root:

```bash
make sync     # create/update the local environment from uv.lock
make test     # run deterministic tests; no live network calls by default
make lint     # run static lint checks
make format   # apply the formatter
make check    # run lint and tests
```

The `.venv/` directory is local and ignored by Git.

## Acquiring a Source Document

This command makes a live network call to the Federal Register API:

```bash
make acquire-api-json DOC=2025-10764   # STORAGE_ROOT defaults to data/
```

It writes the exact response bytes to
`data/raw/federal-register/<doc>/<run-id>/api.json` and a schema-validated
receipt to `data/receipts/<run-id>/`. Failed attempts also produce receipts.
Published files are read-only and never overwritten. `data/` is ignored by Git.

## Acquisition Schemas

Canonical JSON Schemas for artifact receipts and raw-generation manifests are
packaged under `src/faa_directive_impact/schemas/`. Their design and identity
semantics are documented in [`SCHEMA_DECISIONS.md`](SCHEMA_DECISIONS.md).

## Data Boundary

Acquisition and parsing are separate stages:

```text
source retrieval → exact bytes → hashes → receipts → raw manifest
                                                    ─────────────
                                                    parsing begins later
```

Live raw captures are not committed until their size, authority,
redistribution status, and reproducibility requirements have been reviewed.
