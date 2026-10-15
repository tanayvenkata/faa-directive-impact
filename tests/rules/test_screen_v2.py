"""Interpreter v2 constructs, on the v2 reference records and small synthetic engines.

The engines here are written for these tests from the directive texts; they
are not coverage cases.
"""

import copy
import json
from datetime import date
from pathlib import Path

import pytest

from faa_directive_impact.evaluation.seed import load_seed_cases
from faa_directive_impact.fleet.build import compute_fleet
from faa_directive_impact.rules.interpreter import screen_rules
from faa_directive_impact.rules.screen_v2 import (
    RECORD_ACCOMPLISHED,
    rule_record_problems,
)

REPO = Path(__file__).resolve().parents[2]
REFERENCE = REPO / "evaluation/coverage/reference"
RECORDS = {p.stem: json.loads(p.read_text()) for p in sorted(REFERENCE.glob("*.json"))}
OUTPUTS: list[dict] = []
FORBIDDEN_WORDS = ("compliant", "overdue", "airworthy")


def run(document: str, asset: dict, as_of: str, rules: dict | None = None):
    result = screen_rules(rules or RECORDS[document], asset, date.fromisoformat(as_of))
    OUTPUTS.append(result.to_dict())
    return result


def engine(
    model: str,
    serial: str = "V10500",
    components=(),
    readings=(),
    events=(),
    records=(),
    operator=None,
    claims=(),
) -> dict:
    asset = {
        "engine": {
            "asset_id": "SYN-T",
            "engine_serial_number": serial,
            "engine_model": model,
            "engine_cycle_readings": [
                {"at": at, "engine_flight_cycles": n} for at, n in readings
            ],
        },
        "installed_components": [
            {
                "component_name": name,
                "part_number": pn,
                "serial_number": sn,
                **({"cycles_since_new": csn} if csn is not None else {}),
                **(
                    {
                        "cycles_since_new_readings": [
                            {"at": at, "cycles_since_new": n} for at, n in history
                        ]
                    }
                    if history
                    else {}
                ),
            }
            for name, pn, sn, csn, history in components
        ],
        "events": list(events),
        "ad_records": [{"ad": ad, "recorded_status": status} for ad, status in records],
        "amoc_claims": list(claims),
    }
    if operator is not None:
        asset["operator"] = operator
    return asset


def part(name, pn, sn, csn=None, history=()):
    return (name, pn, sn, csn, history)


def visit(at: str, ad: str, answer: str = "yes", counter: int | None = None) -> dict:
    event = {
        "event_type": "shop_visit_induction",
        "at": at,
        "qualifies_as_engine_shop_visit": {ad: answer},
    }
    if counter is not None:
        event["engine_flight_cycles_at_event"] = counter
    return event


def cited(result) -> set[tuple[str, str]]:
    return {(c.document, c.paragraph) for c in result.citations}


def outcome(result) -> tuple:
    return (result.applicability, result.action_status)


# Records ---------------------------------------------------------------


def test_every_directive_in_the_preregistration_has_a_reference_record() -> None:
    assert set(RECORDS) == {
        "2024-12594", "2022-02574", "2021-11960", "2021-14268", "2021-15486",
        "2020-07627", "2016-21061", "2017-14706", "2019-19412", "2019-17403",
        "2015-12068", "2012-12329", "2013-08448", "2025-17066", "2025-18469",
        "2026-16954",
    }  # fmt: skip


@pytest.mark.parametrize("document", sorted(RECORDS))
def test_reference_record_is_schema_valid_and_its_ids_resolve(document) -> None:
    assert rule_record_problems(RECORDS[document]) == []


@pytest.mark.parametrize("document", sorted(RECORDS))
def test_reference_record_cites_only_paragraphs_and_names_its_ambiguities(document):
    record = RECORDS[document]
    assert record["final_rule_document"] == document
    for action in record["required_actions"]:
        assert action["paragraph"].startswith("(")
    assert record["ambiguities"], "every directive text here has at least one"


# Parity with v1 --------------------------------------------------------


