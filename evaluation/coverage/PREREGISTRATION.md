# Full V2500 Coverage: Pre-Registration

Committed 2026-10-15, before any coverage case, rule-schema change, prompt,
or model draft exists. Later changes are numbered deviations at the end,
never edits above them. `GATES.md` is not edited.

## Direction

On 2026-10-15 the owner directed that every in-scope V2500-A5/D5/E5
directive get rules, cases, and an evaluation, with Claude standing in for
the human reviews that would otherwise gate it: "look for the stuff that we
ideally wanted human review, im going to ask you to roleplay and replace
that with your judgement. ik it isnt ideal and we cna say that". This
supersedes the earlier answer to keep the evaluated claim at AD 2025-19-13.
Every result below carries that disclosure.

## Directives

The in-scope final rules found by retrieval for the demo fleet (step 8),
each the latest in-force version of its thread:

| Document | AD | Subject (short) | Triage |
|---|---|---|---|
| 2025-18469 | AD 2025-19-13 | HPT hubs, P/N and S/N table, removal | Covered by S1 (unchanged) |
| 2026-16954 (+ 2026-18423) | AD 2026-17-03 | HPC stage-3 blades, replace at exposure | Reference rule record exists |
| 2024-12594 | AD 2024-11-03 | HPT parts AUSI at shop visit; terminates AD 2022-02-09 | Expressible |
| 2022-02574 | AD 2022-02-09 | HPT 1st-stage disk USI; S/N list in a service bulletin | Needs review by design (S/N list unavailable) |
| 2021-11960 | AD 2021-11-15 | Superseded by AD 2022-02-09 | Superseded |
| 2021-14268 | AD 2021-11-51 | HPT 1st-stage disk USI; S/N tables are images | Needs review by design (E3) |
| 2021-15486 | AD 2021-14-19 | HPT 1st-stage disk USI; S/N list in a service instruction | Needs review by design |
| 2020-07627 | AD 2020-07-51 | HPT 1st-stage disk removal by engine and disk S/N; records review | Expressible |
| 2019-19412 | AD 2019-18-01 | LPT stage-6 disk removal by S/N at piece-part exposure | Expressible |
| 2019-17403 | AD 2019-16-01 | D5 mount stiffener rails inspection | Expressible (inspection with limits) |
| 2017-14706 | AD 2017-14-07 | HPT stage-2 air seal etc. removal by CSN; S/N lists in a bulletin | Partly expressible |
| 2016-21061 | AD 2016-18-10 | HPT 1st/2nd-stage hub inspection by CSN band; applies only to hub S/Ns listed in a service bulletin | Needs review by design (S/N list unavailable) |
| 2015-12068 | AD 2015-10-04 | HPC stage 3-8 drum USI; all D5, and A5 by engine S/N range; also V2500-A1 | Expressible for A5/D5 (engine S/N ranges) |
| 2013-08448 | AD 2013-07-10 | No. 4 bearing scavenge tube check at each installation | Expressible (at each installation) |
| 2012-12329 | AD 2012-09-09 | HPC stage 3-8 drum USI | Superseded by AD 2015-10-04 |
| 2025-17066 | AD 2025-17-16 | Revise the ALS within 90 days | Operator program state |

Triage was read from each directive's paragraphs (c) to (i) before this file
was committed. Engine-serial applicability (AD 2015-10-04) means the demo
fleet needs real-format engine serial numbers (V1xxxx), still synthetic.

## What "Evaluated" Means Here

A directive becomes `evaluated` when all of these hold:

1. It has at least three coverage cases, including at least one where an
   action is due or waits on an event, one where nothing is triggered, and
   one where a named fact is missing, unless the directive cannot produce
   that outcome (stated per directive).
2. The independent label check (below) is complete and every disagreement is
   adjudicated in writing.
3. Its reviewed rule record, run through the interpreter, passes every
   protected gate and stays within every aggregate budget of `GATES.md` v1 on
   its units.

The coverage state stays `evaluated`; every record and page that shows it
also shows `label_review: claude_stand_in` and
`independent_check: claude_subagent`. Nothing is called
practitioner-reviewed.

AD 2025-19-13 keeps S1 as its screener and its existing evaluation.

## Operator Records

Old directives require actions whose deadlines passed years ago. Their
evidence lives in the operator's AD status record, not in part numbers. The
rule, fixed before any case is written:

- An operator record (`ad_records`, `recorded_status: complied` or
  `recurring`) for an action whose deadline has passed is reported as
  `no_action_triggered`, with the note "the operator's AD record shows this
  action accomplished; this screen does not verify it." Gate 5's forbidden
  claims still apply: never "compliant", never "airworthy".
- A record never overrides installed-part facts that contradict it
  (seed-028's principle): a listed part still installed means the action is
  open whatever the record says.
- No record, `open`, or `not_applicable` against facts that make the
  directive apply, for an action whose deadline has passed: `needs_review`,
  naming `ad_records[AD ...]`. Never "overdue", never "noncompliant".

## Cases

- Written by Claude from the directive text and synthetic assets, in a
  separate suite (`evaluation/coverage/cases/`, same schema, source
  generation `gen-20261015T175844Z-57440372`), **before any model draft of
  rules exists**.
- **Independent label check.** A separate Claude Opus subagent receives each
  case without its `expected` block, `rationale`, or `reason`, plus the
  directive text, and derives the outcome itself. Its answers are compared
  field by field (applicability, action status, missing facts, timing).
  Each disagreement is adjudicated by Claude against the cited text and
  recorded under `evaluation/coverage/critique/`. Both are the same model
  family, so their errors can be correlated; this is disclosed.

## Rules

- **Schema v2 and interpreter v2** are designed from the directive text, not
  from the cases, and frozen before the first scored run. Interpreter v1
  behavior is preserved: S1's `outputs.json`, the B3 v1 replays, and the
  current AD 2026-17-03 fleet screens must not change (a test asserts it).
- A deterministic check rejects any serial number in a rule record that does
  not appear in the directive's own text. Serial lists held only in
  incorporated material are recorded as unavailable dependencies, and
  engines whose part number matches go to `needs_review` naming them.
- **Drafting.** B3 prompt v2 is frozen after a plumbing check that tests
  format only, then Claude Opus 5.5 at high effort drafts every directive
  above in one recorded run (Batches API).
- **Stand-in proofread.** Claude reviews each draft against the text as the
  owner's stand-in and commits the reviewed record. Every changed field is
  logged with its reason. The count of changed fields replaces proofreading
  time, which cannot be measured honestly here.

## Scoring

- Both the raw drafts and the reviewed records are scored on the coverage
  cases under `GATES.md` v1, and reported separately.
- Exact counts per directive; no rate is claimed. A directive that fails a
  gate stays `not_yet_evaluated`, and the failure is reported.
- The fleet's queues widen to every directive that becomes `evaluated`.

## Deviations

None yet.
