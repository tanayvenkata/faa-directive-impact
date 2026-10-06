"""S1 rules baseline: screen one engine against AD 2025-19-13.

The rules read the normalized record (``directives.hpt_hub_record``), never the
raw XML, and return a structured answer in which every statement cites the
paragraph it rests on. They are plain conditionals and arithmetic: no model,
no retrieval.

The logic is ported from ``evaluation.hpt_hub_reference``, the oracle written
alongside the seed labels, and adds citations and wording. Agreement with the
labels therefore shows that these rules reproduce one reading of the AD, not
that the reading is independently correct.

Paragraph (g) timing, with SV the next qualifying shop visit after the
effective date, L the engine counter at which a hub reaches its table 1 limit,
and G the effective-date counter plus the (g) window:

- no qualifying visit: latest = max(L, G);
- SV < G: the text reads two ways (A = max(min(SV, L), G), B = min(SV,
  max(L, G))); the informal FAA answer (faa-informal-2026-10-05) gives
  max(L, G), and all three are reported;
- SV >= G: A and B agree.
"""

from dataclasses import asdict, dataclass, field
from datetime import date
from typing import Any

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
FAA_ADJUDICATION = "faa-informal-2026-10-05"
UNKNOWN = "unknown"
PROHIBITION = (
    "Do not install an HPT 1st-stage or 2nd-stage hub whose P/N and S/N are "
    "listed in table 1 to paragraph (g)."
)
QUEUES = {
    "action_required": "potentially_affected",
    "action_required_on_event": "potentially_affected",
    "needs_review": "needs_review",
    "no_action_triggered": "no_action_or_not_applicable",
    "does_not_apply": "no_action_or_not_applicable",
    "outside_supported_scope": "no_action_or_not_applicable",
    "unknown": "needs_review",
}


@dataclass
class Citation:
    document: str
    paragraph: str
    locator: str | None = None
    supports: str = ""


@dataclass
class HubFinding:
    position: str
    part_number: str | None
    serial_number: str | None
    outcome: str  # matched | not_listed | missing | identity_unconfirmed
    statement: str
    table_row: dict[str, Any] | None = None
    latest_engine_flight_cycles: int | None = None
    component_cycles_remaining: int | None = None
    readings: dict[str, int] = field(default_factory=dict)
    adjudication: str | None = None
    timing: str | None = None


@dataclass
class Screen:
    directive: str
    ad_number: str
    applicability: str
    action_status: str | None
    authority_state: str = "in_force"
    computed: dict[str, Any] = field(default_factory=dict)
    missing_facts: list[str] = field(default_factory=list)
    continuing_obligations: list[dict[str, str]] = field(default_factory=list)
    citations: list[Citation] = field(default_factory=list)
    hubs: list[HubFinding] = field(default_factory=list)
    summary: str = ""
    timing: str | None = None
    notes: list[str] = field(default_factory=list)

    @property
    def queue(self) -> str:
        return QUEUES[self.action_status or self.applicability]

    def cite(self, paragraph: str, supports: str, locator: str | None = None):
        citation = Citation(self.directive, paragraph, locator, supports)
        if citation not in self.citations:
            self.citations.append(citation)

    def to_dict(self) -> dict[str, Any]:
        result = asdict(self)
        result["queue"] = self.queue
        return result


