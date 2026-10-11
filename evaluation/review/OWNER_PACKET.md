# Owner Packet

Everything that waits on the project owner, in the order to do it. Each item
is a sign-off that Claude cannot give on its own work. About 2 hours in all.

| # | Item | Where | Time | Why it needs you |
|---|---|---|---|---|
| 1 | Proofread B3's drafted rules with a timer, **before reading any B3 results** | [`b3-opus-r1/`](b3-opus-r1/) part 1 | 30–45 min | Proofreading minutes per AD is a B3 measure; it means nothing if Claude proofreads its own drafts |
| 2 | Judge B3's drafted ambiguities | [`b3-opus-r1/`](b3-opus-r1/) part 2 | 10 min | Whether an ambiguity is real is a reading of the text, and Claude wrote the reference it is scored against |
| 3 | Confirm or dispute the AD 2026-17-03 labels and reference record | [`b3-opus-r1/proofread.yaml`](b3-opus-r1/proofread.yaml) part 3; `seed/cases/seed-011…014, 023` | 15 min | They are Claude drafts (`labeled_by: claude-draft`); B3's AD 2026-17-03 results stay provisional until then |
| 4 | Confirm S1's hand review (gates 5 and 11) | `runs/s1-20261006T223638Z-6a301b1/hand-review.yaml`, set `reviewer_confirmed: true`, then `make s1-conclude RUN=evaluation/runs/s1-20261006T223638Z-6a301b1` | 15 min | S1's go decision is provisional until you do |
| 5 | Confirm B2's first-pass hand review | [`b2-sonnet-r1/`](b2-sonnet-r1/) | 20 min | Same reason, for the B2 comparison |
| 6 | Decide whether to turn on the daily sync on GitHub (Pages and the scheduled workflow) | `DISCOVERY_SYNC.md` once the step-6 branch lands | 5 min | It publishes a public page and runs on a schedule from your account |
| 7 | Attempt one practitioner review | issue #9 | — | An exit criterion for the episode. Do not re-ask the AD 2025-19-13 engineer; batch questions to anyone new |

Disagreements with a label go through "Disputed Labels" in
[`../GATES.md`](../GATES.md); nothing here edits a gate or a case to make a
run pass.
