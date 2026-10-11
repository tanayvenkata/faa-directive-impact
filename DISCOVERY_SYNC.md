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
   2025-01-01). Later syncs start 7 days before the active checkpoint. The
   checkpoint is the latest publication date seen, and the 7-day lookback
   catches documents that appear late. Documents seen before are matched by
   number and by the SHA-256 of their search entry, so a rerun adds nothing.
3. **Read IAE directives in full.** Every AD whose title names International
   Aero Engines is acquired like the frozen corpus: API JSON, XML, HTML, text,
   GovInfo PDF and MODS, and figures, each validated. Other ADs keep only
   their search entry.
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

Nothing is enabled yet. To run it on GitHub:

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
2. Copy `discovery/` to `data/discovery/`.
3. Run the rollback.
4. Copy the result back and commit.

Generations are never deleted, so any promoted generation can be restored.

A rejection caused by changed upstream metadata stops later syncs until a
person investigates. Two kinds of change pass without that:

- the Federal Register adding to an original's `corrections` list, which is
  accepted automatically;
- a change a person has investigated and accepts by rerunning with
  `uv run faa-directive-impact discovery-sync --accept-changed <document>`.

The accepted version is added to the record's history. The earlier
generation is not edited.

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

- **Scheduled workflows stop after 60 days of inactivity.** "In a public
  repository, scheduled workflows are automatically disabled when no
  repository activity has occurred in 60 days"
  ([disabling and enabling
  workflows](https://docs.github.com/en/actions/how-tos/manage-workflow-runs/disable-and-enable-workflows)).
  It is not documented whether the workflow's own commits to
  `discovery-state` count as activity, so do not rely on them. Mitigation:
  - the page turns STALE after 48 hours, so a stopped schedule is visible;
  - commit to `main` at least every 60 days;
  - re-enable a disabled schedule with **Actions → Discovery sync → Enable
    workflow** or `gh workflow enable discovery-sync.yml`.
- A scheduled run can be delayed when GitHub Actions is under high load
  (same events page).
- Airplane ADs that mention V2500 engines without naming International Aero
  Engines in the title are not read in full, so their applicability is not
  checked.
- FAA DRS is not queried. It is recorded as `deferred_access_verification`.
- Incorporated material is listed only for directives read in full, and it
  is never acquired.
- No retrieval index, normalized rules, or impact screening is built for
  `not_yet_evaluated` directives; that is ROADMAP steps 5, 7 and 8.
- The workflow has not been run on GitHub yet. A local run against the live
  API has been, and so has a run restored from receipts only, as CI would
  restore it.

## Cost

- **Compute:** a run takes about a minute: one or two search pages and a few
  documents. GitHub Actions is free on standard runners in public
  repositories ("GitHub Actions usage is free for self-hosted runners and for
  public repositories that use standard GitHub-hosted runners"; [Actions
  billing](https://docs.github.com/en/billing/concepts/product-billing/github-actions)).
- **Model calls:** none. GitHub Pages hosting is also free.
- **Storage:** the state branch grows by roughly the new records each day,
  plus a reference list of about 60 KB per promoted generation.
