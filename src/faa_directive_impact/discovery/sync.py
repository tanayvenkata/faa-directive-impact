"""One checkpointed sync of the discovery corpus: candidate, validate, decide.

A sync searches from the active generation's checkpoint (inclusive), builds a
candidate generation that carries every earlier record forward and adds the
new ones, validates it, and then:

- promotes it: writes the generation, a promotion receipt naming the
  previously active generation, and the active pointer, in that order;
- records ``no_change`` when nothing new or changed was found, leaving the
  active generation in place (the attempt still counts as a successful sync);
- or rejects it: writes the candidate and a rejection receipt with reasons,
  and leaves the active pointer and checkpoint untouched.

Every attempt, including one that crashes, writes an attempt record: the
sync log the freshness page is built from.

Records carried forward are compared by the SHA-256 of their search entry,
which is stored in the generation. Raw bytes from earlier runs are not needed
for that, so a sync runs the same way in CI, where only receipts persist.
"""

import hashlib
import json
import traceback
from collections import defaultdict
from dataclasses import dataclass, field
from datetime import date, datetime, timedelta
from pathlib import Path
from typing import Any

import httpx

from faa_directive_impact.acquisition.document import (
    DocumentAcquisition,
    acquire_document,
)
from faa_directive_impact.acquisition.federal_register import (
    DOCUMENT_NAMESPACE,
    DOCUMENT_NUMBER_PATTERN,
    airworthiness_directive_numbers,
    faa_docket_numbers,
)
from faa_directive_impact.acquisition.manifest import (
    build_validation_report,
    correction_relationships,
    is_correction,
    supersession_relationships,
)
from faa_directive_impact.acquisition.retrieval import (
    AcquisitionContext,
    Clock,
    IdFactory,
    format_utc,
    random_id,
    receipt_path,
    utc_now,
)
from faa_directive_impact.acquisition.storage import RawStorage
from faa_directive_impact.acquisition.versions import VersionIndex
from faa_directive_impact.discovery.scope import (
    COVERAGE_STATES,
    EVALUATED,
    EVALUATED_DOCUMENTS,
    ScopeDecision,
    classify_applicability,
    names_international_aero_engines,
    needs_review,
    outside_by_title,
)
from faa_directive_impact.discovery.search import (
    DISCOVERED_DOCUMENT_NUMBER,
    SearchOutcome,
    search_directives,
)
from faa_directive_impact.discovery.state import (
    attempt_path,
    decision_path,
    read_active,
    read_generation,
    require_discovery_root,
    write_active,
    write_generation,
)

GENERATION_SCHEMA_VERSION = "1.0.0"
CORPUS_TRACK = "refreshable_discovery"
DEFAULT_START_DATE = date(2025, 1, 1)
# Each search re-reads this many days before the checkpoint, so a document
# that becomes visible after a later-dated one is still found. Re-read
# documents are deduplicated against the corpus.
LOOKBACK_DAYS = 7
AD_TITLE_PREFIX = "Airworthiness Directives"
FINAL_RULE_TYPE = "Rule"

PROMOTED = "promoted"
NO_CHANGE = "no_change"
REJECTED = "rejected"
ERROR = "error"
SUCCESSFUL_OUTCOMES = (PROMOTED, NO_CHANGE)
COUNT_KEYS = (
    "searched",
    "new",
    "unchanged",
    "changed",
    "failed",
    "quarantined",
    "not_directive",
    "read_in_full",
)

GENERATION_NOTES = (
    "Proposal-to-final links are not derived: the discovery search covers "
    "final rules only, so proposals are not acquired.",
    "Supersession is derived only for directives read in full (those naming "
    "International Aero Engines); other directives keep search metadata only.",
    "Incorporated material of directives kept as metadata only is not inspected.",
)


