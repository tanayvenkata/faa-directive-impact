# Operations Hardening

This note records ROADMAP step 9, done on 2026-10-15. It covers seven
items. Each one names its artifact, what was verified and how, and what
is still missing. Claude did all of the work and ran every check. No person
reviewed or repeated any of it; the owner waived human review for this step.

The runbook is in [`DISCOVERY_SYNC.md`, "Incidents"](../DISCOVERY_SYNC.md#incidents).

## 1. Scheduled-Workflow Inactivity

**What GitHub says.** These are quotes from docs.github.com, fetched
2026-10-15:

- From [Disabling and enabling a
  workflow](https://docs.github.com/en/actions/how-tos/manage-workflow-runs/disable-and-enable-workflows):
  "In a public repository, scheduled workflows are automatically disabled
  when no repository activity has occurred in 60 days." The page does not
  define "repository activity".
- From [Events that trigger
  workflows](https://docs.github.com/en/actions/reference/workflows-and-actions/events-that-trigger-workflows),
  `schedule`: "Scheduled workflows will only run on the default branch."
  The same section says "The `schedule` event can be delayed during periods
  of high loads of GitHub Actions workflow runs", and "If the load is
  sufficiently high enough, some queued jobs may be dropped."
- From [GITHUB_TOKEN](https://docs.github.com/en/actions/concepts/security/github_token):
  "events triggered by the `GITHUB_TOKEN` will not create a new workflow
  run" (except `workflow_dispatch` and `repository_dispatch`). This page
  says nothing about scheduled workflows or inactivity.

**Risk.** It is real. The workflow pushes only to `discovery-state` with
`GITHUB_TOKEN`, and no page says whether such pushes count as activity.
Without a commit to `main`, the schedule may stop after 60 days.

**Guard.** Two changes in
[`.github/workflows/discovery-sync.yml`](../.github/workflows/discovery-sync.yml):

- The `sync` job measures how many days ago the checked-out commit was made.
  A scheduled run checks out the latest commit on `main`.
- From day 45, the `alert` job opens, or comments on, the issue "Scheduled
  sync at risk: no commit on main for 45 days". The issue quotes the
  documentation above and says how to re-enable the workflow. A later run
  that sees a newer commit closes it.

The guard does not claim that any action resets the 60-day clock. The STALE
banner (48 hours) remains the last line of defense. If the schedule is
already disabled, no run happens, so no issue can be opened. That case is
visible only on the page.

**Verified.**
- `actionlint` 1.7.12 reports no problems.
- The alert script was extracted from the workflow and run with a stub `gh`
  in six scenarios, including the case where 50 days have passed: it opened
  the issue.

**Gap.** The guard has not run on GitHub. The warning fires only while runs
still happen, and it cannot detect a schedule that GitHub has already
disabled.

## 2. Loud Failure

**Artifact.** The `alert` job in the workflow:

- It has `needs: [sync, deploy]`, `if: always()`, and only
  `permissions: issues: write`.
- It makes no checkout, uses no third-party action, and calls only the `gh`
  CLI preinstalled on the runner.
- It raises an alert when either job's result is anything but `success`.
  That includes `failure`, `cancelled`, a timeout, and `skipped`.
- It finds the open issue **"Discovery sync failing"** by exact title
  through the list API, comments on it if it exists, and otherwise opens
  it. So there is never more than one open failure issue.
- It closes the issue after the first run in which both jobs succeed.
- The top-level workflow `permissions` is now `{}`, so no job inherits
  anything.

The freshness page's STALE banner (48 hours, computed in the browser) is
unchanged. The page still deploys after a failed sync.

**Verified.** The same stub-`gh` simulation covered six scenarios:

| Scenario | Action the script took |
|---|---|
| Success, no issue open | Nothing |
| Success, issue open | Closed the issue with a comment |
| Failure, no issue open | Opened an issue |
| Failure, issue open | Commented on the issue; opened no second one |
| `sync` cancelled, `deploy` skipped | Opened an issue |
| 50 days without a commit | Opened the inactivity issue |

**Gap.** The job has not run on GitHub against a real failure. The first
real test is the first failure after this merges.

## 3. Rollback Drill

**Artifacts.**

- [`operations/drills/rollback_drill.sh`](drills/rollback_drill.sh), run as
  `make discovery-drill`.
- The receipt
  [`operations/drills/2026-10-15-rollback-drill.md`](drills/2026-10-15-rollback-drill.md)
  and its log
  [`2026-10-15-rollback-drill.log`](drills/2026-10-15-rollback-drill.log).
- The offline test
  [`tests/discovery/test_rollback_drill.py`](../tests/discovery/test_rollback_drill.py).

**Verified.** The drill ran on a `git archive` copy of the live
`discovery-state` commit `90ecb75`, placed in the git-ignored `data/drill/`.
Nothing was pushed.

- The rollback moved the active generation from
  `gen-20261014T171827Z-398619f9` to `gen-20261011T165831Z-6cea777a`. The
  checkpoint moved from 2026-10-14 back to 2026-10-13, and the page showed
  the backfill generation.
- The restore, `--to gen-20261014T171827Z-398619f9`, returned to the
  original generation. The page was byte-identical to the one built before
  the drill.

The new test runs the same sequence offline: promote twice, roll back,
check the page, restore by id, check the page again. It then syncs and
expects `no_change`. The existing rollback test covered neither the
restore-by-id nor the page.

**Found.** Before this step, the page did not say that a rollback had
happened. It now has an "Activated by" row naming the promotion or rollback
receipt.

**Gap.** Publishing a rollback means committing to `discovery-state`. The
commands are in the runbook, but that path was not run against the live
branch.

## 4. Hostile Input

### Federal Register responses

The tests are in
[`tests/discovery/test_hostile_input.py`](../tests/discovery/test_hostile_input.py).
They cover 16 malformed search bodies plus an oversized page. Each test
syncs once with good data, then once with the hostile response, and checks
all of the following:

- the outcome is `rejected`;
- a rejection receipt with reasons exists;
- the active generation and checkpoint are unchanged;
- the attempt is logged;
- the page shows "did not succeed" and lists the failures.

The bodies were: not JSON (an HTML error page); truncated JSON; an empty
body; an array; `count` as a string, a boolean, or a negative number; a
`count` that disagrees with the results; `results` that is not a list; a
result that is not an object; a numeric document number or title; numeric
docket identifiers; objects in `corrections`; a malformed date; and an
unexpected document type.

Bugs found and fixed, each now covered by a test that failed before the
fix:

1. **`"count": true` was accepted** as the integer 1. In Python, `bool` is a
   subclass of `int`. Now a boolean or negative count is refused.
2. **Wrong-typed entry fields crashed the sync** with outcome `error`, not a
   rejection. Two cases: objects in `corrections`, which raised `TypeError`
   from `set()`, and numbers in `docket_ids`. Now every requested field is
   type-checked in `discovery/search.py`, so the problem becomes a
   rejection with a receipt. Before merging, all 12,962 live entries in the
   active generation were checked against the new type rules, and none
   failed.
3. **No size limit.** A search page was streamed to disk and parsed whole,
   however large. `RepresentationRequest.max_bytes` is now checked while the
   page streams, and search pages are capped at 16 MiB. The largest live
   page was 382,095 bytes (1,000 results, from the `discovery-state`
   receipts), so the cap is about 40 times that. The refused bytes are not
   kept.

### Freshness page

1. **`javascript:` links.** A search entry's `html_url` was escaped, but
   escaping does not neutralize a `javascript:` URL in an `href`. The page
   now links only `https://www.federalregister.gov/` URLs; any other value
   is shown as text.
2. **Titles and failure messages.** HTML in a directive title, and in a
   failure message (an HTML document number), renders as text. The tests
   check for this. Escaping was already correct.
3. **Abstracts.** The search never requests abstracts (`SEARCH_FIELDS`), and
   the page never renders them, so there is nothing to test.

### Engine records fed to both screens

The tests are in
[`tests/impact/test_hostile_engine_records.py`](../tests/impact/test_hostile_engine_records.py).
They apply 30 kinds of damage, each to an engine with a matched hub and to
a clear engine, then run every record through S1 (`screen`) and the
interpreter on both reference rule records (`screen_rules`).

The damage covered: missing or wrong-typed `engine`, `engine_model`,
`installed_components`, `events`, `amoc_claims`, and `ad_records`; null,
numeric, or empty part and serial numbers; a look-alike serial number
(Cyrillic or fullwidth characters); a duplicated position; boolean,
negative, infinite, or word cycle counts; malformed dates; and an engine
model written with a fullwidth letter or an en dash.

Before the fix, the original code was run on the same records, with these
results:

- **It crashed** (`KeyError`, `TypeError`, `AttributeError`, or
  `ValueError`) on 16 of the 30 kinds of damage.
- **It cleared silently** in four ways:
  - A matched hub followed by an unlisted record for the same position went
    to `no_action_triggered`. The dict kept only the last record.
  - A listed serial number with one Cyrillic or fullwidth character went to
    `no_action_triggered`.
  - An empty, numeric, en-dash, or fullwidth engine model went to
    `outside_supported_scope`, which is the no-action queue.
  - On a clear engine, a null or numeric part number, an infinite or word
    cycle count, and malformed readings all stayed `no_action_triggered`.
- **It crashed on a valid record.** S1 read `asset["events"]`, which the
  seed schema makes optional, so any in-force engine without `events`
  crashed.

The fix is one preflight check, `engine_record_problems` in
`impact/hpt_hub_rules.py`, which both screens call first. A malformed
record returns `needs_review`, with the bad field paths in `missing_facts`
and a summary that says the record is malformed. Extra fields are allowed.
S1 now reads `events` with a default. The tests check both directions:

- every damaged record goes to `needs_review` in all three screens;
- every seed case and every engine in the 200-engine demo fleet passes the
  check. Huge cycle counts (10^30) and Unicode in free-text fields still
  screen normally. An unsupported model written plainly is still
  `outside_supported_scope`.

**Regression check.** The S1 run's `outputs.json` was byte-identical
before and after the change. `make fleet-build` produced no diff in
`demo/`. The full suite passed.

**Gap.** `INTERPRETER_VERSION` was not bumped. Recorded runs replay
unchanged, because they contain no malformed records.

## 5. Security Controls

- **Permissions.**
  - The top level is `permissions: {}`.
  - `sync` has `contents: write`, to push `discovery-state`.
  - `deploy` has `pages: write` and `id-token: write`.
  - `alert` has `issues: write`.
- **Pinned actions.** All four actions were already pinned by commit SHA.
  Each SHA was checked against its tag with `gh api
  repos/<owner>/<action>/commits/<tag>`, and all four matched:
  `actions/checkout` v7.0.1, `astral-sh/setup-uv` v10.2.0,
  `actions/upload-pages-artifact` v5.0.0, and `actions/deploy-pages` v5.0.1.
  The new `alert` job uses no action.
- **Script injection.** The `alert` job passes every expression through
  `env:`; none is interpolated into the script. The existing
  `accept_changed` input was already passed this way.
- **Content-Security-Policy**, set as a `<meta>` tag before `<style>`:
  - **Freshness page** (`discovery/site.py`): `default-src 'none'`. The
    style and the staleness script are allowed by their SHA-256 hashes,
    computed from the same constants when the page is rendered, so they
    cannot drift apart. Also `base-uri 'none'` and `form-action 'none'`.
    There is no `unsafe-inline`.
  - **Fleet page** (`fleet/page.py`, where only the meta tag changed):
    `default-src 'none'; script-src 'unsafe-inline'; style-src
    'unsafe-inline'; base-uri 'none'; form-action 'none'`.

    Hashes are not used here, because the meta tag would have to hold
    literal hashes. Another workstream edits this page's script and style,
    and the repository has no CI on pull requests. A stale hash would
    therefore silently ship a page whose script is blocked. The policy
    still refuses every external script, stylesheet, image, font,
    connection, frame, and form target. The page's data is rendered through
    its own `esc()`.

    To move to hashes, compute them in `render_fleet_page`, as `site.py`
    does.
  - A meta-tag policy cannot set `frame-ancestors`, so the policy gives no
    clickjacking protection, and none is claimed.
- **Verified.** Both pages were built in a scratch directory: the freshness
  page from the drill copy of the live state, and the fleet page from
  `demo/fleet-screen.json`. Each was captured with `node
  .claude/skills/site-capture/scripts/capture.js` in light, dark, and phone
  views; the fleet page also had a tile clicked. Both had zero console
  errors and no horizontal overflow.

  As a negative control, the freshness page's script hash was deliberately
  broken in a copy. The capture then reported the CSP violation, which
  shows the check would catch one.

  Tests: `test_page_carries_a_content_security_policy_allowing_only_its_own_code`
  and [`tests/fleet/test_page_security.py`](../tests/fleet/test_page_security.py).
- **Branding.** Both pages state that they are a screening tool, not a
  compliance determination, and carry no FAA logo. An existing test checks
  this for the freshness page.
- **Gaps.**
  - The S1 queue page copied into the site (`s1-queues.html`) has no CSP.
  - `upload-pages-artifact` is a composite action, and the actions it calls
    were not audited.
  - No secret scanning or Dependabot configuration was added.

## 6. Cost and Latency

The run history comes from `gh run list` and `gh api .../runs/<id>/jobs`
for "Discovery sync", 2026-10-11 to 2026-10-15. There were seven runs: one
failure before the fix in #23, the backfill, and five daily runs.

The sample is tiny, so with n = 5 the "p90" is effectively the maximum.

| Five daily runs (4 scheduled, 1 manual) | Median | p90 (n = 5) | Max |
|---|---|---|---|
| Whole run, created to completed | 41 s | 43 s | 43 s |
| `sync` job | 20 s | 23 s | 23 s |
| Sync step itself | 2 s | 3 s | 3 s |
| `deploy` job | 11 s | 18 s | 18 s |

- **Backfill** (run 38157672865): the `sync` job took 163 s, of which the
  sync step was 144 s; `deploy` took 27 s.
- **Schedule delay.** The cron is set for 12:17 UTC. The four scheduled runs
  started at 21:18, 19:20, 17:18, and 17:07 UTC, which is 4.8 to 9.0 hours
  late. This is the largest latency in the system. Even so, it leaves the
  page under 33 hours old, inside the 48-hour STALE limit.
- **Actions minutes.** The measured job time is about 35 seconds a run, or
  about 18 minutes a month. If each of the three jobs (`sync`, `deploy`,
  `alert`) were counted as a whole minute, a run would count 3 minutes:
  about 91 minutes a month, or 1,100 a year.

  That per-job rounding is an assumption, used here as the upper bound.
  GitHub's Actions billing page, fetched 2026-10-15, does not state it.
  The same page does state: "GitHub Actions usage is free for self-hosted
  runners and for public repositories that use standard GitHub-hosted
  runners."
- **Model spend to date** was $7.24 over 868 recorded calls. It is the sum
  of `response.cost_usd` over every `evaluation/runs/*/calls/*.json`:

  | Model | Spend |
  |---|---|
  | Claude Sonnet 5.5 (B2) | $4.80 |
  | Claude Haiku 5.5 (B2) | $2.09 |
  | Claude Opus 5.5 (B3) | $0.35 |

  - **No double counting.** Call files that share a key across repeat runs
    (r1 to r3) carry different batch ids and costs, so they are separate
    calls, not replays.
  - **Cross-check.** The `usage.cost_usd` totals in the runs' `report.json`
    files sum to $7.23. The two B2 plumbing runs, which have no report, add
    $0.008.
  - **Not counted.** Calls made outside an evaluation run (for example
    `make llm-check`) are not recorded here. The Anthropic Console is the
    authority.
  - The sync and the pages make no model calls.

**Operating statement for one year.**

- **Expected cash cost: $0.** This holds while the repository is public and
  no new evaluation runs are made:
  - Actions: at most about 1,100 runner-minutes, free on public repositories.
  - Pages hosting is free.
  - Model calls: none.
- **Storage.** The `discovery-state` branch grows about 20 MB a year
  (DISCOVERY_SYNC.md, "Cost"); it holds 55 MB today.
- **Attention.**
  - Commit to `main` at least once every 60 days. The alert issue reminds
    the owner from day 45.
  - Answer a "Discovery sync failing" issue when one opens. Most causes are
    transient and close themselves on the next run.
  - Decide on a changed document when a sync is rejected for changed
    metadata. That happened 0 times in the first five days.

  An estimate of under an hour a month is a guess, not a measurement.

## 7. Observability and Runbook

[`DISCOVERY_SYNC.md`, "Incidents"](../DISCOVERY_SYNC.md#incidents) covers:

- how a failure surfaces (red run, issue, page banner, job summary);
- where to look (the attempts, decisions, generation checks, and receipts
  on `discovery-state`);
- a failure-mode table;
- exact commands to roll back the published state;
- accepting a changed document;
- re-running.

Every failure mode tested in item 4 has a row:

- HTTP and transport failures;
- unreadable JSON;
- wrong shape or types;
- paging inconsistency;
- the 10,000-result cap;
- an oversized page;
- changed metadata;
- IAE acquisition failure;
- a crash;
- hostile titles and links;
- malformed engine records.

It also has rows for a failed state push, a failed deploy, and a disabled
schedule. Two stale lines in DISCOVERY_SYNC.md were corrected: "has not
been run on GitHub yet", and a daily run taking "about a minute".

## Remaining Gaps

- **No on-call person.** Alerts reach the owner by GitHub notification
  only, and nobody is obliged to act on them. The page's STALE banner is
  the user-facing safeguard.
- **No real user observation.** Nobody outside the project has used the
  pages. User evidence (ROADMAP, "User Evidence") is still open.
- **Untested on GitHub.** The new `alert` job, the inactivity warning, and
  the permission change are first exercised on `main`. The repository has
  no CI on pull requests, so "checks pass" means a local `make check`.
- **Recovery after a disabled schedule** is documented but cannot be
  rehearsed on demand.
- **No uptime check** of the published Pages URL from outside GitHub.
- **No CSP on the copied S1 queue page.** The fleet page allows inline code
  by `unsafe-inline`, not by hash (see item 5).
