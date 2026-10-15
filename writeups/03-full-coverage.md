# From Two Directives to the Whole V2500 Family

*Draft, 2026-10-15. Not published. Every result is in.*

*Read this first. On 2026-10-15 the project owner directed that Claude stand
in for every human review this rung would otherwise need. Every label,
adjudication, proofread, and hand-judged gate below is Claude's. The
second-model check of the labels used the same model family, so it is not
independent in the way a person would be. No practitioner has reviewed any of
it. The fleet is synthetic. Its counts are what the rules output on that
fleet, and they say nothing about any real operator's engines. This post
makes one claim. Retrieval finds 16 V2500-A5/D5/E5 directives for the demo
fleet. Each now has a hand-written reference rule record. Fourteen of them
also have cases written before any model draft, and a paired, disclosed
score on 77 units under the gates frozen on 2026-10-06. AD 2025-19-13 keeps
its S1 evaluation, and AD 2012-09-09, which is superseded, has no scored
unit. One more directive, AD 2020-07-51, became `evaluated`, so the
evaluated set is two of sixteen.*

## Why coverage

[*Evaluated*](02-evaluated.md) scored one directive, AD 2025-19-13, on 18
units. A second directive, AD 2026-17-03, was scored for the model drafting
the rules (B3) only. That was enough to compare approaches. It was not
enough for a screen anyone could use. An engine is subject to every directive
that applies to it, not only the one somebody chose to study. A screen that
answers for one directive and says nothing about the other fifteen is a demo.
Its weakness is the one demos usually have: it shows the path where
everything works.

So the next rungs, in order, were:

1. find every directive an engine might fall under, without a person naming
   it first (step 7, retrieval);
2. make the daily sync safe to leave running (step 9, hardening);
3. decide whether an agent earns a place (step 10);
4. write rules and cases for every directive retrieval finds, and score them.

## Retrieval, and the sync bug it found

S1, B2, and B3 were each handed their directive. Retrieval starts from the
engine instead. The design and results are in
[`evaluation/RETRIEVAL.md`](../evaluation/RETRIEVAL.md). It was
pre-registered before the corpus was acquired.

- **An identifier match, nothing more.** The index covers two kinds of
  token: engine model designations from paragraph (c), and every part number
  in the regulatory text, tables included. Only documents published by the
  as-of date count.
- **No cutoff.** Every candidate goes on to screening, so there is no top-k
  or score threshold to tune. Retrieval proposes; it never clears an engine.
- **Real distractors.** The frozen corpus has 57 documents, including
  near-neighbor IAE, CFM, and Pratt & Whitney directives chosen by a rule
  written before acquisition.

On the 29 seed cases it surfaced 35 of the 37 expected candidates. Both
misses are engines outside the family (a PW1133G-JM and a CFM56-5B4/3),
whose expected outcome is "outside supported scope", so neither is a false
clear. Each in-family engine got 8 to 20 candidates (median 16). No true
distractor reached an in-family engine. Gate 14 passes. The pre-registration
allowed BM25, embeddings, or query rewriting only for a miss that
identifiers could not reach. There was none, so none was added.