def test_v2_records_of_the_two_v1_directives_reproduce_v1_on_seed_and_fleet() -> None:
    """Same applicability, status, and computed values, with two stated changes.

    - seed-021 records its hubs as "HPT 1st-stage disk"; v2 finds the position
      by P/N 2A5001 and the disk alias, so the unlisted S/N clears it, where
      v1 found no "hub" record and sent it to review.
    - Before AD 2026-17-03's effective date v2 reports
      published_not_yet_effective even when applicability is unknown (as
      seed-020 expects); v1 left it in_force.
    """
    cases = [c.record for c in load_seed_cases(REPO / "evaluation/seed/cases")]
    fleet, _ = compute_fleet(REPO)
    assets = [
        (c["case_id"], c["asset_snapshot"], c["source_snapshot"]["as_of"])
        for c in cases
    ] + [
        (
            a["engine"]["asset_id"],
            a,
            a.get("evaluation_case", {}).get("as_of") or a["engine"]["snapshot_at"],
        )
        for a in fleet["engines"]
    ]
    for document in ("2025-18469", "2026-16954"):
        v1 = json.loads((REPO / f"evaluation/b3/reference/{document}.json").read_text())
        for name, asset, as_of in assets:
            if (document, name) == ("2025-18469", "seed-021"):
                continue
            old = screen_rules(v1, asset, date.fromisoformat(as_of))
            new = screen_rules(RECORDS[document], asset, date.fromisoformat(as_of))
            assert (new.applicability, new.action_status, new.computed) == (
                old.applicability,
                old.action_status,
                old.computed,
            ), (document, name)


# Engine serial numbers ---------------------------------------------------


@pytest.mark.parametrize(
    ("model", "serial", "expected"),
    [
        ("V2527-A5", "V12000", "applies"),
        ("V2527-A5", "V15001", "applies"),
        ("V2527-A5", "V16728", "applies"),
        ("V2527-A5", "V14000", "does_not_apply"),
        ("V2527-A5", "V16729", "does_not_apply"),
        ("V2527-A5", "V16707", "does_not_apply"),
        ("V2525-D5", "SYN-ANY-1", "applies"),
        ("V2531-E5", "V12000", "does_not_apply"),
    ],
)
def test_engine_serial_ranges_and_exclusions(model, serial, expected) -> None:
    result = run("2015-12068", engine(model, serial), "2016-01-01")
    assert result.applicability == expected
    if model.endswith("A5") and expected != "applies":
        assert ("2015-12068", "(c)(3)") in cited(result)


@pytest.mark.parametrize("serial", ["unknown", "SYN-V2500-0001", "V 12000x", "v12000"])
def test_an_engine_serial_that_cannot_be_placed_is_never_cleared(serial) -> None:
    result = run("2015-12068", engine("V2527-A5", serial), "2016-01-01")
    assert outcome(result) == ("unknown", "needs_review")
    assert result.missing_facts == ["engine.engine_serial_number"]


def test_open_lower_bound_takes_every_serial_up_to_the_last() -> None:
    low = run("2012-12329", engine("V2527-A5", "V00010"), "2013-01-01")
    high = run("2012-12329", engine("V2527-A5", "V13182"), "2013-01-01")
    assert low.applicability == "applies"
    assert high.applicability == "does_not_apply"


def test_near_miss_engine_serial_goes_to_review() -> None:
    result = run("2019-19412", engine("V2527-A5", "v10631"), "2020-01-01")
    assert outcome(result) == ("unknown", "needs_review")


# Listed parts by S/N, maintenance events, caps --------------------------

LPT = "LPT stage 6 disk"
EFFECTIVE_19412 = "2019-10-15"


def lpt_engine(sn="MAP04258", csn=4000, events=(), records=(), serial="V10631"):
    return engine(
        "V2527-A5",
        serial,
        [part(LPT, "3A2996", sn, csn, [(EFFECTIVE_19412, 3000)])],
        readings=[(EFFECTIVE_19412, 20000), ("2020-06-01", 21000)],
        events=events,
        records=records,
    )


def test_listed_disk_on_a_listed_engine_is_due_by_its_cycle_cap() -> None:
    result = run("2019-19412", lpt_engine(), "2020-06-01")
    assert outcome(result) == ("applies", "action_required")
    assert result.computed == {
        "latest_engine_flight_cycles": 22000,
        "component_cycles_remaining": 1000,
    }
    assert {
        ("2019-19412", "(c)"),
        ("2019-19412", "(g)"),
        ("2019-19412", "(h)"),
    } <= cited(result)


def test_unlisted_engine_serial_does_not_apply() -> None:
    result = run("2019-19412", lpt_engine(serial="V10632"), "2020-06-01")
    assert outcome(result) == ("does_not_apply", None)


