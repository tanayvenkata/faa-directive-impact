# Repository Guidelines

## Current Phase & Scope

Milestone 1: Immutable Acquisition is complete (`CHECKPOINT_REPRODUCIBLE.md`); its accepted frozen generation is under `generations/`. Milestone 2: Evaluation Seed has written the seed cases (E1) and frozen the gates in `evaluation/GATES.md` (E2); the image-transcription decision (E3) is recorded in `evaluation/E3_IMAGE_FIGURES.md`. S1, the rules baseline for AD 2025-19-13, is built (`evaluation/S1_BASELINE.md`): a normalized record (`src/faa_directive_impact/directives/`), deterministic rules and a static three-queue page (`src/faa_directive_impact/impact/`), and a scorer for the frozen gates (`src/faa_directive_impact/evaluation/s1_*.py`). The full-context LLM comparison (B2, `evaluation/B2_FULL_CONTEXT.md`) and LLM rule extraction (B3, `evaluation/B3_RULE_EXTRACTION.md`: a shared rule schema in `src/faa_directive_impact/schemas/b3-rule-record.schema.json` and a general interpreter in `src/faa_directive_impact/rules/`) are scored. The daily sync (`ROADMAP.md` step 6, `src/faa_directive_impact/discovery/`, `DISCOVERY_SYNC.md`) is live: a daily GitHub Actions run publishes the freshness page to GitHub Pages and keeps its state on the `discovery-state` branch. The *Evaluated* write-up is published (`writeups/02-evaluated.md`); the owner waived the hand-review sign-offs in `evaluation/review/OWNER_PACKET.md` on 2026-10-15, so hand-checked results are labeled as Claude's alone. The active work is the fleet view over a seeded demo fleet (`ROADMAP.md` step 8; vault, "Visual Layer and Launch"). `APPROACH.md` explains the workflow and the baselines.

Scope rules for this phase:

- **Model calls run only inside evaluation runs.** Use the Anthropic Python SDK through `src/faa_directive_impact/llm/`. Every request and response is saved in the run directory with its model, settings, tokens, and cost, so a run can be re-scored without calling the model. Tests replay saved responses and never call a model. The API key comes from the environment (`.env`, git-ignored), never from code or commits.
- **Never tune a prompt against the scored cases.** A plumbing check may confirm the output parses; then the prompt is frozen and versioned before any scored run. Never put labels, rationales, or adjudication answers into a prompt.
- **Static hosting only.** The site is static files on GitHub Pages. No server, database, or agent. The step 7 retrieval index is built offline from committed records (`evaluation/retrieval/corpus.json`) and is never the source of truth.
- **The evaluated claim covers only directives that pass `evaluation/coverage/PREREGISTRATION.md`.** On 2026-10-15 the owner directed full V2500 coverage with Claude standing in for human review; every such result is labeled `label_review: claude_stand_in`. A model scoring on other directives does not widen the claim by itself.
- Never edit `evaluation/GATES.md` or a seed case to make a run pass; follow its "Disputed Labels" section.

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
- `make s1` — offline; run the S1 rules baseline for AD 2025-19-13 and write a
  kept run directory under `evaluation/runs/`.
- `make s1-conclude RUN=evaluation/runs/<run-id>` — fold a completed
  hand-review sheet (gates 5 and 11) into that run's verdict.
- `make b3 MODEL=claude-opus-5-5 EFFORT=high REPEAT=1` — live model calls
  (batch); a model drafts the rule records for AD 2025-19-13 and AD
  2026-17-03, and the run is scored and kept under `evaluation/runs/`.
  `make b3-plumbing` is the format-only check made before a prompt freeze.
- `make b3-replay RUN=evaluation/runs/<run-id>` — offline; re-score a
  recorded B3 run. `make b3-summary` — offline; summarize B3 repeats under
  `evaluation/b3/PREREGISTRATION.md`.
- `make discovery-sync` — live network call; one checkpointed sync of the
  discovery corpus (all FAA airworthiness directives) into `DISCOVERY_ROOT`
  (default `data/discovery/`), promoting or rejecting a candidate generation.
  `START_DATE` applies only before the first promotion.
- `make discovery-rollback [TO=gen-...]` — offline; point the active
  discovery generation back at an earlier promoted one, with a receipt.
- `make discovery-drill [STATE=<commit>]` — reads `origin/discovery-state`,
  then offline; rollback-and-restore drill on a copy under `data/drill/`,
  checking the freshness page each time. Never pushes. Receipts:
  `operations/drills/`; hardening record: `operations/HARDENING.md`.
- `make discovery-site` — offline; write the static freshness page to
  `site/index.html`. Operations: `DISCOVERY_SYNC.md`.
- `make retrieval-corpus` — offline, needs `data/retrieval-frozen/`;
  normalize the frozen retrieval generation into
  `evaluation/retrieval/corpus.json`. `make retrieval-run` — offline; score
  candidate retrieval on the seed cases (`evaluation/RETRIEVAL.md`).
- `make fleet-build` — offline; regenerate the seeded demo fleet and its
  recorded screens (`demo/`). `make fleet-site` — offline; write the fleet
  view to `site/fleet/index.html` from `demo/fleet-screen.json`.

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

Pull requests should explain the problem, the approach, and verification performed. Link relevant issues or source directives, call out schema or data changes, and include sample output when analysis results change. Never commit secrets or API tokens. Raw source bytes stay out of Git; accepted frozen generations are published as checksummed release assets per `REDISTRIBUTION.md`. Do not discard raw artifacts merely because they are generated.
