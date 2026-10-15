"""Generate the seeded demo fleet: about 200 synthetic V2500 engines.

The fleet is presentation data for the fleet view, not evaluation data. Its
engines use the same asset shape as the seed cases (``asset_snapshot`` in
``schemas/seed-case.schema.json``), so the same screeners read both. Seed-case
assets for the two directives the fleet view shows are embedded unchanged and
tagged with their case id; they are still scored only by the evaluation runs.

Generation is deterministic: the same seed and seed cases give the same fleet,
byte for byte. Every identifier is ``SYN-`` prefixed except the hub serial
numbers taken from table 1 of AD 2025-19-13, which must match the directive to
be found. Unknown is a first-class value: a share of engines carry an unknown
or missing field so that ``needs_review`` comes from missing data, as it would
in a real operator export.
"""

import random
from datetime import date, timedelta
from typing import Any

FLEET_VERSION = 1
DEFAULT_RANDOM_SEED = 20261015
SNAPSHOT_AT = date(2026, 10, 12)
HPT_HUB_EFFECTIVE = date(2025, 10, 29)  # AD 2025-19-13, paragraph (a)
HPC_BLADE_EFFECTIVE = date(2026, 9, 24)  # AD 2026-17-03, paragraph (a)
HPT_HUB_AD = "AD 2025-19-13"
HPC_BLADE_AD = "AD 2026-17-03"
FLEET_DIRECTIVES = frozenset({"2025-18469", "2026-16954", "2026-18423"})
UNKNOWN = "unknown"

# Airframe type -> engine models it can carry, with fleet weights.
AIRFRAMES = (
    ("A320", ("V2527-A5", "V2527E-A5", "V2527M-A5"), 46),
    ("A321", ("V2530-A5", "V2533-A5"), 26),
    ("A319", ("V2522-A5", "V2524-A5"), 14),
    ("MD-90", ("V2525-D5", "V2528-D5"), 6),
    ("C-390", ("V2531-E5",), 3),
)
CYCLES_PER_DAY = {"A319": 4.6, "A320": 4.2, "A321": 3.6, "MD-90": 3.0, "C-390": 1.4}

# Table 1 to paragraph (g) of AD 2025-19-13: listed hub P/N, S/N, removal limit.
LISTED_HUBS = (
    ("HPT 1st-stage hub", "2A5001", "PKLBSK9287", 100),
    ("HPT 1st-stage hub", "2A5001", "PKLBSS9200", 4800),
    ("HPT 1st-stage hub", "2A5001", "PKLBST7489", 6200),
    ("HPT 2nd-stage hub", "2A4802", "PKLBST5005", 4000),
    ("HPT 2nd-stage hub", "2A4802", "PKLBSS0301", 5000),
    ("HPT 2nd-stage hub", "2A4802", "PKLBSR2100", 6000),
)
HUB_PART_NUMBERS = {"HPT 1st-stage hub": "2A5001", "HPT 2nd-stage hub": "2A4802"}
BLADE_SET = "3rd stage HPC rotor blade set"
AFFECTED_BLADES = ("6A8353", "6A8688")  # AD 2026-17-03, paragraph (c)
ELIGIBLE_BLADES = ("6C8368", "6C8403", "6A8353-001", "6A8688-001")  # (h)(1)


def build_fleet(
    seed_cases: list[dict[str, Any]],
    aircraft: int = 89,
    random_seed: int = DEFAULT_RANDOM_SEED,
) -> dict[str, Any]:
    """Return the fleet: generated engines (two per aircraft) plus seed assets."""
    rng = random.Random(random_seed)
    engines = []
    listed = list(LISTED_HUBS)
    rng.shuffle(listed)
    listed_slots = set(rng.sample(range(aircraft * 2), len(listed)))
    for tail in range(aircraft):
        airframe, models, _ = _pick_airframe(rng)
        model = rng.choice(models)
        rate = CYCLES_PER_DAY[airframe]
        for position in (1, 2):
            index = tail * 2 + position - 1
            listed_hub = listed.pop() if index in listed_slots else None
            engines.append(
                _engine(rng, index, airframe, tail, position, model, rate, listed_hub)
            )
    embedded = [
        _seed_engine(case)
        for case in sorted(seed_cases, key=lambda case: case["case_id"])
        if FLEET_DIRECTIVES & set(case["directive_candidates"])
    ]
    return {
        "fleet_version": FLEET_VERSION,
        "random_seed": random_seed,
        "snapshot_at": SNAPSHOT_AT.isoformat(),
        "synthetic": True,
        "engines": engines + embedded,
    }


