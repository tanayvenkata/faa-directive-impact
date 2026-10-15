# Step 10: Is a Bounded Agent Justified?

- **ROADMAP step:** 10 (evaluate a bounded agent)
- **Decided:** 2026-10-15, by Claude under the owner's delegation; no person
  reviewed the evidence below
- **Decision:** **not justified.** No agent is built. The fixed workflow
  stays deterministic.

## The Bar

The roadmap builds an agent "only if fixed-workflow traces demonstrate a
feedback-dependent limitation that an agent can improve safely." The vault
note (*FAA Directive Impact*, "Workflow and Agent Boundary") names four
such limitations: choosing among near-neighbor directive threads, requesting
a newly material fleet fact, recovering after an unavailable source, and
pausing and resuming a review packet. The series' complexity policy adds
agents "only when a measured failure or real threat model earns them."

A limitation counts only if it shows up in a recorded trace, and only if an
agent's loop of acting, observing, and acting again would fix it better than
a deterministic change.

## The Traces

| Trace | Where | What it shows |
|---|---|---|
| Daily sync, 7 workflow runs since 2026-10-11 | GitHub Actions run history; `discovery-state` branch, `discovery/attempts/` | One failure, the first run's state-branch setup, fixed in code (#23). Six successes since, two promotions and four no-change runs |
| Discovery review list, 29 directives | Discovery generation `gen-20261011T165831Z-6cea777a`, `review` | 20 predate the full-text representations; 6 name V2500 designations outside A5/D5/E5 (V2500-A1 or service-bulletin numbers); 2 have an unfamiliar layout; 1 is a correction |
| Retrieval R0 on 29 cases | [`runs/retrieval-r0-20261015T180258Z`](runs/retrieval-r0-20261015T180258Z/report.md) | No protected miss; thread expansion (corrections, supersession) is a fixed rule over recorded relationships |
| S1, B2, B3 runs | [`S1_BASELINE.md`](S1_BASELINE.md), [`B2_FULL_CONTEXT.md`](B2_FULL_CONTEXT.md), [`B3_RULE_EXTRACTION.md`](B3_RULE_EXTRACTION.md) | Every residual failure turns on an authority question: the paragraph (g) shop-visit window (seed-005) and AD 2026-17-03's carry-forward reading |
| Fleet screen, 200 engines | [`../demo/fleet-screen.json`](../demo/fleet-screen.json) | Missing facts are listed by the screener as named fields; nothing needs a follow-up search to find them |

## The Four Limitations, Checked

| Limitation | Seen in the traces? | Why an agent would not fix it better |
|---|---|---|
| Choosing among near-neighbor threads | No. R0 surfaced every expected candidate; no true distractor reached an in-family engine | Thread choice is decided by recorded relationships (proposal, correction, supersession) and the as-of date. When that failed, the cause was a parser reading too little of paragraph (c), fixed deterministically with a test |
| Requesting a newly material fleet fact | Only in a fixed form. Screeners name each missing field (`installed_components[...].serial_number`, `events[...].qualifies_as_engine_shop_visit`) | The request is already explicit and deterministic. An agent would add a conversation, not information; no fleet owner exists to answer it |
| Recovering after an unavailable source | Once, and it was a code bug, not an outage. The sync's contract already keeps the last good generation and retries the next day | Retry and rollback are deterministic and tested (step 9). An agent improvising recovery is the behavior AGENTS.md rules out: it "must not silently modify authoritative records, resolve source anomalies, or promote a release" |
| Pausing and resuming a review packet | No. There are no users or packets yet | Nothing to measure. Needs observed workflow sessions, which are human-gated |

The residual hard cases need an authority, not iteration. Seed-005's deadline
turns on an informal FAA reply that no text supplies; AD 2026-17-03's
carry-forward reading is the same kind of question. An agent that searched
harder would either find nothing or guess, and a guess there is a possible
false clear.

## What Would Reopen This

Revisit when a recorded trace shows any of these:

- the review list grows faster than a person clears it, and the items need
  reading across several documents to classify (a read-only assistant could
  draft classification notes for a person; it would never set a coverage
  state or promote);
- retrieval misses a candidate that only a follow-up query could reach;
- observed review sessions show people repeatedly assembling the same
  packet by hand across directives and engine records.

Any agent then stays inside the vault's boundary: typed, read-only actions;
state, approvals, and terminal outcomes outside the model; an append-only
action trace; no authority to declare compliance or direct maintenance.
