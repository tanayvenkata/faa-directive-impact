"""Logical source versions derived from retained receipts.

The version index is rebuilt from receipts on every run and is never a source
of truth. Receipts whose artifacts failed validation are excluded. A logical source version is one distinct content hash for one
source identity and representation. Runs keep their own copies of the bytes;
an unchanged rerun adds a receipt but no new logical version.
"""

import hashlib
import json
from collections import defaultdict
from dataclasses import dataclass
from pathlib import Path
from typing import Any

# API JSON fields that change without any change to the document itself.
VOLATILE_API_JSON_FIELDS = ("page_views",)

VersionKey = tuple[str, str, str, str, str]


@dataclass(frozen=True)
class VersionObservation:
    """How one successful retrieval relates to earlier retained versions."""

    receipt_id: str
    key: VersionKey
    status: str  # "new", "unchanged", or "changed"
    content_hash: str
    previous_content_hashes: tuple[str, ...]

    def as_record(self) -> dict[str, Any]:
        system, namespace, value, role, graphic = self.key
        record: dict[str, Any] = {
            "receipt_id": self.receipt_id,
            "source_system": system,
            "source_document_identity": {"namespace": namespace, "value": value},
            "representation_role": role,
            "status": self.status,
            "content_hash": self.content_hash,
            "previous_content_hashes": list(self.previous_content_hashes),
        }
        if graphic:
            record["source_graphic_identifier"] = graphic
        return record


def version_key(receipt: dict[str, Any]) -> VersionKey:
    identity = receipt["source_document_identity"]
    return (
        receipt["source_system"],
        identity["namespace"],
        identity["value"],
        receipt["representation_role"],
        receipt.get("source_graphic_identifier", ""),
    )


def content_hash(receipt: dict[str, Any], storage_root: Path) -> str:
    """Return the hash that defines a logical version for this receipt.

    For API JSON, volatile fields are removed before hashing a canonical form,
    so a page-view counter does not look like a document change. Every other
    representation uses the SHA-256 of its exact retained bytes.
    """
    artifact = receipt["artifact"]
    if receipt["representation_role"] != "api_json":
        return artifact["sha256"]
    path = storage_root / artifact["relative_path"]
    # An unreadable artifact falls back to its byte hash and will classify as
    # changed. A6 turns this into an explicit integrity failure.
    try:
        record = json.loads(path.read_bytes())
    except (OSError, ValueError):
        return artifact["sha256"]
    if not isinstance(record, dict):
        return artifact["sha256"]
    for field in VOLATILE_API_JSON_FIELDS:
        record.pop(field, None)
    canonical = json.dumps(record, sort_keys=True, separators=(",", ":"))
    return "stable-json:" + hashlib.sha256(canonical.encode()).hexdigest()


class VersionIndex:
    """Content hashes already retained for each source identity."""

    def __init__(self, storage_root: Path) -> None:
        self._storage_root = storage_root
        self._hashes: dict[VersionKey, list[str]] = defaultdict(list)

    @classmethod
    def from_receipts(
        cls, storage_root: Path, exclude_run_id: str | None = None
    ) -> "VersionIndex":
        index = cls(storage_root)
        rejected = _receipts_failing_validation(storage_root)
        receipts_root = storage_root / "receipts"
        for path in sorted(receipts_root.glob("*/*.json")):
            if path.parent.name == exclude_run_id:
                continue
            receipt = json.loads(path.read_text(encoding="utf-8"))
            if (
                receipt.get("acquisition_status") == "succeeded"
                and receipt["receipt_id"] not in rejected
            ):
                index._add(receipt)
        return index

    def observe(self, receipt: dict[str, Any]) -> VersionObservation:
        """Classify a successful receipt against earlier versions, then add it."""
        key = version_key(receipt)
        previous = tuple(self._hashes.get(key, ()))
        current = content_hash(receipt, self._storage_root)
        if not previous:
            status = "new"
        elif current in previous:
            status = "unchanged"
        else:
            status = "changed"
        self._add(receipt, current)
        return VersionObservation(receipt["receipt_id"], key, status, current, previous)

    def _add(self, receipt: dict[str, Any], current: str | None = None) -> None:
        key = version_key(receipt)
        current = current or content_hash(receipt, self._storage_root)
        if current not in self._hashes[key]:
            self._hashes[key].append(current)


def _receipts_failing_validation(storage_root: Path) -> set[str]:
    """Receipts whose artifacts failed validation never become versions."""
    rejected = set()
    for path in (storage_root / "validation").glob("*.json"):
        report = json.loads(path.read_text(encoding="utf-8"))
        rejected.update(
            finding["receipt_id"]
            for finding in report.get("findings", [])
            if finding.get("outcome") == "failed"
        )
    return rejected
