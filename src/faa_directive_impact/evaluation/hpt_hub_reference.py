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

B never exceeds A, and they differ only when SV < G.

That case was put to the FAA engineer named in the AD (informal
correspondence, 2026-10-05; see evaluation/seed/adjudication/). The FAA's
stated intent is that the 100 flight cycles is a drawdown for parts already
past their limit: a shop visit inside the window does not force removal, and
the hub is removed at its limit. So when SV < G the reference applies
latest = max(L, G) and records all three readings. When SV >= G, A and B agree
(remove at the shop visit, no later than the limit); the FAA's view of that
case is still pending.
"""

import re
from dataclasses import dataclass, field
from datetime import date, datetime
from typing import Any
from xml.etree.ElementTree import Element

AD_NUMBER = "AD 2025-19-13"
GRACE_FLIGHT_CYCLES = 100
FAA_ADJUDICATION = "faa-informal-2026-10-05"
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
class HubTiming:
    """Removal timing for one installed hub that matches table 1."""

    latest_engine_flight_cycles: int | None = None
    component_cycles_remaining: int | None = None
    readings: dict[str, int] = field(default_factory=dict)
    missing_facts: list[str] = field(default_factory=list)
    adjudication: str | None = None

    @property
    def readings_diverge(self) -> bool:
        """True while competing readings disagree with no adjudication."""
        return self.adjudication is None and len(set(self.readings.values())) > 1


@dataclass
class Derivation:
    applicability: str
    action_status: str | None = None
    authority_state: str = "in_force"
    missing_facts: list[str] = field(default_factory=list)
    continuing_obligations: list[str] = field(default_factory=list)
    hubs: list[HubTiming] = field(default_factory=list)

    @property
    def readings_diverge(self) -> bool:
        return any(hub.readings_diverge for hub in self.hubs)

    @property
    def latest_engine_flight_cycles(self) -> int | None:
        values = [
            hub.latest_engine_flight_cycles
            for hub in self.hubs
            if hub.latest_engine_flight_cycles is not None
        ]
        return min(values) if values else None

    @property
    def component_cycles_remaining(self) -> int | None:
        values = [
            hub.component_cycles_remaining
            for hub in self.hubs
            if hub.component_cycles_remaining is not None
        ]
        return min(values) if values else None

    @property
    def readings(self) -> dict[str, int]:
        recorded = [hub.readings for hub in self.hubs if hub.readings]
        return recorded[0] if len(recorded) == 1 else {}

    @property
    def adjudications(self) -> list[str]:
        return [hub.adjudication for hub in self.hubs if hub.adjudication]


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


def derive(
    asset: dict[str, Any], facts: DirectiveFacts, as_of: date | None = None
) -> Derivation:
    """Derive applicability and action status for AD 2025-19-13.

    Applicability depends only on the engine model. Paragraph (h) binds every
    applicable engine, whether or not a listed hub is installed. Removal is
    required only for an installed hub whose P/N and S/N match table 1.
    Missing hub records are never treated as proof that a hub is absent.
    """
    model = asset["engine"]["engine_model"]
    if model == UNKNOWN:
        return Derivation("unknown", "needs_review", ["engine.engine_model"])
    if model not in SUPPORTED_ENGINE_MODELS:
        return Derivation("outside_supported_scope")
    if model not in facts.applicable_models:
        return Derivation("does_not_apply")
    if as_of is not None and as_of < facts.effective_date:
        # Published but not yet in force: nothing is required, and the
        # installation prohibition does not bind until the effective date.
        return Derivation(
            "applies",
            "no_action_triggered",
            authority_state="published_not_yet_effective",
        )

    result = Derivation("applies", continuing_obligations=["(h)"])
    listed_parts = {row.part_number for row in facts.rows}
    components = {c["component_name"]: c for c in asset["installed_components"]}
    for position in sorted({row.component for row in facts.rows}):
        component = components.get(position)
        if component is None:
            result.missing_facts.append(f"installed_components[{position}]")
            continue
        part_number = component["part_number"]
        serial_number = component["serial_number"]
        if part_number == UNKNOWN:
            result.missing_facts.append(f"installed_components[{position}].part_number")
            continue
        if part_number not in listed_parts:
            continue
        if serial_number == UNKNOWN:
            result.missing_facts.append(
                f"installed_components[{position}].serial_number"
            )
            continue
        for row in facts.rows:
            if (row.part_number, row.serial_number) == (part_number, serial_number):
                result.hubs.append(_timing(asset, facts, component, row))

    for hub in result.hubs:
        result.missing_facts.extend(hub.missing_facts)
    if (
        result.hubs
        and not result.readings_diverge
        and all(hub.latest_engine_flight_cycles is not None for hub in result.hubs)
    ):
        result.action_status = "action_required"
    elif result.hubs or result.missing_facts:
        result.action_status = "needs_review"
    else:
        result.action_status = "no_action_triggered"
    return result


def _timing(
    asset: dict[str, Any],
    facts: DirectiveFacts,
    component: dict[str, Any],
    row: AffectedRow,
) -> HubTiming:
    engine = asset["engine"]
    name = component["component_name"]
    readings = {
        date.fromisoformat(reading["at"]): reading["engine_flight_cycles"]
        for reading in engine.get("engine_cycle_readings", [])
    }
    at_effective = readings.get(facts.effective_date)
    csn_now = component.get("cycles_since_new")
    # Hub cycles at the effective date must come from the hub's own record.
    # Inferring them from engine cycles would assume the hub never moved.
    csn_at_effective = {
        date.fromisoformat(reading["at"]): reading["cycles_since_new"]
        for reading in component.get("cycles_since_new_readings", [])
    }.get(facts.effective_date)
    missing = []
    if at_effective is None:
        missing.append(f"engine.engine_cycle_readings[{facts.effective_date}]")
    if csn_at_effective is None:
        missing.append(
            f"installed_components[{name}].cycles_since_new_readings[{facts.effective_date}]"
        )
    if not isinstance(csn_now, int):
        missing.append(f"installed_components[{name}].cycles_since_new")
    if missing or at_effective is None or csn_at_effective is None:
        return HubTiming(missing_facts=missing)

    limit_at = at_effective + (row.removal_limit_cycles_since_new - csn_at_effective)
    grace_at = at_effective + GRACE_FLIGHT_CYCLES
    shop_visit_at = _next_qualifying_shop_visit(asset, facts.effective_date)
    timing = HubTiming(
        component_cycles_remaining=row.removal_limit_cycles_since_new - csn_now
    )
    if shop_visit_at is None:
        # With no qualifying visit, both readings give max(L, G): the latest
        # removal point unless a qualifying visit intervenes first.
        timing.latest_engine_flight_cycles = max(limit_at, grace_at)
        return timing
    timing.readings = {
        "A": max(min(shop_visit_at, limit_at), grace_at),
        "B": min(shop_visit_at, max(limit_at, grace_at)),
    }
    if shop_visit_at < grace_at:
        timing.readings["FAA"] = max(limit_at, grace_at)
        timing.adjudication = FAA_ADJUDICATION
        timing.latest_engine_flight_cycles = timing.readings["FAA"]
    elif not timing.readings_diverge:
        timing.latest_engine_flight_cycles = timing.readings["A"]
    return timing


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
