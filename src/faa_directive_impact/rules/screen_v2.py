"""Screen one engine against a version 2 rule record.

A version 2 record (``schemas/rule-record-v2.schema.json``) generalizes
version 1 so every in-scope V2500-A5/D5/E5 directive can be stated: part
groups (listed serials, any serial, or serials held in unavailable material),
engine serial ranges, per-action models and operator conditions, triggers
(shop visit, other defined maintenance events, each installation, counted
from another action), limits with roles (caps the event, alternative leg,
overall cap), dependencies on unavailable material, supersession, and
terminating actions.

Rules the engine follows, in order of precedence:

- Never guess. An unsupported construct, a missing fact, or an unavailable
  list sends the engine to ``needs_review`` with the item named. A damaged or
  unknown input is never cleared.
- Facts before records. An installed part that a removal action names means
  the action is open, whatever the operator's AD record says.
- Operator records (``evaluation/coverage/PREREGISTRATION.md``). For an action
  whose compliance time has passed: an operator record of ``complied`` or
  ``recurring`` gives ``no_action_triggered`` with a note that the screen does
  not verify it; no record, ``open``, or ``not_applicable`` gives
  ``needs_review`` naming ``ad_records[AD ...]``.
- An event that may or may not have triggered an action (a visit whose
  qualification is unknown, a maintenance event the record cannot identify) is
  evaluated both ways. If both readings give the same status the status
  stands; otherwise a person decides.
"""

import re
from dataclasses import dataclass, field
from datetime import date, timedelta
from typing import Any

from faa_directive_impact.impact.hpt_hub_rules import (
    SUPPORTED_ENGINE_MODELS,
    UNKNOWN,
    Citation,
    HubFinding,
    Screen,
)

STATUS_ORDER = (
    "needs_review",
    "action_required",
    "action_required_on_event",
    "no_action_triggered",
)
FIRST = "whichever_occurs_first"
LATER = "whichever_occurs_later"
RECORD_ACCOMPLISHED = "the operator's AD record shows this action accomplished; this screen does not verify it."
MAINTENANCE_EVENT_TYPES = (
    "shop_visit_induction",
    "component_exposure",
    "component_removal",
)
SERIAL_FORM = re.compile(r"^([A-Z]+)([0-9]+)$")


@dataclass
class _Group:
    """What the engine record shows for one part group."""

    outcome: str  # matched | clear | unknown
    findings: list[HubFinding] = field(default_factory=list)


@dataclass
class _Event:
    """The triggering event under one reading: occurred (with when) or not."""

    occurred: bool
    at: date | None = None
    counter: int | None = None


@dataclass
class _Timing:
    """One action's deadline under one reading of the events."""

    status: str  # open | pending | passed | unknown | readings_differ | unsupported
    counter: int | None = None
    on_date: date | None = None
    remaining: int | None = None
    readings: dict[str, int] = field(default_factory=dict)
    missing: list[str] = field(default_factory=list)
    text: str = ""


def screen_rules_v2(
    rules: dict[str, Any], asset: dict[str, Any], as_of: date
) -> Screen:
    """Screen a well-formed engine snapshot (checked by the caller)."""
    return _Run(rules, asset, as_of).screen()