@dataclass
class Candidate:
    """The generation being built and everything the decision needs."""

    generation_id: str
    run_id: str
    since: date
    checkpoint_floor: date
    records: dict[str, dict[str, Any]]
    review: dict[str, dict[str, Any]]
    counts: dict[str, int] = field(default_factory=lambda: dict.fromkeys(COUNT_KEYS, 0))
    failures: list[str] = field(default_factory=list)
    skipped: list[dict[str, str]] = field(default_factory=list)
    new_documents: list[str] = field(default_factory=list)
    unaccepted_changes: list[str] = field(default_factory=list)
    documents: list[DocumentAcquisition] = field(default_factory=list)


class RollbackError(RuntimeError):
    """There is no earlier promoted generation to return to."""


def entry_digest(entry: dict[str, Any]) -> str:
    """SHA-256 of a search entry's canonical JSON; its identity for changes."""
    canonical = json.dumps(entry, sort_keys=True, separators=(",", ":"))
    return hashlib.sha256(canonical.encode()).hexdigest()


def run_sync(
    storage_root: Path,
    client: httpx.Client,
    *,
    start_date: date = DEFAULT_START_DATE,
    accept_changed: frozenset[str] = frozenset(),
    clock: Clock = utc_now,
    new_id: IdFactory = random_id,
) -> dict[str, Any]:
    """Run one sync attempt and return its attempt record.

    ``start_date`` applies only before the first promotion; afterwards the
    active generation's checkpoint decides where the search starts.
    ``accept_changed`` names documents whose changed search metadata a person
    has investigated and accepted as a new version.
    """
    root = require_discovery_root(storage_root)
    storage = RawStorage(root)
    started_at = clock()
    attempt: dict[str, Any] = {
        "attempt_id": new_id("attempt", started_at),
        "started_at_utc": format_utc(started_at),
        "corpus_track": CORPUS_TRACK,
    }
    try:
        attempt.update(
            _sync(root, storage, client, clock, new_id, start_date, accept_changed)
        )
    except Exception as error:  # the log must record even an unexpected crash
        attempt.update(
            {
                "outcome": ERROR,
                "failures": [f"{type(error).__name__}: {error}"],
                "traceback": traceback.format_exc()[-4000:],
            }
        )
    active = read_active(root)
    attempt["active_generation_id"] = active["generation_id"] if active else None
    attempt["finished_at_utc"] = format_utc(clock())
    storage.write_json(attempt_path(attempt["attempt_id"]), attempt)
    return attempt


def _sync(
    root: Path,
    storage: RawStorage,
    client: httpx.Client,
    clock: Clock,
    new_id: IdFactory,
    start_date: date,
    accept_changed: frozenset[str],
) -> dict[str, Any]:
    active = read_active(root)
    previous = read_generation(root, active["generation_id"]) if active else None
    floor = date.fromisoformat(active["checkpoint"]) if active else start_date
    since = floor - timedelta(days=LOOKBACK_DAYS) if active else start_date
    run_id = new_id("run", clock())
    candidate = Candidate(
        generation_id=f"gen-{run_id.removeprefix('run-')}",
        run_id=run_id,
        since=since,
        checkpoint_floor=floor,
        records={r["document_number"]: r for r in (previous or {}).get("records", [])},
        review={r["document_number"]: r for r in (previous or {}).get("review", [])},
    )
    context = AcquisitionContext(
        run_id=run_id, storage=storage, client=client, clock=clock, new_id=new_id
    )
    search = search_directives(context, since)
    candidate.failures.extend(search.problems)
    if search.complete:
        versions = VersionIndex.from_receipts(
            root, exclude_run_id=run_id, require_artifacts=True
        )
        for entry in search.entries:
            _consider(candidate, context, versions, search, entry, accept_changed)

    relationships, unresolved = derive_relationships(candidate.records)
    checks = validate_candidate(root, candidate, search, relationships)
    passed = not candidate.failures and all(check["passed"] for check in checks)
    changed = bool(
        candidate.new_documents
        or candidate.counts["changed"]
        or candidate.counts["quarantined"]
    )
    decided_at = clock()
    if candidate.documents:
        storage.write_json(
            f"validation/{candidate.generation_id}.json",
            build_validation_report(
                generation_id=candidate.generation_id,
                created_at=decided_at,
                documents=candidate.documents,
            ),
        )
    summary: dict[str, Any] = {
        "since": since.isoformat(),
        "acquisition_run_id": run_id,
        "search_receipt_ids": [r["receipt_id"] for r in search.receipts],
        "counts": dict(sorted(candidate.counts.items())),
        "failures": candidate.failures
        + [f"check {c['check']}: {c['detail']}" for c in checks if not c["passed"]],
        "new_documents": candidate.new_documents,
    }
    if passed and active is not None and not changed:
        summary["outcome"] = NO_CHANGE
        summary["checkpoint"] = active["checkpoint"]
        return summary

    generation = _generation(
        candidate, search, previous, relationships, unresolved, checks, decided_at
    )
    write_generation(storage, generation)
    receipt_id = new_id("decision", decided_at)
    decision = {
        "receipt_id": receipt_id,
        "receipt_type": "promotion" if passed else "rejection",
        "generation_id": candidate.generation_id,
        "previous_generation_id": active["generation_id"] if active else None,
        "decided_at_utc": format_utc(decided_at),
        "checkpoint": generation["checkpoint"],
        "reasons": summary["failures"],
    }
    storage.write_json(decision_path(receipt_id), decision)
    summary["generation_id"] = candidate.generation_id
    summary["decision_receipt_id"] = receipt_id
    if not passed:
        summary["outcome"] = REJECTED
        summary["checkpoint"] = active["checkpoint"] if active else None
        return summary
    write_active(
        root,
        {
            "generation_id": candidate.generation_id,
            "checkpoint": generation["checkpoint"],
            "decision_receipt_id": receipt_id,
            "previous_generation_id": decision["previous_generation_id"],
            "updated_at_utc": format_utc(decided_at),
        },
    )
    summary["outcome"] = PROMOTED
    summary["checkpoint"] = generation["checkpoint"]
    return summary


