# Reproducible: Getting the Same FAA Directive Twice

*Checkpoint reached 2026-09-26; written 2026-10-11. This post makes one claim:
the project can acquire an FAA airworthiness directive from official sources
in a way anyone can repeat and check byte for byte. It makes no claim yet
about whether the project reads directives correctly.*

## Why start here

An airworthiness directive (AD) is a legally binding order to inspect, repair,
or replace a part on an aircraft or engine. This project's goal is to tell a
maintenance team which of its engines a new directive affects, and why, with
every answer pointing at the paragraph it rests on.

An answer that cites a paragraph is only as good as the copy of the paragraph
it cites. Directives get corrected, superseded, and republished. The official
API's own records change when the document does not. If the project cannot
say exactly which bytes it read, and show they are the official ones, no
later claim about reading them is checkable. So the first rung was
acquisition, before any reading at all.

## What "reproducible" means here

For one directive thread (the proposal and final rule for AD 2025-19-13, a
quality escape on V2500 engine turbine hubs), the code fetches six official
representations of each document: the Federal Register API record, the XML,
HTML and plain text, and GovInfo's official PDF and metadata. For every
attempt, successful or not, it writes a receipt: where the bytes came from,
when, what role they play, and their SHA-256 hash. It never rewrites what it
fetched.

A run ends in a manifest, which compares the representations expected with
the ones found, and a validation report. A set of documents becomes usable
("eligible for normalization") only when it is complete and every check
passes. The accepted set had 12 of 12 artifacts, re-hashed independently, and
54 of 54 checks passing. Running it again changed nothing, which is the point.

You can check it two ways: run the acquisition yourself and compare hashes,
or download the frozen bytes from the
[release](https://github.com/tanayvenkata/faa-directive-impact/releases/tag/raw-gen-20260926T213233Z-000f808f)
and verify them against `SHA256SUMS`, whose entries match the committed
receipts. Steps are in
[`CHECKPOINT_REPRODUCIBLE.md`](../CHECKPOINT_REPRODUCIBLE.md). The test suite
runs fully offline; a test that tries to reach the network fails.

## What the live sources taught us

None of these were in the design. Each was found by running against the real
sources:

1. **The official PDF prints identifiers with an en dash** (`2025–10764`), so
   the first run failed its own identity check. The fix accepts typographic
   dashes but still requires the full `FR Doc.` line.
2. **One PDF page can carry a neighbouring document's identifier.** Matching
   the bare number would have accepted the wrong evidence.
3. **The API record changes when the document does not.** It includes a
   page-view counter. Comparing raw hashes would report a "new version" on
   every run, so versions ignore that one named field while the exact bytes
   are still kept.
4. **HTML paragraph IDs are positional** (`p-1`…`p-46`) and would renumber if
   a paragraph were inserted, so they cannot anchor evidence.
5. **The paragraph listing incorporated material moves**: `(l)` in this
   thread, `(k)` in another directive. It is found by heading, not by letter.
6. **The API does not link a proposal to its final rule.** The project joins
   them on their shared docket number and labels the link as its own join, not
   as something the source asserts.

## What this does not claim

- Nothing about reading directives correctly, applicability, or fleet
  impact. Those come with later rungs and their own evaluations.
- One thread, one engine family. Images and manufacturer documents that
  directives incorporate were exercised offline and in one scratch run, not in
  the accepted set; manufacturer service bulletins are proprietary and are
  recorded only as unavailable dependencies.
- No corroboration against the FAA's own directive system (DRS), whose access
  is unverified.
- No practitioner has reviewed any of it yet.

## What came after

The rungs since this one (evaluation cases with frozen pass/fail gates, a
rules baseline, and model comparisons) are in the
[repository](https://github.com/tanayvenkata/faa-directive-impact) and in the
next write-up, [*Evaluated*](02-evaluated.md).