def screen(record: dict[str, Any], asset: dict[str, Any], as_of: date) -> Screen:
    """Screen one engine snapshot against the directive as of a date."""
    result = Screen(
        record["document"], record["ad_number"], "applies", "no_action_triggered"
    )
    model = asset["engine"]["engine_model"]
    if model == UNKNOWN:
        result.applicability, result.action_status = "unknown", "needs_review"
        result.missing_facts.append("engine.engine_model")
        result.cite("(c)", "the applicable engine models")
        result.summary = (
            "The engine model is not recorded, so applicability cannot be "
            "decided against the models listed in paragraph (c)."
        )
        return result
    if model not in SUPPORTED_ENGINE_MODELS:
        result.applicability, result.action_status = "outside_supported_scope", None
        result.cite("(c)", "the applicable engine models")
        result.summary = (
            f"{model} is not one of the supported V2500-A5/D5/E5 variants. "
            "This screen makes no applicability determination for it."
        )
        return result
    if model not in record["applicable_models"]:
        result.applicability, result.action_status = "does_not_apply", None
        result.cite("(c)", f"{model} is not among the listed models")
        result.summary = f"{model} is not listed in paragraph (c)."
        return result

    result.cite("(c)", f"{model} is a listed model")
    effective = date.fromisoformat(record["effective_date"])
    in_force = as_of >= effective
    if not in_force:
        result.authority_state = "published_not_yet_effective"
        result.cite("(a)", f"the AD takes effect on {effective.isoformat()}")

    rows = record["table_1"]["rows"]
    components = {c["component_name"]: c for c in asset["installed_components"]}
    for position in sorted({row["component"] for row in rows}):
        result.hubs.extend(_check_position(result, rows, position, components))

    matched = [hub for hub in result.hubs if hub.outcome == "matched"]
    if not in_force:
        _not_yet_effective(result, record, matched, effective)
        return result

    result.continuing_obligations.append({"paragraph": "(h)", "text": PROHIBITION})
    result.cite("(h)", "installation prohibition binding every listed engine")
    for hub in matched:
        _time_hub(result, record, asset, hub, effective)

    _operator_claims(result, asset, bool(matched))

    diverging = any(
        hub.adjudication is None and len(set(hub.readings.values())) > 1
        for hub in matched
    )
    if (
        matched
        and not diverging
        and all(h.latest_engine_flight_cycles is not None for h in matched)
    ):
        result.action_status = "action_required"
    elif matched or result.missing_facts:
        result.action_status = "needs_review"
    else:
        result.action_status = "no_action_triggered"
    result.computed = _computed(matched)
    result.summary = _summary(result, model)
    result.timing = _engine_timing(result, matched)
    return result


def _check_position(
    result: Screen,
    rows: list[dict[str, Any]],
    position: str,
    components: dict[str, dict[str, Any]],
) -> list[HubFinding]:
    """Compare the installed hub in one table 1 position with the table."""
    component = components.get(position)
    if component is None:
        result.missing_facts.append(f"installed_components[{position}]")
        result.cite("(g)", f"no {position} record to compare", "table 1")
        return [
            HubFinding(
                position,
                None,
                None,
                "missing",
                f"No {position} record was supplied, so a listed hub can be "
                "neither found nor excluded.",
            )
        ]
    part_number = component["part_number"]
    serial_number = component["serial_number"]
    listed_parts = {row["part_number"] for row in rows}
    if part_number == UNKNOWN:
        result.missing_facts.append(f"installed_components[{position}].part_number")
        result.cite("(g)", f"{position} P/N unknown", f"table 1 rows for {position}")
        return [
            HubFinding(
                position,
                None,
                serial_number,
                "missing",
                f"The {position} P/N is unknown, so the hub cannot be compared "
                "with table 1.",
            )
        ]
    if part_number in listed_parts and serial_number == UNKNOWN:
        result.missing_facts.append(f"installed_components[{position}].serial_number")
        result.cite(
            "(g)",
            f"{position} has a listed P/N",
            f"table 1 rows for P/N {part_number}",
        )
        return [
            HubFinding(
                position,
                part_number,
                None,
                "missing",
                f"The {position} has listed P/N {part_number}, but its S/N is "
                "unknown, so it may be a listed hub.",
            )
        ]

    exact = [
        row
        for row in rows
        if (row["part_number"], row["serial_number"]) == (part_number, serial_number)
    ]
    if exact:
        findings = []
        for row in exact:
            result.cite(
                "(g)",
                f"{position} P/N and S/N match a listed row",
                f"table 1 row S/N {row['serial_number']}",
            )
            findings.append(
                HubFinding(
                    position,
                    part_number,
                    serial_number,
                    "matched",
                    f"The {position} P/N {part_number} S/N {serial_number} "
                    "matches table 1 to paragraph (g) (removal limit "
                    f"{row['removal_limit_cycles_since_new']:,} cycles since new).",
                    table_row=row,
                )
            )
        return findings

    # A listed S/N in its own position under another or differently written
    # P/N may be a mis-keyed record of the listed part; only the record holder
    # can settle it. An S/N that merely resembles a listed one is not matched.
    findings = []
    for row in rows:
        if row["component"] != position or not _same_identifier(
            row["serial_number"], serial_number
        ):
            continue
        field_name = (
            "serial_number" if row["part_number"] == part_number else "part_number"
        )
        result.missing_facts.append(f"installed_components[{position}].{field_name}")
        result.cite(
            "(g)",
            "a listed S/N recorded under a different identity",
            f"table 1 row S/N {row['serial_number']}",
        )
        result.cite("(i)(1)", "eligible parts are defined by P/N and S/N")
        findings.append(
            HubFinding(
                position,
                part_number,
                serial_number,
                "identity_unconfirmed",
                f"The {position} is recorded as P/N {part_number} S/N "
                f"{serial_number}. Table 1 lists P/N {row['part_number']} S/N "
                f"{row['serial_number']} (removal limit "
                f"{row['removal_limit_cycles_since_new']:,} cycles since new). "
                "Paragraph (i)(1) defines eligible parts by P/N and S/N, so a "
                "person must confirm whether this is the listed part before "
                "either removal or no action can be stated.",
                table_row=row,
            )
        )
    if findings:
        return findings

    result.cite("(g)", "the installed P/N and S/N pairs", "table 1 (no matching row)")
    elsewhere = [
        row
        for row in rows
        if row["serial_number"] == serial_number and row["part_number"] != part_number
    ]
    detail = (
        f" S/N {serial_number} is listed only with P/N {elsewhere[0]['part_number']}."
        if elsewhere
        else ""
    )
    return [
        HubFinding(
            position,
            part_number,
            serial_number,
            "not_listed",
            f"The {position} P/N {part_number} S/N {serial_number} is not a "
            f"P/N and S/N pair in table 1.{detail}",
        )
    ]