def _consider(
    candidate: Candidate,
    context: AcquisitionContext,
    versions: VersionIndex,
    search: SearchOutcome,
    entry: dict[str, Any],
    accept_changed: frozenset[str],
) -> None:
    """Classify one search entry as unchanged, changed, skipped, or new."""
    number = entry["document_number"]
    candidate.counts["searched"] += 1
    digest = entry_digest(entry)
    search_receipt_id = search.entry_receipts[number]
    evidence = _evidence(candidate.run_id, search_receipt_id)
    prior = candidate.records.get(number) or candidate.review.get(number)
    if prior is not None:
        if prior["entry_sha256"] == digest:
            candidate.counts["unchanged"] += 1
            return
        candidate.counts["changed"] += 1
        reason = _expected_change(prior["source_entry"], entry)
        if reason is None and number in accept_changed:
            reason = "accepted_by_operator"
        if reason is None:
            candidate.unaccepted_changes.append(number)
            candidate.failures.append(
                f"{number}: search metadata changed since generation "
                f"{prior['versions'][-1]['generation_id']} (entry SHA-256 "
                f"{prior['entry_sha256'][:12]} -> {digest[:12]}). Investigate, "
                f"then rerun with --accept-changed {number}."
            )
            return
        updated = {
            **prior,
            "source_entry": entry,
            "entry_sha256": digest,
            "evidence": {**prior["evidence"], "search": evidence},
            "versions": prior["versions"]
            + [_version(candidate, digest, search_receipt_id, reason)],
        }
        (candidate.records if number in candidate.records else candidate.review)[
            number
        ] = updated
        return

    problems = identifier_problems(entry)
    if problems:
        candidate.counts["failed"] += 1
        candidate.failures.extend(f"{number}: {problem}" for problem in problems)
        return
    if not is_airworthiness_directive(entry):
        candidate.counts["not_directive"] += 1
        candidate.skipped.append({"document_number": number, "title": entry["title"]})
        return

    record = _base_record(candidate, entry, digest, evidence, search_receipt_id)
    iae = names_international_aero_engines(entry["title"])
    if iae and not DOCUMENT_NUMBER_PATTERN.fullmatch(number):
        decision = needs_review(
            "A Federal Register correction or republication of an IAE "
            "directive; read it and the document it corrects by hand."
        )
    elif iae:
        candidate.counts["read_in_full"] += 1
        document = acquire_document(context, number, versions)
        candidate.documents.append(document)
        if document.failed:
            candidate.counts["failed"] += 1
            candidate.failures.append(f"{number}: {describe_failure(document)}")
            return
        # The document is new to the corpus, so a "changed" version can only
        # differ from an earlier attempt that was never promoted (per-document
        # API JSON drifts in fields such as comment counts). It is recorded,
        # not treated as a change to a corpus identity.
        earlier = [v.as_record() for v in document.versions if v.status == "changed"]
        if earlier:
            record["changed_since_unpromoted_attempt"] = earlier
        decision = _classify_document(context, document, record)
    else:
        decision = outside_by_title()
    record["scope"] = decision.as_record()
    record["coverage_state"] = decision.coverage_state
    candidate.new_documents.append(number)
    candidate.counts["new"] += 1
    if not record["ad_numbers"]:
        record["review_reason"] = "No AD number appears in the docket identifiers."
    elif decision.needs_review:
        record["review_reason"] = decision.detail
    if "review_reason" in record:
        candidate.counts["quarantined"] += 1
        candidate.review[number] = record
    else:
        candidate.records[number] = record


