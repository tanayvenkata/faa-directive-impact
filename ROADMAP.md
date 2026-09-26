# Project Roadmap

## Goal

Build a continuously refreshable, evidence-backed FAA directive-impact system
whose first supported evaluation boundary is the IAE V2500-A5/D5/E5 family.

## Delivery Sequence

1. **Acquire** — deterministically fetch official representations, preserve
   exact bytes, and produce immutable manifests and completeness results.
2. **Normalize** — parse source structure into versioned identities,
   relationships, evidence regions, predicates, tables, figures, and
   dependencies.
3. **Evaluate** — freeze the protected corpus and synthetic fleet cases; test
   parsing, retrieval, citations, temporal behavior, applicability, and safe
   abstention.
4. **Retrieve and assess evidence** — establish a lexical baseline, add only
   justified retrieval techniques, and distinguish relevance from evidence
   sufficiency.
5. **Produce fleet-impact queues** — deterministically classify cases as
   potentially affected, not affected for the tested directive, or needs
   review, with cited reasons.
6. **Refresh safely** — poll from checkpoints, build candidate generations,
   validate them, promote atomically, retain rollback, and expose freshness.
7. **Harden operations** — add observability, recovery tests, hostile-input
   checks, runbooks, security controls, and cost/latency measurements.
8. **Evaluate a bounded agent** — only if fixed-workflow traces demonstrate a
   feedback-dependent limitation that an agent can improve safely.

**Acquire** is complete, and the project is at the series' *Reproducible*
claim level ([`CHECKPOINT_REPRODUCIBLE.md`](CHECKPOINT_REPRODUCIBLE.md)). The
active milestone is **Evaluation Seed**: seed cases, frozen gates, and the
image-transcription decision, before normalization.

