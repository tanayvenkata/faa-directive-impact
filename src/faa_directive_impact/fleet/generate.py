"""Generate the seeded demo fleet: 200 synthetic V2500 engines on a real mix.

The fleet is presentation data for the fleet view, not evaluation data. Its
shape comes from the U.S. V2500 population in the FAA Aircraft Registry
(``demo/registry-v2500.json``, aggregate counts only): which airframes, which
engine variants, and which build years. Its state is synthetic: engine serial
numbers in the real format, cycles from build year and airframe utilization,
life-limited parts that change at shop visits, events, and the operator's AD
status records. The rules are pre-declared in ``demo/README.md``.

Engines use the asset shape of the seed cases (``asset_snapshot`` in
``schemas/seed-case.schema.json``), so the same screeners read both. Seed-case
assets for the two directives the fleet view started with, on supported
engine models, are embedded unchanged and tagged with their case id; they are
still scored only by the evaluation runs.

Generation is deterministic: the same seed and inputs give the same fleet,
byte for byte. Each concern draws from its own seeded generator, so changing
one does not reshuffle the others. No identifier printed in a directive is
generated, except the AD 2025-19-13 table 1 hubs planted on purpose.
"""

import math
import random
import re
from dataclasses import dataclass, field
from datetime import date, timedelta
from typing import Any

from faa_directive_impact.impact.hpt_hub_rules import SUPPORTED_ENGINE_MODELS

FLEET_VERSION = 2
DEFAULT_RANDOM_SEED = 20261015
SNAPSHOT_AT = date(2026, 10, 12)
AIRCRAFT = 100
UNKNOWN = "unknown"
SHOP_VISITS_RECORDED_FROM = date(2012, 1, 1)

HPT_HUB_AD = "AD 2025-19-13"
HPC_BLADE_AD = "AD 2026-17-03"
ALS_AD = "AD 2025-17-16"
SEAL_AD_EFFECTIVE = date(2017, 8, 21)  # AD 2017-14-07, paragraph (a)
# Seed cases embedded in the fleet: those for the two directives it began with.
FLEET_DIRECTIVES = ("2025-18469", "2026-16954", "2026-18423")
# Directives whose required inspection repeats (README, "Operator Records").
RECURRING_ADS = ("AD 2012-09-09", "AD 2013-07-10", "AD 2015-10-04", "AD 2019-16-01")
# Directives whose action waits on the next shop visit.
EVENT_WAITING_ADS = (HPT_HUB_AD, HPC_BLADE_AD)

# Cycles a year by airframe family (README, "Cycles").
CYCLES_PER_YEAR = {"A319": 1800, "A320": 1700, "A321": 1500, "MD-90": 1100}
SERIAL_SPANS = {
    # variant suffix -> (first serial number, last, first build year, last)
    "A5": (10002, 17999, 1993.0, 2015.0),
    "D5": (20002, 20400, 1994.0, 2001.0),
}
SERIAL_JITTER = 150

# Table 1 to paragraph (g) of AD 2025-19-13: listed hub P/N, S/N, removal limit.
# The 100-cycle hub (PKLBSK9287) is left out: a year after the effective date
# it would long since have been removed.
LISTED_HUBS = (
    ("HPT 1st-stage hub", "2A5001", "PKLBSS9200", 4800),
    ("HPT 1st-stage hub", "2A5001", "PKLBST7489", 6200),
    ("HPT 2nd-stage hub", "2A4802", "PKLBST5005", 4000),
    ("HPT 2nd-stage hub", "2A4802", "PKLBSS0301", 5000),
    ("HPT 2nd-stage hub", "2A4802", "PKLBSR2100", 6000),
)
BLADE_SET = "3rd stage HPC rotor blade set"
AFFECTED_BLADES = ("6A8353", "6A8688")  # AD 2026-17-03, paragraph (c)
ELIGIBLE_BLADES = ("6C8368", "6C8403", "6A8353-001", "6A8688-001")  # (h)(1)


