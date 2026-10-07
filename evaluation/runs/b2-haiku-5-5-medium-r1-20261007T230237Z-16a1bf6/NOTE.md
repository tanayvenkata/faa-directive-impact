# Post-run note (2026-10-07)

This run used prompt version 1 (`b73f8e333bee`). Its report is kept as
scored and is not re-scored.

- **Gates 6 and 10 failures are dominated by an answer-format problem.** The
  model wrote the citation `document` as, for example, "Federal Register
  2025-18469 (AD 2025-19-13)" instead of "2025-18469", so every citation read
  as a document that was not given. The cited paragraphs themselves exist.
- **Gate 4 failures are partly format.** The model put a record path and an
  explanation in one string, so exact path matching failed even when the
  right fact was named.
- **Gate 9 on non-S1 directives** flagged matches for directives that list a
  part number only, because version 1 had no way to say "no listed S/N".

Version 2 (`e0a54c1578a5`) fixes the answer format only: the document number
alone (enforced by a schema pattern), missing facts split into
`record_path` and `description`, and a nullable listed S/N. The plumbing check
now also checks those conventions; version 1's checked structure only.

Two version-1 failures are content, not format, and stand:

- **seed-013 (gate 1, false clear):** an engine with affected HPC blades,
  expected `action_required_on_event`, was cleared.
- **seed-022/2021-14268 (gate 3, false confidence):** a unit whose expected
  answer is `needs_review` received a settled answer.
