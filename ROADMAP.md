# Project Roadmap

## Goal

Build a continuously refreshable, evidence-backed FAA directive-impact system
whose first supported evaluation boundary is the IAE V2500-A5/D5/E5 family.

## Corpus Layers

| Layer | Contents | Refresh | Claim |
|---|---|---|---|
| Discovery corpus | All FAA airworthiness directives the Federal Register API returns (published since 1994; the page states the coverage start) | Daily scheduled sync | Searchable and current; no correctness claim |
| Evaluated slice | V2500-A5/D5/E5 directives with labeled cases | Frozen generations, promoted explicitly | Impact results measured against the disclosed evaluation |
| Retrieval distractor set | Curated, frozen near-neighbor V2500 and adjacent-family records | Frozen with the evaluation | Controls retrieval evaluation; not a limit on discovery width |

The discovery corpus shows that the system is live. The evaluated slice shows
that it is correct. Widening discovery costs little; widening the evaluated
claim to another engine family requires its own fields, cases, and gates.

## Directive Coverage State

Every directive carries a coverage state, separate from source authority:

- `evaluated` — rules verified and covered by passing cases; its results may
  enter the impact queues.
- `not_yet_evaluated` — synced and parsed, with candidate rules, but not yet
  covered by cases. It is shown as new, and its candidate results stay out of
  the evaluated queues.
- `outside_supported_scope` — searchable only; no impact determination.

A newly published in-scope directive becomes visible the day it syncs, as
`not_yet_evaluated`. Adding its cases and passing the gates promotes it.

## Delivery Sequence

1. **Acquire** — deterministically fetch official representations, preserve
   exact bytes, and produce immutable manifests and completeness results.
   *Complete.*
2. **Evaluation seed** — write the feasibility seed cases, freeze numerical
   gates, and decide image-only figure transcription before normalization
   code (E1–E3). *Active.*
3. **Walking skeleton (rules baseline)** — normalize AD 2025-19-13 only,
   match the synthetic engines deterministically, and show the three queues
   with cited paragraphs on a plain page. This is the series' rules baseline:
   score it against the seed and publish the first failure taxonomy.
   *Built; decision go, hand review by Claude only
   ([`evaluation/S1_BASELINE.md`](evaluation/S1_BASELINE.md)).*
4. **Full-context LLM comparison (B2)** — give a model each directive's text
   and the engine's records and score its answers under the same frozen gates
   as the rules. This is a comparison, not a product component: it answers
   "why not just ask the model?" Start with the cheaper models (Claude Haiku
   5.5, then Claude Sonnet 5.5 at medium effort); record every response, its
   tokens, and its cost. See [`APPROACH.md`](APPROACH.md).
   *Done; hand review pending owner confirmation
   ([`evaluation/B2_FULL_CONTEXT.md`](evaluation/B2_FULL_CONTEXT.md)).*
5. **Rule extraction for new directives (B3)** — a model proposes candidate rules
   (models, part and serial tables, limits, triggers), each tied to the
   paragraph it came from. Automated checks validate them, and a human
   verifies them before promotion. Extracted rules are candidate derived data,
   never authoritative. Evaluate extraction against the hand-labeled seed.
   Compare it with the S1 parser run unchanged on a second directive.
   *Done; proofreading time and the AD 2026-17-03 labels await the owner
   ([`evaluation/B3_RULE_EXTRACTION.md`](evaluation/B3_RULE_EXTRACTION.md)).*
6. **Daily sync and freshness** — schedule the Milestone 1 acquisition for
   the discovery corpus: poll from a checkpoint, build a candidate generation,
   validate, then promote or reject while keeping the previous generation. The
   page shows the last successful sync, the active generation, new
   directives, and failures. Publish it as a static site (GitHub Pages).
   *Live since 2026-10-11: daily at 12:17 UTC, published at
   <https://tanayvenkata.github.io/faa-directive-impact/>, covering every FAA
   airworthiness directive since 1994 ([`DISCOVERY_SYNC.md`](DISCOVERY_SYNC.md)).*
7. **Normalize and retrieve** — normalize the evaluated threads, establish a
   lexical baseline, add only justified retrieval techniques, and distinguish
   relevance from evidence sufficiency.
   *Built and scored ([`evaluation/RETRIEVAL.md`](evaluation/RETRIEVAL.md)):
   an identifier-match retriever over a frozen 57-document corpus with
   near-neighbor distractors passes gate 14; no further technique was
   justified. It found a sync scope bug, now fixed; re-reading the two
   records already filed is a follow-up.*
8. **Fleet-impact queues and demo fleet** — widen the queues to every
   evaluated directive. Build a realistic seeded demo fleet of about 100–300
   engines with the evaluation cases embedded, plausible part numbers and
   cycle counts, and engines affected by several directives at once. The
   evaluation cases are edge cases and are not the demo fleet.
   *Built ([`demo/README.md`](demo/README.md)): 200 engines, each screened
   against the directives step 7 retrieval finds for it (16 across the
   fleet). Queues come from AD 2025-19-13, the only evaluated directive; the
   other 15 are shown beside them as not yet evaluated. Widening the
   queues needs another directive to become evaluated, which needs a person
   to confirm its cases.*
9. **Harden operations** — observability, recovery and rollback drills,
   hostile-input checks, runbooks, security controls, and cost and latency
   measurements. Keep operating cost and attention low enough to run for a
   year while later episodes are built. Upstream failures must surface loudly
   rather than leave the page silently stale. The interface states that it is
   a screening tool, not a compliance determination, and uses no FAA branding.
