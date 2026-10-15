# Discovery Sync Operations

ROADMAP step 6. This note covers what the daily sync does, how to turn it on,
how to roll it back, and what it does not do yet.

## What It Does

Each run (`make discovery-sync`, or the scheduled workflow) does this:

1. **Search.** It queries the Federal Register documents API for FAA final
   rules affecting 14 CFR part 39 (the airworthiness-directive part),
   published on or after a start date, oldest first, 1,000 per page. Each
   page's exact bytes are kept with a receipt (schema 1.1.0, role
   `search_results`). Parameter names come from the API's OpenAPI description
   (`data/open_api_v3.yml` in `usnationalarchives/federalregister-api-core`,
   the source of the official documentation page) and were checked against
   live responses. The API resets to page 1 past 10,000 results and caps the
   reported count at 10,000, so a search that could be truncated, or that
   collects a different number of documents than it reports, fails.
2. **Start date.** The first sync starts at `--start-date` (default
   1994-01-01, where the API's documents begin) and searches one calendar
   year at a time, because the full history (about 13,000 FAA part 39 rules,
   counted live 2026-10-11) is more than one search returns; no year comes
   near the cap. Later syncs start 7 days before the active checkpoint. The
   checkpoint is the latest publication date seen, and the 7-day lookback
   catches documents that appear late. Documents seen before are matched by
   number and by the SHA-256 of their search entry, so a rerun adds nothing.
3. **Read IAE directives in full.** Every AD whose title names International
   Aero Engines is acquired like the frozen corpus: API JSON, XML, HTML, text,
   GovInfo PDF and MODS, and figures, each validated. Other ADs keep only
   their search entry. A directive whose representations all arrive intact
   but whose text is laid out in a way the parser does not know (seen live:
   no "Material Incorporated by Reference" paragraph in 2010-23832 and
   2020-08703) goes to the review list; it does not reject the sync. Any
   other failure (a missing representation, an identity or media-type
   mismatch) still rejects it, so the next run retries.
4. **Coverage state.** The state comes from paragraph (c), "Applicability", in
   the XML, not from the title:
   - `evaluated`: only AD 2025-19-13 (2025-18469).
   - `not_yet_evaluated`: every V2500 model listed is A5, D5 or E5.
   - `outside_supported_scope`: everything else.

   Directives the sync cannot classify are held in a review list and never
   counted in scope: a missing paragraph (c), a mixed or unknown V2500 model,
   an AD with no AD number, or a Federal Register `C1-`/`R1-` correction of
   an IAE directive.
5. **Relationships.** A correction links to the original final rule:
   - as `source_asserted` when the API's `correction_of` names the original
     (an API URL for `C1-`/`R1-` documents);
   - otherwise as an `identifier_join` on the shared AD number, using the
     same rule as the frozen manifests.

   Supersession is read from the "Affected ADs" paragraph, so it is found
   only for directives read in full. A link whose other end is not in the
   corpus is recorded as unresolved. Proposal-to-final links are not derived,
   because proposals are not searched.
6. **Validate, then decide.** The candidate generation must pass these
   checks:
   - the search is complete;
   - every IAE acquisition succeeded;
   - identifiers and dates parse;
   - every record's receipts are retained, and this run's bytes match their
     hashes;
   - every relationship resolves;
   - nothing changed without explanation;
   - only 2025-18469 is `evaluated`.

   The run then ends one of three ways:
   - **Promote:** write the generation, then a promotion receipt naming the
     previous active generation, then atomically replace `active.json`
     (temporary file, then rename).
   - **No change:** nothing new was found, so the active generation stays in
     place. This still counts as a successful sync.
   - **Reject:** write the candidate and a rejection receipt with reasons.
     `active.json` and the checkpoint stay as they were.

   Every attempt, including a crash, writes `attempts/<id>.json`; together
   these files form the sync log.
7. **Freshness page.** `make discovery-site` writes `site/index.html`. It
   shows:
   - the last attempt and its outcome, and the last success;
   - the checkpoint and the active generation;
   - counts;
   - IAE-boundary directives, with `not_yet_evaluated` labeled as unverified
     candidates;
   - new directives, the review list, failures, and unavailable dependencies.

   The browser compares the embedded last-success time with its own clock
   and shows a STALE banner after 48 hours. Without JavaScript the page says
   "As of <date>". If the S1 queue page is committed under
   `evaluation/runs/`, the site copies it and links to it.

The storage root defaults to `data/discovery/`, track `refreshable_discovery`.
The sync refuses any root inside or containing `seed-frozen`,
`frozen-evaluation`, or `generations`.

## Turning It On (Owner Steps)

Done 2026-10-11: Pages was set to build from GitHub Actions and the
workflow was run by hand. The first run failed before syncing (the
state-branch setup; fixed in #23), and the second promoted the full 1994
backfill. The steps, for a fresh fork or a re-enable:

1. Merge the branch to `main`. GitHub only runs scheduled workflows on the
   default branch ("Scheduled workflows will only run on the default
   branch"; [events that trigger
   workflows](https://docs.github.com/en/actions/reference/workflows-and-actions/events-that-trigger-workflows)).
2. **Settings → Pages → Build and deployment → Source: GitHub Actions.**
3. **Settings → Actions → General → Workflow permissions:** keep "Read
   repository contents" as the default. The workflow asks for
   `contents: write` itself so it can push the `discovery-state` branch. If a
   branch ruleset covers all branches, exempt `discovery-state`.
4. **Actions → Discovery sync → Run workflow** once by hand. The first run
   creates the orphan `discovery-state` branch and deploys the page. The
   schedule runs daily at 12:17 UTC after that.

Check after the first run: the job summary, the `discovery-state` branch,
and the Pages URL in the deploy job.

## Rolling Back

Locally, or in a checkout of the state:

```bash
make discovery-rollback                 # back to the active generation's predecessor
make discovery-rollback TO=gen-...      # or to a specific promoted generation
```

A rollback writes a `rollback` receipt naming both generations and repoints
`active.json`. The checkpoint returns to the target's, so the next sync
searches again from there. To roll back the published state:

1. Check out `discovery-state`.
2. Copy `discovery/` to a scratch root such as `data/rollback-work/`. Do not
   use `data/discovery/`, which may hold a local sync's raw bytes.
3. Run the rollback with `DISCOVERY_ROOT` set to that root.
4. Copy the result back and commit.

The exact commands are in "Incidents" below. Rehearse first with
`make discovery-drill`.

Generations are never deleted, so any promoted generation can be restored.

A rejection caused by changed upstream metadata stops later syncs until a
person investigates. Two kinds of change pass without that:

- the Federal Register adding to an original's `corrections` list, which is
  accepted automatically;
- a change a person has investigated and accepts by rerunning with the
  document number: in GitHub, **Actions → Discovery sync → Run workflow**
  with the number in `accept_changed`; locally,
  `uv run faa-directive-impact discovery-sync --accept-changed <document>`.

The accepted version is added to the record's history. The earlier
generation is not edited.

## Incidents

Nobody is on call. This runbook is meant for whoever next reads the alert
issue. Each failure mode below was exercised by a test or a drill, named in
[`operations/HARDENING.md`](operations/HARDENING.md), unless it says
otherwise.

### How a Failure Surfaces

When a run fails, these all happen without anyone acting:

1. **The Actions run is red.** The `sync` job fails at its last step when the
   outcome is not `promoted` or `no_change`, and a crashed or timed-out job
   fails by itself.
2. **A GitHub issue opens.** The `alert` job (`issues: write`, nothing else)
   opens **"Discovery sync failing"**. If that issue is already open, the job
   comments on it with the run link and does not open a second one. The first
   later run in which both `sync` and `deploy` succeed closes it. GitHub
   notifies watchers of new issues, so the owner gets an email if their
   notification settings allow it.
3. **The freshness page says so.** The page is deployed even after a failed
   sync. It shows "The last sync attempt ... did not succeed: rejected" (or
   `error`), lists the failures, and turns STALE 48 hours after the last
   success, measured on the viewer's clock.
4. **The job summary** of the run shows the attempt record as JSON.

If a scheduled run never happens (the schedule was disabled or dropped),
there is no run and so no alert. Only the STALE banner shows it. Separately,
from day 45 without a commit on `main`, each run comments on **"Scheduled
sync at risk: no commit on main for 45 days"**.

### Where to Look

| What | Where |
|---|---|
| Step logs | Actions → the run → `sync` job → **Sync** step (the attempt JSON is printed and also in the job summary) |
| Sync log | `discovery-state` branch, `discovery/attempts/<attempt-id>.json`: `outcome`, `failures`, `counts`, and `traceback` for an `error` |
| Why a candidate was rejected | `discovery/decisions/<receipt-id>.json`, `reasons` |
| Which check failed | `discovery/generations/<generation-id>.json`, `validation.checks` |
| A failed download | `discovery/receipts/<run-id>/*.json`: `failure.reason_code` (`http_error`, `timeout`, `invalid_content`, ...) and `failure.detail` |
| What is live | `discovery/active.json`, and the page's "Activated by" row (promotion or rollback receipt) |

To read the state locally without checking out the branch:
`git fetch origin discovery-state && git show FETCH_HEAD:discovery/active.json`.

### Failure Modes

| Symptom in `failures` or the page | Cause | What to do |
|---|---|---|
| `search page N failed: http_error (HTTP 503 ...)`, `timeout`, or `network_error` | The Federal Register API is down or slow | Nothing. The candidate is rejected, the previous generation stays active, and the next scheduled run retries from the same checkpoint. Re-run by hand only if the page is close to STALE. |
| `search page N is not readable JSON` | The API returned an HTML error page, an empty body, or truncated JSON | As above: transient. If it repeats for several days, look at the saved bytes from a local `make discovery-sync` (CI keeps no raw bytes). |
| `lacks a non-negative integer count or a results list`, `result without a valid document number`, `has wrong-typed fields: ...` | The API's response shape changed | Not transient. Compare a live response with `SEARCH_FIELDS` in `discovery/search.py`, then change the parser in a PR with a test. Never accept by hand. |
| `collected N documents but the search reported M`, `count changed during paging`, `pages overlapped` | Paging was inconsistent, often because documents were published mid-sync | Usually clears on the next run. |
| `search matched N documents, at or above the API's 10000-result cap` | The checkpoint is very far back (for example after a long outage or a rollback to the backfill) | Roll forward, or run the sync locally with a later start; see "Start date" above. |
| `response exceeded 16777216 bytes` | A search page over 16 MiB, about 40 times the largest seen (382,095 bytes) | Something is wrong upstream. Do not raise the cap without looking at what was sent. |
| `<document>: search metadata changed since generation ...` | The Federal Register changed an entry already in the corpus | Investigate, then accept it (below). Syncs keep rejecting until you do. |
| `<document>: missing ...` or `... failed <check>` for an IAE directive | One representation of an IAE directive (XML, PDF, MODS, a figure) failed | Usually transient; the next run retries. If it persists, read the receipt's `failure.detail`. |
| Outcome `error`, with a `traceback` in the attempt | An unexpected crash. Nothing was promoted, and the active pointer is unchanged. | A bug: reproduce it locally from the traceback and fix it with a test. |
| `sync` green but "Save discovery state" red | The push to `discovery-state` failed: a branch rule, a concurrent push, or a missing `contents: write` permission | The run's state is lost, and the next run repeats it. Check the branch rules (DISCOVERY_SYNC.md, "Turning It On", step 3). |
| `deploy` red, `sync` green | GitHub Pages deploy failed | The state is saved, and the page is one run behind. Re-run the workflow; check **Settings → Pages → Source: GitHub Actions**. |
| No run for more than a day; page STALE | The schedule was disabled after 60 days without activity, or GitHub dropped the run under load | `gh workflow enable discovery-sync.yml` if it was disabled; push a commit to `main`; then **Run workflow**. Not tested: it cannot be triggered on demand. |
| A directive title containing HTML, or a non-Federal Register `html_url` | Hostile or odd upstream text | Nothing to do. The page escapes all text and links only `https://www.federalregister.gov/` URLs; anything else is shown as plain text. |
| Fleet tile in "Needs review" with "The engine record is malformed" | An engine record with a missing, wrong-typed, duplicated, or look-alike field | Correct the record in `demo/fleet.json`. The screens never clear a malformed record. |

### Rolling Back the Published State

A rollback is a local command plus a commit to `discovery-state`. Rehearse
it first on a copy (`make discovery-drill`; receipt in
[`operations/drills/`](operations/drills/)). Then:

```bash
git fetch origin discovery-state
git worktree add --detach ../discovery-state-work FETCH_HEAD
# A separate root, so a local data/discovery/ (and its raw bytes) is untouched.
mkdir -p data/rollback-work
cp -R ../discovery-state-work/discovery/. data/rollback-work/
make discovery-rollback DISCOVERY_ROOT=data/rollback-work   # or add TO=gen-...
make discovery-site DISCOVERY_ROOT=data/rollback-work       # "Activated by" says rollback
rsync -a --exclude 'raw/' --exclude '.staging/' --exclude '.active-*' \
  data/rollback-work/ ../discovery-state-work/discovery/
git -C ../discovery-state-work add -A discovery
git -C ../discovery-state-work commit -m "discovery: roll back to <generation>"
git push origin "$(git -C ../discovery-state-work rev-parse HEAD):refs/heads/discovery-state"
git worktree remove ../discovery-state-work
rm -rf data/rollback-work
```

Do not push while a workflow run is in progress (check the Actions tab), or
the run's own push will be rejected. The page updates on the next run. That
run syncs again from the rolled-back checkpoint, so it re-promotes whatever
it finds. If the problem was upstream data, fix or decide it first, and
pause the schedule meanwhile with `gh workflow disable discovery-sync.yml`.
To restore after a mistaken rollback, roll back again with `TO=` set to the
generation that was active before; any promoted generation can be the
target.

### Accepting a Changed Document

When a sync is rejected with `<document>: search metadata changed`:

1. Compare the two versions. The old entry is the record's `source_entry` in
   the active generation. The new one is in a local
   `make discovery-sync`'s `raw/federal-register-search/` pages, or on the
   document's Federal Register API page.
2. If the change is a real correction or a harmless edit, accept it:
   **Actions → Discovery sync → Run workflow** with the document number in
   `accept_changed`. Locally, the same is
   `uv run faa-directive-impact discovery-sync --accept-changed <document>`.
   The new version is added to the record's history. The old generation is
   never edited.
3. If the change is suspicious (an AD number or date rewritten), do not
   accept it. Leave the rejection in place, and record the investigation in
   the alert issue.

### Re-reading After a Scope Fix

The sync reads each IAE directive once, when it is new. When the scope reader
changes, records already in the corpus keep their old classification until
they are re-read. Run the workflow by hand with `reread` set to the document
numbers (or locally, `uv run faa-directive-impact discovery-sync --reread
2012-12329 2015-12068`). Each is acquired again, classified with the current
reader, and given a new version marked `reread_scope`; the candidate is
validated and promoted like any other. Only IAE directives with a full-text
representation can be re-read; anything else rejects the attempt.

First use, 2026-10-15: AD 2012-09-09 (`2012-12329`) and AD 2015-10-04
(`2015-12068`), filed out of scope by the reader that stopped at a lead-in
(`evaluation/RETRIEVAL.md`, "The Sync Bug It Found").

### Re-running

**Actions → Discovery sync → Run workflow** (or
`gh workflow run discovery-sync.yml`). A re-run is safe: a sync with nothing
new reports `no_change`, and documents seen before are matched by number and
by hash. The issue closes itself when the re-run succeeds.

## Raw Bytes and Redistribution

The `discovery-state` branch holds:

- receipts;
- generations;
- content-addressed records;
- validation reports;
- decisions;
- the sync log;
- `active.json`.

It never holds raw bytes. In CI, raw bytes exist only while the run lasts;
no workflow artifact or release asset is made for them. IAE figures are
`review_required` (REDISTRIBUTION.md), and the repository is public. Each
receipt keeps the source URL and the SHA-256 of what was seen.

Two consequences:

- A run verifies only its own bytes. Records carried forward are checked
  against their retained receipts.
- The version index ignores receipts whose bytes are absent
  (`require_artifacts`), so a missing file is not mistaken for a change.

A local `make discovery-sync` keeps raw bytes under `data/discovery/raw/`.

## Known Limitations

- **Coverage starts at the first sync's start date (1994-01-01 by
  default).** That is where the Federal Register API's documents begin, so
  directives published earlier are not in the corpus. The date is recorded
  in every generation as `coverage_start` and shown on the page. A first sync
  started later (for a quick local run) covers only from its own date.
- **Pre-2000 AD numbers and old document numbers.** Before 2000, AD numbers
  had two-digit years (`AD 93-25-17`) and document numbers came in shorter
  forms (`93-31908`, `94-21`, `E6-11333`); both are accepted. Directives with
  no parseable AD number in their docket identifiers go to the review list.

- **Scheduled workflows stop after 60 days of inactivity.** "In a public
  repository, scheduled workflows are automatically disabled when no
  repository activity has occurred in 60 days"
  ([disabling and enabling
  workflows](https://docs.github.com/en/actions/how-tos/manage-workflow-runs/disable-and-enable-workflows)).
  GitHub does not document whether the workflow's own commits to
  `discovery-state` count as activity. Its page on `GITHUB_TOKEN` covers
  only what such pushes trigger: they start no new workflow run. So do not
  rely on the workflow's own commits. Mitigations:
  - the page turns STALE after 48 hours, so a stopped schedule is visible;
  - every run measures how many days ago the last commit on `main` was. At
    45 days or more, the alert job opens the issue "Scheduled sync at risk:
    no commit on main for 45 days";
  - commit to `main` at least every 60 days;
  - re-enable a disabled schedule with **Actions → Discovery sync → Enable
    workflow** or `gh workflow enable discovery-sync.yml`.
- A scheduled run can be delayed when GitHub Actions is under high load
  (same events page). The delays observed so far are long. The cron time is
  12:17 UTC, and the four scheduled runs from 2026-10-12 to 2026-10-15
  started between 17:07 and 21:18 UTC, 4.8 to 9 hours late. The page is
  therefore up to about 33 hours old before the next run, which stays under
  the 48-hour STALE limit.
- The API lists documents a day or two before their publication date
  (public inspection), so the checkpoint can be ahead of today. Their search
  entries were already complete in the live run. If one changes after
  publication, the sync rejects it for review and does not overwrite it.
- Airplane ADs that mention V2500 engines without naming International Aero
  Engines in the title are not read in full, so their applicability is not
  checked.
- FAA DRS is not queried. It is recorded as `deferred_access_verification`.
- Incorporated material is listed only for directives read in full, and it
  is never acquired.
- No retrieval index, normalized rules, or impact screening is built for
  `not_yet_evaluated` directives; that is ROADMAP steps 5, 7 and 8.
- The workflow has run on GitHub daily since 2026-10-11 (see "Cost"). Its
  failure alerting (the `alert` job, added 2026-10-15) has been tested only
  with a stub `gh`, not with a real failed run.

## Cost

- **Compute:** measured from the GitHub run history (2026-10-11 to 15, five
  daily runs; [`operations/HARDENING.md`](operations/HARDENING.md)). A daily
  run takes about 40 seconds from start to finish: a sync job of 17 to 23
  seconds, of which the sync itself is 1 to 3 seconds, and a deploy job of 9
  to 18 seconds. The first run backfilled 1994 onward (about 13,000
  directives, 45 IAE directives read in full). Its sync step took 144 seconds
  on GitHub. GitHub Actions is free on standard runners in public
  repositories ("GitHub Actions usage is free for self-hosted runners and for
  public repositories that use standard GitHub-hosted runners"; [Actions
  billing](https://docs.github.com/en/billing/concepts/product-billing/github-actions)).
- **Model calls:** none. GitHub Pages hosting is also free.
- **Storage:** the first backfill writes about 30 MB of state (one record
  file per directive and one 2.2 MB generation listing, measured
  2026-10-11). After that, a promotion stores only its changed records and
  references, and every 30th generation stores a full listing so a rebuild
  never walks a long chain: roughly 20 MB a year at one promotion per
  business day.
