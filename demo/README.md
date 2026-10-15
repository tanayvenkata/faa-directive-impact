# Demo Fleet

A seeded, synthetic fleet of 200 IAE V2500-A5/D5 engines for the fleet view
(`site/fleet/`, published with the freshness page). It is presentation data,
not evaluation data. Its **shape** comes from the real U.S. population in the
FAA Aircraft Registry (`registry-v2500.json`, aggregate counts only); its
**state** (serial numbers, cycles, parts, events, operator records) is
synthetic.

## Pre-Declared Generation Rules

Fleet version 2. Everything in this section was written and committed before
the version 2 fleet was generated, and is not tuned to the counts it produces.
The numbers are judgment, not operator data; nobody in aviation maintenance
has checked them (issue #20).

### Population

- **Size.** 100 aircraft, two engines each. The seed-case assets for
  AD 2025-19-13 and AD 2026-17-03 on supported engine models are embedded
  unchanged and tagged `evaluation_case`; they take the place of
  `ceil(seed engines / 2)` aircraft, so the generated part is
  `100 - ceil(seed engines / 2)` aircraft (90 for the 20 seed engines today)
  and the total is 200.
- **Airframes.** The generated aircraft are allocated to registry airframe
  models in proportion to `by_airframe` by largest remainder, so a type with
  under 1% of the registry (MD-90-30, 5 of 705) still gets its rounded share
  instead of a coin flip. Within each airframe the build year is drawn with
  the registry's `by_airframe_year` weights over known years; the single
  `unknown`-year row (one A319-132) is left out of the year draw. The engine
  variant is the airframe's `variant_by_airframe`. The registry holds no
  V2527M-A5 or V2531-E5 (C-390) aircraft, so those variants appear only
  through the embedded seed engines.
- **Engine serial numbers.** Real format, synthetic values. A5 engines get
  V10002 to V17999 in build-date order (linear in build date from 1993 to
  2015, jitter of up to 150 serials); D5 engines get V20002 to V20400 the
  same way from 1994 to 2001. Any serial printed anywhere in the frozen
  retrieval corpus (`evaluation/retrieval/corpus.json` identifiers: the
  AD 2019-18-01 engine list, every range bound) is skipped, so no invented
  state attaches to an engine a directive names. Seed engines keep their
  `SYN-V2500-` serials, which no serial range can place; on the
  serial-range directives they go to review for that reason.
- **Cycles.** Engine flight cycles accrue linearly from the build date at the
  airframe's rate: A319 1,800, A320 1,700, A321 1,500, MD-90 1,100 cycles a
  year, each engine scaled by a uniform factor in 0.85 to 1.15. Snapshot
  2026-10-12. Each engine has `engine_cycle_readings` at the snapshot and at
  the effective date of every in-scope directive on or after its build date.

### Shop Visits and Parts

- **Shop visits.** First at 14,000 to 20,000 engine cycles, then every 11,000
  to 16,000 (uniform). Every shop visit since 2012-01-01 is recorded as a
  `shop_visit_induction` event with its engine cycles, and the operator
  asserts it qualifies as an engine shop visit (`yes`) for every directive
  that defines one (AD 2016-18-10, 2019-16-01, 2021-11-15, 2024-11-03,
  2025-19-13, 2026-17-03).
- **Recent inductions.** As in version 1, 8% of generated engines are in the
  shop now: inducted 1 to 17 days before the snapshot, asserted to qualify
  `yes` with probability 2/3 and `unknown` otherwise.
- **Life-limited parts.** Lives (judgment): HPT 1st- and 2nd-stage hubs
  20,000 cycles, HPC stage 3 to 8 drum 20,000, LPT stage-6 disk 25,000, HPT
  air seals and ring plate 15,000. At each shop visit a part that would pass
  its life before the next one is replaced: new (0 cycles) 60% of the time,
  a used serviceable part (2,000 to 10,000 cycles) 40%. A part's cycles since
  new therefore differ from the engine's once it has been replaced. Each part
  records `installed_at` and `cycles_since_new_readings` at every in-scope
  effective date after it was installed in this engine (never before: a
  reading from another engine would mis-time a deadline).
- **Part numbers.** Directive-named P/Ns where the directives read them:
  hubs 2A5001 and 2A4802 (serials `PKLBX` plus five digits), LPT stage-6
  disk 3A2996 on A5 engines (serials `MAPX` plus five digits), the D5 No. 4
  bearing internal and external scavenge tubes 2A2074-01 and 6A5254. HPT
  1st- and 2nd-stage air seals and the 2nd-stage ring plate carry the
  AD 2017-14-07 P/Ns (2A3423, 2A4157, 2A3437) when installed before that
  directive took effect (2017-08-21), and a later synthetic P/N
  (`SYN-` prefixed) when installed after. The HPC stage 3 to 8 drum has a
  synthetic P/N, since no directive prints one. Every synthetic identifier is
  checked against the corpus identifiers.
- **HPC stage-3 blade set** (AD 2026-17-03), as in version 1: 6% have no row,
  7% an unknown P/N, 32% an affected P/N (6A8353, 6A8688), the rest an
  eligible P/N.
- **Unknown fields.** Engine serial number unknown 2%; each hub serial
  unknown 4% and its cycles unknown 3%; each other tracked part (drum, LPT
  disk, air seals, ring plate) serial unknown 2% and cycles unknown 3%.
- **Planted listed parts.** Five AD 2025-19-13 table 1 hubs (every row but
  the 100-cycle hub, as in version 1), installed before its effective date,
  150 to 2,000 cycles below their limits, on engines with no shop visit since
  the effective date. These are the only directive-printed serials in the
  generated fleet, and a test asserts it.

### Operator Records

Every generated engine has `operator.air_carrier_operation: yes`. For each
in-scope directive whose applicable models include the engine's model, the
engine has at most one `ad_records` entry, drawn once per engine and
directive:

| Draw | Recorded status |
|---|---|
| 6% | No record |
| 4% | `open` |
| 90% | The expected status below |

Expected status:

- `not_applicable` when the engine's serial number is outside the
  directive's own serial condition (AD 2012-09-09, 2013-07-10, 2015-10-04,
  2019-18-01).