def _classify_document(
    context: AcquisitionContext, document: DocumentAcquisition, record: dict[str, Any]
) -> ScopeDecision:
    xml_receipt = next(
        receipt
        for receipt in document.receipts
        if receipt["receipt_id"] == document.full_text_xml_receipt_id
    )
    record["evidence"]["api_json"] = _evidence(context.run_id, document.api_receipt_id)
    record["evidence"]["full_text_xml"] = _evidence(
        context.run_id, document.full_text_xml_receipt_id
    )
    record["replaced_ads"] = list(document.replaced_ads)
    material = document.incorporated_material
    if material is not None and material.determined:
        record["incorporated_material"] = {
            "paragraph": material.paragraph,
            "items": list(material.items),
        }
    body = (
        context.storage.root / xml_receipt["artifact"]["relative_path"]
    ).read_bytes()
    if is_correction(document.api_record or {}):
        decision = classify_applicability(body, document.document_number)
        # A correction is never itself the evaluated directive.
        if decision.coverage_state == EVALUATED:
            return needs_review(
                "A correction of an evaluated directive needs a person to "
                "confirm the evaluated rules still hold."
            )
        return decision
    return classify_applicability(body, document.document_number)


def describe_failure(document: DocumentAcquisition) -> str:
    """One line naming what failed for a directive read in full."""
    parts = list(document.problems)
    parts += [
        f"missing {entry['representation_role']} ({entry['reason_code']})"
        for entry in document.missing
    ]
    parts += [
        f"{record['representation_role']} failed {record['check']}: {record['detail']}"
        for validation in document.validations
        for record in validation.records()
        if record["outcome"] == "failed"
    ]
    parts += [
        f"unexpected hash change in {version.key[3]}"
        for version in document.versions
        if version.status == "changed"
    ]
    return "; ".join(parts) or "acquisition failed"


def identifier_problems(entry: dict[str, Any]) -> list[str]:
    """Identifiers and dates that must parse before a record is accepted."""
    problems = []
    if not DISCOVERED_DOCUMENT_NUMBER.fullmatch(str(entry.get("document_number"))):
        problems.append("document number does not parse")
    if not _is_iso_date(entry.get("publication_date")):
        problems.append(f"publication date {entry.get('publication_date')!r}")
    effective = entry.get("effective_on")
    if effective is not None and not _is_iso_date(effective):
        problems.append(f"effective date {effective!r}")
    if entry.get("type") != FINAL_RULE_TYPE:
        problems.append(f"unexpected document type {entry.get('type')!r}")
    if not isinstance(entry.get("title"), str) or not entry["title"]:
        problems.append("title missing")
    return problems


def is_airworthiness_directive(entry: dict[str, Any]) -> bool:
    """A part 39 rule titled as an AD or carrying an AD number."""
    return str(entry.get("title", "")).startswith(AD_TITLE_PREFIX) or bool(
        airworthiness_directive_numbers(entry)
    )


