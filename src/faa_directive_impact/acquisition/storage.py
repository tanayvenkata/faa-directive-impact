"""Immutable local raw storage with staged, atomic, no-overwrite publication."""

import hashlib
import json
import os
import tempfile
from collections.abc import Iterator
from contextlib import contextmanager
from dataclasses import dataclass
from pathlib import Path, PurePosixPath
from typing import Any, BinaryIO

STAGING_DIRECTORY = ".staging"
READ_ONLY_MODE = 0o444


class StoragePathError(ValueError):
    """Raised when a relative path would escape the storage root."""


class ArtifactExistsError(FileExistsError):
    """Raised when publication would overwrite an existing artifact."""


@dataclass(frozen=True)
class StagedArtifact:
    """A fully written temporary file and the digest of its exact bytes."""

    path: Path
    byte_length: int
    sha256: str


class HashingWriter:
    """Write chunks to a staging file while counting and hashing them."""

    def __init__(self, handle: BinaryIO, path: Path) -> None:
        self._handle = handle
        self.path = path
        self._digest = hashlib.sha256()
        self.byte_length = 0

    def write(self, chunk: bytes) -> None:
        self._handle.write(chunk)
        self._digest.update(chunk)
        self.byte_length += len(chunk)

    @property
    def sha256(self) -> str:
        return self._digest.hexdigest()

    def sync(self) -> None:
        self._handle.flush()
        os.fsync(self._handle.fileno())


class RawStorage:
    """A storage root whose published files are never replaced in place."""

    def __init__(self, root: Path) -> None:
        self.root = root.resolve()

    def resolve(self, relative_path: str) -> Path:
        """Return the absolute path for a relative path inside the root."""
        pure = PurePosixPath(relative_path)
        if pure.is_absolute() or ".." in pure.parts or not pure.parts:
            raise StoragePathError(f"unsafe storage path: {relative_path!r}")
        resolved = (self.root / pure).resolve()
        if not resolved.is_relative_to(self.root):
            raise StoragePathError(f"path escapes storage root: {relative_path!r}")
        return resolved

    @contextmanager
    def stage(self) -> Iterator[HashingWriter]:
        """Yield a hashing writer over a temporary file that is removed on exit.

        Callers publish the staged file with ``publish`` before the context
        exits. An exception inside the context leaves nothing behind.
        """
        staging = self.root / STAGING_DIRECTORY
        staging.mkdir(parents=True, exist_ok=True)
        descriptor, name = tempfile.mkstemp(dir=staging)
        path = Path(name)
        try:
            with os.fdopen(descriptor, "wb") as handle:
                yield HashingWriter(handle, path)
        finally:
            path.unlink(missing_ok=True)

    def publish(self, writer: HashingWriter, relative_path: str) -> StagedArtifact:
        """Atomically expose a staged file at ``relative_path`` as read-only."""
        final_path = self.resolve(relative_path)
        final_path.parent.mkdir(parents=True, exist_ok=True)
        writer.sync()
        os.chmod(writer.path, READ_ONLY_MODE)
        try:
            # A hard link fails if the destination exists, unlike rename.
            os.link(writer.path, final_path)
        except FileExistsError as error:
            raise ArtifactExistsError(relative_path) from error
        return StagedArtifact(final_path, writer.byte_length, writer.sha256)

    def write_json(self, relative_path: str, record: dict[str, Any]) -> Path:
        """Publish a JSON record with the same no-overwrite guarantee."""
        body = (json.dumps(record, indent=2, sort_keys=True) + "\n").encode()
        with self.stage() as writer:
            writer.write(body)
            return self.publish(writer, relative_path).path
