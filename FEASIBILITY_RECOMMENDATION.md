# Source-Review Feasibility Recommendation

## Decision

**GO — proceed with the constrained IAE V2500 acquisition and evidence-modeling
slice, with two explicit constraints.**

1. Keep supported impact evaluation limited to the named V2500-A5/D5/E5
   variants and the protected directive cases.
2. Treat image-only figures and unavailable incorporated materials as explicit
   evidence dependencies; do not silently OCR, reconstruct, or promote them as
   authoritative structured facts.

Do not switch to a broader engine or aircraft scope. Do not narrow to a simple
document-search demo. The current scope is large enough to expose real
production evidence problems while still supporting manually reviewable
ground truth.

## Source Strategy

Retain the mixed representation strategy:

```text
Federal Register API JSON
  → discovery, identity, relationships, representation and image URLs

Federal Register XML
  → preferred structured parsing input

Federal Register HTML + original-size referenced images
  → evidence addressing and complete web representation

GovInfo official PDF + MODS
  → authority, pagination, bibliography, and visual verification

FAA DRS
  → FAA identity/status corroboration after API access is verified
```

No one format should be declared canonical for all purposes. “Canonical” must
be qualified by role: official edition, parsing input, identity metadata, or
evidence locator.

## Why the Scope Passes

The protected core exercises the behaviors the proposed system needs to prove:

- immutable multi-representation acquisition;
- proposal-to-final version and relationship tracking;
- structured and image-based evidence;
- paragraph, table, figure, and page citation;
- exact model, part, serial, cycle, and date predicates;
- shop-visit and component-exposure events;
- operator and maintenance-program state;
- corrected task references;
- unavailable incorporated dependencies;
- partial evidence, abstention, and `needs_review`; and
- current versus as-of results.

A broader initial corpus would add volume before these contracts are tested. A
narrower search-only scope would avoid the most valuable correctness problems
and would not substantiate the fleet-impact product.

## Important Constraint Discovered During Review

The initial “XML-first” choice remains valid but is not “XML-only.” Federal
Register XML sometimes represents a compliance figure only as a graphic ID.
The acquisition layer must follow API/HTML image metadata and retain the
original-size image. Any transcription becomes versioned derived data with a
verification status and a citation to the image artifact.

This is a constraint on the parsing design, not a reason to change domain
scope.

## Supported First Claims

After successful implementation and evaluation, the project may aim to claim:

- reproducible acquisition of the protected official-source representations;
- traceable proposal/final and source-version relationships;
- evidence-backed retrieval over the frozen corpus;
- deterministic classification for explicitly modeled V2500 cases; and
- correct escalation when required fleet facts or incorporated evidence are
  missing.

It may not claim:

- general FAA or aviation regulatory coverage;
- a compliance determination;
- maintenance adequacy or return-to-service authority;
- complete manufacturer instructions from public sources;
- continuous monitoring before live synchronization exists; or
- support for adjacent IAE engine families.

## Implementation Entry Gate

Before choosing the application stack, complete these artifacts:

1. first immutable acquisition of the HPT hub proposal/final pair under the
   raw-manifest contract;
2. a checked raw-generation manifest and completeness report;
3. initial normalized identity, relationship, evidence-region, table-row, and
   dependency examples derived from retained raw artifacts;
4. the 25-case feasibility seed with label provenance and forbidden claims;
5. numerical retrieval, citation, applicability, temporal, and abstention
   gates; and
6. a documented decision for image transcription and review.

After those are frozen, discuss the smallest credible acquisition and parsing
stack. Vector, graph, agent, hosting, and incremental-refresh choices remain
deferred until the deterministic baseline demonstrates a need.

## Final Recommendation

Proceed with the planned vertical slice:

```text
official acquisition
→ immutable raw generation
→ normalized evidence and relationships
→ simple candidate retrieval baseline
→ deterministic fleet-impact cases
→ evaluation gates
→ promote, constrain, or reject
```

The next concrete task is the first immutable two-document acquisition—not a
UI, vector database, or agent.

