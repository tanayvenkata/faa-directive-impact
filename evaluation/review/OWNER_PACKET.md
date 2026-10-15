# Owner Packet

> **Waived 2026-10-15.** The project owner chose to finish the episode
> without these sign-offs: items 1–5 are not done, and item 7 is deferred.
> The results docs and `writeups/02-evaluated.md` say which judgments are
> Claude's alone and that proofreading time is not measured. No sheet below
> was filled in on the owner's behalf. The packet is kept as-is in case a
> person does these checks later; the blind-proofread order no longer
> applies, because the owner has seen the results.

Everything that waits on the project owner, in the order to do it. Each item
is a sign-off that Claude cannot give on its own work. About 2 hours in all.

**Do item 1 first, blind.** Until it is done, do not open
`writeups/02-evaluated.md`, `evaluation/B3_RULE_EXTRACTION.md`,
`evaluation/b3-summary.md`, `evaluation/b3/reference/`, or
`evaluation/review/b3-opus-r1/judgments.yaml`. In a B3 run directory, open
only `proofread.md` and `extractions/`. Nothing in this packet states a B3
result.

Paths below are from the repository root; run commands from there.

| # | Item | Where | Time | Why it needs you |
|---|---|---|---|---|
| 1 | Proofread B3's drafted rules with a timer, **before reading any B3 results** | `evaluation/review/b3-opus-r1/README.md` part 1; fill in `proofread.yaml` beside it | 30–45 min | Proofreading minutes per AD is a B3 measure; it means nothing if Claude proofreads its own drafts |
| 2 | Judge B3's drafted ambiguities | same README, part 2; `judgments.yaml` beside it | 10 min | Whether an ambiguity is real is a reading of the text, and Claude wrote the reference it is scored against |
| 3 | Confirm or dispute the AD 2026-17-03 labels and reference record | same README, part 3 (`judgments.yaml`): `evaluation/seed/cases/seed-011.yaml` to `seed-014.yaml` and `seed-023.yaml` (its 2026-16954 outcome), and `evaluation/b3/reference/2026-16954.json` | 15 min | They are Claude drafts (`labeled_by: claude-draft`); B3's AD 2026-17-03 results stay provisional until then |
| 4 | Confirm S1's hand review (gates 5 and 11) | Read `evaluation/runs/s1-20261006T223638Z-6a301b1/hand-review.md`. In `hand-review.yaml` beside it, change any `result` you disagree with, set `reviewer:` to your name and `reviewer_confirmed: true`, then run `make s1-conclude RUN=evaluation/runs/s1-20261006T223638Z-6a301b1` | 15 min | S1's go decision is provisional until you do |
| 5 | Confirm B2's first-pass hand review | `evaluation/review/b2-sonnet-r1/README.md`; fill in `review.yaml` | 20 min | Same reason, for the B2 comparison |
| 6 | ~~Turn on the daily sync~~ Done 2026-10-11 under your delegation: Pages enabled, first run promoted | <https://tanayvenkata.github.io/faa-directive-impact/> | — | — |
| 6a | E3 is decided (double read, under your delegation). Do the person's read of the four image tables when the transcription tool exists | [`../E3_IMAGE_FIGURES.md`](../E3_IMAGE_FIGURES.md) | 15 min, later | A model reading twice is not a double read |
| 7 | Attempt one practitioner review | issue #9; message and brief in [`PRACTITIONER_BRIEF.md`](PRACTITIONER_BRIEF.md) | 10 min to send | An exit criterion for the episode. Do not re-ask the AD 2025-19-13 engineer; batch questions to anyone new |

## What happens after each item

- **Item 4** is folded in by the command itself: it rewrites the run's
  `verdict.md` and `verdict.json`. If every result stays as Claude marked it,
  the decision stays **go** and is no longer provisional. If you mark any
  gate 5 `present` or gate 11 `contradicts`, that gate and the decision
  become `unresolved` until the label is checked under "Disputed Labels".
  This was checked on a copy of the run, not the run itself.
- **Items 1–3 and 5** have no command. Commit the filled-in sheets, then ask
  Claude in a new session to fold them into `evaluation/B3_RULE_EXTRACTION.md`
  and `evaluation/B2_FULL_CONTEXT.md` and to drop the provisional marks from
  `writeups/02-evaluated.md`. Nothing is re-run and no model is called.
- **Item 7**: record the attempt in issue #9 even if nobody agrees. Answers
  go under `evaluation/seed/adjudication/` (see the brief).

Disagreements with a label go through "Disputed Labels" in
[`../GATES.md`](../GATES.md); nothing here edits a gate or a case to make a
run pass.