The 48 distractor hits that did occur all came from two mislabeled
documents, and the mislabel pointed at a bug in the live daily sync. AD 2012-09-09 and AD 2015-10-04
state their applicability as "This AD applies to:" followed by a list that
includes V2522-A5 through V2533-A5. The sync's scope reader read only the
lead-in, found no V2500 model, and filed both `outside_supported_scope`.
Under the sync's own rules, a mixed list goes to a person. The reader now
follows a lead-in into its list, with a regression test. The two records
already in the discovery corpus were re-read on 2026-10-15 with a new
`--reread` option and moved to the review list
([`DISCOVERY_SYNC.md`](../DISCOVERY_SYNC.md), "Re-reading After a Scope
Fix"). The bug surfaced because false inclusion was measured with real
distractors, not because a test failed.

## Hardening, and the bugs it found

Step 9 is recorded in
[`operations/HARDENING.md`](../operations/HARDENING.md). Claude did all of
it and ran every check. No person repeated any of it.

- **Loud failure.** A failed or skipped run opens or comments on one GitHub
  issue and closes it on the next success. From day 45 without a commit to
  `main`, a second issue warns that GitHub may disable the schedule at 60.
  Both were tested with a stub `gh` in six scenarios. Neither has yet run on
  GitHub against a real failure.
- **Rollback drill.** On a copy of the live state, a rollback moved the
  active generation back one step, and a restore by id returned a
  byte-identical page. The drill found that the page did not say a rollback
  had happened. It now names the receipt that activated the current
  generation.
- **Hostile input.** The tests cover 16 malformed Federal Register search
  bodies plus an oversized page, attacks on the page itself, and 30 kinds of
  damage to engine records. ROADMAP step 9 counts seven bugs found and fixed.
  Three examples:
  - `"count": true` was accepted as 1, because a Python `bool` is an `int`.
  - A `javascript:` URL survived HTML escaping inside an `href`.
  - Damaged engine records crashed the screens on 16 of the 30 kinds of
    damage, and cleared silently in four ways. One of those ways: a listed
    hub serial with one Cyrillic letter in it went to `no_action_triggered`.
  A single preflight check now sends any malformed record to `needs_review`.
- **Security and cost.** The jobs run with least privilege. The actions are
  pinned by SHA. Both pages carry a Content-Security-Policy. The expected
  cash cost for a year is $0 while the repository stays public and no new
  evaluation runs are made. Model spend through step 9 was $7.24 over 868
  recorded calls.

## The agent decision

Step 10 asked whether a bounded agent was justified
([`evaluation/AGENT_DECISION.md`](../evaluation/AGENT_DECISION.md)). The bar
was a limitation that depends on feedback, appears in a recorded trace, and
that an agent would fix better than a deterministic change. The four
candidates named in the planning notes were:

- choosing among near-neighbor threads;
- asking for a newly material fleet fact;
- recovering from an unavailable source;
- pausing and resuming a review.

None appeared in that form. The one recovery failure was a code bug. Missing
facts are already named field by field. The residual hard cases (seed-005's
deadline, AD 2026-17-03's carry-forward reading) need an authority's answer.
An agent that searched harder would find nothing or guess, and a guess there
can be a false clear. **Decision: not justified; no agent was built.**
Claude made this decision under the owner's delegation, and no person
reviewed the evidence.

## The coverage method

### Direction and pre-registration

On 2026-10-15 the owner directed full coverage, with Claude standing in for
human review. Quoted as written:

> "look for the stuff that we ideally wanted human review, im going to ask
> you to roleplay and replace that with your judgement. ik it isnt ideal and
> we cna say that"

The plan was committed before any coverage case, rule-schema change, prompt,
or model draft existed:
[`evaluation/coverage/PREREGISTRATION.md`](../evaluation/coverage/PREREGISTRATION.md).
Later changes are six numbered deviations at its end, not edits. `GATES.md`
was not changed.

It fixed four things in advance:

- **What "evaluated" means.** A directive needs at least three cases, a
  completed label check with every disagreement settled in writing, and a
  reviewed rule record that passes every protected gate and stays within
  every aggregate budget.
- **Disclosure fields.** Any record that shows `evaluated` also shows
  `label_review: claude_stand_in`.
- **Operator records.** A rule for old directives whose deadlines passed
  years ago. An operator's "complied" record for such an action is reported
  as "nothing triggered, as the operator's record shows; this screen does not
  verify it". A record never overrides an installed part that contradicts it.
- **Serial guard.** A deterministic check rejects any serial number in a
  rule record that the directive's own text does not contain.

### The 16 directives

They are the in-scope final rules that retrieval finds across the demo
fleet, each the latest in-force version of its thread. Triage sorts each by
how much of it a rule record can express:

- **Expressible:** fully expressible as rules.
- **Needs review by design:** serial lists held only in a manufacturer
  bulletin, or printed as images.
- **Superseded.**
- **Operator program state:** the airworthiness-limitations directive, AD
  2025-17-16.

Three triage rows were wrong and were corrected before scoring (deviation
1).

### Cases written blind to any model draft

Claude wrote 62 coverage cases (`evaluation/coverage/cases/`, cov-001 to
cov-031 and cov-050 to cov-080). It wrote them from the directive text and
synthetic assets, in the seed's schema, before any model drafted a rule.
Separately, a different Claude agent wrote a reference rule record for each
of the 16 directives without seeing the cases (deviation 2). These records
are the rules baseline. They play the part S1 and the B3 references played.

### A second-model blind check of the labels

The labels went through a second-model blind check, with disagreements
settled by Claude acting for the owner
([`critique/2026-10-15-label-check.md`](../evaluation/coverage/critique/2026-10-15-label-check.md)).

- **The packet.** A separate Claude Opus subagent got each case's facts and
  candidates and the directive text. It did not get the expected outcome,
  rationale, reason, notes, or forbidden claims. It derived each outcome
  itself.
- **The comparison.** Its answers were compared field by field:
  applicability, action status, and whether missing facts are named.
- **Who settled disagreements.** Claude, acting for the owner, settled each
  one against the cited text.

The checker and the case writer are the same model family, so their errors
can be correlated. This check makes the labels less likely to rest on one
careless reading. It does not show that the labels are right.

| Group | Cases | Outcomes | Field disagreements | Outcomes with a disagreement | Labels changed |
|---|---|---|---|---|---|
| B (AD 2019-18-01, 2019-16-01, 2015-10-04, 2013-07-10, 2025-17-16, 2026-17-03) | 39 | 41 | 8 | 6 | 1 (cov-055) |
| A (AD 2024-11-03, 2022-02-09, 2021-11-51, 2021-14-19, 2020-07-51, 2016-18-10, 2017-14-07) | 34 | 37 | 7 | 4 | 0 |

The one changed label shows why the check was worth running. Read
literally, AD 2019-18-01's paragraph (c) lists engine serial numbers only, so
it does not apply to cov-055's engine. But that engine carries a disk that
paragraph (g) names for removal, and a screen must not clear that. The label
became `needs_review`, with the interpretation question named. The other
disagreements were settled in favor of the label, each with its reason
written down against the cited paragraph. Four
disputes were raised later by the reference-record author. Three labels
were kept. Two missing-fact labels (cov-017, cov-026) were corrected for
format only, in their own commit; the file states that no earlier result
changed.

### Rules v2, then 2.1: the paired result

A new rule schema (v2) and interpreter (v2) were designed from the
directive text and frozen at commit `3c9a1ff`. A test asserts that every
earlier output is unchanged: S1, the B3 replays, and the AD 2026-17-03 fleet
screens. The first scored run screened the 16 reference records on 77
units. Those units cover the 14 directives with coverage units; AD
2025-19-13 keeps S1, and AD 2012-09-09, superseded, has no scored unit. That
run exposed three general gaps in the interpreter
(deviation 4):

1. citations covered only part of a record's basis (gate 10);
2. facts that contradict an operator record, but are not a part number to
   remove, were not read, which gave two false clears (cov-067 and cov-076,
   gate 1);
3. a part named for removal, installed in an engine outside the serial list,
   was cleared (cov-055, gates 3 and 9).

Interpreter 3 (schema v2 with optional 2.1 fields; v1 records unchanged
byte for byte) fixes all three in general form (deviation 5). **These
changes were made after reading the cases and the v2.0 run, so 2.1 is not
blind.** Both runs are reported:

| Run | Interpreter | Directives passing every mechanical gate | Gate 1 (false clear) failures | Source |
|---|---|---|---|---|
| reference v2.0 | v2 | 2 of 14 | 2 (cov-067, cov-076) | [`report.md`](../evaluation/runs/coverage-reference-v2.0-20261015T192640Z/report.md) |
| reference v2.1 | 3 | 7 of 14 | 0 | [`report.md`](../evaluation/runs/coverage-reference-v2.1-20261015T194038Z/report.md) |
| reference v2.1, re-scored (deviation 8) | 3 | 8 of 14 | 0 | [`report.md`](../evaluation/runs/coverage-reference-v2.1-index-fix-20261015T225944Z/report.md) |

The re-scored row uses the fixed section index described below, and the
corrected cov-017 label, committed four minutes after the first v2.1 run.
Under it cov-017 passes. Even so, the hand-written references fail
mechanical gates on 6 of 14 directives. Here is what remains:

- **Gate 8, exact arithmetic.** AD 2019-16-01, 2019-18-01, 2024-11-03.
- **Gate 12, needless escalation, over budget.** AD 2019-16-01, 2024-11-03,
  and the ALS directive AD 2025-17-16, which does not read a program
  revision stated only in words.
- **Gate 4, every missing fact named.** cov-026, failing before and after
  its format correction.
- **Gate 10, required evidence cited.** cov-006 on AD 2022-02-09. It needs
  a citation to AD 2024-11-03 (i), but the frozen manifest records no
  relationship between the two directives. Citing it would be a
  fabrication under gate 6. Reported, not patched.

None is a false clear: gate 1 passes on all 14 directives. Not every
remaining failure is harmless. Two units settled `action_required` with a
wrong or missing cycle count. cov-059 expected 17,000 engine cycles and got
19,400; cov-050 computed none (`report.json`, gate 8 detail). Gates 5 and 11
are judged by hand, and they were not judged for the reference runs. They
were judged only where a directive could otherwise become evaluated (below).

### Model drafting

Prompt v2 was frozen at `226de36424d1`. Its schema's field descriptions had
been written after the cases were read, so they were first scrubbed of
case-specific examples (deviation 6). A format-only plumbing check then had
the model draft a CFM International directive outside the evaluation
(`2025-02204`). The answer parsed, validated, and passed the serial guard, at
a cost of $0.1323
([`summary.json`](../evaluation/runs/coverage-plumbing-20261015T194653Z/summary.json)).
Then Claude Opus 5.5 at high effort drafts all 16 directives in one recorded
run, and Claude proofreads each draft as the owner's stand-in.

The drafting run cost $2.31 for 16 drafts. All 16 validated against the
schema and passed the serial guard, and every one ended normally
([`summary.json`](../evaluation/runs/coverage-drafts-opus-5-5-high-20261015T195012Z/summary.json)).
The run nearly went unrecorded. The process that submitted the batch
stopped before results came back, and it had kept the batch id only in
memory. The batch was found in the account's batch list and collected
unchanged when it ended. Every result's request hash matched the rebuilt
request, so the 16 requests are the ones submitted. The runner now saves
the batch id at submission (deviation 7).

Scored raw, before any proofread:

| Run | Records | Directives passing every mechanical gate | Gate 1 (false clear) failures | Source |
|---|---|---|---|---|
| raw drafts | model, unreviewed | 4 of 14 | 0 | [`report.md`](../evaluation/runs/coverage-drafts-raw-20261015T225328Z/report.md) |
| raw drafts, re-scored (deviation 8) | model, unreviewed | 4 of 14 | 0 | [`report.md`](../evaluation/runs/coverage-drafts-raw-index-fix-20261015T225944Z/report.md) |

The raw drafts cleared no engine that needed action. They failed more
often than the hand-written references, almost always on the safe side:
21 needless escalations against the references' 10 (gate 12), six missing
facts left unnamed (gate 4), seven arithmetic misses (gate 8), and six
units with required evidence uncited (gate 10).

The first scoring also showed six fabricated citations (gate 6), all on AD
2015-10-04, all to paragraphs (e)(2) to (e)(5). The draft was right and the
scorer was wrong. That directive sets each numbered subparagraph of (e) as
its own heading, and the section index read numbered items only from body
text, so it never indexed them. The hand-written reference had cited only
paragraphs the index knew, because a test requires exactly that, so the
bug never showed. The index now reads those headings, with a regression
test. No seed-generation document changes, so S1, B2, and B3 stand. Both
runs were re-scored, and the gate 6 failures are gone (deviation 8).

The raw drafts were scored before the proofread, so the session running
the evaluation knew which units they failed. The proofread was therefore
handed to a separate agent under a brief frozen first
([`PROOFREAD_BRIEF.md`](../evaluation/coverage/reviewed/PROOFREAD_BRIEF.md)).
That agent saw each draft and its directive text, but not the cases, the
scores, or the reference records. Its blindness rests on instruction, not
on file access, and it is the same model family as the drafter.

### The proofread

The proofread changed 23 fields across 8 of the 16 drafts. Eight
directives came back unchanged
([`CHANGES.md`](../evaluation/coverage/reviewed/CHANGES.md)). That count
stands in for proofreading time, which nobody measured. A leaf-by-leaf
diff of each reviewed record against its draft matches the log. The
changes that matter for screening:

- **AD 2016-18-10, 8 fields.** Its inspections apply only to hubs whose
  serials are listed in a service bulletin the text does not print. The
  draft left those actions with no dependency. Each now points at the
  bulletin table, so an engine goes to a person instead of being judged
  without the list.
- **AD 2021-11-51, 6 fields.** Two eligible-part entries had empty
  part-number lists, which the schema reads as "any part number". They were
  removed, along with four ambiguities the text settles.
- **AD 2025-19-13, 4 fields.** The draft listed paragraph (g)'s timing as
  ambiguous but still encoded the lenient reading. Its combination is now
  `unclear`. This is the clause that went to the FAA. The fleet still
  screens this directive with S1.
- **The rest, 5 fields.** Three removed ambiguities the text settles
  (AD 2020-07-51, 2022-02-09, 2026-17-03), one added a "before further
  flight" limit (AD 2021-14-19), and one corrected a note's source
  (AD 2015-10-04).

None changed an identifier, and none moved an engine toward a clear.

### The reviewed records, scored once

| Run | Records | Directives passing every mechanical gate | Gate 1 (false clear) failures | Source |
|---|---|---|---|---|
| reviewed drafts | model, stand-in proofread | 4 of 14 | 0 | [`report.md`](../evaluation/runs/coverage-drafts-reviewed-20261015T230605Z/report.md) |

The proofread did not change the mechanical result. The same four
directives pass, with the same failure counts on every gate as the
re-scored raw drafts. Its changes made records stricter in places no case
exercises. The reviewed records were scored once and not proofread again,
as pre-registered.

### Which directives became evaluated

One. AD 2020-07-51 meets all three pre-registered conditions
([`evaluated.md`](../evaluation/runs/coverage-drafts-reviewed-20261015T230605Z/evaluated.md)):

- four cases covering action due, a missing fact, and nothing triggered;
- a complete label check;
- every mechanical gate passing, and gates 5 and 11 judged on all four
  units ([`hand-review.json`](../evaluation/runs/coverage-drafts-reviewed-20261015T230605Z/hand-review.json)).

Three more directives pass every mechanical gate but miss the first
condition:

- **AD 2017-14-07 and AD 2021-14-19.** Neither has a case where action is
  due. Their serial lists sit in service documents the screen does not
  have, so it may never be able to say "action due". The pre-registration
  allows that exception only if it was stated per directive in advance. It
  was not, and stating it now, after the scores, would be post hoc.
- **AD 2021-11-15.** It has no coverage case of its own, only two seed
  units. It is superseded by AD 2022-02-09.

The other ten stay `not_yet_evaluated` on a failing gate, mostly
needless escalation (12), arithmetic (8), unnamed missing facts (4), or
uncited evidence (10). None of them is a false clear.

So the evaluated set is two directives: AD 2025-19-13 on S1, and AD
2020-07-51 on a model draft that a stand-in proofread left almost
unchanged. Both carry `label_review: claude_stand_in`.

## The fleet: real registry shape, synthetic state

The demo fleet is 200 V2500-A5/D5 engines on 100 aircraft
([`demo/README.md`](../demo/README.md)). Its generation rules were committed
before version 2 was generated and were not changed after seeing the
output.

- **Shape: real, aggregate only.** The fleet's shape comes from the FAA
  Aircraft Registry (`demo/registry-v2500.json`): 705 U.S. aircraft with
  V2500 engines. Of those, 286 are A320-232 and 275 are A321-231. The 90
  generated aircraft are allocated in proportion, and build years are drawn
  from the registry's years.
- **Seed engines.** The 20 seed engines are embedded unchanged.
- **State: synthetic.** Everything else is invented: serial numbers (real
  format, values skipped if any directive prints them), cycles, shop visits,
  part replacements, unknown fields, and 2,362 operator AD records. The rates
  behind them are judgment, and nobody in aviation maintenance has checked
  them (issue #20). Five listed AD 2025-19-13 hubs were planted on purpose.

Every engine is screened against every candidate retrieval finds for it.
The queues come from the two evaluated directives, AD 2025-19-13 and AD
2020-07-51: 15 potentially affected, 19 needs review, and 166 no action
([`demo/fleet-screen.json`](../demo/fleet-screen.json),
`evaluated_counts` and `evaluated_directives`). The other fourteen are
shown beside the queues as not yet evaluated.

Widening the queues did not move a single engine. AD 2020-07-51 does not
apply to 186 engines. It sends 14 to review, and all 14 were already
there for AD 2025-19-13, for the same reason: the engine record lacks the
HPT hub or disk serial number both directives turn on. Those engines now
carry two reasons for review instead of one. No synthetic engine holds a
listed AD 2020-07-51 disk, because the fleet generator skips every serial
number a directive prints.

## Documents block more decisions than reading does

The fleet screen also records, for each engine, what kept it from a
decision (`fleet-screen.json`, `blocking_documents` and
`missing_fact_kinds`). The largest single cause is not a hard sentence. It
is a manufacturer document the directive incorporates by reference, which
the project cannot obtain.

| Unavailable document | Directive | Engines left in review |
|---|---|---|
| IAE NMSB V2500-ENG-72-0713 | AD 2022-02-09 | 195 |
| IAE NMSB V2500-ENG-72-0720 | AD 2024-11-03 | 195 |
| P&W SI No. 112F-21 | AD 2021-14-19 | 195 |
| P&W SI No. 114F-21 | AD 2021-14-19 | 195 |
| IAE NMSB V2500-ENG-72-0661 | AD 2016-18-10 | 193 |

Each count is per document, not combined. The mechanism is simple. These
directives name a hub or disk part number in their own text but print the
affected serial numbers only in the manufacturer's bulletin. The fleet
generator gives the generated engines the directive-named hub part numbers
2A5001 and 2A4802 ([`demo/README.md`](../demo/README.md), "Part
Numbers"). So those engines carry the part, and the screen cannot tell
whether its serial is on the list. It sends the engine to review and names
the document. AD 2022-02-09, AD 2024-11-03, and AD 2021-14-19 each send all
200 engines to review (`fleet-screen.json`, `directives[].outcomes`).

**These counts come from the rules running on a synthetic fleet. They are
not findings about any real fleet.** They are mostly a product of the
generation rules. The general point does carry over. When a serial list
exists only in incorporated material, every engine carrying the named part
waits on that document, however well the directive itself is read. That is
a data-access problem, not a reading problem, and neither a model nor an
agent fixes it. A separate cause: AD 2025-17-16, the ALS directive, sends
160 engines to review. Interpreter 3 does not accept a program revision
stated only in words as proof, by its stated rule
([`demo/README.md`](../demo/README.md), "What blocks decisions").

## What this can and cannot show

It can show:

- that retrieval, run from the engine, surfaced every expected in-family
  candidate on 29 author-written cases, and that measuring false inclusion
  found a real bug in the live sync;
- that hand-written rules for 16 directives, under the same gates frozen on
  2026-10-06, pass every mechanical gate on 8 of 14 scored directives
  (re-scored, deviation 8) after a disclosed, non-blind interpreter change,
  with no false clear;
- that model drafts of the same 16, from one recorded run costing $2.31,
  pass every mechanical gate on 4 of 14, before and after a stand-in
  proofread, with no false clear;
- that one model-drafted directive, AD 2020-07-51, met every
  pre-registered condition to become `evaluated`;
- where decisions get blocked on this synthetic fleet, and why.

It cannot show:

- **Correctness against a person's reading.** Claude wrote the cases, the
  reference records, and the adjudications. The label check used a second
  model of the same family. A shared misreading passes every gate.
  Practitioner review (issue #9) is deferred and is not claimed.
- **Rates.** 77 units over 14 directives is two to eight per directive.
  Counts are exact; no failure rate is claimed.
- **Blind results for 2.1.** Interpreter 3 was written after the v2.0 run
  and the cases were read. Only v2.0 is a blind score of the interpreter.
- **The hand-judged gates beyond one directive.** Gates 5 (forbidden
  claims) and 11 (timing) were judged, by Claude, only for AD 2020-07-51,
  the one directive that met every other condition. They are not judged
  for the reference runs or for directives that already failed.
- **A blind proofread by a person.** The proofreaders were agents of the
  drafter's model family, kept from the cases and scores by instruction,
  not by file access.
- **Anything about real fleets.** The fleet's shape is from the registry;
  its state is invented. Its queue and blocking counts describe the rules
  on that fleet only.
- **Use.** Nobody outside the project has used the pages. This is a
  screening tool, not a compliance determination.

Every run is kept under [`evaluation/runs/`](../evaluation/runs/) and
re-scores offline.
