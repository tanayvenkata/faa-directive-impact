# Repository Guidelines

## Current Phase & Scope

This repository is in **source-review and feasibility planning**, before implementation. Do not scaffold an application, select a language or framework, add package configuration, or commit to infrastructure until the focused FAA/Federal Register sources have been read and the implementation approach has been discussed.

The first intended vertical slice is acquisition and manifesting, not the polished fleet-impact application:

```text
official source acquisition
→ immutable raw captures
→ versioned normalized records
→ candidate search/index generation
→ validation and evaluation gates
→ explicit promotion or rejection
```

The initial supported evaluation boundary is the International Aero Engines V2500-A5/D5/E5 family described in the vault's `Production Evidence Systems/FAA Directive Impact.md`. Do not silently broaden supported applicability to adjacent engine families. A broader FAA discovery corpus may be indexed later without expanding the evaluated applicability claim.

For now, limit work to reading and recording the focused official sources: Federal Register API records and their official editions, FAA Dynamic Regulatory System records, the selected proposed-to-final directive threads, and explicitly identified incorporated-material dependencies. Do not begin coding unless the user asks after the source review.

## Project Structure & Module Organization

This repository currently contains planning guidance only. Any future structure must follow the chosen stack and the source/evaluation contracts; the example below is illustrative, not authorization to scaffold it. As implementation begins, keep production code separate from automated tests, immutable source artifacts, derived data, and generated reports.

Organize modules by domain responsibility rather than by file type. For example:

```text
src/
  directives/    # FAA directive ingestion and normalization
  impact/        # Impact analysis and scoring
tests/
  fixtures/      # Small deterministic test inputs
```

## Build, Test, and Development Commands

No build, test, or package configuration has been committed yet. When adding tooling, provide one documented entry point (such as a `Makefile`, `package.json`, or `pyproject.toml`) and update this section and the README in the same change. Prefer commands that work from the repository root, such as `make test`, `make lint`, and `make run`, rather than undocumented local scripts.

Do not choose or add this tooling during the current source-review phase.

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

Add tests with every behavior change. Mirror source paths under `tests/`, and name tests after observable behavior (for example, `test_parser_rejects_missing_directive_id`). Tests should use small fixtures, avoid live network calls by default, and produce deterministic results. Once a test framework is introduced, document the exact full-suite and targeted-test commands here.

## Commit & Pull Request Guidelines

There is no existing Git history from which to infer a convention. Use short, imperative commit subjects, optionally with a focused prefix, such as `parser: normalize directive identifiers`. Keep commits cohesive.

Pull requests should explain the problem, the approach, and verification performed. Link relevant issues or source directives, call out schema or data changes, and include sample output when analysis results change. Never commit secrets or API tokens. Decide whether raw source artifacts belong in Git, release assets, or external object storage only after reviewing their size, authority, redistribution status, and reproducibility requirements; do not discard them merely because they are generated.