def test_unlisted_disk_on_a_listed_engine_needs_no_action() -> None:
    result = run("2019-19412", lpt_engine(sn="MAP09999"), "2020-06-01")
    assert outcome(result) == ("applies", "no_action_triggered")


def test_missing_disk_record_on_a_listed_engine_is_named() -> None:
    asset = lpt_engine()
    asset["installed_components"] = []
    result = run("2019-19412", asset, "2020-06-01")
    assert result.action_status == "needs_review"
    assert result.missing_facts == [f"installed_components[{LPT}]"]


def test_possible_exposure_keeps_the_removal_open_but_drops_the_cap_number() -> None:
    exposure = {"event_type": "component_exposure", "at": "2020-02-01"}
    result = run("2019-19412", lpt_engine(events=[exposure]), "2020-06-01")
    assert result.action_status == "action_required"
    assert "latest_engine_flight_cycles" not in result.computed
    assert any("may be the" in note for note in result.notes)


def test_installed_listed_part_outweighs_a_complied_record() -> None:
    result = run(
        "2019-19412",
        lpt_engine(csn=5200, records=[("AD 2019-18-01", "complied")]),
        "2020-06-01",
    )
    assert result.action_status == "action_required"
    assert result.computed["component_cycles_remaining"] == -200


# Operator records (pre-registered rule) ---------------------------------

AD_TEC = "AD 2019-16-01"


def tec_engine(now=20000, records=(), events=(), readings=None):
    return engine(
        "V2528-D5",
        "V20500",
        readings=readings or [("2019-09-19", 10000), ("2026-10-01", now)],
        events=events,
        records=records,
    )


def test_inspection_before_its_deadline_is_due_with_the_counter() -> None:
    result = run("2019-17403", tec_engine(now=12000), "2026-10-01")
    assert outcome(result) == ("applies", "action_required")
    assert result.computed == {"latest_engine_flight_cycles": 14000}


def test_passed_deadline_without_a_record_names_the_record() -> None:
    result = run("2019-17403", tec_engine(), "2026-10-01")
    assert result.action_status == "needs_review"
    assert result.missing_facts == [f"ad_records[{AD_TEC}]"]


@pytest.mark.parametrize("status", ["complied", "recurring"])
def test_passed_deadline_with_an_accomplished_record_needs_no_action(status) -> None:
    result = run("2019-17403", tec_engine(records=[(AD_TEC, status)]), "2026-10-01")
    assert result.action_status == "no_action_triggered"
    assert f"Paragraph (g)(1): {RECORD_ACCOMPLISHED}" in result.notes
    assert ("2019-17403", "(h)") in cited(result)  # credit for previous actions


@pytest.mark.parametrize("status", ["open", "not_applicable"])
def test_passed_deadline_with_an_open_or_na_record_goes_to_review(status) -> None:
    result = run("2019-17403", tec_engine(records=[(AD_TEC, status)]), "2026-10-01")
    assert result.action_status == "needs_review"
    assert f"ad_records[{AD_TEC}]" in result.missing_facts


def test_a_qualifying_visit_after_the_effective_date_makes_the_deadline_pass() -> None:
    result = run(
        "2019-17403",
        tec_engine(now=11000, events=[visit("2020-03-01", AD_TEC, counter=10500)]),
        "2026-10-01",
    )
    assert result.missing_facts == [f"ad_records[{AD_TEC}]"]


def test_a_visit_of_unknown_qualification_is_evaluated_both_ways() -> None:
    result = run(
        "2019-17403",
        tec_engine(now=11000, events=[visit("2020-03-01", AD_TEC, "unknown", 10500)]),
        "2026-10-01",
    )
    assert result.action_status == "needs_review"
    assert "events[2020-03-01].qualifies_as_engine_shop_visit" in result.missing_facts


def test_missing_effective_date_reading_is_named_not_guessed() -> None:
    result = run(
        "2019-17403", tec_engine(readings=[("2026-10-01", 20000)]), "2026-10-01"
    )
    assert result.action_status == "needs_review"
    assert result.missing_facts == ["engine.engine_cycle_readings[2019-09-19]"]


# Calendar limits, terminating actions, maintenance events ---------------

AD_DRUM = "AD 2015-10-04"


def drum_engine(records=(), events=(), readings=()):
    return engine(
        "V2525-D5",
        "V20100",
        [part("HPC stage 3 to 8 drum", "2A1234", "SYN-DRUM", 9000)],
        readings=readings,
        events=events,
        records=records,
    )


