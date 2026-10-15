"""Summarize the U.S. V2500 fleet from the FAA Aircraft Registry.

The demo fleet's shape (airframe types, engine models, and build years) is
drawn from the real population of U.S.-registered aircraft with IAE V2500
engines. Only aggregate counts are kept: no registration number, owner, or
airframe serial leaves this module, so no invented engine state can be read
as a claim about a real aircraft.

Input is the Registry's public download (``ReleasableAircraft.zip``,
extracted): ``MASTER.txt``, ``ACFTREF.txt``, and ``ENGINE.txt``.
"""

import csv
from collections import Counter
from pathlib import Path
from typing import Any

REGISTRY_URL = "https://registry.faa.gov/database/ReleasableAircraft.zip"
# The Registry often records the engine only as "V2500SERIES"; the airframe
# model fixes the variant (Airbus and Boeing type certificate data sheets).
VARIANT_BY_AIRFRAME = {
    "A319-131": "V2522-A5",
    "A319-132": "V2524-A5",
    "A320-232": "V2527-A5",
    "A320-233": "V2527E-A5",
    "A321-231": "V2533-A5",
    "A321-232": "V2530-A5",
    "MD-90-30": "V2525-D5",
}


def summarize_registry(extracted: Path) -> dict[str, Any]:
    engines = _table(extracted / "ENGINE.txt", key=0, columns=(1, 2))
    aircraft = _table(extracted / "ACFTREF.txt", key=0, columns=(2,))
    by_airframe: Counter[str] = Counter()
    by_airframe_year: Counter[tuple[str, str]] = Counter()
    recorded_engine: Counter[str] = Counter()
    with (extracted / "MASTER.txt").open(encoding="utf-8-sig", newline="") as handle:
        for row in csv.reader(handle):
            if len(row) < 21 or row[0].strip() == "N-NUMBER":
                continue
            engine = engines.get(row[3].strip())
            if not engine or engine[0] != "IAE" or not engine[1].startswith("V25"):
                continue
            if row[20].strip() != "V":  # registration status: valid
                continue
            airframe = aircraft.get(row[2].strip(), ("unknown",))[0]
            variant = VARIANT_BY_AIRFRAME.get(airframe)
            if variant is None:
                continue
            year = row[4].strip()
            by_airframe[airframe] += 1
            by_airframe_year[(airframe, year if year.isdigit() else "unknown")] += 1
            recorded_engine[engine[1]] += 1
    return {
        "source": REGISTRY_URL,
        "aircraft": sum(by_airframe.values()),
        "engines": 2 * sum(by_airframe.values()),
        "variant_by_airframe": VARIANT_BY_AIRFRAME,
        "by_airframe": dict(sorted(by_airframe.items())),
        "by_airframe_year": [
            {"airframe": airframe, "year": year, "aircraft": count}
            for (airframe, year), count in sorted(by_airframe_year.items())
        ],
        "engine_model_as_recorded": dict(sorted(recorded_engine.items())),
    }


def _table(path: Path, key: int, columns: tuple[int, ...]) -> dict[str, tuple[str, ...]]:
    with path.open(encoding="utf-8-sig", newline="") as handle:
        return {
            row[key].strip(): tuple(row[c].strip() for c in columns)
            for row in csv.reader(handle)
            if len(row) > max(columns)
        }