class _Run:
    def __init__(self, rules: dict[str, Any], asset: dict[str, Any], as_of: date):
        self.rules = rules
        self.asset = asset
        self.as_of = as_of
        self.document = rules["governing_document"]["document"]
        self.ad = rules["ad_number"]
        self.effective = date.fromisoformat(rules["effective_date"]["date"])
        self.groups = {group["id"]: group for group in rules["parts"]}
        self.dependencies = {d["id"]: d for d in rules["dependencies"]}
        self.group_states: dict[str, _Group] = {}
        self.timing_parts: list[str] = []
        self.latest: list[int] = []
        self.remaining: list[int] = []
        self.readings: list[dict[str, int]] = []
        self.records_used = False
        self.result = Screen(
            rules["final_rule_document"], self.ad, "applies", "no_action_triggered"
        )

    # Output helpers ------------------------------------------------------

    def cite(self, paragraph: str, supports: str, locator: str | None = None) -> None:
        if not paragraph:
            return
        citation = Citation(self.document, paragraph, locator, supports)
        if citation not in self.result.citations:
            self.result.citations.append(citation)

    def missing(self, fact: str) -> None:
        if fact not in self.result.missing_facts:
            self.result.missing_facts.append(fact)

    def note(self, text: str) -> None:
        if text not in self.result.notes:
            self.result.notes.append(text)

    # Screen --------------------------------------------------------------

    def screen(self) -> Screen:
        result = self.result
        superseding = self._superseding()
        if superseding is not None:
            return self._superseded(superseding)

        in_force = self.as_of >= self.effective
        emergency = self.rules["effective_date"]["emergency_ad"]
        if not in_force:
            result.authority_state = "published_not_yet_effective"
            self.cite(
                self.rules["effective_date"]["paragraph"],
                f"the AD takes effect on {self.effective.isoformat()}",
            )

        model = self.asset["engine"]["engine_model"]
        if not self._model_applies(model):
            return result
        if not self._engine_serial_applies(model):
            return result
        if not self._parts_apply():
            return result

        if not in_force:
            if emergency and date.fromisoformat(emergency["issued"]) <= self.as_of:
                self._notice_date_missing(emergency)
                result.action_status = "needs_review"
                result.summary = (
                    f"{model} is within the directive's applicability. Its published "
                    f"effective date is {self.effective.isoformat()}, but "
                    f"{emergency['ad_number']} bound operators from their date of "
                    "actual notice, which the record does not show."
                )
                return result
            self._not_yet_effective()
            return result

        for obligation in self.rules["continuing_obligations"]:
            result.continuing_obligations.append(
                {
                    "paragraph": obligation["paragraph"],
                    "text": obligation["description"],
                }
            )
            self.cite(obligation["paragraph"], "continuing obligation")
        for relation in self.rules["relationships"]:
            if relation["type"] == "terminated_by_compliance":
                self.note(
                    f"Under {relation['ad_number']} paragraph {relation['paragraph']}, "
                    f"{relation['description']} This screen does not check that "
                    "directive's work."
                )

        statuses = self._actions(model)
        self._operator_claims()

        if result.missing_facts and "action_required" not in statuses:
            statuses.append("needs_review")
        statuses = [s for s in statuses if s] or ["no_action_triggered"]
        result.action_status = min(statuses, key=STATUS_ORDER.index)
        if self.latest:
            result.computed["latest_engine_flight_cycles"] = min(self.latest)
        if self.remaining:
            result.computed["component_cycles_remaining"] = min(self.remaining)
        if len(self.readings) == 1:
            result.computed["readings"] = self.readings[0]
        result.summary = self._summary(model)
        result.timing = " ".join(self.timing_parts) or None
        return result

    # Authority -----------------------------------------------------------

    def _superseding(self) -> dict[str, Any] | None:
        for relation in self.rules["relationships"]:
            when = relation["effective_date"]
            if (
                relation["type"] == "superseded_by"
                and when is not None
                and self.as_of >= date.fromisoformat(when)
            ):
                return relation
        return None

    def _superseded(self, relation: dict[str, Any]) -> Screen:
        result = self.result
        result.applicability = "superseded"
        result.authority_state = "superseded"
        result.action_status = None
        result.citations.append(
            Citation(
                relation["stated_in"],
                relation["paragraph"],
                None,
                f"{relation['ad_number']} replaces {self.ad}",
            )
        )
        result.summary = (
            f"{self.ad} was replaced by {relation['ad_number']} from "
            f"{relation['effective_date']}; its requirements are screened under "
            f"{relation['ad_number']}, not separately."
        )
        return result

    def _notice_date_missing(self, emergency: dict[str, Any]) -> None:
        self.missing(
            f"operator date of actual notice of Emergency {emergency['ad_number']}"
        )
        self.cite(
            self.rules["effective_date"]["paragraph"],
            f"effective on actual notice of Emergency {emergency['ad_number']}",
        )

    def _not_yet_effective(self) -> None:
        result = self.result
        result.action_status = "no_action_triggered"
        result.summary = (
            f"The engine is within the directive's applicability, but {self.ad} "
            f"does not take effect until {self.effective.isoformat()}. Nothing is "
            "required yet."
        )
        actions = "; ".join(
            f"paragraph {a['paragraph']}: {a['description']}"
            for a in self.rules["required_actions"]
        )
        result.timing = f"From {self.effective.isoformat()}, {actions}"

    # Applicability -------------------------------------------------------

    def _model_applies(self, model: str) -> bool:
        result = self.result
        paragraph = self.rules["applicability"]["models_paragraph"]
        if model == UNKNOWN:
            result.applicability, result.action_status = "unknown", "needs_review"
            self.missing("engine.engine_model")
            self.cite(paragraph, "the applicable engine models")
            result.summary = (
                "The engine model is not recorded, so applicability cannot be "
                f"decided against the models listed in paragraph {paragraph}."
            )
            return False
        if model not in SUPPORTED_ENGINE_MODELS:
            result.applicability, result.action_status = "outside_supported_scope", None
            self.cite(paragraph, "the applicable engine models")
            result.summary = (
                f"{model} is not one of the supported V2500-A5/D5/E5 variants. "
                "This screen makes no applicability determination for it."
            )
            return False
        if model not in self.rules["applicability"]["engine_models"]:
            result.applicability, result.action_status = "does_not_apply", None
            self.cite(paragraph, f"{model} is not among the listed models")
            result.summary = f"{model} is not listed in paragraph {paragraph}."
            return False
        self.cite(paragraph, f"{model} is a listed model")
        return True

    def _engine_serial_applies(self, model: str) -> bool:
        conditions = [
            c
            for c in self.rules["applicability"]["engine_serials"]
            if model in c["models"]
        ]
        if not conditions:
            return True
        result = self.result
        serial = self.asset["engine"].get("engine_serial_number")
        for condition in conditions:
            paragraph = condition["paragraph"]
            if not isinstance(serial, str) or not serial.strip() or serial == UNKNOWN:
                return self._serial_unknown(
                    paragraph, "the engine serial number is not recorded"
                )
            if not (serial.isascii() and serial.isprintable()):
                return self._serial_unknown(
                    paragraph, f"the engine serial number {serial!r} is not plain text"
                )
            near = [
                s
                for s in condition["serial_numbers"] + condition["excluded"]
                if s != serial and _same_identifier(s, serial)
            ]
            if near:
                return self._serial_unknown(
                    paragraph,
                    f"engine S/N {serial} matches {near[0]} only when case or "
                    "spacing is ignored",
                )
            if serial in condition["excluded"]:
                result.applicability, result.action_status = "does_not_apply", None
                self.cite(
                    paragraph, f"engine S/N {serial} is excluded", f"S/N {serial}"
                )
                result.summary = f"Paragraph {paragraph} excludes engine S/N {serial}."
                return False
            if serial in condition["serial_numbers"]:
                self.cite(paragraph, f"engine S/N {serial} is listed", f"S/N {serial}")
                continue
            if condition["ranges"]:
                inside = _in_ranges(serial, condition["ranges"])
                if inside is None:
                    return self._serial_unknown(
                        paragraph,
                        f"engine S/N {serial} is not in the letter-and-number form "
                        "the ranges are written in, so it cannot be placed",
                    )
                if inside:
                    self.cite(
                        paragraph,
                        f"engine S/N {serial} is within a listed range",
                        f"S/N {serial}",
                    )
                    continue
            result.applicability, result.action_status = "does_not_apply", None
            self.cite(paragraph, f"engine S/N {serial} is not among the listed serials")
            result.summary = (
                f"Paragraph {paragraph} limits {model} engines to listed serial "
                f"numbers, and S/N {serial} is not among them."
            )
            return False
        return True

    def _serial_unknown(self, paragraph: str, reason: str) -> bool:
        result = self.result
        result.applicability, result.action_status = "unknown", "needs_review"
        self.missing("engine.engine_serial_number")
        self.cite(paragraph, "applicability depends on the engine serial number")
        result.summary = (
            f"Paragraph {paragraph} applies only to certain engine serial numbers, "
            f"and {reason}."
        )
        return False

    def _parts_apply(self) -> bool:
        applicability = self.rules["applicability"]
        ids = applicability["parts"]
        if not ids:
            return True
        result = self.result
        states = [self._group(group_id) for group_id in ids]
        outcomes = [s.outcome for s in states]
        paragraph = applicability["parts_paragraph"]
        if applicability["parts_combine"] == "all":
            settled = (
                "applies"
                if all(o == "matched" for o in outcomes)
                else "does_not_apply"
                if "clear" in outcomes
                else "unknown"
            )
        else:
            settled = (
                "applies"
                if "matched" in outcomes
                else "unknown"
                if "unknown" in outcomes
                else "does_not_apply"
            )
        names = " and " if applicability["parts_combine"] == "all" else " or "
        described = names.join(
            f"{self.groups[i]['component']} P/N {'/'.join(self.groups[i]['part_numbers'])}"
            for i in ids
        )
        if settled == "applies":
            self.cite(paragraph, f"the engine has an installed {described}")
            return True
        if settled == "does_not_apply":
            result.applicability, result.action_status = "does_not_apply", None
            self.cite(paragraph, f"the AD applies only with an installed {described}")
            result.summary = (
                f"Paragraph {paragraph} covers only engines with an installed "
                f"{described}, and the engine record shows none."
            )
            return False
        result.applicability, result.action_status = "unknown", "needs_review"
        self.cite(paragraph, "applicability depends on the installed parts")
        result.summary = (
            f"Paragraph {paragraph} covers only engines with an installed {described}, "
            "and the record does not settle whether one is installed."
        )
        return False

    def _group(self, group_id: str) -> _Group:
        if group_id in self.group_states:
            return self.group_states[group_id]
        group = self.groups[group_id]
        names = {_name_key(n) for n in [group["component"], *group["aliases"]]}
        numbers = set(group["part_numbers"])
        eligible = {
            number: part
            for part in self.rules["eligible_parts"]
            if part["part_group"] == group_id
            for number in part["part_numbers"]
        }
        candidates = [
            c
            for c in self.asset["installed_components"]
            if c["part_number"] in numbers
            or c["part_number"] in eligible
            or _name_key(c["component_name"]) in names
        ]
        if not candidates:
            self.missing(f"installed_components[{group['component']}]")
            self.cite(group["paragraph"], f"no {group['component']} record to compare")
            state = _Group(
                "unknown",
                [
                    HubFinding(
                        group["component"],
                        None,
                        None,
                        "missing",
                        f"No {group['component']} record was supplied, so a part "
                        f"named in paragraph {group['paragraph']} can be neither "
                        "found nor excluded.",
                    )
                ],
            )
        else:
            findings = [self._check(group, c, eligible) for c in candidates]
            outcomes = {f.outcome for f in findings}
            state = _Group(
                "matched"
                if "matched" in outcomes
                else "unknown"
                if outcomes & {"missing", "identity_unconfirmed", "unverifiable"}
                else "clear",
                findings,
            )
        self.group_states[group_id] = state
        self.result.hubs.extend(state.findings)
        return state

    def _check(
        self,
        group: dict[str, Any],
        component: dict[str, Any],
        eligible: dict[str, dict[str, Any]],
    ) -> HubFinding:
        """Compare one installed component with one part group."""
        name = component["component_name"]
        part_number = component["part_number"]
        serial = component["serial_number"]
        paragraph = group["paragraph"]
        if part_number == UNKNOWN:
            self.missing(f"installed_components[{name}].part_number")
            self.cite(paragraph, f"{name} P/N unknown")
            return HubFinding(
                name,
                None,
                serial,
                "missing",
                f"The {name} P/N is unknown, so it cannot be compared with the "
                f"parts named in paragraph {paragraph}.",
            )
        rows = group["listed"]
        if part_number in group["part_numbers"]:
            if group["serials"] == "any":
                self.cite(
                    paragraph,
                    f"{name} P/N {part_number} is a listed part",
                    f"P/N {part_number}",
                )
                return HubFinding(
                    name,
                    part_number,
                    serial,
                    "matched",
                    f"The {name} P/N {part_number} is named in paragraph {paragraph}.",
                    table_row={"part_number": part_number, "serial_number": None},
                )
            if group["serials"] == "listed_in_dependency":
                title = self.dependencies[group["dependency"]]["title"]
                self.missing(f"{title} (unavailable incorporated material)")
                self.cite(
                    paragraph,
                    f"{name} P/N {part_number} is affected only if its S/N is listed "
                    f"in {title}",
                    f"P/N {part_number}",
                )
                return HubFinding(
                    name,
                    part_number,
                    serial,
                    "unverifiable",
                    f"The {name} has P/N {part_number}; paragraph {paragraph} covers "
                    f"it only if S/N {serial} is listed in {title}, which is not "
                    "available to this screen.",
                )
            same_number = [r for r in rows if r["part_number"] == part_number]
            if same_number and serial == UNKNOWN:
                self.missing(f"installed_components[{name}].serial_number")
                self.cite(paragraph, f"{name} has a listed P/N", f"P/N {part_number}")
                return HubFinding(
                    name,
                    part_number,
                    None,
                    "missing",
                    f"The {name} has listed P/N {part_number}, but its S/N is "
                    "unknown, so it may be a listed part.",
                )
            exact = [r for r in same_number if r["serial_number"] == serial]
            if exact:
                row = exact[0]
                self.cite(paragraph, f"{name} matches a listed part", f"S/N {serial}")
                limit = row["cycles_since_new_limit"]
                detail = f" (limit {limit:,} cycles since new)" if limit else ""
                return HubFinding(
                    name,
                    part_number,
                    serial,
                    "matched",
                    f"The {name} P/N {part_number} S/N {serial} matches a part "
                    f"listed in paragraph {paragraph}{detail}.",
                    table_row=row,
                )
        elif part_number in eligible:
            part = eligible[part_number]
            self.cite(
                part["paragraph"],
                f"P/N {part_number} is eligible for installation",
                f"P/N {part_number}",
            )
            return HubFinding(
                name,
                part_number,
                serial,
                "not_listed",
                f"The {name} is P/N {part_number}, a part eligible for installation "
                f"under paragraph {part['paragraph']}.",
            )
        # A listed S/N under another or differently written identity may be a
        # mis-keyed record of the listed part; only the record holder can say.
        for row in rows:
            if serial != UNKNOWN and _same_identifier(row["serial_number"], serial):
                field_name = (
                    "serial_number"
                    if row["part_number"] == part_number
                    else "part_number"
                )
                self.missing(f"installed_components[{name}].{field_name}")
                self.cite(
                    paragraph,
                    "a listed S/N recorded under a different identity",
                    f"S/N {row['serial_number']}",
                )
                return HubFinding(
                    name,
                    part_number,
                    serial,
                    "identity_unconfirmed",
                    f"The {name} is recorded as P/N {part_number} S/N {serial}; "
                    f"paragraph {paragraph} lists P/N {row['part_number']} S/N "
                    f"{row['serial_number']}. A person must confirm whether this is "
                    "the listed part.",
                    table_row=row,
                )
        self.cite(paragraph, f"the installed {name} is not a listed part")
        return HubFinding(
            name,
            part_number,
            serial,
            "not_listed",
            f"The {name} P/N {part_number} S/N {serial} is not a part named in "
            f"paragraph {paragraph}.",
        )

    # Actions -------------------------------------------------------------

    def _actions(self, model: str) -> list[str | None]:
        actions = [
            a
            for a in self.rules["required_actions"]
            if not a["models"] or model in a["models"]
        ]
        ended: set[str] = set()
        statuses: list[str | None] = []
        # A terminating action whose compliance time has passed ends the
        # actions it names: their status is the terminating action's.
        for action in actions:
            if action["terminates"]:
                status, passed = self._action(action)
                statuses.append(status)
                if passed:
                    ended.update(action["terminates"])
                    self.note(
                        f"Paragraph {action['paragraph']} is a terminating action "
                        "whose compliance time has passed, so paragraphs "
                        f"{', '.join(action['terminates'])} are not screened "
                        "separately."
                    )
        for action in actions:
            if action["terminates"] or action["paragraph"] in ended:
                continue
            statuses.append(self._action(action)[0])
        return statuses

    def _action(self, action: dict[str, Any]) -> tuple[str | None, bool]:
        """One action's status, and whether its compliance time has passed."""
        paragraph = action["paragraph"]
        if action["kind"] == "replace_if_finding":
            self.timing_parts.append(
                f"Paragraph {paragraph} (if an inspection finds the condition): "
                f"{action['description']}"
            )
            return None, False
        if action["kind"] == "other":
            return self._unsupported(action, "this kind of action"), False
        if action["operator_condition"]:
            carrier = (self.asset.get("operator") or {}).get("air_carrier_operation")
            if carrier == "no":
                self.cite(paragraph, "binds air carrier operations only")
                return None, False
            if carrier != "yes":
                self.missing("operator.air_carrier_operation")
                self.cite(paragraph, "binds air carrier operations only")
                self.timing_parts.append(
                    f"Whether paragraph {paragraph} also applies depends on whether "
                    "the engine is in air carrier operation, which the record does "
                    "not show."
                )
                return "needs_review", False

        # From here, an action blocked only by a missing fact returns no status
        # of its own: the fact is named, and the screen goes to review unless
        # another action is established and timed (as in S1).
        parts: list[HubFinding] = []
        if action["target"]:
            state = self._group(action["target"])
            if state.outcome == "clear":
                self.cite(paragraph, "no installed part is named for this action")
                return "no_action_triggered", False
            if state.outcome == "unknown":
                self.cite(paragraph, "the action depends on the installed part")
                return None, False
            parts = [f for f in state.findings if f.outcome == "matched"]

        if action["dependencies"]:
            for dependency_id in action["dependencies"]:
                dependency = self.dependencies[dependency_id]
                self.missing(
                    f"{dependency['title']} (unavailable incorporated material)"
                )
                self.cite(dependency["paragraph"], "material this screen does not have")
            self.cite(
                paragraph, "a required action that depends on unavailable material"
            )
            self.timing_parts.append(
                f"Paragraph {paragraph}: {action['description']} Whether and when it "
                "applies is set by material this screen does not have."
            )
            return None, False
        if action["unrecorded_conditions"]:
            for condition in action["unrecorded_conditions"]:
                self.missing(f"{condition['description']} ({condition['paragraph']})")
            self.cite(paragraph, "a required action whose condition no record holds")
            self.timing_parts.append(
                f"Paragraph {paragraph}: {action['description']} Whether it applies "
                "depends on a condition no engine record field holds."
            )
            return None, False
        if action["combination"] == "unclear":
            return self._unsupported(action, "how its limits combine"), False
        if action["trigger"]["event"] == "none" and not any(
            limit["role"] == "alternative" for limit in action["limits"]
        ):
            return self._unsupported(
                action, "an action with no event and no limit"
            ), False
        for limit in action["limits"]:
            if limit["kind"] == "other" or limit["dependency"]:
                return self._unsupported(action, "one of its limits"), False
            if (
                limit["kind"]
                in ("days_after_effective_date", "flight_cycles_after_effective_date")
                and limit["value"] is None
            ):
                return self._unsupported(action, "a limit with no value"), False
            if limit["kind"] == "calendar_date" and limit["date"] is None:
                return self._unsupported(action, "a limit with no date"), False

        trigger = action["trigger"]
        self.cite(paragraph, "the required action and its compliance time")
        if trigger["definition_paragraph"]:
            self.cite(
                trigger["definition_paragraph"], "how the triggering event is defined"
            )
        if trigger["event"] == "prior_action":
            self.timing_parts.append(
                f"Paragraph {paragraph}: {action['description']} It is counted from "
                f"{trigger['condition'] or 'another action of this AD'}, which the "
                "record does not date; it binds once that action is done."
            )
            return None, False
        if trigger["recurrence"] == "each" or trigger["event"] == "part_installation":
            self.timing_parts.append(
                f"Paragraph {paragraph}: {action['description']} Due at each "
                f"{trigger['condition'] or trigger['event'].replace('_', ' ')}; "
                "this recurs and has no cycle or calendar deadline."
            )
            return "action_required_on_event", False

        targets: list[HubFinding | None] = list(parts) if parts else [None]
        statuses = []
        passed_all = True
        for part in targets:
            status, passed = self._timed(action, part)
            statuses.append(status)
            passed_all = passed_all and passed
        return min(statuses, key=STATUS_ORDER.index), passed_all

    def _timed(
        self, action: dict[str, Any], part: HubFinding | None
    ) -> tuple[str, bool]:
        """Status of a next-event or compliance-time action for one target."""
        paragraph = action["paragraph"]
        readings = self._event_readings(action)
        timings = [self._deadline(action, part, event) for event in readings]
        kinds = {t.status for t in timings}
        if "unsupported" in kinds:
            return self._unsupported(
                action, "combining calendar and cycle limits this way"
            ), False

        emergency = self.rules["effective_date"]["emergency_ad"]
        remove = action["kind"] == "remove"
        verdicts = [self._verdict(t, remove, bool(emergency)) for t in timings]
        first = timings[0]
        where = f"the {part.position}" if part else "the engine"

        if len(set(verdicts)) > 1:
            for t in timings:
                for fact in t.missing:
                    self.missing(fact)
            self._event_unsettled_note(action, readings)
            self.timing_parts.append(
                f"Paragraph {paragraph}: {action['description']} Whether it is due "
                "now depends on an event the record does not settle."
            )
            return "needs_review", False

        verdict = verdicts[0]
        same_numbers = all(
            (t.counter, t.on_date) == (first.counter, first.on_date) for t in timings
        )
        if len(timings) > 1 and not same_numbers:
            self._event_unsettled_note(action, readings)
        if first.status == "readings_differ":
            self.readings.append(first.readings)
            self.note(
                f"Paragraph {paragraph} reads two ways for {where}: counter "
                f"{first.readings['A']:,} (A, the event before the cap or the "
                f"alternative, whichever is later) or {first.readings['B']:,} (B, the "
                "event, but no earlier than the later of the cap and the "
                "alternative). A person must decide."
            )
            if part:
                part.readings = first.readings
            self.timing_parts.append(first.text)
            return "needs_review", False
        for fact in first.missing:
            self.missing(fact)

        if same_numbers and first.counter is not None:
            self.latest.append(first.counter)
            if part:
                part.latest_engine_flight_cycles = first.counter
        if first.remaining is not None:
            self.remaining.append(first.remaining)
            if part:
                part.component_cycles_remaining = first.remaining
        if part:
            part.timing = first.text
        self.timing_parts.append(first.text)
        if emergency and verdict == "needs_review_notice":
            self._notice_date_missing(emergency)
            self.note(
                f"Paragraph {paragraph}'s deadline is counted from the effective date, "
                f"which for an operator with actual notice of Emergency "
                f"{emergency['ad_number']} is earlier than "
                f"{self.effective.isoformat()}; the deadline above is the latest "
                "possible one."
            )
            return "needs_review", False
        if verdict == "passed":
            return self._operator_record(action, where), True
        return verdict, first.status == "passed"

    def _verdict(self, timing: _Timing, remove: bool, emergency: bool) -> str:
        """The status a timing gives, before operator records are read."""
        if timing.status in ("unknown", "readings_differ"):
            return "needs_review"
        if remove:
            # An installed part a removal names means the removal is open.
            if timing.status == "open":
                return "action_required_on_event"
            if emergency and timing.status == "pending":
                return "needs_review_notice"
            return "action_required"
        if timing.status == "open":
            return "action_required_on_event"
        if timing.status == "pending":
            return "needs_review_notice" if emergency else "action_required"
        return "passed"

    def _operator_record(self, action: dict[str, Any], where: str) -> str:
        """The pre-registered Operator Records rule, for a passed deadline."""
        paragraph = action["paragraph"]
        records = [r for r in self.asset.get("ad_records") or [] if r["ad"] == self.ad]
        self.records_used = True
        accomplished = [
            r for r in records if r["recorded_status"] in ("complied", "recurring")
        ]
        if accomplished:
            self.note(f"Paragraph {paragraph}: {RECORD_ACCOMPLISHED}")
            for credit in self.rules["credit_for_previous_actions"]:
                if paragraph in credit["actions"]:
                    self.cite(credit["paragraph"], "credit for previous actions")
            return "no_action_triggered"
        self.missing(f"ad_records[{self.ad}]")
        shown = (
            f"shows '{records[0]['recorded_status']}'"
            if records
            else "has no entry for this AD"
        )
        self.note(
            f"The compliance time of paragraph {paragraph} for {where} has passed, "
            f"and the operator's AD record {shown}. Whether the action was done is "
            "for a person to establish from the records."
        )
        return "needs_review"

    def _event_unsettled_note(
        self, action: dict[str, Any], readings: list[_Event]
    ) -> None:
        trigger = action["trigger"]
        happened = [e for e in readings if e.occurred and e.at]
        if not happened:
            return
        when = happened[0].at.isoformat() if happened[0].at else "an unknown date"
        what = trigger["condition"] or trigger["event"].replace("_", " ")
        self.note(
            f"An event on {when} may be the {what} that paragraph "
            f"{action['paragraph']} counts. Whether it is, as the directive defines "
            "it, is not a structured record field, so a person must decide."
        )

    # Events and deadlines ------------------------------------------------

    def _event_readings(self, action: dict[str, Any]) -> list[_Event]:
        """The possible histories of the triggering event since the effective date.

        One reading when the record settles it; two (it happened at the first
        candidate event, or not at all before the next certain one) when not.
        """
        trigger = action["trigger"]
        if trigger["event"] == "none":
            return [_Event(False)]
        candidates = []
        for event in sorted(self.asset.get("events") or [], key=lambda e: e["at"]):
            at = date.fromisoformat(event["at"])
            if at <= self.effective or at > self.as_of:
                continue
            counter = event.get("engine_flight_cycles_at_event")
            if trigger["event"] == "engine_shop_visit":
                if event["event_type"] != "shop_visit_induction":
                    continue
                answer = (event.get("qualifies_as_engine_shop_visit") or {}).get(
                    self.ad, UNKNOWN
                )
                if answer == "no":
                    continue
                certain = answer == "yes" and not trigger["condition"]
                if answer not in ("yes", "no"):
                    self.missing(
                        f"events[{event['at']}].qualifies_as_engine_shop_visit"
                    )
            elif event["event_type"] in MAINTENANCE_EVENT_TYPES:
                certain = False
            else:
                continue
            candidates.append((certain, _Event(True, at, counter)))
        if not candidates:
            return [_Event(False)]
        certain_at = next((e for c, e in candidates if c), None)
        if candidates[0][0]:
            return [candidates[0][1]]
        return [candidates[0][1], certain_at or _Event(False)]

    def _deadline(
        self, action: dict[str, Any], part: HubFinding | None, event: _Event
    ) -> _Timing:
        """Combine the event leg and the limits into one deadline."""
        paragraph = action["paragraph"]
        missing: list[str] = []
        caps, alternatives, overall = [], [], []
        remaining = None
        for limit in action["limits"]:
            leg, more, left = self._limit(limit, part)
            missing.extend(more)
            if left is not None:
                remaining = left
            {"caps_event": caps, "alternative": alternatives, "overall_cap": overall}[
                limit["role"]
            ].append(leg)
        if missing:
            return _Timing(
                "unknown", missing=missing, text=self._gap_text(action, part, missing)
            )

        has_event = action["trigger"]["event"] != "none"
        event_leg: tuple[int | None, date | None] | None = None  # None: still waiting
        if has_event and event.occurred:
            if event.counter is None:
                assert event.at is not None
                fact = f"events[{event.at.isoformat()}].engine_flight_cycles_at_event"
                if action["combination"] == LATER:
                    return _Timing(
                        "unknown",
                        missing=[fact],
                        text=self._gap_text(action, part, [fact]),
                    )
                # Due at the event, whose counter is not recorded: the
                # deadline has passed, but no engine counter can be stated.
                return _Timing(
                    "passed",
                    remaining=remaining,
                    text=self._due_text(action, part, event, None, None, remaining),
                )
            # Under whichever-later the event's counter competes with the other
            # legs; its date alone does not make the deadline pass.
            when = None if action["combination"] == LATER else event.at
            event_leg = _earliest([(event.counter, when), *caps])
        elif has_event and caps:
            event_leg = _earliest(caps)
        combination = action["combination"]
        legs = ([event_leg] if has_event else []) + alternatives

        readings: dict[str, int] = {}
        if combination == LATER:
            if any(leg is None for leg in legs):
                combined = None
            elif any(leg[1] is not None and leg[0] is None for leg in legs) and any(
                leg[0] is not None for leg in legs
            ):
                return _Timing("unsupported")
            else:
                combined = _latest(legs)
                if (
                    has_event
                    and event.occurred
                    and caps
                    and alternatives
                    and event.counter is not None
                    and all(c[0] is not None for c in caps + alternatives)
                ):
                    cap = min(c[0] for c in caps)
                    window = max(a[0] for a in alternatives)
                    readings = {
                        "A": max(min(event.counter, cap), window),
                        "B": min(event.counter, max(cap, window)),
                    }
                    if readings["A"] != readings["B"]:
                        return _Timing(
                            "readings_differ",
                            readings=readings,
                            remaining=remaining,
                            text=(
                                f"The event at engine counter {event.counter:,} falls "
                                f"before the alternative leg ends, and paragraph "
                                f"{paragraph} reads two ways: counter "
                                f"{readings['A']:,} or {readings['B']:,}."
                            ),
                        )
                    combined = (readings["A"], None)
        else:
            present = [leg for leg in legs if leg is not None]
            combined = _earliest(present) if present else None
        if combined is not None and overall:
            combined = _earliest([combined, *overall])
        elif combined is None and overall:
            combined = _earliest(overall)

        if combined is None:
            return _Timing(
                "open", remaining=remaining, text=self._open_text(action, part)
            )
        counter, on_date = combined
        if event.occurred and event.at and combination != LATER:
            status = "passed"
        else:
            status, unknown = self._passed(counter, on_date)
            if status == "unknown":
                return _Timing(
                    "unknown",
                    missing=unknown,
                    text=self._gap_text(action, part, unknown),
                )
        return _Timing(
            status,
            counter=counter,
            on_date=on_date,
            remaining=remaining,
            text=self._due_text(action, part, event, counter, on_date, remaining),
        )

    def _limit(
        self, limit: dict[str, Any], part: HubFinding | None
    ) -> tuple[tuple[int | None, date | None], list[str], int | None]:
        """One limit as (engine counter, date), with missing facts and part cycles left."""
        kind = limit["kind"]
        if kind == "calendar_date":
            return (None, date.fromisoformat(limit["date"])), [], None
        if kind == "days_after_effective_date":
            return (None, self.effective + timedelta(days=limit["value"])), [], None
        if kind == "flight_cycles_after_effective_date":
            anchor = self.effective + timedelta(days=limit["anchor_offset_days"])
            at_anchor = self._counter_at(anchor)
            if at_anchor is None:
                return (
                    (None, None),
                    [f"engine.engine_cycle_readings[{anchor.isoformat()}]"],
                    None,
                )
            return (at_anchor + limit["value"], None), [], None
        # part_cycles_since_new: the engine counter at which the part reaches it.
        if part is None or part.table_row is None:
            return (
                (None, None),
                ["part_cycles_since_new limit without a target part"],
                None,
            )
        value = limit["value"]
        if value is None:
            value = part.table_row.get("cycles_since_new_limit")
        if value is None:
            return (
                (None, None),
                [f"the paragraph {limit['paragraph']} limit for {part.position}"],
                None,
            )
        component = next(
            c
            for c in self.asset["installed_components"]
            if c["component_name"] == part.position
        )
        missing = []
        at_effective = self._counter_at(self.effective)
        if at_effective is None:
            missing.append(
                f"engine.engine_cycle_readings[{self.effective.isoformat()}]"
            )
        # Part cycles at the effective date come from the part's own record,
        # never from engine cycles: the two differ once a part has moved.
        csn_at_effective = {
            date.fromisoformat(r["at"]): r["cycles_since_new"]
            for r in component.get("cycles_since_new_readings") or []
        }.get(self.effective)
        if csn_at_effective is None:
            missing.append(
                f"installed_components[{part.position}]"
                f".cycles_since_new_readings[{self.effective.isoformat()}]"
            )
        csn_now = component.get("cycles_since_new")
        if not isinstance(csn_now, int):
            missing.append(f"installed_components[{part.position}].cycles_since_new")
        if missing:
            return (None, None), missing, None
        assert at_effective is not None and csn_at_effective is not None
        assert isinstance(csn_now, int)
        return (at_effective + (value - csn_at_effective), None), [], value - csn_now

    def _counter_at(self, when: date) -> int | None:
        for reading in self.asset["engine"].get("engine_cycle_readings") or []:
            if date.fromisoformat(reading["at"]) == when:
                return reading["engine_flight_cycles"]
        return None

    def _passed(
        self, counter: int | None, on_date: date | None
    ) -> tuple[str, list[str]]:
        """Whether a deadline has passed by the as-of date: passed, pending, or unknown."""
        if on_date is not None and self.as_of > on_date:
            return "passed", []
        if counter is None:
            return "pending", []
        now = self._counter_at(self.as_of)
        if now is None:
            return "unknown", [
                f"engine.engine_cycle_readings[{self.as_of.isoformat()}]"
            ]
        return ("passed" if now > counter else "pending"), []

    # Wording -------------------------------------------------------------

    def _due_text(
        self,
        action: dict[str, Any],
        part: HubFinding | None,
        event: _Event,
        counter: int | None,
        on_date: date | None,
        remaining: int | None,
    ) -> str:
        where = f" on the {part.position}" if part else ""
        bounds = []
        if counter is not None:
            bounds.append(f"engine counter {counter:,}")
        if on_date is not None:
            bounds.append(on_date.isoformat())
        when = (
            f"at the event on {event.at.isoformat()}"
            if event.occurred and event.at
            else self._event_phrase(action)
        )
        text = f"Paragraph {action['paragraph']}{where}: {action['description']} Due {when}"
        text += f", no later than {' or '.join(bounds)}." if bounds else "."
        if remaining is not None:
            text += (
                f" ({remaining:,} part cycles remain to the limit.)"
                if remaining >= 0
                else f" The part is already {-remaining:,} cycles past its limit."
            )
        return text

    def _open_text(self, action: dict[str, Any], part: HubFinding | None) -> str:
        where = f" on the {part.position}" if part else ""
        return (
            f"Paragraph {action['paragraph']}{where}: {action['description']} Due "
            f"{self._event_phrase(action)}; no cycle or calendar limit applies."
        )

    def _gap_text(
        self, action: dict[str, Any], part: HubFinding | None, missing: list[str]
    ) -> str:
        where = f" on the {part.position}" if part else ""
        return (
            f"Paragraph {action['paragraph']} requires action{where}, but its "
            "deadline cannot be computed until these are supplied: "
            + "; ".join(missing)
            + "."
        )

    def _event_phrase(self, action: dict[str, Any]) -> str:
        trigger = action["trigger"]
        if trigger["event"] == "none":
            return "within the compliance time"
        what = (
            "engine shop visit"
            if trigger["event"] == "engine_shop_visit"
            else trigger["condition"] or "triggering event"
        )
        phrase = f"at the next {what} after {self.effective.isoformat()}"
        if trigger["event"] == "engine_shop_visit" and trigger["condition"]:
            phrase += f" where {trigger['condition']}"
        return phrase

    def _unsupported(self, action: dict[str, Any], what: str) -> str:
        self.cite(action["paragraph"], "a required action this screen cannot evaluate")
        self.note(
            f"The rule record's paragraph {action['paragraph']} action is not "
            f"evaluated: this interpreter does not support {what}. A person must "
            "decide."
        )
        return "needs_review"

    def _operator_claims(self) -> None:
        """Report operator assertions as facts to verify; never let them clear."""
        result = self.result
        claims = [c for c in self.asset.get("amoc_claims") or [] if c["ad"] == self.ad]
        if claims:
            self.cite(
                self.rules["amoc_paragraph"],
                "AMOCs must be approved by the FAA before use",
            )
            self.note(
                "An AMOC is claimed, but no FAA approval is on file. The required "
                "action stands unless a person verifies an approved AMOC and its "
                "scope."
            )
            if (
                any(f.outcome == "matched" for f in result.hubs)
                or not self.rules["applicability"]["parts"]
            ):
                self.missing(f"amoc_claims[{self.ad}]")
        if self.records_used:
            return
        for record in self.asset.get("ad_records") or []:
            if record["ad"] == self.ad:
                self.note(
                    f"The operator's AD record shows '{record['recorded_status']}'. "
                    "This screen does not use that record; a person should review "
                    "it against the findings above."
                )

    def _summary(self, model: str) -> str:
        result = self.result
        applies = f"{model} is within the directive's applicability."
        if result.action_status == "action_required":
            return f"{applies} A required action is due."
        if result.action_status == "action_required_on_event":
            return (
                f"{applies} A required action is due only when its triggering event "
                "occurs."
            )
        if result.action_status == "needs_review":
            return (
                f"{applies} A required fact, record, or reading is missing or "
                "unsettled, so the outcome is left to a person."
            )
        obligations = (
            " A continuing obligation still binds this engine."
            if result.continuing_obligations
            else ""
        )
        return (
            f"{applies} No required action is triggered by the supplied records."
            f"{obligations}"
        )