@dataclass(frozen=True)
class PartSpec:
    """A tracked part: its name (as the rule records read it) and its life."""

    name: str
    life: int
    part_number: str
    serial_prefix: str
    unknown_serial: float
    unknown_cycles: float
    # Part number when installed before SEAL_AD_EFFECTIVE (AD 2017-14-07).
    early_part_number: str | None = None
    variants: tuple[str, ...] = ("A5", "D5")


LIFE_LIMITED_PARTS = (
    PartSpec("HPT 1st-stage hub", 20_000, "2A5001", "PKLBX", 0.04, 0.03),
    PartSpec("HPT 2nd-stage hub", 20_000, "2A4802", "PKLBX", 0.04, 0.03),
    PartSpec("HPC stage 3 to 8 drum", 20_000, "SYN-HPC38-DRUM", "DRMX", 0.02, 0.03),
    PartSpec("LPT stage 6 disk", 25_000, "3A2996", "MAPX", 0.02, 0.03, None, ("A5",)),
    PartSpec(
        "HPT 1st-stage air seal", 15_000, "SYN-HPT1-SEAL", "SLX", 0.02, 0.03, "2A3423"
    ),
    PartSpec(
        "HPT 2nd-stage air seal", 15_000, "SYN-HPT2-SEAL", "SLX", 0.02, 0.03, "2A4157"
    ),
    PartSpec(
        "HPT 2nd-stage ring plate", 15_000, "SYN-HPT2-RING", "RPX", 0.02, 0.03, "2A3437"
    ),
)
# D5 only: AD 2013-07-10 reads both tubes. Not life-limited; installed at build.
SCAVENGE_TUBES = (
    ("No. 4 bearing internal scavenge tube", "2A2074-01"),
    ("No. 4 bearing external scavenge tube", "6A5254"),
)


@dataclass
class _Part:
    spec_name: str
    part_number: str
    serial_number: str
    installed_at: date
    csn_at_install: int


@dataclass
class _Engine:
    index: int
    airframe: str
    family: str
    variant: str
    model: str
    tail: str
    position: int
    built: date
    rate: float  # cycles a day
    year: int  # the aircraft's registry build year
    serial: str = ""
    shop_visits: list[tuple[date, int]] = field(default_factory=list)
    parts: list[_Part] = field(default_factory=list)

    def counter(self, when: date) -> int:
        return max(0, round(self.rate * (when - self.built).days))


def build_fleet(
    seed_cases: list[dict[str, Any]],
    registry: dict[str, Any],
    references: list[dict[str, Any]],
    forbidden: set[str],
    random_seed: int = DEFAULT_RANDOM_SEED,
) -> dict[str, Any]:
    """Return the fleet: generated engines (two per aircraft) plus seed assets.

    ``references`` are the in-scope rule records (effective dates, applicable
    models, serial conditions, which directives define a shop visit);
    ``forbidden`` is every identifier printed in the retrieval corpus.
    """
    embedded = [
        _seed_engine(case)
        for case in sorted(seed_cases, key=lambda case: case["case_id"])
        if set(FLEET_DIRECTIVES) & set(case["directive_candidates"])
        and case["asset_snapshot"]["engine"]["engine_model"] in SUPPORTED_ENGINE_MODELS
    ]
    aircraft = AIRCRAFT - math.ceil(len(embedded) / 2)
    quotas = allocate(registry["by_airframe"], aircraft)
    references = sorted(references, key=lambda r: r["final_rule_document"])
    effective_dates = sorted(
        {date.fromisoformat(r["effective_date"]["date"]) for r in references}
    )
    shop_visit_ads = sorted(
        {
            r["ad_number"]
            for r in references
            for action in r["required_actions"]
            if action["trigger"]["event"] == "engine_shop_visit"
        }
    )
    used = set(forbidden)

    engines = _airframes(registry, quotas, random_seed)
    _assign_serials(engines, used, random_seed)
    states = [_history(engine, used, random_seed) for engine in engines]
    planted = _plant_listed_hubs(engines, states, random_seed)
    assets = []
    for engine, state in zip(engines, states, strict=True):
        assets.append(
            _asset(
                engine,
                state,
                effective_dates,
                shop_visit_ads,
                references,
                random_seed,
            )
        )
    return {
        "fleet_version": FLEET_VERSION,
        "random_seed": random_seed,
        "snapshot_at": SNAPSHOT_AT.isoformat(),
        "synthetic": True,
        "composition": {
            "registry_source": registry["source"],
            "registry_snapshot": registry["snapshot"],
            "registry_aircraft": registry["by_airframe"],
            "generated_aircraft": dict(sorted(quotas.items())),
            "generated_build_years": _build_years(engines),
            "embedded_seed_engines": len(embedded),
            "planted_listed_parts": planted,
        },
        "engines": assets + embedded,
    }