def _time_hub(
    result: Screen,
    record: dict[str, Any],
    asset: dict[str, Any],
    hub: HubFinding,
    effective: date,
) -> None:
    """Compute removal timing for one matched hub, or name what is missing."""
    assert hub.table_row is not None
    engine = asset["engine"]
    component = next(
        c for c in asset["installed_components"] if c["component_name"] == hub.position
    )
    limit = hub.table_row["removal_limit_cycles_since_new"]
    window = record["grace_flight_cycles_after_effective_date"]
    engine_readings = {
        date.fromisoformat(r["at"]): r["engine_flight_cycles"]
        for r in engine.get("engine_cycle_readings", [])
    }
    at_effective = engine_readings.get(effective)
    # Hub cycles at the effective date come from the hub's own record, never
    # from engine cycles: the two differ once a hub has moved between engines.
    csn_at_effective = {
        date.fromisoformat(r["at"]): r["cycles_since_new"]
        for r in component.get("cycles_since_new_readings", [])
    }.get(effective)
    csn_now = component.get("cycles_since_new")
    missing = []
    if at_effective is None:
        missing.append(f"engine.engine_cycle_readings[{effective.isoformat()}]")
    if csn_at_effective is None:
        missing.append(
            f"installed_components[{hub.position}]"
            f".cycles_since_new_readings[{effective.isoformat()}]"
        )
    if not isinstance(csn_now, int):
        missing.append(f"installed_components[{hub.position}].cycles_since_new")
    if missing or at_effective is None or csn_at_effective is None:
        result.missing_facts.extend(missing)
        hub.timing = (
            f"Removal of the {hub.position} is required under paragraph (g), but "
            "its deadline cannot be computed until these are supplied: "
            + "; ".join(missing)
            + "."
        )
        return
    assert isinstance(csn_now, int)

    result.cite("(a)", f"effective date {effective.isoformat()} anchors the timing")
    result.cite("(i)(2)", "what counts as an engine shop visit", "engine shop visit")
    limit_at = at_effective + (limit - csn_at_effective)
    window_at = at_effective + window
    hub.component_cycles_remaining = limit - csn_now
    visit_at = _next_qualifying_shop_visit(asset, record["ad_number"], effective)
    now = max(engine_readings.items())[1] if engine_readings else None
    past = (
        f" The hub is already {-hub.component_cycles_remaining:,} cycles past "
        "its listed limit."
        if hub.component_cycles_remaining < 0
        else f" ({hub.component_cycles_remaining:,} hub cycles remain to the "
        "listed limit.)"
    )
    by_limit = (
        f"before it exceeds {limit:,} cycles since new, no later than engine "
        f"counter {limit_at:,}"
    )
    by_window = (
        f"within {window} flight cycles after {effective.isoformat()}, no later "
        f"than engine counter {window_at:,}"
    )

    if visit_at is None:
        hub.latest_engine_flight_cycles = max(limit_at, window_at)
        if limit_at >= window_at:
            hub.timing = (
                f"Remove the {hub.position} at the next qualifying engine shop "
                f"visit (paragraph (i)(2)), and {by_limit}.{past} The "
                f"{window}-flight-cycle window after the effective date ends "
                f"earlier (counter {window_at:,}), so it does not extend this."
            )
        else:
            remaining = (
                f" That is {window_at - now:,} flight cycles after this snapshot."
                if now is not None and now <= window_at
                else ""
            )
            hub.timing = (
                f"Remove the {hub.position} {by_window}.{remaining}{past} "
                f"Its table 1 limit is reached earlier (counter {limit_at:,}), "
                "but paragraph (g) allows whichever occurs later."
            )
        return

    hub.readings = {
        "A": max(min(visit_at, limit_at), window_at),
        "B": min(visit_at, max(limit_at, window_at)),
    }
    if visit_at < window_at:
        hub.readings["FAA"] = max(limit_at, window_at)
        hub.adjudication = FAA_ADJUDICATION
        hub.latest_engine_flight_cycles = hub.readings["FAA"]
        result.notes.append(
            f"Timing for the {hub.position} follows informal FAA correspondence "
            f"({FAA_ADJUDICATION}), which is not an official interpretation."
        )
        deadline = by_limit if limit_at >= window_at else by_window
        hub.timing = (
            f"The qualifying shop visit at engine counter {visit_at:,} falls "
            f"inside the first {window} flight cycles after the effective date. "
            "Per informal FAA correspondence, removal is not required at that "
            f"visit: remove the {hub.position} {deadline}.{past} Removing it at "
            "that visit is a conservative choice, not an AD requirement. The "
            "two grammatical readings of paragraph (g), not adopted here, give "
            f"counter {hub.readings['A']:,} (A) and {hub.readings['B']:,} (B)."
        )
        return
    if hub.readings["A"] == hub.readings["B"]:
        hub.latest_engine_flight_cycles = hub.readings["A"]
        hub.timing = (
            f"Remove the {hub.position} at the qualifying engine shop visit at "
            f"engine counter {visit_at:,}, and {by_limit}; the latest point is "
            f"counter {hub.latest_engine_flight_cycles:,}.{past}"
        )