def test_terminating_action_past_its_calendar_date_decides_alone() -> None:
    result = run("2015-12068", drum_engine(), "2026-10-01")
    assert result.action_status == "needs_review"
    assert result.missing_facts == [f"ad_records[{AD_DRUM}]"]
    assert any("terminating action" in note for note in result.notes)
    done = run("2015-12068", drum_engine(records=[(AD_DRUM, "complied")]), "2026-10-01")
    assert done.action_status == "no_action_triggered"
    assert done.continuing_obligations[0]["paragraph"] == "(i)"


def test_before_its_deadline_the_terminating_action_is_due_and_groups_are_named() -> (
    None
):
    result = run(
        "2015-12068",
        drum_engine(readings=[("2015-07-01", 1000), ("2016-01-01", 1500)]),
        "2016-01-01",
    )
    assert result.action_status == "action_required"
    assert result.computed == {"latest_engine_flight_cycles": 10450}
    assert any("A0615" in fact for fact in result.missing_facts)


def test_unidentifiable_maintenance_event_sends_an_event_action_to_review() -> None:
    exposure = {"event_type": "component_exposure", "at": "2015-12-01"}
    readings = [("2015-07-01", 1000), ("2016-01-01", 1500)]
    quiet = run("2015-12068", drum_engine(readings=readings), "2016-01-01")
    busy = run(
        "2015-12068", drum_engine(readings=readings, events=[exposure]), "2016-01-01"
    )
    assert "piece-part exposure" in (quiet.timing or "")
    assert busy.action_status == "needs_review"


def test_overall_cap_bounds_a_whichever_later_deadline() -> None:
    asset = engine(
        "V2528-D5",
        "V20100",
        [
            part(
                "HPC stage 3 to 8 drum",
                "2A1234",
                "SYN-DRUM",
                13600,
                [("2012-06-27", 13500)],
            )
        ],
        readings=[("2012-06-27", 30000), ("2012-08-01", 30100)],
    )
    result = run("2012-12329", asset, "2012-08-01")
    # Later of (12,500 CSN: already passed) and 500 FCs; capped at 13,700 CSN.
    assert result.computed["latest_engine_flight_cycles"] == 30200


# Parts in unavailable material, all-of conditions, recurring events -----


def test_part_number_match_with_an_unavailable_serial_list_is_unknown() -> None:
    asset = engine(
        "V2527-A5",
        components=[
            part("HPT 1st-stage hub", "2A5001", "SYN-1"),
            part("HPT 2nd-stage hub", "2A4802", "SYN-2"),
        ],
    )
    result = run("2016-21061", asset, "2017-01-01")
    assert outcome(result) == ("unknown", "needs_review")
    assert any("V2500-ENG-72-0661" in fact for fact in result.missing_facts)


def test_other_part_numbers_clear_an_unavailable_list() -> None:
    asset = engine(
        "V2527-A5",
        components=[
            part("HPT 1st-stage hub", "2A9999", "SYN-1"),
            part("HPT 2nd-stage hub", "2A9998", "SYN-2"),
        ],
    )
    assert outcome(run("2016-21061", asset, "2017-01-01")) == ("does_not_apply", None)


def tube_engine(internal="2A2074-01", external="6A5254", csn=None, serial="V20100"):
    components = []
    if internal:
        components.append(
            part("No. 4 bearing internal scavenge tube", internal, "T-1", csn)
        )
    if external:
        components.append(part("No. 4 bearing external scavenge tube", external, "T-2"))
    return engine("V2525-D5", serial, components)


def test_both_tubes_installed_makes_both_recurring_actions_wait_on_events() -> None:
    result = run("2013-08448", tube_engine(), "2014-01-01")
    assert outcome(result) == ("applies", "action_required_on_event")
    assert result.missing_facts == []  # the AD settles an unknown tube age itself
    assert {
        ("2013-08448", "(f)"),
        ("2013-08448", "(g)"),
        ("2013-08448", "(h)"),
    } <= cited(result)


def test_all_of_condition_clears_when_one_tube_is_another_part() -> None:
    result = run("2013-08448", tube_engine(external="6A9999"), "2014-01-01")
    assert outcome(result) == ("does_not_apply", None)


def test_all_of_condition_with_a_missing_tube_record_is_unknown() -> None:
    result = run("2013-08448", tube_engine(external=None), "2014-01-01")
    assert outcome(result) == ("unknown", "needs_review")
    assert result.missing_facts == [
        "installed_components[No. 4 bearing external scavenge tube]"
    ]