def _build_years(engines: list[_Engine]) -> list[dict[str, Any]]:
    """Generated aircraft per registry airframe and build year."""
    counts: dict[tuple[str, int], int] = {}
    for engine in engines:
        if engine.position == 1:
            key = (engine.airframe, engine.year)
            counts[key] = counts.get(key, 0) + 1
    return [
        {"airframe": airframe, "year": str(year), "aircraft": n}
        for (airframe, year), n in sorted(counts.items())
    ]


def allocate(counts: dict[str, int], total: int) -> dict[str, int]:
    """Largest-remainder allocation of ``total`` in proportion to ``counts``."""
    population = sum(counts.values())
    shares = {k: counts[k] * total / population for k in sorted(counts)}
    quotas = {k: math.floor(v) for k, v in shares.items()}
    left = total - sum(quotas.values())
    by_remainder = sorted(shares, key=lambda k: (-(shares[k] - quotas[k]), k))
    for key in by_remainder[:left]:
        quotas[key] += 1
    return quotas


def _airframes(
    registry: dict[str, Any], quotas: dict[str, int], random_seed: int
) -> list[_Engine]:
    rng = random.Random(f"{random_seed}-airframes")
    years: dict[str, list[tuple[int, int]]] = {}
    for row in registry["by_airframe_year"]:
        if row["year"].isdigit():
            years.setdefault(row["airframe"], []).append(
                (int(row["year"]), row["aircraft"])
            )
    engines: list[_Engine] = []
    tails: dict[str, int] = {}
    for airframe in sorted(quotas):
        family = airframe.split("-")[0] if not airframe.startswith("MD") else "MD-90"
        model = registry["variant_by_airframe"][airframe]
        variant = model.rsplit("-", 1)[1]
        for _ in range(quotas[airframe]):
            year = rng.choices(
                [y for y, _ in years[airframe]], [n for _, n in years[airframe]]
            )[0]
            delivered = date(year, 1, 1) + timedelta(days=rng.randint(0, 364))
            tails[family] = tails.get(family, 0) + 1
            tail = f"SYN-{family}-{tails[family]:03d}"
            for position in (1, 2):
                built = delivered - timedelta(days=rng.randint(30, 150))
                rate = CYCLES_PER_YEAR[family] * rng.uniform(0.85, 1.15) / 365.25
                engines.append(
                    _Engine(
                        len(engines),
                        airframe,
                        family,
                        variant,
                        model,
                        tail,
                        position,
                        built,
                        rate,
                        year,
                    )
                )
    return engines


def _assign_serials(engines: list[_Engine], used: set[str], random_seed: int) -> None:
    """Real-format engine serial numbers, roughly in build-date order."""
    rng = random.Random(f"{random_seed}-serials")
    for variant, (first, last, start, end) in sorted(SERIAL_SPANS.items()):
        group = sorted(
            (e for e in engines if e.variant == variant),
            key=lambda e: (e.built, e.index),
        )
        for engine in group:
            when = engine.built.year + engine.built.timetuple().tm_yday / 366
            target = first + (when - start) / (end - start) * (last - first)
            number = round(target) + rng.randint(-SERIAL_JITTER, SERIAL_JITTER)
            number = min(max(number, first), last)
            while f"V{number}" in used:
                number = number + 1 if number < last else first
            engine.serial = f"V{number}"
            used.add(engine.serial)