def _not_yet_effective(
    result: Screen,
    record: dict[str, Any],
    matched: list[HubFinding],
    effective: date,
) -> None:
    window = record["grace_flight_cycles_after_effective_date"]
    result.action_status = "no_action_triggered"
    result.missing_facts.clear()
    result.summary = (
        f"The engine model is listed in paragraph (c), but {record['ad_number']} "
        f"does not take effect until {effective.isoformat()} (paragraph (a)). "
        "Nothing is required yet."
    )
    if matched:
        hubs = "; ".join(
            f"{hub.position} S/N {hub.serial_number} (limit "
            f"{hub.table_row['removal_limit_cycles_since_new']:,} cycles since new)"
            for hub in matched
            if hub.table_row
        )
        result.timing = (
            f"From {effective.isoformat()}, paragraph (g) requires removing the "
            f"listed hub ({hubs}) at the next qualifying engine shop visit before "
            f"it exceeds its limit, or within {window} flight cycles after the "
            "effective date, whichever occurs later. Per informal FAA "
            f"correspondence ({FAA_ADJUDICATION}), a shop visit within the first "
            f"{window} flight cycles does not by itself require earlier removal. "
            "The paragraph (h) installation prohibition also begins on that date."
        )


def _operator_claims(result: Screen, asset: dict[str, Any], matched: bool) -> None:
    """Report operator assertions as facts to verify; never let them clear."""
    ad = result.ad_number
    claims = [c for c in asset.get("amoc_claims", []) if c["ad"] == ad]
    if claims:
        result.cite("(j)", "AMOCs must be approved by the FAA before use")
        result.notes.append(
            "An AMOC is claimed, but no FAA approval is on file. The paragraph "
            "(g) action stands unless a person verifies an approved AMOC and "
            "its scope."
        )
        if matched:
            result.missing_facts.append(f"amoc_claims[{ad}]")
    for record in asset.get("ad_records", []):
        if record["ad"] == ad:
            result.notes.append(
                f"The operator's AD record shows '{record['recorded_status']}'. "
                "This screen does not use that record; a person should review it "
                "against the findings above."
            )
    if any(e["event_type"] in ("repair", "inspection") for e in asset["events"]):
        result.notes.append(
            "Recorded repairs and inspections do not change applicability or "
            "the table 1 limits (14 CFR 39.15), and are not treated as shop "
            "visits unless recorded as one."
        )


