# Rollback Drill Receipt, 2026-10-15

ROADMAP step 9. Claude ran this drill. It used a local copy of the live
discovery state and pushed nothing. Nobody else watched or repeated it.

## What Was Run

From the repository root, on branch `step9-harden`:

```bash
operations/drills/rollback_drill.sh 90ecb75925e89700b5e0bf37e7a0b9b796882406 data/drill
```

The script ([`rollback_drill.sh`](rollback_drill.sh)) does the following:

1. Copies the `discovery/` folder from the `discovery-state` commit given into
   the git-ignored `data/drill/`. It uses `git archive`, so it creates no
   branch and no worktree, and there is nothing to push.
2. Runs `faa-directive-impact discovery-rollback` with no target.
3. Runs `faa-directive-impact discovery-rollback --to <original>`.
4. After each step, builds the freshness page and checks the "Active
   generation" row.

The full output is in
[`2026-10-15-rollback-drill.log`](2026-10-15-rollback-drill.log).

## State Used

| Item | Value |
|---|---|
| `discovery-state` commit | `90ecb75925e89700b5e0bf37e7a0b9b796882406` ("discovery: state after run 38775794470", 2026-10-15T17:15:40Z) |
| Promotion receipts | 2 |
| Active before the drill | `gen-20261014T171827Z-398619f9`, checkpoint 2026-10-14 |
| Its predecessor | `gen-20261011T165831Z-6cea777a`, the 1994 backfill, checkpoint 2026-10-13 |

## Results (UTC)

| Time | Step | Active generation | Page check |
|---|---|---|---|
| 18:04:31 | Before | `gen-20261014T171827Z-398619f9` | Shows it; 1 new directive in the active generation |
| 18:04:34 | Rollback (receipt `decision-20261015T180434Z-14899a4c`) | `gen-20261011T165831Z-6cea777a`, checkpoint 2026-10-13 | Shows it; 12,932 new (the backfill); no rollback target listed |
| 18:04:37 | Restore with `--to gen-20261014T171827Z-398619f9` (receipt `decision-20261015T180437Z-41707195`) | `gen-20261014T171827Z-398619f9`, checkpoint 2026-10-14 | Shows it; byte-identical to the page from before the drill |

The drill passed, with exit status 0. Each `discovery-rollback` wrote a
`rollback` receipt naming both generations, as expected. Each run took about
two seconds; most of that was reading the 1994 backfill snapshot.

## What It Shows, and What It Does Not

- The command works on the real 13,000-directive state, not only on test
  fixtures.
- The page follows the active pointer.
- A restore is an ordinary rollback to a generation that was promoted before,
  so recovering from a mistaken rollback needs no special tool.
- The pages in this drill were built with the code on `main` at the time.
  Since then the branch has added an "Activated by" row, which names the
  receipt (promotion or rollback) that made the generation active. Before
  that row, a rolled-back page did not say that a rollback had happened.
- The drill did not publish a rollback. Publishing one also needs the copy
  and commit back to `discovery-state` described in DISCOVERY_SYNC.md,
  "Incidents". That path was not exercised against the live branch.

The same sequence runs offline in
`tests/discovery/test_rollback_drill.py`, which ends with a sync that reports
`no_change` on the restored generation.
