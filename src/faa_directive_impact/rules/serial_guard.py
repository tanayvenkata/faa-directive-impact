"""Reject rule records that state an identifier the directive does not print.

A serial number decides whether an engine is affected, so a record must never
carry one that is not in the directive's own regulatory text. The guard walks
the whole record and checks every value held under an identifier key (serial
numbers, range bounds and exclusions, part numbers, engine models) against the
identifier tokens of the governing document and the final rule, as the
committed retrieval corpus (``evaluation/retrieval/corpus.json``) records them
from paragraph (a) on. A serial list held only in incorporated material
cannot pass: it is recorded as an unavailable dependency instead.
"""

from collections.abc import Iterator
from typing import Any

from faa_directive_impact.retrieval.corpus import normalize

# Keys whose values are identifiers. Any schema field holding a serial or part
# number must use one of these names (a test checks the v2 schema).
IDENTIFIER_KEYS = frozenset(
    {
        "serial_number",
        "serial_numbers",
        "excluded",
        "first",
        "last",
        "part_number",
        "part_numbers",
        "engine_models",
        "models",
    }
)


def record_identifiers(value: Any, path: str = "") -> Iterator[tuple[str, str]]:
    """Every (path, identifier) the record holds under an identifier key."""
    if isinstance(value, dict):
        for key, item in value.items():
            child = f"{path}.{key}" if path else key
            if key in IDENTIFIER_KEYS:
                if isinstance(item, str):
                    yield child, item
                elif isinstance(item, list):
                    for index, entry in enumerate(item):
                        if isinstance(entry, str):
                            yield f"{child}[{index}]", entry
                        else:
                            yield from record_identifiers(entry, f"{child}[{index}]")
                else:
                    yield from record_identifiers(item, child)
            else:
                yield from record_identifiers(item, child)
    elif isinstance(value, list):
        for index, item in enumerate(value):
            yield from record_identifiers(item, f"{path}[{index}]")


def invented_identifiers(
    record: dict[str, Any], corpus: dict[str, Any]
) -> list[tuple[str, str]]:
    """Identifiers in the record that its directive's text does not contain.

    Empty means the record passes. A document missing from the corpus fails
    every identifier: nothing can be confirmed against it.
    """
    documents = {
        record["final_rule_document"],
        record["governing_document"]["document"],
    }
    printed: set[str] = set()
    for entry in corpus["records"]:
        if entry["document"] in documents:
            printed.update(entry["identifiers"])
    return [
        (path, value)
        for path, value in record_identifiers(record)
        if normalize(value) not in printed
    ]
