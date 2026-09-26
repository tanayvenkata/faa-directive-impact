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

## Acquiring Source Documents

This command makes live network calls to the Federal Register and GovInfo:

```bash
make acquire DOCS="2025-10764 2025-18469"   # STORAGE_ROOT defaults to data/
```

For each document it fetches the API JSON record, resolves the XML, HTML,
plain-text, GovInfo PDF, GovInfo MODS, and original-size image URLs from that
record, and retrieves each one. Every attempt writes a schema-validated receipt
to `data/receipts/<run-id>/`. Artifacts are read-only and never overwritten.

Each run writes one schema-validated raw-generation manifest to
`data/manifests/`. It lists the expected document/representation matrix,
receipts, missing artifacts, the proposal/final relationship, and deferred
dependencies, plus whether the generation is complete. `CORPUS_TRACK` defaults
to `frozen_evaluation`.

Every retained artifact is validated as it arrives: integrity, format,
document identity, and the directive's incorporated-material statement. The
findings are written to `data/validation/<generation-id>.json`. A generation is
eligible for normalization only if it is complete and every check passed.

Standard output summarizes the run and reports each representation as new,
unchanged, or changed since earlier runs. That comparison is derived from
receipts and is not stored.

Exit status: `0` eligible, `1` incomplete or failed validation, `2` content
changed since an earlier run and needs review. `data/` is ignored by Git.

## Accepted Raw Generations

- [`gen-20260926T213233Z-000f808f`](generations/gen-20260926T213233Z-000f808f/DECISION.md)
  — HPT hub proposal/final pair, `frozen_evaluation`, accepted for
  normalization. Its receipts, manifest, and validation report are committed;
  the raw bytes are not.

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
