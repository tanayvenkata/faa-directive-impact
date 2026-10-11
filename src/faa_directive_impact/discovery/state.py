"""Where the discovery corpus keeps its state, and how the pointer moves.

Layout under the discovery storage root (default ``data/discovery/``)::

    raw/federal-register-search/<run-id>/page-0001.json   search pages
    raw/federal-register/<document>/<run-id>/...           IAE directives
    raw/govinfo/<document>/<run-id>/...
    receipts/<run-id>/<receipt-id>.json                    one per attempt
    validation/<generation-id>.json                        IAE artifact checks
    generations/<generation-id>.json                       candidate manifests
    records/<sha[:2]>/<sha256>.json                        directive records
    decisions/<receipt-id>.json                            promote/reject/rollback
    attempts/<attempt-id>.json                             the sync log
    active.json                                            the active pointer

Everything except ``active.json`` is written once and never replaced.
A generation lists its directive records by the SHA-256 of their canonical
JSON, and each record is stored once under ``records/``. Most records are
unchanged from one generation to the next, so the state kept in Git grows by
the new records and a list of references, not by a copy of the corpus.
``active.json`` is replaced atomically (temporary file, then rename), so a
reader sees either the old pointer or the new one, never a partial write.
"""

import hashlib
import json
import os
import tempfile
from pathlib import Path
from typing import Any

from faa_directive_impact.acquisition.storage import RawStorage

ACTIVE_POINTER = "active.json"
# Roots the discovery sync must never write into: the frozen evaluation
# corpora and the accepted frozen generations.
PROTECTED_DIRECTORY_NAMES = ("seed-frozen", "frozen-evaluation", "generations")


class StorageRootRefused(ValueError):
    """The storage root would mix discovery state with frozen evaluation data."""


def require_discovery_root(root: Path) -> Path:
    """Return the resolved root, refusing frozen-evaluation locations.

    A root inside ``seed-frozen``, ``frozen-evaluation``, or ``generations``
    is refused, and so is a directory that contains the frozen corpora (such
    as ``data/`` itself), so discovery receipts never join their version
    history.
    """
    resolved = root.resolve()
    inside = set(resolved.parts) & set(PROTECTED_DIRECTORY_NAMES)
    contains = [
        name for name in PROTECTED_DIRECTORY_NAMES[:2] if (resolved / name).exists()
    ]
    if inside or contains:
        raise StorageRootRefused(
            f"refusing discovery storage root {resolved}: it is inside or "
            f"contains frozen evaluation data ({', '.join(sorted(inside) or contains)})"
        )
    return resolved


def read_json(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def read_active(root: Path) -> dict[str, Any] | None:
    """Return the active pointer, or ``None`` before the first promotion."""
    path = root / ACTIVE_POINTER
    return read_json(path) if path.is_file() else None


def generation_path(generation_id: str) -> str:
    return f"generations/{generation_id}.json"


RECORD_LISTS = ("records", "review")


class RecordStoreError(ValueError):
    """A referenced record is missing or does not match its hash."""


def record_digest(record: dict[str, Any]) -> str:
    canonical = json.dumps(record, sort_keys=True, separators=(",", ":"))
    return hashlib.sha256(canonical.encode()).hexdigest()


def record_path(digest: str) -> str:
    return f"records/{digest[:2]}/{digest}.json"


def write_generation(storage: RawStorage, generation: dict[str, Any]) -> None:
    """Store each record once by its hash, then the generation's references."""
    stored = dict(generation)
    for key in RECORD_LISTS:
        references = []
        for record in generation[key]:
            digest = record_digest(record)
            if not (storage.root / record_path(digest)).is_file():
                storage.write_json(record_path(digest), record)
            references.append(
                {"document_number": record["document_number"], "record_sha256": digest}
            )
        stored[key] = references
    storage.write_json(generation_path(generation["generation_id"]), stored)


def read_generation(root: Path, generation_id: str) -> dict[str, Any]:
    """Return a generation with its record references resolved and verified."""
    generation = read_json(root / generation_path(generation_id))
    for key in RECORD_LISTS:
        records = []
        for reference in generation[key]:
            digest = reference["record_sha256"]
            path = root / record_path(digest)
            if not path.is_file():
                raise RecordStoreError(f"{generation_id}: record {digest} is missing")
            record = read_json(path)
            if record_digest(record) != digest:
                raise RecordStoreError(f"{generation_id}: record {digest} was altered")
            records.append(record)
        generation[key] = records
    return generation


def decision_path(receipt_id: str) -> str:
    return f"decisions/{receipt_id}.json"


def attempt_path(attempt_id: str) -> str:
    return f"attempts/{attempt_id}.json"


def read_attempts(root: Path) -> list[dict[str, Any]]:
    """Every recorded sync attempt, oldest first."""
    directory = root / "attempts"
    return sorted(
        (read_json(path) for path in directory.glob("*.json")),
        key=lambda attempt: (attempt["started_at_utc"], attempt["attempt_id"]),
    )


def read_decisions(root: Path) -> list[dict[str, Any]]:
    """Every promotion, rejection, and rollback receipt, oldest first."""
    directory = root / "decisions"
    return sorted(
        (read_json(path) for path in directory.glob("*.json")),
        key=lambda receipt: (receipt["decided_at_utc"], receipt["receipt_id"]),
    )


def write_active(root: Path, pointer: dict[str, Any]) -> None:
    """Replace ``active.json`` atomically."""
    root.mkdir(parents=True, exist_ok=True)
    body = (json.dumps(pointer, indent=2, sort_keys=True) + "\n").encode()
    descriptor, name = tempfile.mkstemp(dir=root, prefix=".active-", suffix=".tmp")
    try:
        with os.fdopen(descriptor, "wb") as handle:
            handle.write(body)
            handle.flush()
            os.fsync(handle.fileno())
        os.replace(name, root / ACTIVE_POINTER)
    except BaseException:
        Path(name).unlink(missing_ok=True)
        raise