10. **Evaluate a bounded agent** — only if fixed-workflow traces demonstrate a
   feedback-dependent limitation that an agent can improve safely.
   *Decided: not justified ([`evaluation/AGENT_DECISION.md`](evaluation/AGENT_DECISION.md)).
   None of the four limitations the vault names appears in the traces; the
   residual failures need an authority's answer, not iteration.*

## User Evidence

No operator will upload a real fleet to this project; fleet records are
proprietary. User evidence is reviewer agreement on cases, observed
walkthrough sessions, and a time-to-answer comparison with the manual
process, not usage counts.

The demo leads with a story someone outside aviation follows in 60 seconds:
the directive that took effect, how many of the fleet's engines it affects,
the first deadline, and which engines need review and why. Evidence and
release history sit one level below.

## Publishing and Exit

Publish a write-up at each claim rung as it is reached:
[*Reproducible*](writeups/01-reproducible.md) and
[*Evaluated*](writeups/02-evaluated.md).

The FAA episode is done enough to hand off when all of these hold:

- it has reached *Evaluated*: baseline, frozen gates, paired results, and
  failures published;
- the daily sync is running with a visible freshness panel;
- at least one practitioner review has been attempted and recorded.

Then the series moves to Regulation E, while the FAA system keeps syncing at
low cost.

### Exit checklist

| Condition | State | What finishes it |
|---|---|---|
| *Evaluated*: baseline, frozen gates, paired results, failures published | **Done** ([`02-evaluated.md`](writeups/02-evaluated.md)). Hand-checked gates judged by Claude only; the owner waived re-checking them on 2026-10-15 ([`OWNER_PACKET.md`](evaluation/review/OWNER_PACKET.md)) | Nothing |
| Daily sync with a visible freshness panel | **Done** (live since 2026-10-11) | Nothing |
| One practitioner review attempted and recorded | **Deferred** by the owner on 2026-10-15 (issue #9) | Send [`PRACTITIONER_BRIEF.md`](evaluation/review/PRACTITIONER_BRIEF.md) and record the attempt in issue #9 |

Until the practitioner attempt is recorded, the episode has reached
*Evaluated* but has not met its handoff bar.

## Status

**Acquire** is complete, and the project is at the series' *Reproducible*
claim level ([`CHECKPOINT_REPRODUCIBLE.md`](CHECKPOINT_REPRODUCIBLE.md);
write-up [*Reproducible*](writeups/01-reproducible.md)). The
evaluation seed (E1) and frozen gates (E2) are done; the image-transcription
decision (E3) is recorded. S1, the rules baseline for AD 2025-19-13, is built and
scored: every gate passes on its 18 units, and the decision is go, with its
two hand-checked gates judged by Claude only
([`evaluation/S1_BASELINE.md`](evaluation/S1_BASELINE.md)). The full-context
LLM comparison (B2) is scored: no model setting matched the rules
([`evaluation/B2_FULL_CONTEXT.md`](evaluation/B2_FULL_CONTEXT.md)). Rule
extraction (B3) is scored
([`evaluation/B3_RULE_EXTRACTION.md`](evaluation/B3_RULE_EXTRACTION.md)). The daily
sync (step 6) is live with a public freshness page
([`DISCOVERY_SYNC.md`](DISCOVERY_SYNC.md)). The image-figure decision (E3)
is recorded ([`evaluation/E3_IMAGE_FIGURES.md`](evaluation/E3_IMAGE_FIGURES.md)).
The *Evaluated* write-up is published
([`writeups/02-evaluated.md`](writeups/02-evaluated.md)); the owner waived
the planned hand-review sign-offs on 2026-10-15. The practitioner review is
deferred. The active work is the fleet view and launch video (vault, "Visual
Layer and Launch"), which needs the seeded demo fleet (step 8).

## Revisions

- **2026-10-15 (b)** — The owner chose to finish every step that needs no
  person (7 to 10) before the visuals. The evaluated claim stays AD
  2025-19-13; other in-scope directives join retrieval and the fleet as
  `not_yet_evaluated`. A static, offline-built retrieval index is now in
  scope (AGENTS.md).

- **2026-10-15** — The owner waived the planned hand-review sign-offs and
  deferred the practitioner review, to finish the episode quickly. Results
  stay labeled as Claude's judgment where a person did not check them. The
  next work is the fleet view and launch video, which pulls the seeded demo
  fleet (step 8) forward.

- **2026-10-07** — Moved the LLM work ahead of the daily sync: a full-context
  LLM comparison (B2) and rule extraction (B3) now come before the sync and a
  static hosted site, so the measured AI results exist early. Retrieval,
  the demo fleet, hardening, and the agent keep their order after them.
  Steps renumbered: retrieval is now step 7. Frozen `evaluation/GATES.md`
  (v1) still calls it "ROADMAP step 6"; that reference means retrieval.

- **2026-10-06** — Moved a walking skeleton and the daily sync ahead of
  retrieval, so that a usable and visibly current system exists early. Set
  the discovery corpus to all FAA airworthiness directives while keeping
  correctness claims to V2500. Added directive coverage state, rule
  extraction for new directives, a demo fleet distinct from the evaluation
  cases, operating constraints, feedback-based user evidence, and an episode
  exit point. The sequence also now records that the evaluation seed precedes
  normalization, as already practiced.
