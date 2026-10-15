"""Screen one engine against a directive from its rule record alone.

A rule record (``schemas/b3-rule-record.schema.json``) states a directive's
predicates: applicable models, an optional part condition, listed parts and
their limits, required actions with their trigger and limits, installation
prohibitions, definitions, and the paragraph each rests on. The record may be
hand-written or drafted by a model (B3); this interpreter treats both alike and
reads nothing else about the directive.

The vocabulary is fixed and small. An action whose trigger, limits, or target
the interpreter does not support is never guessed at: the engine goes to
``needs_review`` with a note naming what is unsupported.

It generalizes the S1 rules (``impact.hpt_hub_rules``) with two deliberate
differences:

- It applies no adjudication. When the readings of a whichever-later window
  give different deadlines, it reports them and returns ``needs_review``. S1
  follows informal FAA correspondence there, which no text extraction can
  supply.
- It cites the governing document: the final rule, or the correction that
  republished its regulatory text.
"""

from datetime import date
from typing import Any

from faa_directive_impact.impact.hpt_hub_rules import (
    SUPPORTED_ENGINE_MODELS,
    UNKNOWN,
    Citation,
    HubFinding,
    Screen,
    engine_record_problems,
    malformed_screen,
)

INTERPRETER_VERSION = 1
LATER = "whichever_occurs_later"
FIRST = "whichever_occurs_first"
TABLE_LIMIT = "listed_part_cycles_since_new"
WINDOW = "flight_cycles_after_effective_date"
STATUS_ORDER = (
    "needs_review",
    "action_required",
    "action_required_on_event",
    "no_action_triggered",
)


def screen_rules(rules: dict[str, Any], asset: dict[str, Any], as_of: date) -> Screen:
    """Screen one engine snapshot against a rule record as of a date.

    A malformed snapshot is never screened: it goes to needs_review with the
    fields that failed (``engine_record_problems``), as in S1.
    """
    problems = engine_record_problems(asset)
    if problems:
        return malformed_screen(
            rules["final_rule_document"], rules["ad_number"], problems
        )
    run = _Run(rules, asset, as_of)
    return run.screen()