def _corrects_another(entry: dict[str, Any]) -> bool:
    return is_correction(entry) or bool(entry.get("correction_of"))


def corrected_document(entry: dict[str, Any]) -> str | None:
    """The document ``correction_of`` names, given as a number or an API URL."""
    value = entry.get("correction_of")
    if not isinstance(value, str):
        return None
    number = value.rstrip("/").rsplit("/", 1)[-1].removesuffix(".json")
    return number if DISCOVERED_DOCUMENT_NUMBER.fullmatch(number) else None


def _is_iso_date(value: Any) -> bool:
    if not isinstance(value, str):
        return False
    try:
        date.fromisoformat(value)
    except ValueError:
        return False
    return len(value) == 10


def _evidence(run_id: str, receipt_id: str | None) -> dict[str, str]:
    if receipt_id is None:
        raise ValueError("evidence needs a receipt")
    return {
        "receipt_id": receipt_id,
        "receipt_path": receipt_path(run_id, receipt_id),
        "run_id": run_id,
    }


def _expected_change(old: dict[str, Any], new: dict[str, Any]) -> str | None:
    """Name a change that needs no investigation, or return ``None``.

    The only expected change is the Federal Register adding a correction to an
    original document's ``corrections`` list; every other field must match.
    """
    differing = {key for key in old.keys() | new.keys() if old.get(key) != new.get(key)}
    old_list, new_list = old.get("corrections") or [], new.get("corrections") or []
    if (
        differing == {"corrections"}
        and isinstance(new_list, list)
        and set(old_list) < set(new_list)
    ):
        return "corrections_added"
    return None


def _version(
    candidate: Candidate, digest: str, receipt_id: str, change: str | None = None
) -> dict[str, Any]:
    version: dict[str, Any] = {
        "generation_id": candidate.generation_id,
        "entry_sha256": digest,
        "search_receipt_id": receipt_id,
    }
    if change is not None:
        version["change"] = change
    return version


def _base_record(
    candidate: Candidate,
    entry: dict[str, Any],
    digest: str,
    evidence: dict[str, str],
    receipt_id: str,
) -> dict[str, Any]:
    return {
        "document_number": entry["document_number"],
        "ad_numbers": sorted(airworthiness_directive_numbers(entry)),
        "faa_dockets": sorted(faa_docket_numbers(entry)),
        "kind": "correction" if _corrects_another(entry) else "final_rule",
        "title": entry["title"],
        "publication_date": entry["publication_date"],
        "effective_on": entry.get("effective_on"),
        "html_url": entry.get("html_url"),
        "source_entry": entry,
        "entry_sha256": digest,
        "evidence": {"search": evidence},
        "first_seen_generation_id": candidate.generation_id,
        "versions": [_version(candidate, digest, receipt_id)],
    }


def derive_relationships(
    records: dict[str, dict[str, Any]],
) -> tuple[list[dict[str, Any]], list[dict[str, Any]]]:
    """Corrections and supersessions among the records, and links left open.

    A document whose ``correction_of`` names another links to it as a
    source assertion. Otherwise the joins are the frozen-manifest ones from
    ``acquisition.manifest``: a correction links to the original final rule
    sharing its AD number, and an AD supersedes the AD its "Affected ADs"
    paragraph says it replaces.
    """
    by_ad: dict[str, list[str]] = defaultdict(list)
    for number, record in sorted(records.items()):
        for ad in record["ad_numbers"]:
            by_ad[ad].append(number)
    adapters = {number: _adapter(record) for number, record in records.items()}
    relationships: list[dict[str, Any]] = []
    unresolved: list[dict[str, Any]] = []
    for number, record in sorted(records.items()):
        asserted = corrected_document(record["source_entry"])
        if asserted is not None:
            if asserted in records:
                relationships.append(_asserted_correction(record, records[asserted]))
            else:
                unresolved.append(
                    {
                        "relationship_type": "corrects",
                        "from_document": number,
                        "reason": f"The corrected document {asserted} is not in "
                        "the discovery corpus.",
                    }
                )
        elif record["kind"] == "correction":
            targets = sorted(
                other
                for ad in record["ad_numbers"]
                for other in by_ad[ad]
                if records[other]["kind"] == "final_rule"
            )
            found = correction_relationships(
                [adapters[number]] + [adapters[n] for n in targets]
            )
            found = [r for r in found if r["from_identity"]["value"] == number]
            relationships.extend(found)
            if not found:
                unresolved.append(
                    {
                        "relationship_type": "corrects",
                        "from_document": number,
                        "reason": "No original final rule with AD number "
                        f"{', '.join(record['ad_numbers']) or '(none)'} is in "
                        "the discovery corpus.",
                    }
                )
        for replaced in record.get("replaced_ads", []):
            related = [n for n in by_ad.get(replaced, []) if n != number]
            found = supersession_relationships(
                [adapters[number]] + [adapters[n] for n in related]
            )
            found = [r for r in found if r["from_identity"]["value"] == number]
            relationships.extend(found)
            if not found:
                unresolved.append(
                    {
                        "relationship_type": "supersedes",
                        "from_document": number,
                        "to_ad_number": replaced,
                        "reason": f"AD {replaced} is not in the discovery corpus.",
                    }
                )
    return relationships, unresolved


