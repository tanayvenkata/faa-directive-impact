# Post-run note (2026-10-07)

This run used prompt version 1 (`b73f8e333bee`) and is kept as scored. The
same answer-format problems as the version 1 Haiku run dominate gates 6, 10,
and part of 4 and 9 (citation document numbers with extra text, paths mixed
with prose, no way to omit a listed S/N); see that run's note and prompt
version 2 (`e0a54c1578a5`).

Content findings that are not format:

- **Deadline counter left empty** on seed-006, 007, 008, 023/2025-18469, 026,
  027, and 028 (gate 8). The answers treat the latest removal point as not
  computable because a shop visit could come first; the labels compute the
  latest allowed counter.
- **seed-019 arithmetic (gate 8):** cycles remaining -150 instead of -190,
  computed from the hub's cycles at the effective date instead of now.
- **seed-013 (gate 1, false clear)** and **seed-014 (gate 3, settled answer
  on an unadjudicated expert question)** on AD 2026-17-03.
- **seed-018 (gate 13, false alarm):** action stated for a directive not yet
  in force on the question date.
- **seed-022/2021-14268 (gate 3):** a settled answer where the expected
  answer is `needs_review`.
