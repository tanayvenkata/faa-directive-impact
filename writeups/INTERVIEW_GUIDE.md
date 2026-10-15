# Interview Guide: FAA Directive Impact

*For the owner. A study guide for speaking to the project, not a public
page. Written 2026-10-15 from the repository at branch `v2500-coverage`.
Every number below names its file. Numbers that do not exist yet are marked
**PENDING**, with where they will come from. When in doubt in an interview,
say the file name rather than round a number.*

## Rules for talking about it

- **Lead with the gap when asked about evidence.** Nobody outside the
  project uses it. No practitioner has reviewed it (issue #9, deferred). The
  hand-judged gates and every coverage label are Claude's, by your direction
  on 2026-10-15.
- **Say "screening tool", never "compliance".** The pages say so
  themselves (`operations/HARDENING.md`, item 5, "Branding").
- **Synthetic fleet, real shape.** The fleet's shape comes from the FAA
  Registry, and its state is invented (`demo/README.md`). Fleet counts are
  the rules' output on that fleet. They are not findings about real
  airlines.
- **The label check.** Call it "a second-model blind check, with
  disagreements settled by Claude acting for me." Never say "independently
  verified."
- **Don't say "production-ready".** Say "built to production habits":
  immutable inputs, frozen gates, promotion and rollback, loud failure.

## The 30-second pitch

> FAA airworthiness directives are legally binding orders to inspect or
> replace engine parts. The FAA publishes 300 to 400 final ones a year. The
> hard part isn't noticing them. It's checking each one against every
> engine's part and serial numbers, cycles, and shop visits. I built a
> system for one engine family, the IAE V2500, that does that check with
> deterministic rules. Every answer cites the paragraph it rests on, and
> anything it can't decide goes to review with the missing fact named. I
> scored it against an LLM reading the directive directly, on cases and
> gates I froze before any run. Plain rules passed every gate; no model
> setting matched them.

Sources: `APPROACH.md` ("The Problem", 2022 to 2025 counts);
`writeups/02-evaluated.md` ("Results").

## The 2-minute version

1. **Problem.** An AD names engine models, but whether a given engine must
   act depends on its records. AD 2025-19-13 names 10 engine models, but
   only engines carrying 8 specific hubs need action (`APPROACH.md`). Misses
   are costly. In 2008 the FAA proposed a $10.2 million penalty against
   Southwest over missed inspections; Southwest settled for $7.5 million
   (`APPROACH.md`, "Why It Matters").
2. **Reproducible first.** Before reading anything, I made acquisition
   checkable byte for byte. The system writes a receipt with a SHA-256 for
   every fetch, publishes immutable generations, and promotes a generation
   only when it is complete and validated. The first accepted set: 12 of 12
   artifacts, 54 of 54 checks (`writeups/01-reproducible.md`).
3. **Evaluated against a frozen bar.** I wrote 29 edge-case cases (33
   scoring units, 18 for AD 2025-19-13) and froze 14 gates before any run.
   Nine gates are protected, where one failure fails the system: no false
   clear, no made-up citation, exact cycle arithmetic
   (`evaluation/GATES.md`).
4. **Three approaches, same cases.**
   - **Rules (S1):** zero protected failures.
   - **The best model reading the directive (B2):** about 2 per run.
   - **A model drafting the rules once (B3):** every data field right, but
     it left one ambiguous clause open, so 10 units went to review. That was
     the very clause I had to ask the FAA about.
   (`writeups/02-evaluated.md`)
5. **Live.** A daily sync covers every FAA AD since 1994, about 13,000. It
   publishes a freshness page that turns STALE after 48 hours
   (`DISCOVERY_SYNC.md`).
6. **Widened.** Retrieval now finds every directive an engine might fall
   under. I wrote rules and cases for all 16 V2500 directives it finds, plus
   a 200-engine demo fleet shaped like the real U.S. registry
   (`evaluation/RETRIEVAL.md`, `writeups/03-full-coverage.md`).
7. **Conclusion.** Use the model to draft rules, once per directive, where a
   person proofreads them once. Then let the rules decide for every engine.

## Architecture walk-through

Code is under `src/faa_directive_impact/`, organized by domain: `acquisition/`,
`directives/`, `discovery/`, `retrieval/`, `rules/`, `impact/`, `fleet/`,
`evaluation/`, `llm/`.

### 1. Acquisition (`acquisition/`)

- **What.** For each document, the system fetches the Federal Register API
  record, its XML, HTML, and text, and GovInfo's PDF and MODS metadata.
- **Decision: fetch every official representation, not just one.** The
  representations can cross-check each other. Live runs found six surprises
  no design anticipated. Two examples: the PDF prints identifiers with an en
  dash, and the API record changes on every fetch because it carries a
  page-view counter (`writeups/01-reproducible.md`, "What the live sources
  taught us").

### 2. Immutable receipts (`acquisition/storage.py`, `schemas/`)

- **What.** Every attempt, success or failure, writes a schema-validated
  receipt. It records the source URL, the time, the role, and a SHA-256.
  Artifacts are read-only and never overwritten (`README.md`).
- **Decision: receipts before parsing.** A citation is only as good as the
  bytes it points at. If you cannot say which bytes you read, no later claim
  can be checked. Versions ignore the one named volatile field, and the
  exact bytes are still kept.

### 3. Generations, promotion, rollback (`acquisition/manifest.py`, `discovery/state.py`)

- **What.** A run produces a candidate generation and a manifest of what
  was expected versus found. A candidate is promoted only if it is complete
  and every check passes. Promotion writes a receipt naming the previous
  generation, then atomically replaces `active.json`. Rollback is one
  command (`DISCOVERY_SYNC.md`, step 6).
- **Decision: two corpus tracks.** One is frozen for evaluation and one is
  refreshable for discovery, so a daily sync can never change what was
  scored. The sync refuses any storage root that holds frozen corpora.
- **Proof.** A rollback drill ran on a copy of the live state. The restore
  produced a byte-identical page. The drill found that the page did not say
  a rollback had happened, and that is now fixed (`operations/HARDENING.md`,
  item 3).

### 4. Discovery sync (`discovery/`)

- **What.** A daily GitHub Actions job queries the Federal Register for FAA
  part 39 final rules from a checkpoint, with a 7-day lookback. It reads IAE
  directives in full and sets each one's coverage state from paragraph (c),
  not the title: `evaluated`, `not_yet_evaluated`, or
  `outside_supported_scope`. Anything it cannot classify goes to a review
  list (`DISCOVERY_SYNC.md`).
- **Decision: deterministic sync, not a browsing agent** (AGENTS.md). A
  search that might be truncated fails, because the API caps results at
  10,000.
- **Numbers.**
  - Backfill: about 13,000 rules, with 45 IAE directives read in full.
  - Daily run: about 40 seconds.
  - Cash cost: $0 on a public repository.
  - Schedule delay: 4.8 to 9.0 hours late, which is still inside the
    48-hour STALE limit.
  (`DISCOVERY_SYNC.md`, "Cost"; `operations/HARDENING.md`, item 6)

### 5. Retrieval (`retrieval/`)

- **What.** It starts from an engine and finds every directive the engine
  might fall under. It matches identifiers only: model designations from
  paragraph (c), and part numbers from anywhere in the regulatory text.
- **Decision: relevance, not sufficiency, and no cutoff.** Retrieval only
  proposes candidates and never clears. Every candidate is screened, so
  there is no threshold to miscalibrate. BM25 and embeddings were allowed
  only for a miss that identifiers could not reach. There was none.
- **Numbers.** 35 of 37 expected candidates surfaced. Both misses were
  out-of-family engines. No true distractor reached an in-family engine, in
  a frozen 57-document corpus (`evaluation/RETRIEVAL.md`).
- **The sync bug it found.** The scope reader stopped at "This AD applies
  to:" and filed two V2500 directives out of scope. It is now fixed and
  both were re-read.

### 6. Rules and interpreter (`impact/hpt_hub_rules.py`, `rules/`)

- **What.** S1 is hand-written code for AD 2025-19-13. For other
  directives, a rule record is data: models, part and serial tables, limits,
  and triggers, each tied to a paragraph. A fixed interpreter applies the
  record to each engine.
- **Decision: the model writes data, not decisions.** The interpreter never
  guesses. An "unclear" field sends the engine to review. A serial guard
  rejects any serial number that is not in the directive's own text
  (`rules/serial_guard.py`). A preflight check sends any malformed engine
  record to review (`operations/HARDENING.md`, item 4).
- **Versioning.** Interpreter 3 keeps every v1 output byte for byte, and a
  test asserts it (`evaluation/coverage/PREREGISTRATION.md`, deviation 5).

### 7. Fleet screen (`fleet/`)

- **What.** 200 synthetic V2500-A5/D5 engines. Each one is retrieved
  against, then screened on every candidate. The output records per-engine
  outcomes, the missing facts, and the unavailable documents blocking a
  decision (`demo/fleet-screen.json`).
- **Decision: realistic shape, declared before generation.** Airframe mix
  and build years come from the FAA Registry: 705 U.S. aircraft. Rates were
  committed before generating, and the edge-case seed engines are embedded
  but are not the fleet (`demo/README.md`).
- **Decision: queues only from evaluated directives.** Today that is AD
  2025-19-13: 15 potentially affected, 19 needs review, 166 no action
  (`demo/fleet-screen.json`, `evaluated_counts`). The other directives sit
  beside the queues as not yet evaluated.

### 8. The page (`discovery/site.py`, `fleet/page.py`)

- **What.** Static HTML on GitHub Pages: no server and no database. The
  freshness page shows the last success, the checkpoint, the active
  generation, failures, and the receipt that activated it.
- **Decision: static, with a strict CSP.** The freshness page allows only
  its own hashed script and style. Links go only to federalregister.gov. A
  failed run opens a GitHub issue (`operations/HARDENING.md`, items 2 and
  5).

## The evaluation story

### Frozen gates

`evaluation/GATES.md` was frozen on 2026-10-06, before any run.

- **Protected gates (1 to 9):** no false clear, no scope leak, no false
  confidence, every missing fact named, no forbidden claim, no fabricated
  citation, authority respected, exact arithmetic, exact part identity.
- **Aggregate gates (10 to 13), each with a small budget:** evidence cited,
  timing stated correctly, no needless escalation, no false alarm.
- **Retrieval gate (14):** candidate recall.
- **Judged by hand:** gates 5 and 11.
- **Exact counts, not rates.** Zero failures in 18 units still allows a
  true failure rate of about 17% ("What the Sample Can Show").

### S1 vs B2 vs B3 (AD 2025-19-13, 18 units)

| Approach | Protected failures per run | False clears | Cost | What it means |
|---|---|---|---|---|
| S1 rules | 0 | 0 | ~$0 | Rules reproduce one reading of the directive, with citations |
| B2, Sonnet 5.5 high (best setting) | 2.0 | 0 | $0.565 per 33-unit run | Asking a model each time is not as good as the rules, and costs per engine |
| B2, other six settings | 1.0 to 9.7 | up to 1.0 per run | $0.024 to $0.443 per run | Lower effort misread paragraph (g) as "no shop visit, no deadline" |
| B3, Opus 5.5 high drafts rules | 10 (all gate 8) | 0 | $0.35 for three runs | 17/17 fields right, but one clause left "unclear": a safe failure |

Source: `writeups/02-evaluated.md`, "Results". More points to know:

- **Instability.** Between identical runs, Haiku changed its answer on 6 to
  11 of 33 units, and Sonnet on 1 to 3.
- **One field.** Changing B3's one field reproduces the reference on all 23
  units B3 scored.
- **Fleet scale.** Re-screening 300 engines against about 20 directives:
  up to about $100 with Sonnet high (an upper estimate), about $0 with rules
  (`evaluation/B2_FULL_CONTEXT.md`, "What It Would Cost at Fleet Scale").
- **Total spend.** Model spend through step 9 was $7.24 over 868 recorded
  calls (`operations/HARDENING.md`, item 6).

### Coverage (all 16 V2500 directives)

- **Pre-registered** before any case, schema change, or prompt
  (`evaluation/coverage/PREREGISTRATION.md`), with six numbered deviations.
- **Cases.** 62 coverage cases (`evaluation/coverage/cases/`), written
  before any model draft. Reference rule records were written by a separate
  agent that never saw the cases.
- **Second-model blind check.**
  - 73 cases, 78 outcomes.
  - 15 field disagreements in 10 outcomes.
  - 1 label changed (cov-055).
  - Same model family.
  (`evaluation/coverage/critique/2026-10-15-label-check.md`)
- **Paired reference runs** on 77 units over 14 directives:
  - v2.0 (blind): 2 of 14 directives pass every mechanical gate, with 2
    false clears.
  - v2.1, interpreter 3, changed after reading the cases (**not blind**): 7
    of 14 pass, with 0 false clears.
  (`evaluation/runs/coverage-reference-v2.*/report.md`)
- **Model drafts: PENDING.** Raw and reviewed scores, the changed-field
  count, and the number of directives evaluated
  (`writeups/03-full-coverage.md` placeholders).
- **Fleet finding.** On the synthetic fleet, four unavailable manufacturer
  documents each leave 195 of 200 engines in review (`demo/fleet-screen.json`,
  `blocking_documents`). The directives print the part number but keep the
  serial list in a bulletin. This is a demo output, not a finding about real
  fleets.

## Limitations, and how to say them

| Limitation | How to say it |
|---|---|
| No users | "Nobody uses it. Fleet records are proprietary, so no operator will upload one. User evidence would be reviewer agreement and observed sessions, and those haven't happened." (`ROADMAP.md`, "User Evidence") |
| No practitioner review | "The independent check is a practitioner review. I deferred it, and the write-ups don't claim it." (issue #9) |
| One author | "The same reader, Claude under my direction, wrote the labels, gates, and rules. A shared misreading passes every gate." (`writeups/02-evaluated.md`) |
| Stand-in review | "I directed Claude to stand in for human review on coverage, and every record says so." (`PREREGISTRATION.md`, "Direction") |
| Small samples | "Exact counts. Zero failures in 18 units still allows about 17%." (`GATES.md`) |
| One engine family | "The evaluated claim is V2500-A5/D5/E5. Discovery covers every AD, but carries no correctness claim." (`ROADMAP.md`, "Corpus Layers") |
| Settings chosen on test set | "B2's effort sweep ran on the scored units, so I report every setting, not just the best." |
| Not-blind 2.1 | "I changed the interpreter after seeing the first run. I report both runs paired and call 2.1 not blind." |
| Unavailable documents | "Manufacturer bulletins are proprietary, so engines that depend on them go to review, named." |
| Untested alerting | "The alert job has been simulated, but it hasn't fired on a real failure yet." (`HARDENING.md`) |

## Likely questions, with model answers

### Product

1. **Who uses it?**
   Nobody yet, and I say so on the page and in the write-ups. Fleet records
   are proprietary, so no operator will hand me one. That is why there is a
   synthetic fleet. What would count as user evidence is reviewer agreement,
   observed sessions, and a time-to-answer comparison (`ROADMAP.md`, "User
   Evidence"). The practitioner review is the next rung, and I deferred it
   (issue #9).

2. **What problem does it solve that maintenance tracking software doesn't?**
   Tracking systems store and track the applicability decision. A person
   still makes it, mostly when the AD arrives (`APPROACH.md`, "The Workflow
   Today"). The pitch is a second check that never tires, re-runs on every
   fleet change, and shows its evidence. That claim is unconfirmed until a
   practitioner says so.

3. **Isn't this just one engine family?**
   Yes, on purpose. The evaluated claim is V2500-A5/D5/E5. Discovery covers
   every FAA AD since 1994, but it makes no correctness claim. Widening
   discovery is cheap. Widening an evaluated claim needs its own fields,
   cases, and gates (`ROADMAP.md`, "Corpus Layers"). Within V2500 I went
   from one directive to all 16 that retrieval finds.

4. **How would you scale to all engine families?**
   - The pipeline stays as it is. Acquisition, sync, retrieval, and the
     interpreter are already family-agnostic, and the sync already reads
     every AD.
   - What scales per directive is a rule record: a model drafts it once, the
     serial guard and schema check it, and a person proofreads it.
   - What scales per family is cases and gates. That is human work, and it
     should be.
   - The real ceiling is access to the manufacturer documents. On the demo
     fleet, unavailable bulletins block more decisions than any reading
     problem does (`demo/fleet-screen.json`, `blocking_documents`).

5. **What's the business?**
   Not analyst salary savings. The value is misses caught, time to answer
   an urgent AD across a fleet, and re-checks that would otherwise not
   happen (`APPROACH.md`, "Why It Matters"). The manual baseline (B0) has
   not been measured. Vendor time-per-AD claims cite no study.

6. **What does a user actually see?**
   The page shows three queues: potentially affected, needs review, and no
   action. Each engine carries its cited paragraphs and the named missing
   facts. A freshness page shows when the corpus last synced. It is a
   screen, not a compliance determination.

### Technical

7. **Why fetch six representations of the same document?**
   They check each other. The PDF is the official version and the XML has
   structure. Live runs found an en dash in PDF identifiers, a neighbouring
   document's number on a shared PDF page, and a page-view counter in the
   API record. Any one of those would have broken a single-source design
   (`writeups/01-reproducible.md`).

8. **How do you know the corpus didn't change under you?**
   Every artifact has a SHA-256 receipt, and generations are immutable. A
   hash change for an existing identity rejects the sync for review instead
   of overwriting (`DISCOVERY_SYNC.md`; `AGENTS.md`, "Data-Lifecycle
   Contract"). Evaluation runs use frozen generations that the sync cannot
   write to.

9. **Walk me through a failed sync.**
   - The candidate is rejected with a receipt, and `active.json` and the
     checkpoint stay put.
   - The attempt is logged.
   - The page says "did not succeed" and lists failures.
   - A GitHub issue opens.
   - After 48 hours without success, the page turns STALE in the browser.
   (`operations/HARDENING.md`, items 2 and 4)

10. **Why no vector search?**
    The pre-registration allowed embeddings only for a miss that identifier
    matching could not reach. Applicability turns on model designations and
    part numbers, and identifier match surfaced every expected in-family
    candidate. Adding a mechanism without a measured failure only adds
    things to get wrong (`evaluation/RETRIEVAL.md`).

11. **What's the hardest bug you found?**
    The scope-reader bug. The sync read "This AD applies to:" and stopped,
    so two V2500 directives were silently filed out of scope. Unit tests
    didn't catch it. Measuring false inclusion against real distractors
    did. Second place: Unicode look-alike serials. A listed hub serial with
    one Cyrillic letter in it was silently cleared (`operations/HARDENING.md`,
    item 4).

12. **How do you test without hitting the network?**
    An autouse fixture fails any test that reaches a real network
    transport. Model calls are recorded, and tests replay saved responses
    (`AGENTS.md`).

13. **How do you handle a malformed engine record?**
    One preflight check runs before every screen. Any malformed record goes
    to `needs_review`, with the bad field paths named. Before the fix, 16 of
    30 damage kinds crashed the screens and four silently cleared
    (`operations/HARDENING.md`, item 4).

14. **How do you stop a model inventing a serial number?**
    The serial guard rejects any serial in a rule record that does not
    appear in the directive's own text. Serial lists held only in
    incorporated material are recorded as unavailable. Engines with a
    matching part number go to review naming that document
    (`PREREGISTRATION.md`, "Rules").

15. **What does it cost to run?**
    The expected cash cost is $0 a year while the repository is public and
    no new evaluation runs are made. Model spend to date is $7.24 over 868
    calls through step 9 (`operations/HARDENING.md`, item 6). The coverage
    plumbing check added $0.1323
    (`evaluation/runs/coverage-plumbing-20261015T194653Z/summary.json`). The
    full drafting run's cost is PENDING.

### ML judgment

16. **Why not just use an LLM?**
    I measured it. On the same 18 units, the best setting (Sonnet 5.5,
    high effort) averaged about 2 protected-gate failures per run; rules
    had 0. Lower settings misread the timing clause in a way that could let
    a listed hub fly past its limit. Answers changed between identical runs:
    Haiku on 6 to 11 of 33 units. And per-engine calls cost money on every
    re-screen (`writeups/02-evaluated.md`).

17. **So where does the model help?**
    Drafting rules once per directive. Opus drafted 17/17 data fields
    right in 3 of 3 repeats. Its one gap was a clause it marked "unclear",
    which is the clause I had to ask the FAA about. A person catches a
    drafting mistake once, not once per engine (`writeups/02-evaluated.md`,
    "What it suggests").

18. **Isn't B3 failing 10 units a bad result?**
    It fails gate 8, and I report it as a failure. But it fails safe: every
    one of those engines went to review, and none was cleared. Changing that
    one field reproduces the hand-written reference on all 23 units. A model
    that flags ambiguity is what you want. One that picked a reading would
    have been confidently wrong, because the FAA's answer matched neither
    grammatical reading (`APPROACH.md`, "The Proposed Workflow").

19. **Who checked your labels?**
    For AD 2025-19-13, Claude wrote and judged them, and I waived re-checking
    on 2026-10-15 (`evaluation/review/OWNER_PACKET.md`). For coverage I
    directed Claude to stand in for review. A second Claude model checked
    the labels blind, and Claude, acting for me, settled each disagreement
    against the text. That is the same model family, so its errors can be
    correlated. It's a consistency check, not independent verification. No
    practitioner has checked them.

20. **How do you avoid overfitting prompts to the test set?**
    - Prompts are frozen and versioned before any scored run.
    - A plumbing check may confirm only the format, and the coverage
      plumbing check deliberately drafted a CFM directive outside the
      evaluation.
    - No labels or rationales go into a prompt.
    - When I found the schema's field descriptions had been written after
      reading the cases, I scrubbed them before freezing and disclosed it as
      deviation 6.
    - I did tune B2's effort setting on the scored units. I disclose that
      and report every setting.

21. **You changed the interpreter after seeing results. Isn't that cheating?**
    It would be if I hid it. I pre-registered that any change would be a
    numbered deviation, reported paired with the blind run. v2.0, which was
    blind, passed 2 of 14 directives with 2 false clears. v2.1, which was
    not blind, passed 7 of 14 with none. The fixes are general (fuller
    citations, reading contradicted operator records), not per-case, and I
    label 2.1 not blind.

22. **What does zero failures in 18 cases actually tell you?**
    Not a rate. By the rule of three, the true failure rate could still be
    about 17%, or about 30% on gate 1's ten units (`GATES.md`, "What the
    Sample Can Show"). It shows agreement with one reading on the hard
    cases I could think of.

23. **Why didn't you build an agent?**
    The roadmap required a recorded trace showing a limitation that depends
    on feedback, which an agent would fix better than a deterministic
    change. None of the four candidates showed up. The remaining hard cases
    need an authority's answer. An agent searching harder would find nothing
    or guess, and a guess can be a false clear
    (`evaluation/AGENT_DECISION.md`). I wrote down what would reopen the
    question.

24. **What would make a directive "evaluated"?**
    It needs at least three cases covering the main outcomes, a completed
    label check with written adjudications, and a reviewed rule record that
    passes every protected gate and stays within every aggregate budget.
    Each record also carries `label_review: claude_stand_in`
    (`PREREGISTRATION.md`). How many of the 16 reached it is PENDING.

### Hostile and reflective

25. **Isn't the fleet fake?**
    The state is synthetic, and I say so everywhere. The shape is real: the
    airframe mix and build years come from 705 U.S. registry aircraft. The
    generation rules were committed before generating and not tuned
    afterwards (`demo/README.md`). The counts are demo outputs of the rules,
    not claims about any airline.

26. **Claude wrote most of this. What did you do?**
    I set the scope and the claim boundary, ordered the roadmap, and made
    the calls on what counts as evidence. Those include freezing gates
    before runs, no prompt tuning on scored cases, and disclosing every
    stand-in review. I also directed the trade-offs, for example finishing
    coverage with Claude standing in rather than claiming a review that
    didn't happen. Every decision with its date is in `ROADMAP.md`,
    "Revisions". *(Make this answer your own. Be specific about which
    decisions were yours.)*

27. **What would you do differently?**
    - Get one practitioner on a call before writing cases, not after. The
      single most valuable input was an FAA engineer's answer that matched
      neither of my readings.
    - Measure the manual baseline (B0) early.
    - Separate who writes the labels from who writes the rules: one author
      for both is the biggest weakness in the evaluation.
    - Treat incorporated documents as the first-class blocker they turned
      out to be.

28. **What's the strongest evidence it works?**
    Be careful here. The strongest evidence is narrow: on 18 frozen units
    for one directive, rules hit every gate, and a model did not. Beyond
    that, the evidence is consistency checks by the same model family, and
    a synthetic fleet. I wouldn't claim more until a practitioner reviews
    it.

29. **Why should I trust any number in your write-ups?**
    Each one names a file, every run is kept, and runs re-score offline
    without calling a model (`make b3-replay`, `make s1-conclude`). The
    gates were frozen before the runs. Limitations come first in each
    write-up.

30. **What happens when the FAA corrects or supersedes a directive?**
    Nothing is replaced in place. Corrections link to their original, and
    supersession is read from the "Affected ADs" paragraph. A superseded
    directive reports `superseded`, and retrieval brings a final's
    corrections with it (`DISCOVERY_SYNC.md`, step 5;
    `evaluation/RETRIEVAL.md`).

## Glossary

General definitions. Where the repository relies on a specific one, the
source is named.

- **AD (airworthiness directive).** A legally binding FAA rule under 14 CFR
  part 39 that requires an inspection, repair, or part change on a product,
  usually by a deadline.
- **NPRM (notice of proposed rulemaking).** The proposed version of an AD,
  published for comment before the final rule. Proposals are not searched
  by the sync (`DISCOVERY_SYNC.md`, step 5).
- **Final rule.** The binding published AD. It has a publication date and
  a later effective date.
- **Effective date.** When the AD comes into force. An AD that is published
  but not yet effective requires no action (gate 7; label check, cov-077).
- **Federal Register / GovInfo.** The U.S. government's daily journal of
  rules, and the Government Publishing Office's official repository (PDF,
  MODS). These are the project's official sources.
- **Docket number.** The rulemaking file identifier. The project joins a
  proposal to its final rule on a shared docket number, labeled as its own
  join (`writeups/01-reproducible.md`).
- **Applicability, paragraph (c).** The paragraph that names the products
  an AD covers. Coverage state is read from it, not the title.
- **Correction / supersession.** A correction fixes a published AD. A
  superseding AD replaces an earlier one. Both are kept as relationships,
  never as overwrites.
- **AMOC (alternative method of compliance).** An FAA-approved way to meet
  an AD other than the one it states. Engine records can carry AMOC claims
  (`amoc_claims`).
- **Incorporated by reference.** An AD makes a manufacturer document, such
  as a service bulletin, legally part of itself without printing it. Those
  documents are often proprietary, and here they are recorded as
  unavailable dependencies.
- **NMSB / SB / SI.** Non-modification service bulletin, service bulletin,
  and service instruction: manufacturer documents. They often hold the
  serial-number lists an AD depends on.
- **P/N, S/N.** Part number, serial number. Gate 9 requires an exact P/N
  and S/N pair.
- **Life-limited part (LLP).** A rotating part, such as a hub, disk, or
  drum, that must be retired at a set number of cycles.
- **CSN (cycles since new).** Flight cycles a part has accumulated since
  manufacture. They differ from the engine's cycles once the part moves
  between engines (`APPROACH.md`, "Why It Matters").
- **Flight cycle.** One takeoff and landing. Gate 8 allows zero tolerance
  on cycle arithmetic.
- **Shop visit.** An engine induction into a maintenance shop for certain
  work. Each AD defines it, and the definition matters. AD 2026-17-03 (h)(3)
  defines it by its induction (label check, seed-013).
- **ALS (airworthiness limitations section).** The part of the instructions
  for continued airworthiness that sets mandatory limits. AD 2025-17-16
  requires revising it within 90 days, which is operator program state
  rather than a part fact.
- **USI / AUSI.** Ultrasonic inspection, and automated ultrasonic
  inspection: ways to find subsurface defects in disks and hubs.
- **HPT / HPC / LPT.** High-pressure turbine, high-pressure compressor,
  low-pressure turbine.
- **V2500-A5 / D5 / E5.** IAE V2500 variants: A5 for the Airbus A319, A320,
  and A321, D5 for the MD-90, and E5 for the C-390. These form the
  evaluation boundary.
- **DRS.** The FAA's Dynamic Regulatory System. Its access is unverified,
  so it is not used (`writeups/01-reproducible.md`).
- **Back-to-birth records, Form 8130-3 / EASA Form 1.** A part's full
  history, and the release certificates that travel with it (`APPROACH.md`,
  "Note: Part History Already Exists").
- **Screening vs compliance determination.** This system screens and
  points at evidence. Only the operator determines and records compliance.