def _asserted_correction(
    correction: dict[str, Any], target: dict[str, Any]
) -> dict[str, Any]:
    receipts = [
        correction["evidence"]["search"]["receipt_id"],
        target["evidence"]["search"]["receipt_id"],
    ]
    return {
        "relationship_type": "corrects",
        "from_identity": {
            "namespace": DOCUMENT_NAMESPACE,
            "value": correction["document_number"],
        },
        "to_identity": {
            "namespace": DOCUMENT_NAMESPACE,
            "value": target["document_number"],
        },
        "evidence_receipt_ids": list(dict.fromkeys(receipts)),
        "confidence_class": "source_asserted",
    }


def _adapter(record: dict[str, Any]) -> DocumentAcquisition:
    """Present a stored record to the frozen-manifest relationship joins."""
    evidence = record["evidence"]
    document = DocumentAcquisition(
        record["document_number"], evidence["search"]["run_id"]
    )
    document.api_record = record["source_entry"]
    document.api_receipt_id = evidence.get("api_json", evidence["search"])["receipt_id"]
    if "full_text_xml" in evidence:
        document.full_text_xml_receipt_id = evidence["full_text_xml"]["receipt_id"]
        document.replaced_ads = tuple(record.get("replaced_ads", []))
    return document


def validate_candidate(
    root: Path,
    candidate: Candidate,
    search: SearchOutcome,
    relationships: list[dict[str, Any]],
) -> list[dict[str, Any]]:
    """Run the promotion checks; each returns ``passed`` and a detail."""
    every = {**candidate.records, **candidate.review}
    checks = [
        _check(
            "search_complete",
            search.complete,
            f"{len(search.entries)} result(s) across {len(search.receipts)} page(s)"
            if search.complete
            else "; ".join(search.problems),
        ),
        _check(
            "acquisitions_complete",
            not any(d.failed for d in candidate.documents),
            f"{len(candidate.documents)} directive(s) read in full",
        ),
    ]
    identifier_failures = [
        f"{number}: {problem}"
        for number, record in every.items()
        for problem in identifier_problems(record["source_entry"])
    ]
    checks.append(
        _check(
            "identifiers_and_dates",
            not identifier_failures,
            "; ".join(identifier_failures) or f"{len(every)} record(s) parse",
        )
    )
    evidence_failures = _evidence_failures(root, candidate.run_id, every)
    checks.append(
        _check(
            "raw_evidence_retained",
            not evidence_failures,
            "; ".join(evidence_failures[:20])
            or "every record's receipts are retained; this run's bytes verified",
        )
    )
    relationship_failures = _relationship_failures(relationships, candidate.records)
    checks.append(
        _check(
            "relationships_valid",
            not relationship_failures,
            "; ".join(relationship_failures)
            or f"{len(relationships)} relationship(s) resolve",
        )
    )
    unaccepted = candidate.unaccepted_changes
    checks.append(
        _check(
            "no_unexpected_changes",
            not unaccepted,
            f"{candidate.counts['changed']} changed record(s), "
            f"{len(unaccepted)} not accepted",
        )
    )
    claim_failures = [
        number
        for number, record in every.items()
        if record["coverage_state"] not in COVERAGE_STATES
        or (record["coverage_state"] == EVALUATED and number not in EVALUATED_DOCUMENTS)
    ]
    checks.append(
        _check(
            "evaluated_claim_bounded",
            not claim_failures,
            ", ".join(claim_failures)
            or "only AD 2025-19-13 (2025-18469) may be evaluated",
        )
    )
    return checks