def test_engine_serial_outside_the_range_clears_before_parts() -> None:
    result = run("2013-08448", tube_engine(serial="V20286"), "2014-01-01")
    assert outcome(result) == ("does_not_apply", None)


# Calendar days and operator conditions (AD 2025-17-16) -------------------


@pytest.mark.parametrize(
    ("carrier", "status", "missing"),
    [
        ("yes", "action_required", []),
        ("unknown", "action_required", ["operator.air_carrier_operation"]),
        ("no", "action_required", []),
    ],
)
def test_program_revision_by_model_and_air_carrier(carrier, status, missing) -> None:
    asset = engine("V2527-A5", operator={"air_carrier_operation": carrier})
    result = run("2025-17066", asset, "2025-11-15")
    assert result.action_status == status
    assert result.missing_facts == missing
    assert ("2025-17066", "(g)(1)(i)") in cited(result)
    assert ("2025-17066", "(g)(1)(ii)") not in cited(result)
    assert ("2025-17066", "(g)(2)") in cited(result)
    assert "2026-01-08" in (result.timing or "")


def test_program_revision_after_ninety_days_reads_the_operator_record() -> None:
    asset = engine("V2533-A5", operator={"air_carrier_operation": "yes"})
    assert run("2025-17066", asset, "2026-10-06").missing_facts == [
        "ad_records[AD 2025-17-16]"
    ]
    asset["ad_records"] = [{"ad": "AD 2025-17-16", "recorded_status": "complied"}]
    result = run("2025-17066", asset, "2026-10-06")
    assert result.action_status == "no_action_triggered"
    assert result.continuing_obligations[0]["paragraph"] == "(h)"


# Supersession and emergency ADs -----------------------------------------


def disk_engine(model="V2533-A5", sn1="SYN-D1", sn2="SYN-D2", readings=(), records=()):
    return engine(
        model,
        components=[
            part("HPT 1st-stage disk", "2A5001", sn1),
            part("HPT 2nd-stage disk", "2A4802", sn2),
        ],
        readings=readings,
        records=records,
    )


def test_superseded_directive_screens_until_its_replacement_takes_effect() -> None:
    before = run("2021-11960", disk_engine(), "2022-03-01")
    after = run("2021-11960", disk_engine(), "2022-04-01")
    assert outcome(before) == ("unknown", "needs_review")
    assert after.applicability == "superseded" and after.action_status is None
    assert after.queue == "no_action_or_not_applicable"
    assert ("2022-02574", "(b)") in cited(after)


def test_replacing_directive_before_its_effective_date() -> None:
    result = run("2022-02574", disk_engine(), "2022-03-01")
    assert result.authority_state == "published_not_yet_effective"
    assert outcome(result) == ("unknown", "needs_review")


def test_listed_disk_named_inline_but_action_table_is_an_image() -> None:
    result = run("2021-14268", disk_engine(sn1="PKLBSH1829"), "2021-07-20")
    assert outcome(result) == ("applies", "needs_review")
    assert any("ER02JY21.000" in fact for fact in result.missing_facts)


def test_unlisted_disks_clear_the_inline_list() -> None:
    result = run("2021-14268", disk_engine(), "2021-07-20")
    assert outcome(result) == ("does_not_apply", None)


def emergency_disk(sn: str, readings):
    return engine(
        "V2527-A5",
        components=[part("HPT 1st-stage disk", "2A5001", sn)],
        readings=readings,
    )


def test_removal_named_in_text_is_open_once_its_latest_deadline_has_passed() -> None:
    asset = emergency_disk("PKLBR37442", [("2020-05-01", 1000), ("2026-10-01", 9000)])
    result = run("2020-07627", asset, "2026-10-01")
    assert outcome(result) == ("applies", "action_required")
    assert result.computed == {"latest_engine_flight_cycles": 1005}


def test_pending_deadline_under_an_emergency_ad_names_the_notice_date() -> None:
    asset = emergency_disk("PKLBR37442", [("2020-05-01", 1000), ("2020-05-01", 1000)])
    result = run("2020-07627", asset, "2020-05-01")
    assert result.action_status == "needs_review"
    assert (
        "operator date of actual notice of Emergency AD 2020-07-51"
        in result.missing_facts
    )


