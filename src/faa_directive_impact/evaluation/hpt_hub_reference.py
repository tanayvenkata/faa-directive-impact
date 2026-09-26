"""Independent reference derivation for AD 2025-19-13 (HPT hub quality escape).

This re-derives seed labels directly from the directive's XML so hand-written
labels can be checked mechanically. It is a verification aid and the first
rules baseline for one directive, not the product's general impact engine.

Paragraph (g) removes a listed hub "at the next engine shop visit after the
effective date ... before exceeding the applicable removal cycle limit ... or
within 100 flight cycles from the effective date ..., whichever occurs later".
With SV the next qualifying shop visit, L the engine counter at which the hub
reaches its limit, and G the effective-date counter plus 100:

- Reading A: latest = max(min(SV, L), G)
- Reading B: latest = min(SV, max(L, G))

B never exceeds A, and they differ only when SV < G. When they differ, the
reference returns ``needs_review`` and reports both results.
"""

import re
from dataclasses import dataclass, field
from datetime import date, datetime
from typing import Any
from xml.etree.ElementTree import Element

AD_NUMBER = "AD 2025-19-13"
GRACE_FLIGHT_CYCLES = 100
SUPPORTED_ENGINE_MODELS = frozenset(
    {
        "V2522-A5",
        "V2524-A5",
        "V2525-D5",
        "V2527-A5",
        "V2527E-A5",
        "V2527M-A5",
        "V2528-D5",
        "V2530-A5",
        "V2531-E5",
        "V2533-A5",
    }
)
MODEL_PATTERN = re.compile(r"\bV25\d\d[EM]?-[ADE]5\b")
EFFECTIVE_PATTERN = re.compile(r"effective (\w+ \d{1,2}, \d{4})")
UNKNOWN = "unknown"


@dataclass(frozen=True)
class AffectedRow:
    component: str
    part_number: str
    serial_number: str
    removal_limit_cycles_since_new: int


@dataclass(frozen=True)
class DirectiveFacts:
    """The predicates this derivation reads from AD 2025-19-13's XML."""

    effective_date: date
    applicable_models: frozenset[str]
    rows: tuple[AffectedRow, ...]


@dataclass
class Derivation:
    classification: str
    missing_facts: list[str] = field(default_factory=list)
    latest_engine_flight_cycles: int | None = None
    component_cycles_remaining: int | None = None
    readings: dict[str, int] = field(default_factory=dict)

    @property
    def readings_diverge(self) -> bool:
        return len(set(self.readings.values())) > 1


def read_directive_facts(root: Element) -> DirectiveFacts:
    """Read the effective date, applicable models, and table 1 rows."""
    sections = _sections(root)
    effective = EFFECTIVE_PATTERN.search(" ".join(sections["(a)"]))
    if effective is None:
        raise ValueError("paragraph (a) has no effective date")
    models = frozenset(MODEL_PATTERN.findall(" ".join(sections["(c)"])))
    rows = []
    for row in sections["(g)-rows"]:
        component, part_number, serial_number, limit = row
        rows.append(
            AffectedRow(
                component, part_number, serial_number, int(limit.replace(",", ""))
            )
        )
    if not models or not rows:
        raise ValueError("applicability models or table 1 rows are missing")
    return DirectiveFacts(
        datetime.strptime(effective.group(1), "%B %d, %Y").date(),
        models,
        tuple(rows),
    )


