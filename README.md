# FAA Directive Impact

This project is building a continuously refreshable, evidence-backed FAA
directive-impact system. The first supported evaluation boundary is the
International Aero Engines V2500-A5/D5/E5 family.

**Status: Evaluated** — see
[`CHECKPOINT_REPRODUCIBLE.md`](CHECKPOINT_REPRODUCIBLE.md), the write-up
[*Reproducible: Getting the Same FAA Directive Twice*](writeups/01-reproducible.md),
and the write-up
[*Evaluated: Rules, a Model, and a Model Writing Rules*](writeups/02-evaluated.md).
Milestone 1 (immutable official-source acquisition) is complete, and the
evaluation seed and frozen gates are written. S1, the rules baseline for AD
2025-19-13, is in [`evaluation/S1_BASELINE.md`](evaluation/S1_BASELINE.md);
the model comparisons are in
[`evaluation/B2_FULL_CONTEXT.md`](evaluation/B2_FULL_CONTEXT.md) and
[`evaluation/B3_RULE_EXTRACTION.md`](evaluation/B3_RULE_EXTRACTION.md), and
the daily discovery sync in [`DISCOVERY_SYNC.md`](DISCOVERY_SYNC.md). Their
hand-checked gates were judged by Claude only; the owner waived re-checking
them on 2026-10-15
([`evaluation/review/OWNER_PACKET.md`](evaluation/review/OWNER_PACKET.md)).
Retrieval and agent work remain deferred.

## Current Flow

```text
official acquisition
→ immutable raw generation
→ versioned normalization
→ candidate retrieval indexes
→ evaluation gates
→ explicit promotion or rejection
```

For the manual workflow, the proposed one, and the baselines each stage is
compared against, see [`APPROACH.md`](APPROACH.md). See
[`ROADMAP.md`](ROADMAP.md) and
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
make s1       # run the S1 rules baseline offline; writes evaluation/runs/<run-id>/
make s1-conclude RUN=evaluation/runs/<run-id>   # fold in the completed hand review
make b3-replay RUN=evaluation/runs/<run-id>     # re-score a recorded B3 run offline
make b3-summary                                 # summarize B3 repeats
```

Each S1 run directory holds the normalized record, every unit's output, the
gate report, a hand-review sheet for gates 5 and 11, and `queues.html`, a
static page you can open directly in a browser. Runs are kept, never
overwritten.

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

## Discovery Sync

The discovery corpus is every FAA airworthiness directive in the Federal
Register. It is synced from a checkpoint into `data/discovery/`, a separate
storage root and corpus track (`refreshable_discovery`); the sync never
writes to the frozen evaluation corpora:

```bash
make discovery-sync       # live: search, read IAE directives in full, validate, promote or reject
make discovery-rollback   # offline: return to the previous promoted generation
make discovery-site       # offline: write the freshness page to site/index.html
make retrieval-corpus     # offline: normalize the frozen retrieval corpus (needs data/retrieval-frozen)
make retrieval-run        # offline: score candidate retrieval on the seed cases
make fleet-build          # offline: regenerate demo/fleet.json and demo/fleet-screen.json
make fleet-site           # offline: write the fleet view to site/fleet/index.html
```

Each directive gets a coverage state: `evaluated` (AD 2025-19-13 only),
`not_yet_evaluated` (paragraph (c) lists only V2500-A5/D5/E5 models), or
`outside_supported_scope`. Anything unclassifiable is held for review. The
freshness page shows the last attempt and success, the checkpoint, the active
generation, new directives, failures, and unavailable dependencies, and turns
STALE in the browser 48 hours after the last success. The scheduled GitHub
workflow runs daily and publishes the page to
<https://tanayvenkata.github.io/faa-directive-impact/>; see
[`DISCOVERY_SYNC.md`](DISCOVERY_SYNC.md).

## Accepted Raw Generations

- [`gen-20260926T213233Z-000f808f`](generations/gen-20260926T213233Z-000f808f/DECISION.md)
  — HPT hub proposal/final pair, `frozen_evaluation`, accepted for
  normalization. Its receipts, manifest, and validation report are committed;
  the raw bytes are not.
- [`gen-20260926T215105Z-7fe9da08`](generations/gen-20260926T215105Z-7fe9da08/DECISION.md)
  — ten-document seed corpus (three protected threads, a correction, a
  supersession pair, and incorporated-material challenges), `frozen_evaluation`,
  the source snapshot for the evaluation seed.

Raw bytes for each accepted generation are published as a deterministic
release archive, rebuilt from local storage with:

```bash
uv run faa-directive-impact package-generation <generation-id> --storage-root <root> --output dist/
```

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

Raw bytes are not committed to Git. Accepted frozen generations are published
as release assets with checksums; see [`REDISTRIBUTION.md`](REDISTRIBUTION.md).