def _computed(matched: list[HubFinding]) -> dict[str, Any]:
    computed: dict[str, Any] = {}
    latest = [h.latest_engine_flight_cycles for h in matched]
    remaining = [h.component_cycles_remaining for h in matched]
    if any(value is not None for value in latest):
        computed["latest_engine_flight_cycles"] = min(
            v for v in latest if v is not None
        )
    if any(value is not None for value in remaining):
        computed["component_cycles_remaining"] = min(
            v for v in remaining if v is not None
        )
    readings = [h.readings for h in matched if h.readings]
    if len(readings) == 1:
        computed["readings"] = readings[0]
    return computed


def _summary(result: Screen, model: str) -> str:
    applies = f"{model} is listed in paragraph (c), so the AD applies."
    if result.action_status == "action_required":
        return f"{applies} A listed hub is installed; paragraph (g) requires removal."
    if result.action_status == "needs_review":
        return (
            f"{applies} A required fact is missing or unconfirmed, so the outcome "
            "is left to a person."
        )
    return (
        f"{applies} No installed hub matches a table 1 row, so no removal is "
        "triggered by the supplied records. The paragraph (h) installation "
        "prohibition continues to bind this engine."
    )


def _engine_timing(result: Screen, matched: list[HubFinding]) -> str | None:
    timed = [h for h in matched if h.timing]
    if not timed:
        return None
    text = " ".join(h.timing for h in timed if h.timing)
    dated = [h for h in timed if h.latest_engine_flight_cycles is not None]
    if len(dated) > 1:
        first = min(dated, key=lambda h: h.latest_engine_flight_cycles or 0)
        text += (
            f" Each listed hub must be removed; the earliest deadline is the "
            f"{first.position}'s, engine counter "
            f"{first.latest_engine_flight_cycles:,}."
        )
    for hub in result.hubs:
        if hub.outcome in ("missing", "identity_unconfirmed"):
            text += (
                f" Whether the {hub.position} must also be removed is unknown "
                "until its missing or unconfirmed record is resolved."
            )
    if any(fact.startswith("amoc_claims[") for fact in result.missing_facts):
        text += " A verified, FAA-approved AMOC could change this deadline."
    return text


def _same_identifier(listed: str, recorded: str) -> bool:
    """Compare identifiers ignoring case and whitespace."""
    return "".join(listed.split()).upper() == "".join(recorded.split()).upper()


def _next_qualifying_shop_visit(
    asset: dict[str, Any], ad_number: str, effective: date
) -> int | None:
    visits = [
        event["engine_flight_cycles_at_event"]
        for event in asset.get("events", [])
        if event["event_type"] == "shop_visit_induction"
        and date.fromisoformat(event["at"]) > effective
        and event.get("qualifies_as_engine_shop_visit", {}).get(ad_number) == "yes"
        and "engine_flight_cycles_at_event" in event
    ]
    return min(visits) if visits else None