def _earliest(
    legs: list[tuple[int | None, date | None]],
) -> tuple[int | None, date | None]:
    counters = [c for c, _ in legs if c is not None]
    dates = [d for _, d in legs if d is not None]
    return (min(counters) if counters else None, min(dates) if dates else None)


def _latest(
    legs: list[tuple[int | None, date | None]],
) -> tuple[int | None, date | None]:
    counters = [c for c, _ in legs if c is not None]
    dates = [d for _, d in legs if d is not None]
    return (max(counters) if counters else None, max(dates) if dates else None)


def _in_ranges(serial: str, ranges: list[dict[str, str | None]]) -> bool | None:
    """Whether an engine S/N is inside any range, or None if it cannot be placed."""
    match = SERIAL_FORM.match(serial)
    if not match:
        return None
    prefix, number = match.group(1), int(match.group(2))
    for bounds in ranges:
        limits = []
        for bound in (bounds["first"], bounds["last"]):
            if bound is None:
                limits.append(None)
                continue
            bound_match = SERIAL_FORM.match(bound)
            if not bound_match or bound_match.group(1) != prefix:
                return None
            limits.append(int(bound_match.group(2)))
        low, high = limits
        if (low is None or number >= low) and (high is None or number <= high):
            return True
    return False


def _name_key(name: str) -> str:
    return " ".join(name.lower().replace("-", " ").split())


def _same_identifier(listed: str, recorded: str) -> bool:
    """Compare identifiers ignoring case and whitespace."""
    return "".join(listed.split()).upper() == "".join(recorded.split()).upper()
