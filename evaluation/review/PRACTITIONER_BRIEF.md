# Practitioner Review Brief (issue #9)

For the owner to send to one person with aviation-maintenance or
directive-compliance experience. Ask once, with everything batched. Do not
contact the FAA engineer named in AD 2025-19-13 and AD 2026-17-03; that
engineer has already been asked twice.

## Outreach message (paste-ready, edit freely)

> Hi [name] — I'm building an open-source tool that screens engines against
> FAA airworthiness directives (V2500 family) and shows which paragraph each
> answer rests on. It's a portfolio project, not a product, and it never
> claims compliance. Would you spare 30–45 minutes to sanity-check how it
> reads two directives (AD 2025-19-13 and AD 2026-17-03)? There are seven
> specific questions where the text is ambiguous, plus a look at whether my
> made-up engine records carry fields a real operator would have. Happy to
> credit you by role, or not at all, whichever you prefer.

## What the reviewer gets

1. **The questions:**
   [`../seed/REVIEWER_QUESTIONS.md`](../seed/REVIEWER_QUESTIONS.md), items 1–5
   (interpretation and realism). Each names the test cases it settles.
2. **Two worked cases to react to:** seed-014 (AD 2026-17-03, a shop visit
   with no blade removed) and seed-005 (AD 2025-19-13, a shop visit inside
   the 100-cycle window). Show the case, the expected answer, and the
   paragraph cited; ask "would you have said the same?"
3. **One synthetic engine record** (any seed case's `asset_snapshot`), to ask
   whether the fields match what an operator's records hold.

## What to record afterwards

- Reviewer role and qualifications, only with their permission.
- Each answer, by question number, in a new file under
  `evaluation/seed/adjudication/` (informal correspondence is labeled as
  such, as with `faa-informal-2026-10-05`).
- Label changes go through "Disputed Labels" in `../GATES.md`.
- If nobody agrees to review, record the attempt in issue #9; an attempt
  meets the episode exit bar (ROADMAP "Publishing and Exit"). The public
  claim then stays at *Evaluated* and cannot reach *Practitioner-reviewed*,
  the next rung of the series claim ladder, until a review happens.
