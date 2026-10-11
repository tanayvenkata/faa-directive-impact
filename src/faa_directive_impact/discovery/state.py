"""Where the discovery corpus keeps its state, and how the pointer moves.

Layout under the discovery storage root (default ``data/discovery/``)::

    raw/federal-register-search/<run-id>/page-0001.json   search pages
    raw/federal-register/<document>/<run-id>/...           IAE directives
    raw/govinfo/<document>/<run-id>/...
    receipts/<run-id>/<receipt-id>.json                    one per attempt
    validation/<generation-id>.json                        IAE artifact checks
    generations/<generation-id>.json                       candidate manifests
    decisions/<receipt-id>.json                            promote/reject/rollback
    attempts/<attempt-id>.json                             the sync log
    active.json                                            the active pointer

Everything except ``active.json`` is written once and never replaced.
``active.json`` is replaced atomically (temporary file, then rename), so a
reader sees either the old pointer or the new one, never a partial write.
"""

import json
import os
import tempfile
from pathlib import Path
from typing import Any

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


def read_generation(root: Path, generation_id: str) -> dict[str, Any]:
    return read_json(root / generation_path(generation_id))


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