def test_between_emergency_issue_and_effective_date_is_left_to_a_person() -> None:
    result = run("2020-07627", emergency_disk("PKLBR37442", []), "2020-04-01")
    assert result.authority_state == "published_not_yet_effective"
    assert result.action_status == "needs_review"


def test_disk_listed_only_in_the_image_table_goes_to_review() -> None:
    asset = emergency_disk("PKLBR38359", [("2020-05-01", 1000), ("2026-10-01", 9000)])
    result = run("2020-07627", asset, "2026-10-01")
    assert result.action_status == "needs_review"
    assert any("ER13AP20.000" in fact for fact in result.missing_facts)


# Bands, part cycles after the effective date, unsupported constructs ----


def banded_record() -> dict:
    """AD 2016-18-10 with its serial lists made inline, to exercise the bands."""
    rules = copy.deepcopy(RECORDS["2016-21061"])
    for group in rules["parts"]:
        group["serials"], group["dependency"] = "any", ""
    return rules


def hub_engine(csn_at_effective: int, events=()):
    return engine(
        "V2527-A5",
        components=[
            part(
                "HPT 1st-stage hub",
                "2A5001",
                "H1",
                csn_at_effective + 100,
                [("2016-10-07", csn_at_effective)],
            ),
            part("HPT 2nd-stage hub", "2A9999", "H2"),
        ],
        readings=[("2016-10-07", 40000), ("2016-11-01", 40100)],
        events=events,
    )


@pytest.mark.parametrize(
    ("csn", "latest", "remaining"),
    [
        (5000, 48000, 7900),  # (i): before 13,000 CSN
        (8000, 46000, 5900),  # (ii): first of 6,000 hub cycles and 15,000 CSN
        (14000, 43000, 2900),  # (iii): 17,000 CSN comes before 4,000 hub cycles
        (16000, 41500, 1400),  # (iv): 1,500 hub cycles
    ],
)
def test_csn_bands_pick_the_limits(csn, latest, remaining) -> None:
    result = run("2016-21061", hub_engine(csn), "2016-11-01", banded_record())
    assert result.action_status == "action_required"
    assert result.computed == {
        "latest_engine_flight_cycles": latest,
        "component_cycles_remaining": remaining,
    }


def test_band_needs_the_part_cycles_on_the_effective_date() -> None:
    asset = hub_engine(5000)
    del asset["installed_components"][0]["cycles_since_new_readings"]
    result = run("2016-21061", asset, "2016-11-01", banded_record())
    assert result.action_status == "needs_review"
    assert result.missing_facts == [
        "installed_components[HPT 1st-stage hub].cycles_since_new_readings[2016-10-07]"
    ]


def test_unrecorded_condition_is_named() -> None:
    rules = copy.deepcopy(RECORDS["2021-15486"])
    for group in rules["parts"]:
        group["serials"], group["dependency"] = "any", ""
    result = run("2021-15486", disk_engine("V2527-A5"), "2021-09-01", rules)
    assert result.action_status == "needs_review"
    assert any("installed at any time" in fact for fact in result.missing_facts)


@pytest.mark.parametrize(
    "change",
    [
        lambda a: a.update(combination="unclear"),
        lambda a: a["limits"].__setitem__(0, {**a["limits"][0], "kind": "other"}),
        lambda a: a.update(kind="other"),
    ],
)
def test_unsupported_constructs_are_declined(change) -> None:
    rules = copy.deepcopy(RECORDS["2019-17403"])
    change(rules["required_actions"][0])
    result = run("2019-17403", tec_engine(now=12000), "2026-10-01", rules)
    assert result.action_status == "needs_review"
    assert any("is not evaluated" in note for note in result.notes)


# Damaged input ------------------------------------------------------------


@pytest.mark.parametrize(
    ("mutate", "field"),
    [
        (
            lambda a: a["engine"].__setitem__("engine_serial_number", 10631),
            "engine.engine_serial_number",
        ),
        (
            lambda a: a.__setitem__("operator", {"air_carrier_operation": "maybe"}),
            "operator.air_carrier_operation",
        ),
        (lambda a: a.__setitem__("operator", "yes"), "operator"),
    ],
)
def test_malformed_v2_fields_are_never_screened(mutate, field) -> None:
    asset = lpt_engine()
    mutate(asset)
    result = run("2019-19412", asset, "2020-06-01")
    assert outcome(result) == ("unknown", "needs_review")
    assert result.missing_facts == [field]


