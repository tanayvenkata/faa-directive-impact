"""The compact on-disk form of the fleet screen.

Every engine's screens repeat the same summaries, timings, notes, missing
facts, and citations (a few hundred distinct values across thousands of
screens). The slim form stores each distinct value once in a content-addressed
table, keyed by the first ten hex characters of its SHA-256, and a screen
refers to values by key. Keys depend only on content, so a rule change touches
only the table entries it changes and the screens that now point at them.

``slim_fleet_screen`` and ``expand_fleet_screen`` are exact inverses: the
expanded form is the full per-engine screen, field for field.
"""

import hashlib
import json
import re
from typing import Any

SLIM_FORMAT = "slim-1"
KEY_LENGTH = 10
# Screen fields holding one string (or null), a list of strings, or citations.
SCALAR_FIELDS = ("summary", "timing")
LIST_FIELDS = ("notes", "missing_facts")
CITATION_FIELD = "citations"
STRING_TABLE = "strings"
CITATION_TABLE = "citation_table"
# Lists made only of table keys are written on one line, so the file stays
# short without changing what it parses to.
KEY_LIST = re.compile(r'\[\s*("[0-9a-f]{10}"(?:,\s*"[0-9a-f]{10}")*)\s*\]')


def _key(value: Any) -> str:
    text = json.dumps(value, sort_keys=True, ensure_ascii=False, separators=(",", ":"))
    return hashlib.sha256(text.encode()).hexdigest()[:KEY_LENGTH]


def _intern(table: dict[str, Any], value: Any) -> str:
    key = _key(value)
    if table.setdefault(key, value) != value:
        raise ValueError(f"table key collision on {key}")
    return key


def slim_fleet_screen(screened: dict[str, Any]) -> dict[str, Any]:
    """The fleet screen with repeated strings and citations moved to tables."""
    strings: dict[str, Any] = {}
    citations: dict[str, Any] = {}
    engines = []
    for engine in screened["engines"]:
        slim_screens = {}
        for document, entry in engine["screens"].items():
            slim = dict(entry)
            for field in SCALAR_FIELDS:
                if entry[field] is not None:
                    slim[field] = _intern(strings, entry[field])
            for field in LIST_FIELDS:
                slim[field] = [_intern(strings, item) for item in entry[field]]
            slim[CITATION_FIELD] = [
                _intern(citations, item) for item in entry[CITATION_FIELD]
            ]
            slim_screens[document] = slim
        engines.append({**engine, "screens": slim_screens})
    return {
        **{k: v for k, v in screened.items() if k != "engines"},
        "format": SLIM_FORMAT,
        STRING_TABLE: dict(sorted(strings.items())),
        CITATION_TABLE: dict(sorted(citations.items())),
        "engines": engines,
    }


def expand_fleet_screen(slim: dict[str, Any]) -> dict[str, Any]:
    """The full fleet screen; a screen that is not slim is returned as it is."""
    if slim.get("format") != SLIM_FORMAT:
        return slim
    strings, citations = slim[STRING_TABLE], slim[CITATION_TABLE]
    engines = []
    for engine in slim["engines"]:
        screens = {}
        for document, entry in engine["screens"].items():
            full = dict(entry)
            for field in SCALAR_FIELDS:
                if entry[field] is not None:
                    full[field] = strings[entry[field]]
            for field in LIST_FIELDS:
                full[field] = [strings[key] for key in entry[field]]
            full[CITATION_FIELD] = [citations[key] for key in entry[CITATION_FIELD]]
            screens[document] = full
        engines.append({**engine, "screens": screens})
    keep = {"format", STRING_TABLE, CITATION_TABLE, "engines"}
    return {**{k: v for k, v in slim.items() if k not in keep}, "engines": engines}


def dump_slim(slim: dict[str, Any]) -> str:
    text = json.dumps(slim, indent=2, sort_keys=True, ensure_ascii=False)
    text = KEY_LIST.sub(lambda m: "[" + re.sub(r"\s+", "", m.group(1)) + "]", text)
    return text + "\n"
