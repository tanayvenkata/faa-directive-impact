import json
import re
from datetime import date
from pathlib import Path

import yaml

from faa_directive_impact.fleet.build import (
    FLEET_FILE,
    FLEET_SCREEN_FILE,
    compute_fleet,
    corpus_identifiers,
    dump,
    load_inputs,
)
from faa_directive_impact.fleet.generate import (
    AIRCRAFT,
    LISTED_HUBS,
    allocate,
    build_fleet,
)
from faa_directive_impact.fleet.page import render_fleet_page
from faa_directive_impact.fleet.screen import (
    EVALUATED,
    EVALUATED_DIRECTIVES,
    NO_ACTION,
    NOT_YET_EVALUATED,
    QUEUE_ORDER,
    RULE_RECORD_PATHS,
    S1_DOCUMENT,
    _blockers,
    _dependency,
    review_provenance,
    rule_record_path,
)
from faa_directive_impact.fleet.slim import (
    dump_slim,
    expand_fleet_screen,
    slim_fleet_screen,
)

REPO = Path(__file__).resolve().parents[2]


def _computed():
    if not hasattr(_computed, "value"):
        _computed.value = compute_fleet(REPO)
    return _computed.value


def _inputs():
    if not hasattr(_inputs, "value"):
        _inputs.value = load_inputs(REPO)
    return _inputs.value


def _generated(fleet):
    return [e for e in fleet["engines"] if "evaluation_case" not in e]


def _build(cases, random_seed):
    inputs = _inputs()
    return build_fleet(
        cases,
        inputs["registry"],
        list(inputs["references"].values()),
        corpus_identifiers(inputs["corpus"]),
        random_seed=random_seed,
    )


def test_committed_fleet_matches_a_fresh_regeneration():
    fleet, screened = _computed()
    assert (REPO / FLEET_FILE).read_text(encoding="utf-8") == dump(fleet)
    assert (REPO / FLEET_SCREEN_FILE).read_text(encoding="utf-8") == dump_slim(
        slim_fleet_screen(screened)
    )


def test_fleet_generation_is_deterministic():
    assert _build([], 1) == _build([], 1)
    assert _build([], 1) != _build([], 2)


def test_fleet_is_two_hundred_engines_on_one_hundred_aircraft():
    fleet, _ = _computed()
    ids = [engine["engine"]["asset_id"] for engine in fleet["engines"]]
    assert len(ids) == 2 * AIRCRAFT
    assert len(set(ids)) == len(ids)
    assert all(asset_id.startswith("SYN-") for asset_id in ids)
    tails = {e["engine"]["aircraft_tail_id"] for e in _generated(fleet)}
    assert len(tails) * 2 == len(_generated(fleet))