def _check(name: str, passed: bool, detail: str) -> dict[str, Any]:
    return {"check": name, "passed": passed, "detail": detail}


def _evidence_failures(
    root: Path, run_id: str, records: dict[str, dict[str, Any]]
) -> list[str]:
    """Receipts must exist for every record; this run's bytes must verify.

    Bytes from earlier runs are verified when they are first promoted. In CI
    they are not kept between runs (see DISCOVERY_SYNC.md), so carried-forward
    records are checked against their retained receipts.
    """
    failures = []
    verified: dict[str, str | None] = {}
    for number, record in sorted(records.items()):
        for role, evidence in sorted(record["evidence"].items()):
            receipt_id = evidence["receipt_id"]
            if receipt_id not in verified:
                verified[receipt_id] = _verify_receipt(root, run_id, evidence)
            problem = verified[receipt_id]
            if problem:
                failures.append(f"{number} {role}: {problem}")
    return failures


def _verify_receipt(root: Path, run_id: str, evidence: dict[str, str]) -> str | None:
    path = root / evidence["receipt_path"]
    if not path.is_file():
        return f"receipt {evidence['receipt_id']} is not retained"
    receipt = json.loads(path.read_text(encoding="utf-8"))
    if receipt.get("acquisition_status") != "succeeded":
        return f"receipt {evidence['receipt_id']} records a failed acquisition"
    if receipt["acquisition_run_id"] != run_id:
        return None
    artifact = receipt["artifact"]
    try:
        body = (root / artifact["relative_path"]).read_bytes()
    except OSError:
        return f"artifact {artifact['relative_path']} is not retained"
    if hashlib.sha256(body).hexdigest() != artifact["sha256"]:
        return f"artifact {artifact['relative_path']} does not match its receipt"
    return None


def _relationship_failures(
    relationships: list[dict[str, Any]], records: dict[str, dict[str, Any]]
) -> list[str]:
    failures = []
    for relationship in relationships:
        ends = (relationship["from_identity"], relationship["to_identity"])
        names = [end["value"] for end in ends]
        if any(
            end["namespace"] != DOCUMENT_NAMESPACE or end["value"] not in records
            for end in ends
        ):
            failures.append(f"{relationship['relationship_type']} {names} dangles")
            continue
        known = {
            evidence["receipt_id"]
            for name in names
            for evidence in records[name]["evidence"].values()
        }
        if not set(relationship["evidence_receipt_ids"]) <= known:
            failures.append(
                f"{relationship['relationship_type']} {names} cites unknown receipts"
            )
    return failures


