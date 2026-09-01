# Data Synchronization and Release Lifecycle

## Purpose

This document records how a future production version avoids becoming a stale demo. It is a lifecycle contract, not an instruction to implement the live pipeline during the current source-reading phase.

The project should eventually maintain both reproducibility and freshness:

- a **frozen evaluation corpus** whose artifacts, hashes, cases, and labels change only through an explicit versioned release;
- a **refreshable discovery corpus** that detects and processes new or changed FAA/Federal Register records.

## Intended Flow

```text
Federal Register API and FAA DRS
                ↓
        scheduled deterministic poll
                ↓
          immutable raw capture
                ↓
        parse and normalize version
                ↓
       compare with previous state
                ↓
      build candidate derived indexes
                ↓
       validation and regression gates
                ↓
        promote, constrain, or reject
                ↓
       active evidence-search release
```

Ordinary acquisition should be deterministic code, not an autonomous agent scraping pages and deciding what to retain.

## Data Layers

### Immutable raw captures

Preserve what the source returned along with:

- canonical source URL;
- source system;
- retrieval timestamp;
- Federal Register, AD, docket, and related identifiers where available;
- media type and representation;
- HTTP metadata where useful;
- SHA-256 hash;
- authority role;
- redistribution status;
- acquisition success or failure;
- named unavailable dependencies.

Raw captures are append-only. An existing file is not silently overwritten when a representation changes.

The first concrete receipt and generation requirements are defined in
[`RAW_MANIFEST_CONTRACT.md`](RAW_MANIFEST_CONTRACT.md). The initial source-role
decision is API JSON for discovery/identity, Federal Register XML for preferred
structured parsing, Federal Register HTML for evidence addressing, and the
GovInfo PDF for official-edition verification. This choice must be rechecked
against the other protected threads before it becomes a general parser claim.

### Versioned normalized records

Derive structured records for:

- document identity and authority state;
- publication, effective, correction, and supersession time;
- proposal-to-final directive threads;
- engine models and normalized family relationships;
- component, part, serial, cycle, date, shop-visit, and program predicates;
- paragraph and table evidence regions;
- incorporated-material dependencies and availability.

Normalized data is versioned and rebuildable from raw captures. Parser and schema versions must be recorded.

### Rebuildable retrieval projections

Lexical indexes, vector indexes, graph projections, chunks, summaries, and caches are derived views. Record the source generation, parser/chunker version, retrieval configuration, and embedding model where applicable.

The retrieval index is never authoritative state. It must be possible to rebuild it.

## Synchronization Semantics

### Checkpointed polling

A scheduler may eventually run daily and query for records published or changed since the last successful checkpoint. Advance the checkpoint only after acquisition is complete enough to preserve the run's result.

### Idempotency

Repeating the same synchronization must not create duplicate records. A stable identity plus content hash should distinguish:

- an already-seen representation;
- a newly discovered document;
- a legitimate new version or related record;
- an unexpected representation change requiring investigation.

### Preserve history

Never replace proposals, final rules, corrections, superseded directives, or earlier source representations in place. Build current and as-of projections over preserved history.

### Failure isolation

A failed download, parse, relationship resolution, or dependency check must be recorded. A partial run must not silently become the active production generation.

## Candidate Release Process

Build refreshed normalized data and retrieval indexes as a candidate generation separate from the active generation.

Before promotion, check at minimum:

- expected acquisitions completed or explicitly failed;
- every derived record points to retained raw evidence;
- required identifiers and dates parse consistently;
- proposal/final/correction/supersession relationships remain valid;
- citations resolve to the correct source version and region;
- protected retrieval and applicability regressions pass;
- new unavailable dependencies produce `needs_review` rather than invented evidence;
- unexpected changes in fleet-impact results are explained.

Promotion should be an atomic pointer or alias change. Retain the previous known-good generation and a release receipt so rollback can be demonstrated.

## Freshness in the Product

The eventual interface and evidence packet should expose:

- last attempted synchronization;
- last successful synchronization;
- source coverage or checkpoint;
- active raw/normalized/index generation identifiers;
- new, changed, failed, and quarantined record counts;
- known unavailable dependencies;
- whether the system is current, degraded, incomplete, or stale.

If synchronization is stale or incomplete, say so visibly. Do not present the corpus as current merely because search is operational.

## Full Rebuild Before Incremental Complexity

For the bounded initial corpus, rebuilding all normalized records and indexes may be simpler and safer than incremental mutation. Add selective reprocessing only after measured corpus size, build latency, or cost justifies it.

## Agent Boundary

An agent is not required for routine synchronization. Deterministic code should own querying, downloading, hashing, parsing known structures, deduplication, validation, index construction, and release gates.

A future bounded agent could assist with exception investigation, such as:

- an unfamiliar document or table structure;
- an unresolved proposed-to-final relationship;
- an unavailable incorporated dependency;
- a conflict between source representations.

Any agent proposal must be reviewable and traced. The agent must not silently change authoritative records, invent missing evidence, advance a checkpoint, or promote a release.

## Deferred Decisions

Do not choose these during the current reading phase:

- scheduler or hosting provider;
- database and object-storage products;
- lexical/vector/graph engines;
- orchestration framework;
- full versus incremental refresh implementation;
- agent framework;
- retention and public redistribution mechanism for larger source artifacts.

Choose them after inspecting the real source representations and freezing the first acquisition and evaluation contracts.

## Production Claim Discipline

Before live refresh exists, describe the project as operating on a frozen, versioned corpus. Do not claim continuous monitoring.

If live synchronization is implemented later, preserve evidence for:

- successful and failed refreshes;
- candidate validation;
- promotion and rollback;
- stale/degraded behavior;
- source-change impact;
- latency and operating cost.

If a lifecycle responsibility is deliberately deferred to another portfolio episode, record the reason, current limitation, owning episode, and how the limitation is visible to users and reviewers.