class _Run:
    def __init__(self, rules: dict[str, Any], asset: dict[str, Any], as_of: date):
        self.rules = rules
        self.asset = asset
        self.as_of = as_of
        self.document = rules["governing_document"]["document"]
        self.ad = rules["ad_number"]
        self.timing_parts: list[str] = []
        self.result = Screen(
            rules["final_rule_document"], self.ad, "applies", "no_action_triggered"
        )

    def cite(self, paragraph: str, supports: str, locator: str | None = None) -> None:
        citation = Citation(self.document, paragraph, locator, supports)
        if citation not in self.result.citations:
            self.result.citations.append(citation)

    def screen(self) -> Screen:
        result = self.result
        applicability = self.rules["applicability"]
        models_paragraph = applicability["models_paragraph"]
        model = self.asset["engine"]["engine_model"]
        if model == UNKNOWN:
            result.applicability, result.action_status = "unknown", "needs_review"
            result.missing_facts.append("engine.engine_model")
            self.cite(models_paragraph, "the applicable engine models")
            result.summary = (
                "The engine model is not recorded, so applicability cannot be "
                f"decided against the models listed in paragraph {models_paragraph}."
            )
            return result
        if model not in SUPPORTED_ENGINE_MODELS:
            result.applicability, result.action_status = "outside_supported_scope", None
            self.cite(models_paragraph, "the applicable engine models")
            result.summary = (
                f"{model} is not one of the supported V2500-A5/D5/E5 variants. "
                "This screen makes no applicability determination for it."
            )
            return result
        if model not in applicability["engine_models"]:
            result.applicability, result.action_status = "does_not_apply", None
            self.cite(models_paragraph, f"{model} is not among the listed models")
            result.summary = f"{model} is not listed in paragraph {models_paragraph}."
            return result
        self.cite(models_paragraph, f"{model} is a listed model")

        condition_parts = []
        if applicability["part_condition"]["part_numbers"]:
            condition_parts = self._check_part_condition(
                applicability["part_condition"]
            )
            if result.applicability != "applies":
                return result

        effective = date.fromisoformat(self.rules["effective_date"]["date"])
        effective_paragraph = self.rules["effective_date"]["paragraph"]
        in_force = self.as_of >= effective
        if not in_force:
            result.authority_state = "published_not_yet_effective"
            self.cite(effective_paragraph, f"the AD takes effect on {effective}")

        listed = []
        if any(
            a["applies_to"] == "listed_parts" for a in self.rules["required_actions"]
        ):
            listed = self._check_listed_parts()
        matched = [hub for hub in listed if hub.outcome == "matched"]

        if not in_force:
            self._not_yet_effective(matched, effective)
            return result

        for prohibition in self.rules["installation_prohibitions"]:
            result.continuing_obligations.append(
                {
                    "paragraph": prohibition["paragraph"],
                    "text": prohibition["description"],
                }
            )
            self.cite(prohibition["paragraph"], "installation prohibition")

        statuses = []
        for action in self.rules["required_actions"]:
            if action["applies_to"] == "listed_parts":
                statuses.append(self._listed_part_action(action, matched, effective))
            elif action["applies_to"] == "part_condition_parts":
                statuses.append(self._event_action(action, condition_parts, effective))
            else:
                statuses.append(self._unsupported(action, "its target"))
        self._operator_claims(bool(matched) or bool(condition_parts))

        # As in S1, an established, timed action stands while another fact
        # (an AMOC claim, a second position's record) is still missing.
        if result.missing_facts and "action_required" not in statuses:
            statuses.append("needs_review")
        statuses = [s for s in statuses if s] or ["no_action_triggered"]
        result.action_status = min(statuses, key=STATUS_ORDER.index)
        result.computed = _computed(matched)
        result.summary = self._summary(model)
        result.timing = self._timing(matched)
        return result

    # Applicability -------------------------------------------------------

    def _check_part_condition(self, condition: dict[str, Any]) -> list[HubFinding]:
        """Find an installed part the applicability paragraph names.

        A part number in the condition list makes the AD apply. A recorded part
        number that a definition makes eligible for installation clears it.
        Anything else (no record, an unknown part number, or a part number the
        record names nowhere) is not evidence of absence and goes to review.
        """
        result = self.result
        paragraph = condition["paragraph"]
        listed = set(condition["part_numbers"])
        eligible = {
            number: part
            for part in self.rules["eligible_parts"]
            for number in part["part_numbers"]
        }
        components = self.asset["installed_components"]
        found = []
        for component in components:
            if component["part_number"] in listed:
                self.cite(
                    paragraph,
                    f"{component['component_name']} P/N "
                    f"{component['part_number']} is a listed part",
                    f"P/N {component['part_number']}",
                )
                found.append(
                    HubFinding(
                        component["component_name"],
                        component["part_number"],
                        component.get("serial_number"),
                        "matched",
                        f"The {component['component_name']} P/N "
                        f"{component['part_number']} is named in paragraph "
                        f"{paragraph}.",
                        table_row={
                            "part_number": component["part_number"],
                            "serial_number": None,
                        },
                    )
                )
        if found:
            result.hubs.extend(found)
            return found

        cleared = [c for c in components if c["part_number"] in eligible]
        if cleared:
            result.applicability, result.action_status = "does_not_apply", None
            self.cite(
                paragraph, f"the AD applies only with P/N {', '.join(sorted(listed))}"
            )
            for component in cleared:
                part = eligible[component["part_number"]]
                self.cite(
                    part["paragraph"],
                    f"P/N {component['part_number']} is eligible for installation",
                    f"P/N {component['part_number']}",
                )
            result.summary = (
                f"The installed {cleared[0]['component_name']} is P/N "
                f"{cleared[0]['part_number']}, a part eligible for installation, and "
                f"paragraph {paragraph} requires P/N {' or '.join(sorted(listed))}."
            )
            return []

        unknown = [c for c in components if c["part_number"] == UNKNOWN]
        result.applicability, result.action_status = "unknown", "needs_review"
        self.cite(paragraph, "applicability depends on the installed part")
        if unknown:
            result.missing_facts.extend(
                f"installed_components[{c['component_name']}].part_number"
                for c in unknown
            )
        else:
            result.missing_facts.append(
                f"installed_components[{condition['component']}]"
            )
        result.summary = (
            f"Paragraph {paragraph} covers only engines with a {condition['component']} "
            f"of P/N {' or '.join(sorted(listed))}, and the record does not show "
            "which part is installed."
        )
        return []

    def _check_listed_parts(self) -> list[HubFinding]:
        rows = self.rules["affected_parts"]
        components = {
            _name_key(c["component_name"]): c
            for c in self.asset["installed_components"]
        }
        findings = []
        for position in sorted({row["component"] for row in rows}):
            position_rows = [row for row in rows if row["component"] == position]
            findings.extend(
                self._check_position(
                    position, position_rows, rows, components.get(_name_key(position))
                )
            )
        self.result.hubs.extend(findings)
        return findings

    def _check_position(
        self,
        position: str,
        position_rows: list[dict[str, Any]],
        rows: list[dict[str, Any]],
        component: dict[str, Any] | None,
    ) -> list[HubFinding]:
        """Compare the installed part in one listed position with the listed rows."""
        result = self.result
        paragraph = position_rows[0]["paragraph"]
        if component is None:
            result.missing_facts.append(f"installed_components[{position}]")
            self.cite(paragraph, f"no {position} record to compare")
            return [
                HubFinding(
                    position,
                    None,
                    None,
                    "missing",
                    f"No {position} record was supplied, so a listed part can be "
                    "neither found nor excluded.",
                )
            ]
        name = component["component_name"]
        part_number = component["part_number"]
        serial_number = component.get("serial_number", UNKNOWN)
        listed_parts = {row["part_number"] for row in position_rows}
        if part_number == UNKNOWN:
            result.missing_facts.append(f"installed_components[{name}].part_number")
            self.cite(paragraph, f"{name} P/N unknown")
            return [
                HubFinding(
                    name,
                    None,
                    serial_number,
                    "missing",
                    f"The {name} P/N is unknown, so it cannot be compared with the "
                    "listed parts.",
                )
            ]
        serial_rows = [
            row
            for row in position_rows
            if row["part_number"] == part_number and row["serial_number"] is not None
        ]
        if part_number in listed_parts and serial_rows and serial_number == UNKNOWN:
            result.missing_facts.append(f"installed_components[{name}].serial_number")
            self.cite(paragraph, f"{name} has a listed P/N", f"P/N {part_number}")
            return [
                HubFinding(
                    name,
                    part_number,
                    None,
                    "missing",
                    f"The {name} has listed P/N {part_number}, but its S/N is "
                    "unknown, so it may be a listed part.",
                )
            ]

        exact = [
            row
            for row in position_rows
            if row["part_number"] == part_number
            and row["serial_number"] in (None, serial_number)
        ]
        if exact:
            findings = []
            for row in exact:
                locator = (
                    f"S/N {row['serial_number']}"
                    if row["serial_number"]
                    else f"P/N {row['part_number']}"
                )
                self.cite(paragraph, f"{name} matches a listed part", locator)
                limit = row["removal_limit_cycles_since_new"]
                detail = f" (removal limit {limit:,} cycles since new)" if limit else ""
                findings.append(
                    HubFinding(
                        name,
                        part_number,
                        serial_number,
                        "matched",
                        f"The {name} P/N {part_number} S/N {serial_number} matches "
                        f"a part listed in paragraph {paragraph}{detail}.",
                        table_row=row,
                    )
                )
            return findings

        # A listed S/N under another or differently written P/N may be a
        # mis-keyed record of the listed part; only the record holder can say.
        findings = []
        for row in position_rows:
            if row["serial_number"] is None or not _same_identifier(
                row["serial_number"], serial_number
            ):
                continue
            field_name = (
                "serial_number" if row["part_number"] == part_number else "part_number"
            )
            result.missing_facts.append(f"installed_components[{name}].{field_name}")
            self.cite(
                paragraph,
                "a listed S/N recorded under a different identity",
                f"S/N {row['serial_number']}",
            )
            for part in self.rules["eligible_parts"]:
                self.cite(
                    part["paragraph"],
                    "which parts are eligible for installation",
                )
            findings.append(
                HubFinding(
                    name,
                    part_number,
                    serial_number,
                    "identity_unconfirmed",
                    f"The {name} is recorded as P/N {part_number} S/N "
                    f"{serial_number}; paragraph {paragraph} lists P/N "
                    f"{row['part_number']} S/N {row['serial_number']}. A person must "
                    "confirm whether this is the listed part.",
                    table_row=row,
                )
            )
        if findings:
            return findings

        self.cite(paragraph, "the installed part is not listed")
        elsewhere = [
            row
            for row in rows
            if row["serial_number"] == serial_number
            and row["part_number"] != part_number
        ]
        detail = (
            f" S/N {serial_number} is listed only with P/N {elsewhere[0]['part_number']}."
            if elsewhere
            else ""
        )
        return [
            HubFinding(
                name,
                part_number,
                serial_number,
                "not_listed",
                f"The {name} P/N {part_number} S/N {serial_number} is not a listed "
                f"part.{detail}",
            )
        ]

    # Actions ---------------------------------------------------------------

    def _listed_part_action(
        self, action: dict[str, Any], matched: list[HubFinding], effective: date
    ) -> str | None:
        if not matched:
            if not any(h.outcome != "not_listed" for h in self.result.hubs):
                self.cite(action["paragraph"], "no installed part is listed")
            return "no_action_triggered"
        kinds = {limit["kind"] for limit in action["limits"]}
        if action["trigger"] != "next_shop_visit_after_effective_date" or not kinds <= {
            TABLE_LIMIT,
            WINDOW,
        }:
            return self._unsupported(action, "its trigger or limits")
        if action["combination"] == "unclear" or (
            len(kinds) > 1 and action["combination"] == "single"
        ):
            return self._unsupported(action, "how its limits combine")
        statuses = [self._time_part(action, hub, effective) for hub in matched]
        return min(statuses, key=STATUS_ORDER.index)

    def _time_part(
        self, action: dict[str, Any], hub: HubFinding, effective: date
    ) -> str:
        """Compute the latest engine counter for one matched part, or name gaps."""
        assert hub.table_row is not None
        result = self.result
        engine = self.asset["engine"]
        component = next(
            c
            for c in self.asset["installed_components"]
            if c["component_name"] == hub.position
        )
        limits = {limit["kind"]: limit for limit in action["limits"]}
        limit = (
            hub.table_row["removal_limit_cycles_since_new"]
            if TABLE_LIMIT in limits
            else None
        )
        window = limits[WINDOW]["value"] if WINDOW in limits else None
        if (
            TABLE_LIMIT in limits
            and limit is None
            or WINDOW in limits
            and window is None
        ):
            return self._unsupported(action, "a limit with no value")

        engine_readings = {
            date.fromisoformat(r["at"]): r["engine_flight_cycles"]
            for r in engine.get("engine_cycle_readings", [])
        }
        at_effective = engine_readings.get(effective)
        # Part cycles at the effective date come from the part's own record,
        # never from engine cycles: the two differ once a part has moved.
        csn_at_effective = {
            date.fromisoformat(r["at"]): r["cycles_since_new"]
            for r in component.get("cycles_since_new_readings", [])
        }.get(effective)
        csn_now = component.get("cycles_since_new")
        missing = []
        if at_effective is None:
            missing.append(f"engine.engine_cycle_readings[{effective.isoformat()}]")
        if limit is not None:
            if csn_at_effective is None:
                missing.append(
                    f"installed_components[{hub.position}]"
                    f".cycles_since_new_readings[{effective.isoformat()}]"
                )
            if not isinstance(csn_now, int):
                missing.append(f"installed_components[{hub.position}].cycles_since_new")
        if missing or at_effective is None:
            result.missing_facts.extend(missing)
            hub.timing = (
                f"Paragraph {action['paragraph']} requires action on the "
                f"{hub.position}, but its deadline cannot be computed until these "
                "are supplied: " + "; ".join(missing) + "."
            )
            return "needs_review"

        self.cite(
            self.rules["effective_date"]["paragraph"],
            f"effective date {effective.isoformat()} anchors the timing",
        )
        if action["shop_visit_definition_paragraph"]:
            self.cite(action["shop_visit_definition_paragraph"], "engine shop visit")
        self.cite(action["paragraph"], "the required action and its compliance time")
        limit_at = None
        if limit is not None:
            assert isinstance(csn_now, int) and csn_at_effective is not None
            limit_at = at_effective + (limit - csn_at_effective)
            hub.component_cycles_remaining = limit - csn_now
        window_at = at_effective + window if window is not None else None
        visit_at = self._next_counted_visit(effective)

        # The visit is due no later than the part limit; the window is the
        # other leg. With no visit, the visit leg is the limit itself.
        visit_leg = (
            limit_at
            if visit_at is None
            else (visit_at if limit_at is None else min(visit_at, limit_at))
        )
        if window_at is None:
            hub.latest_engine_flight_cycles = visit_leg
        elif visit_leg is None:
            hub.latest_engine_flight_cycles = window_at
        elif action["combination"] == FIRST:
            hub.latest_engine_flight_cycles = min(visit_leg, window_at)
        elif visit_at is None or limit_at is None:
            hub.latest_engine_flight_cycles = max(visit_leg, window_at)
        else:
            hub.readings = {
                "A": max(min(visit_at, limit_at), window_at),
                "B": min(visit_at, max(limit_at, window_at)),
            }
            if hub.readings["A"] != hub.readings["B"]:
                result.notes.append(
                    f"Paragraph {action['paragraph']} reads two ways for the "
                    f"{hub.position}: counter {hub.readings['A']:,} (A, the visit "
                    f"before the limit or the window, whichever is later) or "
                    f"{hub.readings['B']:,} (B, the visit, but no earlier than "
                    "the later of the limit and the window). A person must decide."
                )
                hub.timing = (
                    f"The qualifying shop visit at engine counter {visit_at:,} falls "
                    f"inside the {window}-flight-cycle window after the effective "
                    f"date, and paragraph {action['paragraph']} reads two ways: "
                    f"counter {hub.readings['A']:,} or {hub.readings['B']:,}."
                )
                return "needs_review"
            hub.latest_engine_flight_cycles = hub.readings["A"]

        latest = hub.latest_engine_flight_cycles
        visit = (
            f"at the qualifying engine shop visit at counter {visit_at:,}"
            if visit_at is not None
            else "at the next qualifying engine shop visit"
        )
        hub.timing = (
            f"Paragraph {action['paragraph']}: act on the {hub.position} {visit}, "
            f"no later than engine counter {latest:,}."
        )
        if hub.component_cycles_remaining is not None:
            hub.timing += (
                f" ({hub.component_cycles_remaining:,} part cycles remain to the "
                "listed limit.)"
                if hub.component_cycles_remaining >= 0
                else f" The part is already {-hub.component_cycles_remaining:,} "
                "cycles past its listed limit."
            )
        return "action_required"

    def _event_action(
        self, action: dict[str, Any], parts: list[HubFinding], effective: date
    ) -> str | None:
        """Actions on the condition parts, due at a future shop visit."""
        if not parts:
            return "no_action_triggered"
        trigger = action["trigger"]
        if (
            trigger
            not in (
                "next_shop_visit_after_effective_date",
                "next_shop_visit_after_effective_date_with_condition",
            )
            or action["limits"]
        ):
            return self._unsupported(action, "its trigger or limits")
        self.cite(action["paragraph"], "the required action and when it is due")
        if action["shop_visit_definition_paragraph"]:
            self.cite(action["shop_visit_definition_paragraph"], "engine shop visit")
        condition = action["condition_description"]
        if action["condition_definition_paragraph"]:
            self.cite(
                action["condition_definition_paragraph"], "what the condition means"
            )
        when = (
            f"at the next engine shop visit inducted after {effective.isoformat()}"
            + (f" where {condition}" if condition else "")
        )
        visits = self._visits_after(effective)
        unknown = [v for v in visits if v["qualifies"] not in ("yes", "no")]
        counted = [v for v in visits if v["qualifies"] == "yes"]
        for visit in unknown:
            self.result.missing_facts.append(
                f"events[{visit['at']}].qualifies_as_engine_shop_visit"
            )
        self.timing_parts.append(
            f"Paragraph {action['paragraph']}: {action['description']} Due {when}; "
            "no cycle or calendar limit applies."
        )
        if unknown:
            return "needs_review"
        if not counted:
            return "action_required_on_event"
        first = counted[0]
        if trigger.endswith("_with_condition"):
            self.result.notes.append(
                f"A qualifying shop visit was inducted on {first['at']}. Whether "
                f"{condition or 'the condition'} "
                "occurred at it, as the directive defines it, is not a structured "
                "record field, so a person must decide whether the action is due."
            )
            return "needs_review"
        self.timing_parts.append(
            f"The shop visit inducted on {first['at']} is that visit."
        )
        return "action_required"

    def _unsupported(self, action: dict[str, Any], what: str) -> str:
        self.cite(action["paragraph"], "a required action this screen cannot evaluate")
        self.result.notes.append(
            f"The rule record's paragraph {action['paragraph']} action is not "
            f"evaluated: this interpreter does not support {what}. A person must "
            "decide."
        )
        return "needs_review"

    def _not_yet_effective(self, matched: list[HubFinding], effective: date) -> None:
        result = self.result
        result.action_status = "no_action_triggered"
        result.missing_facts.clear()
        result.summary = (
            f"The engine is within the directive's applicability, but {self.ad} "
            f"does not take effect until {effective.isoformat()}. Nothing is "
            "required yet."
        )
        actions = "; ".join(
            f"paragraph {a['paragraph']}: {a['description']}"
            for a in self.rules["required_actions"]
        )
        listed = "; ".join(f"{h.position} S/N {h.serial_number}" for h in matched)
        result.timing = f"From {effective.isoformat()}, {actions}" + (
            f" Listed parts installed: {listed}." if listed else ""
        )

    def _operator_claims(self, matched: bool) -> None:
        """Report operator assertions as facts to verify; never let them clear."""
        result = self.result
        claims = [c for c in self.asset.get("amoc_claims", []) if c["ad"] == self.ad]
        if claims:
            if self.rules["amoc_paragraph"]:
                self.cite(
                    self.rules["amoc_paragraph"],
                    "AMOCs must be approved by the FAA before use",
                )
            result.notes.append(
                "An AMOC is claimed, but no FAA approval is on file. The required "
                "action stands unless a person verifies an approved AMOC and its "
                "scope."
            )
            if matched:
                result.missing_facts.append(f"amoc_claims[{self.ad}]")
        for record in self.asset.get("ad_records", []):
            if record["ad"] == self.ad:
                result.notes.append(
                    f"The operator's AD record shows '{record['recorded_status']}'. "
                    "This screen does not use that record; a person should review "
                    "it against the findings above."
                )

    # Events and wording --------------------------------------------------

    def _visits_after(self, effective: date) -> list[dict[str, Any]]:
        visits = [
            {
                "at": event["at"],
                "qualifies": event.get("qualifies_as_engine_shop_visit", {}).get(
                    self.ad, UNKNOWN
                ),
                "counter": event.get("engine_flight_cycles_at_event"),
            }
            for event in self.asset.get("events", [])
            if event["event_type"] == "shop_visit_induction"
            and date.fromisoformat(event["at"]) > effective
        ]
        return sorted(visits, key=lambda visit: visit["at"])

    def _next_counted_visit(self, effective: date) -> int | None:
        counters = [
            visit["counter"]
            for visit in self._visits_after(effective)
            if visit["qualifies"] == "yes" and visit["counter"] is not None
        ]
        return min(counters) if counters else None

    def _summary(self, model: str) -> str:
        result = self.result
        applies = f"{model} is within the directive's applicability."
        if result.action_status == "action_required":
            return f"{applies} A listed part is installed and a required action is due."
        if result.action_status == "action_required_on_event":
            return (
                f"{applies} A listed part is installed; the required action is due "
                "only when its triggering event occurs."
            )
        if result.action_status == "needs_review":
            return (
                f"{applies} A required fact or reading is missing or unsettled, so "
                "the outcome is left to a person."
            )
        obligations = (
            " The installation prohibition continues to bind this engine."
            if result.continuing_obligations
            else ""
        )
        return f"{applies} No required action is triggered by the supplied records.{obligations}"

    def _timing(self, matched: list[HubFinding]) -> str | None:
        parts = [h.timing for h in matched if h.timing] + self.timing_parts
        dated = [h for h in matched if h.latest_engine_flight_cycles is not None]
        if len(dated) > 1:
            first = min(dated, key=lambda h: h.latest_engine_flight_cycles or 0)
            parts.append(
                f"Each listed part must be acted on; the earliest deadline is the "
                f"{first.position}'s, engine counter "
                f"{first.latest_engine_flight_cycles:,}."
            )
        for hub in self.result.hubs:
            if hub.outcome in ("missing", "identity_unconfirmed"):
                parts.append(
                    f"Whether the {hub.position} is affected is unknown until its "
                    "missing or unconfirmed record is resolved."
                )
        return " ".join(parts) or None


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


def _name_key(name: str) -> str:
    return " ".join(name.lower().replace("-", " ").split())


def _same_identifier(listed: str, recorded: str) -> bool:
    """Compare identifiers ignoring case and whitespace."""
    return "".join(listed.split()).upper() == "".join(recorded.split()).upper()