- `recurring` for the repeat-inspection directives (AD 2012-09-09,
  2013-07-10, 2015-10-04, 2019-16-01).
- For AD 2025-19-13 and AD 2026-17-03, whose action waits on the next shop
  visit: `open` when a listed hub or an affected or unknown blade P/N is
  installed, otherwise `not_applicable`. No record ever says `complied`
  while a part the directive names for removal is still installed.
- `complied` otherwise.

AD 2025-17-16 (revise the ALS) is operator program state, so it is drawn
once per aircraft and both engines share it, together with
`operator.maintenance_program_revision`: a stated revision for `complied`, a
statement that it is not yet incorporated for `open`, and no field when
there is no record.

## What Version 2 Produced

Reported after generation; the rules above were not changed after seeing it.

- **Composition.** 90 generated aircraft: A319-131 7, A319-132 8, A320-232
  36, A320-233 3, A321-231 35, A321-232 0, MD-90-30 1 (registry 55, 60, 286,
  22, 275, 2, 5 of 705). Plus 20 seed engines (including V2527M-A5,
  V2531-E5, and D5 cases).
- **State.** 231 shop-visit events (14 engines in the shop now); 78 of 540
  air seals and ring plates still carry an AD 2017-14-07 P/N; 6 unknown
  engine serials, 30 unknown part serials, 31 unknown part cycles; 2,362
  operator records (1,451 complied, 563 not applicable, 192 recurring, 156
  open).
- **Screens.** Every in-scope directive's reference record runs on every
  engine; only AD 2025-19-13 sets the queues (15 potentially affected, 19
  needs review, 166 no action). Per-directive outcome counts are in
  `fleet-screen.json` under `directives[].outcomes`.
- **What blocks decisions.** The unavailable service documents dominate:
  IAE NMSB V2500-ENG-72-0713 and -0720 and P&W SI 112F-21 and 114F-21 each
  leave 195 engines in review, NMSB -0661 193. The ALS directive
  (AD 2025-17-16) goes to review for 160 engines because interpreter 3 does
  not read the free-text program revision as proof; that is the
  interpreter's stated rule, not a data gap.
- **Size.** `fleet-screen.json` is about 17 MB, most of it repeated
  citations; the page stores each citation once (about 3 MB of HTML).

## Files

- **`fleet.json`**: the generated engines plus the embedded seed engines.
- **`fleet-screen.json`**: for each engine, the candidate directives found by
  the step 7 retriever ([`../evaluation/RETRIEVAL.md`](../evaluation/RETRIEVAL.md))
  over the frozen retrieval corpus as of the engine's snapshot date, and a
  screen of each candidate final rule; per directive and fleet-wide, the
  missing facts that leave engines in review and the unavailable documents
  that block them.

Both files are generated offline by `make fleet-build` from committed inputs
only, and a test checks that regenerating gives identical bytes. CI renders
the page (`make fleet-site`) and never regenerates the fleet.
