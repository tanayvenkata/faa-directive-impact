# Demo Fleet

A seeded, synthetic fleet of 200 IAE V2500-A5/D5/E5 engines for the fleet
view (`site/fleet/`, published with the freshness page). It is presentation
data, not evaluation data.

- **`fleet.json`**: 178 generated engines (89 aircraft, two engines each) plus
  the 22 seed-case assets for AD 2025-19-13 and AD 2026-17-03, embedded
  unchanged and tagged with their case id. The seed cases are still scored
  only by the evaluation runs. Identifiers are `SYN-` prefixed, except six hub
  serial numbers taken from table 1 of AD 2025-19-13, which must match the
  directive to be found. Of the 178 generated engines, 32 have an unknown hub
  serial or cycle count, 29 have no usable blade-set part number, and 14 have
  a recent shop visit, so `needs_review` comes from missing data.
- **`fleet-screen.json`**: each engine screened against both directives, and
  two releases of the rule set: AD 2025-19-13 alone, then with AD 2026-17-03
  added. An engine's queue in a release is the most urgent across its
  directives.

| Directive | Coverage | Screener |
|---|---|---|
| AD 2025-19-13 | `evaluated` | S1 rules on the normalized record kept with the S1 run |
| AD 2026-17-03 | `not_yet_evaluated` | Rule interpreter on the hand-written reference rule record (`evaluation/b3/reference/2026-16954.json`); its labels are Claude drafts no person has confirmed |

Both files are generated offline by `make fleet-build` from committed inputs
only, and a test checks that regenerating gives identical bytes. CI renders
the page (`make fleet-site`) and never regenerates the fleet.

Known simplifications: realistic airframe mix and cycle rates are judgment,
not operator data; the embedded seed engines keep their own snapshot dates,
and listed hub serials repeat across seed cases and generated engines,
which a real fleet would not show; nobody
in aviation maintenance has checked the fleet's realism (issue #20).