def _serial(rng: random.Random, prefix: str, used: set[str]) -> str:
    while True:
        serial = f"{prefix}{rng.randint(0, 99_999):05d}"
        if serial not in used:
            used.add(serial)
            return serial


@dataclass
class _State:
    recent_induction: date | None
    unknown_serial_number: bool
    unknown: dict[str, tuple[bool, bool]]  # part -> (serial unknown, cycles unknown)
    blade_part_number: str | None


def _history(engine: _Engine, used: set[str], random_seed: int) -> _State:
    """Shop visits and the life-limited parts each one left installed."""
    rng = random.Random(f"{random_seed}-engine-{engine.index}")
    now = engine.counter(SNAPSHOT_AT)
    visits = []
    cycles = rng.randint(14_000, 20_000)
    while cycles < now:
        at = engine.built + timedelta(days=round(cycles / engine.rate))
        visits.append((at, engine.counter(at)))
        cycles += rng.randint(11_000, 16_000)
    engine.shop_visits = visits
    next_visit = cycles
    specs = [s for s in LIFE_LIMITED_PARTS if engine.variant in s.variants]
    for spec in specs:
        part = _Part(spec.name, "", "", engine.built, 0)
        for number, (at, counter) in enumerate(visits):
            following = (
                visits[number + 1][1] if number + 1 < len(visits) else next_visit
            )
            at_visit = part.csn_at_install + counter - engine.counter(part.installed_at)
            if at_visit + (following - counter) > spec.life:
                used_csn = rng.randint(2_000, 10_000)
                new = rng.random() < 0.6 or used_csn + (following - counter) > spec.life
                part = _Part(spec.name, "", "", at, 0 if new else used_csn)
        part.part_number = (
            spec.early_part_number
            if spec.early_part_number and part.installed_at < SEAL_AD_EFFECTIVE
            else spec.part_number
        )
        part.serial_number = _serial(rng, spec.serial_prefix, used)
        engine.parts.append(part)
    unknown = {
        spec.name: (
            rng.random() < spec.unknown_serial,
            rng.random() < spec.unknown_cycles,
        )
        for spec in specs
    }
    blades = _blade_part_number(rng)
    induction = None
    if rng.random() < 0.08:
        induction = SNAPSHOT_AT - timedelta(days=rng.randint(1, 17))
    return _State(induction, rng.random() < 0.02, unknown, blades)


def _blade_part_number(rng: random.Random) -> str | None:
    roll = rng.random()
    if roll < 0.06:
        return None  # The operator export has no row for the blade set.
    if roll < 0.13:
        return UNKNOWN
    if roll < 0.45:
        return rng.choice(AFFECTED_BLADES)
    return rng.choice(ELIGIBLE_BLADES)


def _plant_listed_hubs(
    engines: list[_Engine], states: list[_State], random_seed: int
) -> list[dict[str, Any]]:
    """Put the table 1 hubs on engines where they could plausibly still fly."""
    rng = random.Random(f"{random_seed}-planted")
    effective = date(2025, 10, 29)  # AD 2025-19-13, paragraph (a)
    order = list(range(len(engines)))
    rng.shuffle(order)
    taken: set[int] = set()
    planted = []
    for name, part_number, serial, limit in LISTED_HUBS:
        for index in order:
            engine, state = engines[index], states[index]
            if index in taken or state.recent_induction:
                continue
            if any(at > effective for at, _ in engine.shop_visits):
                continue
            part = next(p for p in engine.parts if p.spec_name == name)
            if part.installed_at >= effective or state.unknown[name] != (False, False):
                continue
            csn_now = limit - rng.randint(150, 2_000)
            since_install = engine.counter(SNAPSHOT_AT) - engine.counter(
                part.installed_at
            )
            if csn_now - since_install < 0:
                continue
            part.part_number, part.serial_number = part_number, serial
            part.csn_at_install = csn_now - since_install
            taken.add(index)
            planted.append(
                {
                    "directive": HPT_HUB_AD,
                    "component_name": name,
                    "serial_number": serial,
                    "engine_asset_id": _asset_id(engine),
                }
            )
            break
    return planted


