# Repository Guidelines

## Current Phase & Scope

Source review is complete (see `FEASIBILITY_RECOMMENDATION.md`). The repository is implementing **Milestone 1: Immutable Acquisition**, tracked as GitHub issues A1–A9 and described in `ACQUISITION_MILESTONE.md`. Implementation within that milestone is authorized; do not scaffold retrieval, indexing, agent, UI, hosting, or long-term storage components ahead of it.

The first vertical slice is acquisition and manifesting, not the polished fleet-impact application:

```text
official source acquisition
→ immutable raw captures
→ versioned normalized records
→ candidate search/index generation
→ validation and evaluation gates
→ explicit promotion or rejection
```

The initial supported evaluation boundary is the International Aero Engines V2500-A5/D5/E5 family described in the vault's `Production Evidence Systems/FAA Directive Impact.md`. Do not silently broaden supported applicability to adjacent engine families. A broader FAA discovery corpus may be indexed later without expanding the evaluated applicability claim.

Milestone 1 acquires only the HPT hub proposal/final pair (`2025-10764`, `2025-18469`) from Federal Register and GovInfo. FAA DRS automation stays deferred until its external API contract is verified.

## Project Structure & Module Organization

Code lives under `src/faa_directive_impact/`, with tests under `tests/`. Keep production code separate from automated tests, immutable source artifacts, derived data, and generated reports.

Organize modules by domain responsibility rather than by file type. For example:

```text
src/
  directives/    # FAA directive ingestion and normalization
  impact/        # Impact analysis and scoring
tests/
  fixtures/      # Small deterministic test inputs
```

## Build, Test, and Development Commands

The project uses Python 3.12 or later, `uv` for environment and dependency
management, and a root `Makefile` as the documented command entry point.

- `make sync` — create or update the local environment from `uv.lock`.
- `make test` — run the deterministic test suite; live network calls are not
  part of the default suite.
- `make lint` — run Ruff lint checks.
- `make format` — apply Ruff formatting.
- `make check` — run lint and tests.
- `make acquire DOCS="2025-10764 2025-18469"` — live network call; acquire
  every expected representation into `STORAGE_ROOT` (default `data/`) and
  write a raw-generation manifest for `CORPUS_TRACK` (default
  `frozen_evaluation`).

Run all commands from the repository root. Update this section and the README
when commands or tooling change.

## Source, Freshness & Data-Lifecycle Contract

Treat freshness as a first-class production responsibility, even if the first implementation uses a frozen corpus. The project must either implement each lifecycle behavior below or explicitly document why it is deferred, which later episode owns it, and how the limitation appears in the product and public claims.

- Use reproducible official-source queries or API requests; ordinary synchronization should be deterministic rather than delegated to an autonomous browsing agent.
- Preserve raw acquisitions immutably with source URL, retrieval timestamp, authority role, HTTP or source metadata where useful, and SHA-256 hash.
- Never replace an older proposal, final rule, correction, superseded directive, or changed representation in place. Preserve versions and relationships so both current-state and as-of queries remain possible.
- Make acquisition idempotent: rerunning the same synchronization must not duplicate records, while an unexpected hash change for an existing identity must be surfaced for investigation.
- Separate immutable raw artifacts, versioned normalized records, and rebuildable lexical/vector/graph indexes. A derived index is never the source of truth.
- Maintain two explicit corpus tracks: a frozen, versioned evaluation corpus for reproducible comparisons and a refreshable discovery corpus for current search and monitoring.
- Build new normalized/index generations as candidates. Validate acquisition completeness, parsing, identifiers, dates, relationships, citations, and protected regressions before atomically promoting a candidate.
- Retain the previous known-good generation and promotion receipt so rollback is demonstrable. Do not let a partial synchronization silently become active.
- Expose freshness honestly: last successful synchronization, source coverage or checkpoint, active generation, failures, and known unavailable dependencies. If synchronization is stale or incomplete, the workflow must say so.
- Begin with full rebuilds when they are simpler and safe. Add incremental reprocessing only after corpus size, latency, or cost demonstrates the need.
- An agent may later assist with bounded exception investigation, but it must not silently modify authoritative records, resolve source anomalies, or promote a release.

The first frozen manifest should record raw files, hashes, source and document versions, authority, acquisition timestamps, redistribution status, relationships, and unavailable incorporated dependencies.

## Coding Style & Naming Conventions

Follow the formatter and linter selected by the project configuration; do not mix manual formatting conventions with tool output. Use four spaces for Python and two spaces for JSON, YAML, and JavaScript/TypeScript. Name Python modules and functions with `snake_case`, classes with `PascalCase`, and constants with `UPPER_SNAKE_CASE`. Choose descriptive domain names such as `parse_airworthiness_directive` instead of abbreviations.

Keep external data access separate from analysis logic. Configuration, credentials, and environment-specific paths must not be hard-coded.

## Testing Guidelines

Add tests with every behavior change. Mirror source paths under `tests/`, and name tests after observable behavior (for example, `test_parser_rejects_missing_directive_id`). Tests should use small fixtures, avoid live network calls by default, and produce deterministic results. Run the full suite with `make test` (an autouse fixture fails any test that reaches a real network transport; `tests/test_lifecycle.py` is the end-to-end offline acquisition suite); run one file or test with `uv run pytest tests/acquisition/test_retrieval.py` or `uv run pytest -k <name>`.

## Commit & Pull Request Guidelines

There is no existing Git history from which to infer a convention. Use short, imperative commit subjects, optionally with a focused prefix, such as `parser: normalize directive identifiers`. Keep commits cohesive.

Pull requests should explain the problem, the approach, and verification performed. Link relevant issues or source directives, call out schema or data changes, and include sample output when analysis results change. Never commit secrets or API tokens. Decide whether raw source artifacts belong in Git, release assets, or external object storage only after reviewing their size, authority, redistribution status, and reproducibility requirements; do not discard them merely because they are generated.
