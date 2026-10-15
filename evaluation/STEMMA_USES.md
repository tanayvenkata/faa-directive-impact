# Where Stemma Shaped This Project

[Stemma](https://github.com/tanayvenkata/stemma) is the RAG and retrieval-evaluation
skill used while building this project (`/stemma`, loaded in Claude Code). This
file records each time it was consulted, which notes were read, and what
changed in the repository because of them, so a write-up can cite decisions
rather than recollections. The skill's own cross-project log is in the Stemma
repository (`docs/usage-log.md`).

Add one row per use: date, the decision being made, the notes read, and what
it changed here, with a link.

| Date | Decision | Notes read | What it changed here |
|---|---|---|---|
| 2026-10-05 | Writing the Milestone 2 gates (E2) | Statistical Decision-Making for Evaluation; Evaluation Strategy & Experimental Design; Production Evaluation Gates & Release Engineering; Ground-Truth Labeling & Label Lifecycle | Gates built on the repo's own seed cases rather than generic categories; exact counts with sparse-failure bounds instead of rates; `unresolved` as an allowed verdict ([`GATES.md`](GATES.md), "What the Sample Can Show") |
| 2026-10-05 | Planning the path from the seed to a first retrieval baseline | RAG Production Lifecycle; RAG System Design & Improvement Loop; Production Evaluation Gates & Release Engineering; Standard & Modular RAG; Production Data Lifecycle, Lineage & Freshness; Retrieval Calibration, Abstention & Authorization | Baseline before any retrieval technique; frozen generations promoted explicitly; retrieval deferred until gates existed ([`../ROADMAP.md`](../ROADMAP.md) step order) |
| 2026-10-15 | Designing and scoring step 7 candidate retrieval | Retrieval Calibration, Abstention & Authorization; Evidence Sufficiency & Correction; Retrieval & Metadata Evaluation; Sparse Retrieval; Filtered Retrieval | See below |

## 2026-10-15: Step 7 Retrieval

How each note turned into a concrete choice in
[`RETRIEVAL.md`](RETRIEVAL.md) and
[`retrieval/PREREGISTRATION.md`](retrieval/PREREGISTRATION.md):

- **Start from the simplest baseline; add a mechanism only for a measured
  failure** (SKILL.md thesis; Retrieval & Metadata Evaluation, "Controlled
  Protocol"). R0 is an identifier match. BM25 over prose, embeddings, and
  query rewriting were pre-registered as allowed only for a miss identifiers
  could not reach. None occurred, so none was added.
- **Freeze corpus, judgments, and evaluation code before the run**
  (Retrieval & Metadata Evaluation). The corpus selection rule, R0, and the
  measures were committed before acquisition; later changes are numbered
  deviations, not edits.
- **Relevance is not evidence sufficiency** (Evidence Sufficiency &
  Correction). Retrieval only proposes candidates; the screeners decide, and
  a candidate with no rule record goes to review as `not_yet_evaluated`.
  Retrieval can never clear an engine.
- **Never copy a score threshold; calibrate on the shipped pipeline**
  (Retrieval Calibration, Abstention & Authorization). There is no cutoff or
  top-k at all: every candidate goes to screening, so there is nothing to
  miscalibrate. Abstention is structural: no model on the record means
  `needs_review`.
- **Sparse retrieval wins on identifiers when tokenization preserves them**
  (Sparse Retrieval). The tokenizer keeps hyphens and slashes, so
  `6A8353-001` and `CFM56-5B4/3` survive as single tokens.
- **Scope as a hard filter, measured for false exclusion** (Filtered
  Retrieval; Retrieval & Metadata Evaluation, "Measure false exclusions
  separately"). The as-of date is a hard filter (no document published after
  the question date), and near-neighbor distractors (IAE outside the family,
  CFM, Pratt & Whitney) were acquired to measure false inclusion. That
  measurement is what exposed the daily sync's scope bug.
- **Evaluate the path that ships** (SKILL.md, "Mistakes seen in practice").
  The fleet view retrieves with the same R0 code and corpus that were
  scored ([`../src/faa_directive_impact/fleet/screen.py`](../src/faa_directive_impact/fleet/screen.py)).

Not used: the `gate_stats.py` script. The rule-of-three bound in
`RETRIEVAL.md` (3/27, about 11%) was computed by hand.