def derive(asset: dict[str, Any], facts: DirectiveFacts) -> Derivation:
    """Classify one asset snapshot against AD 2025-19-13."""
    engine = asset["engine"]
    model = engine["engine_model"]
    if model == UNKNOWN:
        return Derivation("needs_review", ["engine.engine_model"])
    if model not in SUPPORTED_ENGINE_MODELS:
        return Derivation("outside_supported_scope")
    if model not in facts.applicable_models:
        return Derivation("not_affected_for_directive")

    listed_parts = {row.part_number for row in facts.rows}
    matched: tuple[dict[str, Any], AffectedRow] | None = None
    missing: list[str] = []
    for component in asset["installed_components"]:
        part_number = component["part_number"]
        serial_number = component["serial_number"]
        if part_number == UNKNOWN:
            missing.append(
                f"installed_components[{component['component_name']}].part_number"
            )
            continue
        if part_number not in listed_parts:
            continue
        if serial_number == UNKNOWN:
            missing.append(
                f"installed_components[{component['component_name']}].serial_number"
            )
            continue
        for row in facts.rows:
            if (row.part_number, row.serial_number) == (part_number, serial_number):
                matched = (component, row)
    if matched is None:
        if missing:
            return Derivation("needs_review", missing)
        return Derivation("not_affected_for_directive")

    return _timing(asset, facts, *matched)


def _timing(
    asset: dict[str, Any],
    facts: DirectiveFacts,
    component: dict[str, Any],
    row: AffectedRow,
) -> Derivation:
    engine = asset["engine"]
    readings = {
        date.fromisoformat(reading["at"]): reading["engine_flight_cycles"]
        for reading in engine.get("engine_cycle_readings", [])
    }
    snapshot = date.fromisoformat(engine["snapshot_at"])
    csn_now = component.get("cycles_since_new")
    at_effective = readings.get(facts.effective_date)
    at_snapshot = readings.get(snapshot)
    if not isinstance(csn_now, int) or at_effective is None or at_snapshot is None:
        return Derivation(
            "needs_review",
            ["engine.engine_cycle_readings or component cycles_since_new"],
        )

    csn_at_effective = {
        date.fromisoformat(reading["at"]): reading["cycles_since_new"]
        for reading in component.get("cycles_since_new_readings", [])
    }.get(facts.effective_date, csn_now - (at_snapshot - at_effective))
    limit_at = at_effective + (row.removal_limit_cycles_since_new - csn_at_effective)
    grace_at = at_effective + GRACE_FLIGHT_CYCLES
    shop_visit_at = _next_qualifying_shop_visit(asset, facts.effective_date)

    if shop_visit_at is None:
        # With no qualifying visit, both readings give max(L, G): the latest
        # removal point unless a qualifying visit intervenes first.
        latest = max(limit_at, grace_at)
        result = Derivation("potentially_affected", latest_engine_flight_cycles=latest)
    else:
        reading_a = max(min(shop_visit_at, limit_at), grace_at)
        reading_b = min(shop_visit_at, max(limit_at, grace_at))
        result = Derivation(
            "potentially_affected",
            readings={"A": reading_a, "B": reading_b},
        )
        if result.readings_diverge:
            result.classification = "needs_review"
        else:
            result.latest_engine_flight_cycles = reading_a
    result.component_cycles_remaining = row.removal_limit_cycles_since_new - csn_now
    return result


def _next_qualifying_shop_visit(asset: dict[str, Any], effective: date) -> int | None:
    visits = [
        event["engine_flight_cycles_at_event"]
        for event in asset.get("events", [])
        if event["event_type"] == "shop_visit_induction"
        and date.fromisoformat(event["at"]) > effective
        and event.get("qualifies_as_engine_shop_visit", {}).get(AD_NUMBER) == "yes"
        and "engine_flight_cycles_at_event" in event
    ]
    return min(visits) if visits else None


def _sections(root: Element) -> dict[str, list]:
    """Group paragraph text by lettered heading; collect table rows under (g)."""
    sections: dict[str, list] = {"(a)": [], "(c)": [], "(g)-rows": []}
    current = None
    for element in root.iter():
        text = " ".join("".join(element.itertext()).split())
        if element.tag == "HD":
            label = re.match(r"^\(([a-z])\)", text)
            current = f"({label.group(1)})" if label else None
        elif element.tag == "P" and current in ("(a)", "(c)"):
            sections[current].append(text)
        elif element.tag == "ROW" and current == "(g)":
            cells = [" ".join("".join(cell.itertext()).split()) for cell in element]
            if len(cells) == 4:
                sections["(g)-rows"].append(cells)
    return sections