def test_generated_aircraft_follow_the_registry_mix():
    fleet, _ = _computed()
    registry = _inputs()["registry"]
    generated = _generated(fleet)
    quotas = allocate(registry["by_airframe"], len(generated) // 2)
    assert fleet["composition"]["generated_aircraft"] == quotas
    # The largest-remainder share keeps a small type (MD-90-30, 5 of 705).
    assert quotas["MD-90-30"] == 1
    variants = registry["variant_by_airframe"]
    expected_models: dict[str, int] = {}
    for airframe, count in quotas.items():
        model = variants[airframe]
        expected_models[model] = expected_models.get(model, 0) + 2 * count
    models: dict[str, int] = {}
    for engine in generated:
        model = engine["engine"]["engine_model"]
        models[model] = models.get(model, 0) + 1
    assert models == {m: n for m, n in expected_models.items() if n}


def test_build_years_come_from_the_registry_rows():
    fleet, _ = _computed()
    registry = {
        (row["airframe"], row["year"]): row["aircraft"]
        for row in _inputs()["registry"]["by_airframe_year"]
    }
    drawn = fleet["composition"]["generated_build_years"]
    assert sum(row["aircraft"] for row in drawn) == len(_generated(fleet)) // 2
    for row in drawn:
        assert row["year"] != "unknown"
        assert registry.get((row["airframe"], row["year"]), 0) > 0
    per_airframe: dict[str, int] = {}
    for row in drawn:
        per_airframe[row["airframe"]] = (
            per_airframe.get(row["airframe"], 0) + row["aircraft"]
        )
    quotas = fleet["composition"]["generated_aircraft"]
    assert per_airframe == {k: v for k, v in quotas.items() if v}


def test_engine_serials_are_real_format_and_never_printed_in_a_directive():
    fleet, _ = _computed()
    forbidden = corpus_identifiers(_inputs()["corpus"])
    serials = [e["engine"]["engine_serial_number"] for e in _generated(fleet)]
    known = [s for s in serials if s != "unknown"]
    assert len(known) == len(set(known))
    for engine in _generated(fleet):
        serial = engine["engine"]["engine_serial_number"]
        if serial == "unknown":
            continue
        assert serial not in forbidden
        number = int(re.fullmatch(r"V(\d{5})", serial).group(1))
        if engine["engine"]["engine_model"].endswith("-D5"):
            assert 20002 <= number <= 20400
        else:
            assert 10002 <= number <= 17999


def test_only_the_planted_hubs_carry_an_identifier_a_directive_prints():
    fleet, _ = _computed()
    forbidden = corpus_identifiers(_inputs()["corpus"])
    planted = {serial for _, _, serial, _ in LISTED_HUBS}
    printed_serials = set()
    for engine in _generated(fleet):
        for component in engine["installed_components"]:
            if component["serial_number"] in forbidden:
                printed_serials.add(component["serial_number"])
            part_number = component["part_number"]
            if part_number.startswith("SYN-"):
                assert part_number not in forbidden
    assert printed_serials == planted
    assert {
        p["serial_number"] for p in fleet["composition"]["planted_listed_parts"]
    } == planted


def test_part_readings_accrue_with_this_engine():
    """A part reading is only kept while the part was in this engine."""
    fleet, _ = _computed()
    for engine in _generated(fleet):
        counter = {
            r["at"]: r["engine_flight_cycles"]
            for r in engine["engine"]["engine_cycle_readings"]
        }
        now = counter[engine["engine"]["snapshot_at"]]
        for component in engine["installed_components"]:
            csn = component.get("cycles_since_new")
            for reading in component.get("cycles_since_new_readings", []):
                assert reading["at"] > component["installed_at"]
                assert csn - reading["cycles_since_new"] == now - counter[reading["at"]]


def test_every_in_scope_effective_date_has_an_engine_reading():
    fleet, _ = _computed()
    dates = {r["effective_date"]["date"] for r in _inputs()["references"].values()}
    for engine in _generated(fleet):
        readings = {r["at"] for r in engine["engine"]["engine_cycle_readings"]}
        built_after = {d for d in dates if d not in readings}
        first = min(readings)
        assert all(d < first for d in built_after)


def test_every_reference_part_group_finds_its_component_by_name():
    fleet, _ = _computed()

    def key(name):
        return " ".join(name.lower().replace("-", " ").split())

    for record in _inputs()["references"].values():
        read = set(record["applicability"]["parts"]) | {
            a["target"] for a in record["required_actions"] if a["target"]
        }
        for group in record["parts"]:
            if group["id"] not in read:
                continue  # e.g. a part only an installation prohibition names
            names = {key(n) for n in [group["component"], *group["aliases"]]}
            models = set(record["applicability"]["engine_models"])
            engines = [
                e for e in _generated(fleet) if e["engine"]["engine_model"] in models
            ]
            if group["id"] == "lpt6" or group["id"].startswith("tube"):
                engines = [
                    e
                    for e in engines
                    if any(
                        key(c["component_name"]) in names
                        for c in e["installed_components"]
                    )
                ]
                assert engines, (record["ad_number"], group["id"])
            found = [
                e
                for e in engines
                if any(
                    key(c["component_name"]) in names
                    or c["part_number"] in group["part_numbers"]
                    for c in e["installed_components"]
                )
            ]
            assert len(found) >= 0.9 * len(engines), (
                record["ad_number"],
                group["id"],
            )


def test_no_record_says_complied_while_a_named_part_is_installed():
    fleet, _ = _computed()
    planted = {serial for _, _, serial, _ in LISTED_HUBS}
    for engine in _generated(fleet):
        records = {r["ad"]: r["recorded_status"] for r in engine["ad_records"]}
        components = engine["installed_components"]
        if any(c["serial_number"] in planted for c in components):
            assert records.get("AD 2025-19-13") != "complied"
        if any(c["part_number"] in ("6A8353", "6A8688") for c in components):
            assert records.get("AD 2026-17-03") != "complied"


def test_both_engines_of_an_aircraft_share_its_program_state():
    fleet, _ = _computed()
    by_tail: dict[str, set[str]] = {}
    for engine in _generated(fleet):
        statuses = [
            r["recorded_status"]
            for r in engine["ad_records"]
            if r["ad"] == "AD 2025-17-16"
        ]
        state = json.dumps([statuses, engine["operator"]], sort_keys=True)
        by_tail.setdefault(engine["engine"]["aircraft_tail_id"], set()).add(state)
    assert all(len(states) == 1 for states in by_tail.values())


def test_seed_assets_are_embedded_unchanged_and_tagged():
    fleet, _ = _computed()
    embedded = {
        engine["evaluation_case"]["case_id"]: engine
        for engine in fleet["engines"]
        if "evaluation_case" in engine
    }
    assert embedded
    for case_id, engine in embedded.items():
        case = yaml.safe_load(
            (REPO / "evaluation/seed/cases" / f"{case_id}.yaml").read_text()
        )
        asset = {k: v for k, v in engine.items() if k != "evaluation_case"}
        assert asset == case["asset_snapshot"]


def test_unknown_hub_serial_goes_to_needs_review():
    _, screened = _computed()
    unknown = [
        engine
        for engine in screened["engines"]
        if "evaluation_case" not in engine["asset"]
        and any(
            c["component_name"].startswith("HPT")
            and c["component_name"].endswith("hub")
            and c["serial_number"] == "unknown"
            for c in engine["asset"]["installed_components"]
        )
    ]
    assert unknown
    planted = {serial for _, _, serial, _ in LISTED_HUBS}
    for engine in unknown:
        components = engine["asset"]["installed_components"]
        # A listed hub in the other stage makes the engine affected anyway.
        if any(c["serial_number"] in planted for c in components):
            continue
        assert engine["screens"]["2025-18469"]["queue"] == "needs_review"


def test_planted_hubs_are_potentially_affected_under_s1():
    fleet, screened = _computed()
    planted = {
        p["engine_asset_id"] for p in fleet["composition"]["planted_listed_parts"]
    }
    for engine in screened["engines"]:
        if engine["asset"]["engine"]["asset_id"] in planted:
            assert engine["evaluated_queue"] == "potentially_affected"


def test_only_evaluated_directives_set_the_queue():
    _, screened = _computed()
    assert screened["evaluated_directives"] == sorted(EVALUATED_DIRECTIVES)
    for engine in screened["engines"]:
        evaluated = [
            entry["queue"]
            for entry in engine["screens"].values()
            if entry["coverage_state"] == EVALUATED
        ]
        expected = min(evaluated, key=QUEUE_ORDER.index) if evaluated else NO_ACTION
        assert engine["evaluated_queue"] == expected
    counts = screened["evaluated_counts"]
    assert sum(counts.values()) == len(screened["engines"])


def test_every_in_scope_directive_is_screened_by_its_rule_record():
    _, screened = _computed()
    states = {d["document"]: d for d in screened["directives"]}
    assert states["2025-18469"]["coverage_state"] == EVALUATED
    assert states["2025-18469"]["screener"] == "S1 rules"
    for document in _inputs()["references"]:
        assert document in states
        if document != "2025-18469":
            expected = (
                EVALUATED if document in EVALUATED_DIRECTIVES else NOT_YET_EVALUATED
            )
            assert states[document]["coverage_state"] == expected
            assert states[document]["screener"].startswith("rule interpreter")
    for engine in screened["engines"]:
        retrieved = {c["document"] for c in engine["candidates"]}
        assert set(engine["screens"]) <= retrieved
        for entry in engine["screens"].values():
            if entry["screener"] == "none" and entry["applicability"] == "candidate":
                assert entry["queue"] == "needs_review"


def test_superseded_directive_is_not_queued_for_review():
    _, screened = _computed()
    for engine in screened["engines"]:
        superseded = engine["screens"].get("2021-11960")
        if superseded:
            assert superseded["applicability"] == "superseded"
            assert "2021-11960" not in engine["not_yet_evaluated"]


def test_blocking_documents_count_review_engines_once_each():
    _, screened = _computed()
    rows = {row["document"]: row for row in screened["blocking_documents"]}
    assert rows["IAE NMSB V2500-ENG-72-0720"]["engines"] > 0
    review = {
        e["asset"]["engine"]["asset_id"]
        for e in screened["engines"]
        if any(s["queue"] == "needs_review" for s in e["screens"].values())
    }
    for row in screened["blocking_documents"]:
        assert row["engines"] <= len(review)
    # An E5-only document never blocks an A5 or D5 engine.
    e5 = sum(
        1
        for e in screened["engines"]
        if e["asset"]["engine"]["engine_model"] == "V2531-E5"
    )
    assert rows["P&W SI No. 189F-23"]["engines"] <= e5


def test_a_missing_fact_names_its_dependency_by_longest_title():
    record = {
        "ad_number": "AD 2022-02-09",
        "dependencies": [
            {
                "id": "one",
                "kind": "incorporated_by_reference",
                "title": "NMSB X Table 1",
            },
            {
                "id": "either",
                "kind": "incorporated_by_reference",
                "title": "NMSB X Table 1, or NMSB Y Table 1",
            },
        ],
    }
    fact = "NMSB X Table 1, or NMSB Y Table 1 (unavailable incorporated material)"
    assert _dependency(fact, record)["id"] == "either"
    assert _dependency("NMSB X Table 1 (unavailable)", record)["id"] == "one"


def test_service_documents_are_named_once_and_e5_ones_only_for_e5():
    record = {
        "dependencies": [
            {
                "id": "t1",
                "kind": "incorporated_by_reference",
                "title": "IAE AG NMSB V2500-ENG-72-0720 (November 20, 2023) Table 1, "
                "and PW SI No. 189F-23 (November 20, 2023) Table 1 (V2531-E5)",
            }
        ]
    }
    entry = {
        "missing_facts": [
            record["dependencies"][0]["title"] + " (unavailable incorporated material)",
            "ad_records[AD 2024-11-03]",
        ]
    }
    documents, others = _blockers(entry, record, "V2527-A5", "AD 2024-11-03")
    assert [name for name, _ in documents] == ["IAE NMSB V2500-ENG-72-0720"]
    assert others == ["ad_records[AD 2024-11-03]"]
    documents, _ = _blockers(entry, record, "V2531-E5", "AD 2024-11-03")
    assert [name for name, _ in documents] == [
        "IAE NMSB V2500-ENG-72-0720",
        "P&W SI No. 189F-23",
    ]


def test_snapshot_is_after_every_effective_date():
    fleet, _ = _computed()
    snapshot = date.fromisoformat(fleet["snapshot_at"])
    for record in _inputs()["references"].values():
        assert date.fromisoformat(record["effective_date"]["date"]) <= snapshot


def test_page_embeds_the_recorded_screen_safely():
    _, screened = _computed()
    page = render_fleet_page(screened)
    assert page.startswith("<!doctype html>")
    assert "__" not in page.split('<script id="fleet-data"')[0]
    data = json.loads(page.split('type="application/json">')[1].split("</script>")[0])
    # Without a replay the replay sections are left out, not failed.
    assert data["states"] == [] and data["engines"] == []
    assert 'id="replay" aria-label="As-of replay" hidden' in page
    strip = {row["document"]: row for row in data["strip"]}
    for directive in screened["directives"]:
        row = strip[directive["document"]]
        assert row["queues"] == directive["queues"]
        assert row["held"] == [
            {"document": b["document"], "engines": b["engines"]}
            for b in directive["blocking_documents"]
        ]
    assert "Screening tool, not a compliance determination" in page
    # Citations are stored once and referred to by index.
    for fixture in data["fixtures"]:
        if fixture["sc"]:
            assert all(0 <= i < len(data["cites"]) for i in fixture["sc"]["c"])


def test_slim_screen_expands_to_the_full_per_engine_screens():
    _, screened = _computed()
    slim = slim_fleet_screen(screened)
    assert expand_fleet_screen(slim) == screened
    # The committed file is the slim form and expands to the same screens.
    committed = json.loads((REPO / FLEET_SCREEN_FILE).read_text(encoding="utf-8"))
    assert expand_fleet_screen(committed) == screened
    assert len(dump_slim(slim)) < len(dump(screened)) / 2


def test_slim_screen_stores_each_distinct_value_once():
    _, screened = _computed()
    slim = slim_fleet_screen(screened)
    assert len(slim["citation_table"]) == len(
        {
            json.dumps(c, sort_keys=True)
            for e in screened["engines"]
            for s in e["screens"].values()
            for c in s["citations"]
        }
    )
    for engine in slim["engines"]:
        for entry in engine["screens"].values():
            assert all(k in slim["citation_table"] for k in entry["citations"])
            assert all(k in slim["strings"] for k in entry["notes"])


def test_rule_record_source_defaults_to_the_reference_record():
    # Only an evaluated directive reads its reviewed draft; every other
    # directive keeps its reference record.
    assert set(RULE_RECORD_PATHS) <= EVALUATED_DIRECTIVES
    for document, path in RULE_RECORD_PATHS.items():
        assert path == f"evaluation/coverage/reviewed/{document}.json"
        assert (REPO / path).exists()
    assert (
        rule_record_path("2025-18469")
        == "evaluation/coverage/reference/2025-18469.json"
    )
    _, screened = _computed()
    for row in screened["directives"]:
        if row["document"] == S1_DOCUMENT:
            assert row["rule_record_source"].startswith("evaluation/runs/")
        elif row["screener"] != "none: listed for a person to read":
            assert row["rule_record_source"] == rule_record_path(row["document"])
        else:
            assert row["rule_record_source"] is None


def test_review_provenance_labels_evaluated_directives_only():
    evaluated = frozenset({S1_DOCUMENT, "2019-16-01"})
    assert review_provenance("2019-16-01", evaluated) == {
        "label_review": "claude_stand_in",
        "independent_check": "claude_subagent",
    }
    assert review_provenance(S1_DOCUMENT, evaluated)["hand_gates"] == (
        "judged by Claude only"
    )
    assert review_provenance("2013-08448", evaluated) is None


def test_page_shows_review_provenance_in_the_strip_and_the_drawer():
    _, screened = _computed()
    page = render_fleet_page(screened)
    data = json.loads(page.split('type="application/json">')[1].split("</script>")[0])
    first = next(d for d in data["strip"] if d["document"] == S1_DOCUMENT)
    assert first["provenance"]["rules"] == "hand-written (S1)"
    assert data["directive"]["provenance"]["hand_gates"] == "judged by Claude only"
    assert "${provenance()}" in page