def _asset_id(engine: _Engine) -> str:
    return f"SYN-FLT-{engine.index + 1:04d}"


def _asset(
    engine: _Engine,
    state: _State,
    effective_dates: list[date],
    shop_visit_ads: list[str],
    references: list[dict[str, Any]],
    random_seed: int,
) -> dict[str, Any]:
    reading_dates = sorted(set(effective_dates) | {SNAPSHOT_AT})
    identity = {
        "asset_id": _asset_id(engine),
        "engine_serial_number": UNKNOWN
        if state.unknown_serial_number
        else engine.serial,
        "engine_model": engine.model,
        "aircraft_tail_id": engine.tail,
        "installation_position": engine.position,
        "snapshot_at": SNAPSHOT_AT.isoformat(),
        "engine_cycle_readings": [
            {"at": when.isoformat(), "engine_flight_cycles": engine.counter(when)}
            for when in reading_dates
            if when >= engine.built
        ],
    }
    components = [
        _component(engine, part, state.unknown[part.spec_name], effective_dates)
        for part in engine.parts
    ]
    if engine.variant == "D5":
        for name, part_number in SCAVENGE_TUBES:
            components.append(
                {
                    "component_name": name,
                    "part_number": part_number,
                    "serial_number": "not tracked",
                    "installed_at": engine.built.isoformat(),
                }
            )
    if state.blade_part_number is not None:
        components.append(
            {
                "component_name": BLADE_SET,
                "part_number": state.blade_part_number,
                "serial_number": "not tracked at set level",
            }
        )
    asset: dict[str, Any] = {
        "synthetic": True,
        "engine": identity,
        "installed_components": components,
        "events": _events(engine, state, shop_visit_ads, random_seed),
    }
    records, operator = _operator_records(engine, state, references, random_seed)
    asset["operator"] = operator
    asset["ad_records"] = records
    return asset


def _component(
    engine: _Engine,
    part: _Part,
    unknown: tuple[bool, bool],
    effective_dates: list[date],
) -> dict[str, Any]:
    serial_unknown, cycles_unknown = unknown
    base = engine.counter(part.installed_at)
    component: dict[str, Any] = {
        "component_name": part.spec_name,
        "part_number": part.part_number,
        "serial_number": UNKNOWN if serial_unknown else part.serial_number,
        "installed_at": part.installed_at.isoformat(),
    }
    if cycles_unknown:
        component["cycles_since_new"] = UNKNOWN
        return component
    component["cycles_since_new"] = (
        part.csn_at_install + engine.counter(SNAPSHOT_AT) - base
    )
    readings = [
        {
            "at": when.isoformat(),
            "cycles_since_new": part.csn_at_install + engine.counter(when) - base,
        }
        for when in effective_dates
        if part.installed_at < when <= SNAPSHOT_AT
    ]
    if readings:
        component["cycles_since_new_readings"] = readings
    return component


def _events(
    engine: _Engine, state: _State, shop_visit_ads: list[str], random_seed: int
) -> list[dict[str, Any]]:
    events = [
        {
            "event_type": "shop_visit_induction",
            "at": at.isoformat(),
            "engine_flight_cycles_at_event": counter,
            "qualifies_as_engine_shop_visit": dict.fromkeys(shop_visit_ads, "yes"),
            "detail": "Performance restoration shop visit; life-limited parts "
            "replaced as their lives required.",
            "source_note": "Asserted by the synthetic operator record.",
        }
        for at, counter in engine.shop_visits
        if at >= SHOP_VISITS_RECORDED_FROM
    ]
    if state.recent_induction is not None:
        rng = random.Random(f"{random_seed}-induction-{engine.index}")
        qualifies = rng.choice(("yes", "yes", UNKNOWN))
        events.append(
            {
                "event_type": "shop_visit_induction",
                "at": state.recent_induction.isoformat(),
                "engine_flight_cycles_at_event": engine.counter(state.recent_induction),
                "qualifies_as_engine_shop_visit": dict.fromkeys(
                    shop_visit_ads, qualifies
                ),
                "detail": "Inducted for hot-section and HPC maintenance.",
                "source_note": "Asserted by the synthetic operator record.",
            }
        )
    return events