@pytest.mark.parametrize("document", sorted(RECORDS))
def test_unknown_model_is_never_cleared_by_any_record(document) -> None:
    result = run(document, engine("unknown"), "2026-10-01")
    if RECORDS[document]["relationships"] and result.applicability == "superseded":
        return  # screened under the replacing directive instead
    assert result.action_status == "needs_review"


def test_no_output_uses_a_forbidden_word() -> None:
    """GATES.md standing claims: never compliant/noncompliant, airworthy; never overdue."""
    assets = [
        lpt_engine(),
        lpt_engine(csn=5200, records=[("AD 2019-18-01", "complied")]),
        tec_engine(),
        tec_engine(records=[(AD_TEC, "complied")]),
        drum_engine(),
        drum_engine(records=[(AD_DRUM, "open")]),
        tube_engine(),
        disk_engine(sn1="PKLBR37442"),
        emergency_disk("PKLBR37442", [("2020-05-01", 1000), ("2026-10-01", 9000)]),
        engine("V2527-A5", operator={"air_carrier_operation": "unknown"}),
    ]
    for document in RECORDS:
        for asset in assets:
            for as_of in ("2016-01-01", "2020-06-01", "2026-10-01"):
                run(document, copy.deepcopy(asset), as_of)
    for output in OUTPUTS:
        text = json.dumps(output).lower()
        for word in FORBIDDEN_WORDS:
            assert word not in text, (word, output["summary"])


# Citations, emergency clocks, and how missing material is named ---------

PARAGRAPH_INDEX = json.loads(
    (REPO / "tests/fixtures/rules/coverage-paragraph-index.json").read_text()
)["documents"]
LABEL_KEYS = ("paragraph", "models_paragraph", "parts_paragraph", "amoc_paragraph")
LABEL_LISTS = ("definition_paragraphs", "terminates", "actions")


def paragraph_labels(node):
    if isinstance(node, dict):
        for key, value in node.items():
            if key in LABEL_KEYS and isinstance(value, str) and value:
                yield value
            elif key in LABEL_LISTS and isinstance(value, list):
                yield from value
            elif key != "relationships":
                yield from paragraph_labels(value)
    elif isinstance(node, list):
        for item in node:
            yield from paragraph_labels(item)


@pytest.mark.parametrize("document", sorted(RECORDS))
def test_every_cited_paragraph_exists_in_the_section_index(document) -> None:
    """Gate 6 resolves citations against this index (the frozen generation)."""
    record = RECORDS[document]
    known = set(PARAGRAPH_INDEX[record["governing_document"]["document"]])
    assert sorted(set(paragraph_labels(record)) - known) == []
    for relation in record["relationships"]:
        assert relation["paragraph"] in PARAGRAPH_INDEX[relation["stated_in"]]


def test_blocked_action_under_an_emergency_ad_still_names_the_notice_date() -> None:
    asset = disk_engine(
        sn1="PKLBSH1829", readings=[("2021-07-19", 33000), ("2021-07-20", 33004)]
    )
    result = run("2021-14268", asset, "2021-07-20")
    assert "operator date of actual notice of Emergency AD 2021-11-51" in (
        result.missing_facts
    )
    assert ("2021-14268", "(a)") in cited(result)
    image = next(f for f in result.missing_facts if "ER02JY21.000" in f)
    assert "not transcribed" in image and "incorporated" not in image


def test_notice_date_is_not_asked_once_the_published_clock_has_run_out() -> None:
    asset = disk_engine(
        sn1="PKLBSH1829", readings=[("2021-07-19", 33000), ("2026-10-01", 40000)]
    )
    result = run("2021-14268", asset, "2026-10-01")
    assert not any("actual notice" in fact for fact in result.missing_facts)


def test_procedure_material_is_noted_and_cited_but_never_blocks() -> None:
    result = run("2013-08448", tube_engine(), "2014-01-01")
    assert result.action_status == "action_required_on_event"
    assert any("V2500-ENG-72-0630" in note for note in result.notes)
    assert ("2013-08448", "(g)") in cited(result)


def test_two_different_readings_on_one_date_are_malformed() -> None:
    asset = tec_engine(readings=[("2019-09-19", 10000), ("2019-09-19", 10500)])
    result = run("2019-17403", asset, "2026-10-01")
    assert outcome(result) == ("unknown", "needs_review")
    assert result.missing_facts == ["engine.engine_cycle_readings"]