def _pick_airframe(rng: random.Random) -> tuple[str, tuple[str, ...], int]:
    return rng.choices(AIRFRAMES, weights=[weight for *_, weight in AIRFRAMES])[0]


def _engine(
    rng: random.Random,
    index: int,
    airframe: str,
    tail: int,
    position: int,
    model: str,
    rate: float,
    listed_hub: tuple[str, str, str, int] | None,
) -> dict[str, Any]:
    number = f"{index + 1:04d}"
    since_effective = round((SNAPSHOT_AT - HPT_HUB_EFFECTIVE).days * rate)
    engine_cycles = rng.randint(9_000, 46_000)
    engine = {
        "asset_id": f"SYN-FLT-{number}",
        "engine_serial_number": f"SYN-V25-{number}",
        "engine_model": model,
        "aircraft_tail_id": f"SYN-{airframe}-{tail + 1:03d}",
        "installation_position": position,
        "snapshot_at": SNAPSHOT_AT.isoformat(),
        "engine_cycle_readings": [
            {
                "at": HPT_HUB_EFFECTIVE.isoformat(),
                "engine_flight_cycles": engine_cycles - since_effective,
            },
            {"at": SNAPSHOT_AT.isoformat(), "engine_flight_cycles": engine_cycles},
        ],
    }
    components = [
        _hub(rng, name, number, engine_cycles, since_effective, listed_hub)
        for name in HUB_PART_NUMBERS
    ]
    blades = _blade_set(rng)
    if blades is not None:
        components.append(blades)
    return {
        "synthetic": True,
        "engine": engine,
        "installed_components": components,
        "events": _events(rng, engine_cycles, rate),
    }


def _hub(
    rng: random.Random,
    name: str,
    number: str,
    engine_cycles: int,
    since_effective: int,
    listed_hub: tuple[str, str, str, int] | None,
) -> dict[str, Any]:
    stage = "1" if name.startswith("HPT 1st") else "2"
    if listed_hub is not None and listed_hub[0] == name:
        _, part_number, serial_number, limit = listed_hub
        # Spread listed hubs around their limits: some past, some close, some far.
        cycles = max(since_effective + 50, limit + rng.randint(-2_500, 300))
    else:
        part_number = HUB_PART_NUMBERS[name]
        serial_number = f"SYN-HUB{stage}-{number}"
        cycles = rng.randint(
            since_effective + 200, max(engine_cycles, since_effective + 400)
        )
        roll = rng.random()
        if roll < 0.04:
            serial_number = UNKNOWN
        elif roll < 0.07:
            cycles = UNKNOWN
    hub: dict[str, Any] = {
        "component_name": name,
        "part_number": part_number,
        "serial_number": serial_number,
        "cycles_since_new": cycles,
    }
    if cycles != UNKNOWN:
        hub["cycles_since_new_readings"] = [
            {
                "at": HPT_HUB_EFFECTIVE.isoformat(),
                "cycles_since_new": cycles - since_effective,
            }
        ]
    return hub


def _blade_set(rng: random.Random) -> dict[str, Any] | None:
    roll = rng.random()
    if roll < 0.06:
        return None  # The operator export has no row for the blade set.
    if roll < 0.13:
        part_number = UNKNOWN
    elif roll < 0.45:
        part_number = rng.choice(AFFECTED_BLADES)
    else:
        part_number = rng.choice(ELIGIBLE_BLADES)
    return {
        "component_name": BLADE_SET,
        "part_number": part_number,
        "serial_number": "not tracked at set level",
    }


def _events(
    rng: random.Random, engine_cycles: int, rate: float
) -> list[dict[str, Any]]:
    """A recent shop visit for about one engine in twelve."""
    if rng.random() >= 0.08:
        return []
    days_ago = rng.randint(1, 17)
    at = SNAPSHOT_AT - timedelta(days=days_ago)
    qualifies = rng.choice(("yes", "yes", UNKNOWN))
    return [
        {
            "event_type": "shop_visit_induction",
            "at": at.isoformat(),
            "engine_flight_cycles_at_event": engine_cycles - round(days_ago * rate),
            "qualifies_as_engine_shop_visit": {
                HPT_HUB_AD: qualifies,
                HPC_BLADE_AD: qualifies,
            },
            "detail": "Inducted for hot-section and HPC maintenance.",
            "source_note": "Asserted by the synthetic operator record.",
        }
    ]


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