def _operator_records(
    engine: _Engine,
    state: _State,
    references: list[dict[str, Any]],
    random_seed: int,
) -> tuple[list[dict[str, Any]], dict[str, Any]]:
    """The operator's AD status records, as pre-declared in demo/README.md."""
    rng = random.Random(f"{random_seed}-records-{engine.index}")
    aircraft = random.Random(f"{random_seed}-program-{engine.tail}")
    operator: dict[str, Any] = {"air_carrier_operation": "yes"}
    records = []
    for record in references:
        ad = record["ad_number"]
        if engine.model not in record["applicability"]["engine_models"]:
            continue
        draw = aircraft.random() if ad == ALS_AD else rng.random()
        if draw < 0.06:
            status = None
        elif draw < 0.10:
            status = "open"
        else:
            status = _expected_status(engine, state, record)
        if ad == ALS_AD:
            effective = date.fromisoformat(record["effective_date"]["date"])
            if status == "complied":
                done = effective + timedelta(days=aircraft.randint(20, 85))
                operator["maintenance_program_revision"] = (
                    "Engine ALS Maintenance Scheduling paragraph B.1 revised to "
                    f"incorporate table 1 to paragraph (g) of {ad} on "
                    f"{done.isoformat()}."
                )
            elif status == "open":
                operator["maintenance_program_revision"] = (
                    f"Revision for {ad} not yet incorporated in the maintenance "
                    "program."
                )
        if status is not None:
            records.append(
                {
                    "ad": ad,
                    "recorded_status": status,
                    "detail": "Synthetic operator AD status record.",
                }
            )
    return records, operator


def _expected_status(engine: _Engine, state: _State, record: dict[str, Any]) -> str:
    ad = record["ad_number"]
    for condition in record["applicability"]["engine_serials"]:
        if engine.model in condition["models"] and not _serial_listed(
            engine.serial, condition
        ):
            return "not_applicable"
    if ad in RECURRING_ADS:
        return "recurring"
    if ad == HPT_HUB_AD:
        listed = {serial for _, _, serial, _ in LISTED_HUBS}
        return (
            "open"
            if any(p.serial_number in listed for p in engine.parts)
            else "not_applicable"
        )
    if ad == HPC_BLADE_AD:
        affected = state.blade_part_number in (*AFFECTED_BLADES, UNKNOWN)
        return "open" if affected else "not_applicable"
    return "complied"


SERIAL_FORM = re.compile(r"^([A-Z]+)([0-9]+)$")


def _serial_listed(serial: str, condition: dict[str, Any]) -> bool:
    """Whether an engine S/N falls within a directive's serial condition."""
    if serial in condition["excluded"]:
        return False
    if serial in condition["serial_numbers"]:
        return True
    match = SERIAL_FORM.match(serial)
    if not match:
        return False
    number = int(match.group(2))
    for bounds in condition["ranges"]:
        low, high = (
            None if b is None else int(SERIAL_FORM.match(b).group(2))  # type: ignore[union-attr]
            for b in (bounds["first"], bounds["last"])
        )
        if (low is None or number >= low) and (high is None or number <= high):
            return True
    return False


def _seed_engine(case: dict[str, Any]) -> dict[str, Any]:
    asset = case["asset_snapshot"]
    return {
        **asset,
        "evaluation_case": {
            "case_id": case["case_id"],
            "as_of": case["source_snapshot"]["as_of"],
            "title": case["title"],
        },
    }