def _generation(
    candidate: Candidate,
    search: SearchOutcome,
    previous: dict[str, Any] | None,
    relationships: list[dict[str, Any]],
    unresolved: list[dict[str, Any]],
    checks: list[dict[str, Any]],
    created_at: datetime,
) -> dict[str, Any]:
    records = sorted(
        candidate.records.values(),
        key=lambda r: (r["publication_date"], r["document_number"]),
    )
    review = sorted(
        candidate.review.values(),
        key=lambda r: (r["publication_date"], r["document_number"]),
    )
    published = [
        e["publication_date"]
        for e in search.entries
        if isinstance(e.get("publication_date"), str)
        and _is_iso_date(e["publication_date"])
    ]
    checkpoint = max([candidate.checkpoint_floor.isoformat(), *published])
    by_state: dict[str, int] = defaultdict(int)
    for record in records:
        by_state[record["coverage_state"]] += 1
    return {
        "schema_version": GENERATION_SCHEMA_VERSION,
        "generation_id": candidate.generation_id,
        "corpus_track": CORPUS_TRACK,
        "created_at_utc": format_utc(created_at),
        "previous_generation_id": previous["generation_id"] if previous else None,
        "acquisition_run_id": candidate.run_id,
        "query": {
            "publication_date_gte": candidate.since.isoformat(),
            "search_receipt_ids": [r["receipt_id"] for r in search.receipts],
            "reported_count": search.count,
        },
        "checkpoint": checkpoint,
        "counts": {
            **dict(sorted(candidate.counts.items())),
            "records": len(records),
            "review": len(review),
            "by_coverage_state": dict(sorted(by_state.items())),
        },
        "new_documents": candidate.new_documents,
        "records": records,
        "review": review,
        "skipped_not_directive": candidate.skipped,
        "relationships": relationships,
        "unresolved_relationships": unresolved,
        "dependencies": dependencies(records),
        "notes": list(GENERATION_NOTES),
        "validation": {
            "status": "passed"
            if not candidate.failures and all(c["passed"] for c in checks)
            else "failed",
            "checks": checks,
            "failures": candidate.failures,
        },
    }


def dependencies(records: list[dict[str, Any]]) -> list[dict[str, Any]]:
    """Known unavailable dependencies: incorporated material and FAA DRS."""
    found = []
    for record in records:
        material = record.get("incorporated_material")
        if not material:
            continue
        for item in material["items"]:
            found.append(
                {
                    "name": item,
                    "dependency_type": "incorporated_material",
                    "availability_status": "unavailable",
                    "document_number": record["document_number"],
                    "ad_numbers": record["ad_numbers"],
                }
            )
    found.append(
        {
            "name": "FAA Dynamic Regulatory System (DRS) records",
            "dependency_type": "source_access",
            "availability_status": "deferred_access_verification",
            "detail": "DRS corroboration stays deferred until its API contract "
            "is verified.",
        }
    )
    return found


def rollback(
    storage_root: Path,
    *,
    to_generation: str | None = None,
    clock: Clock = utc_now,
    new_id: IdFactory = random_id,
) -> dict[str, Any]:
    """Point ``active.json`` back at an earlier promoted generation.

    Without ``to_generation`` the target is the active generation's
    predecessor. The target must have been promoted before. A rollback
    receipt names both generations; the checkpoint returns to the target's,
    so the next sync searches again from there.
    """
    root = require_discovery_root(storage_root)
    storage = RawStorage(root)
    active = read_active(root)
    if active is None:
        raise RollbackError("no generation is active")
    current = read_generation(root, active["generation_id"])
    target_id = to_generation or current["previous_generation_id"]
    if not target_id:
        raise RollbackError(
            f"{active['generation_id']} has no previous generation to return to"
        )
    if target_id == active["generation_id"]:
        raise RollbackError(f"{target_id} is already active")
    promoted = {
        json.loads(path.read_text(encoding="utf-8"))["generation_id"]
        for path in (root / "decisions").glob("*.json")
        if json.loads(path.read_text(encoding="utf-8"))["receipt_type"] == "promotion"
    }
    if target_id not in promoted:
        raise RollbackError(f"{target_id} was never promoted")
    target = read_generation(root, target_id)
    decided_at = clock()
    receipt_id = new_id("decision", decided_at)
    storage.write_json(
        decision_path(receipt_id),
        {
            "receipt_id": receipt_id,
            "receipt_type": "rollback",
            "generation_id": target_id,
            "previous_generation_id": active["generation_id"],
            "decided_at_utc": format_utc(decided_at),
            "checkpoint": target["checkpoint"],
            "reasons": [f"rolled back from {active['generation_id']}"],
        },
    )
    pointer = {
        "generation_id": target_id,
        "checkpoint": target["checkpoint"],
        "decision_receipt_id": receipt_id,
        "previous_generation_id": target["previous_generation_id"],
        "updated_at_utc": format_utc(decided_at),
    }
    write_active(root, pointer)
    return pointer
