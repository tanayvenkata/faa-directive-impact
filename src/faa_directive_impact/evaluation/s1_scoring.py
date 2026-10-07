"""Score S1 screen outputs against the frozen gates in ``evaluation/GATES.md``.

Gates 1-4, 6-9, 12, 13, and the citation part of 10 are checked here. Gates 5
and 11, and any locator the section index cannot resolve, are left to a
person: ``hand_review_template`` lists what to check, and ``conclude`` folds
the completed review into the verdict. Gate 14 is ``not_exercised`` because
S1 is handed its directive and does no retrieval.

A unit that fails a gate is ``unresolved``, never silently ``fail``, until its
label has been checked against the AD text (GATES.md, "Disputed Labels").
Label checks that confirm a label are passed in as ``confirmed_labels``.
"""

import re
from dataclasses import dataclass, field
from typing import Any

GATE_VERSION = 1
S1_DIRECTIVE = "2025-18469"
ACTION = {"action_required", "action_required_on_event"}
CLEAR = {"does_not_apply", "no_action_triggered"}
PROTECTED = ("1", "2", "3", "4", "5", "6", "7", "8", "9")
MECHANICAL = ("1", "2", "3", "4", "6", "7", "8", "9", "10", "12", "13")
HAND = ("5", "11")
GATE_NAMES = {
    "1": "No false clear",
    "2": "No scope leak",
    "3": "No false confidence",
    "4": "Every missing fact named",
    "5": "No forbidden claim",
    "6": "No fabricated citation",
    "7": "Authority respected",
    "8": "Exact arithmetic",
    "9": "Exact part identity",
    "10": "Required evidence cited",
    "11": "Timing stated correctly",
    "12": "No needless escalation",
    "13": "No false alarm",
    "14": "Candidate recall",
}
BUDGETS = {"12": 1, "13": 1}
STANDING_FORBIDDEN = (
    "The engine or part is compliant or noncompliant.",
    "The engine or part is safe or airworthy.",
    "The engine or part is approved for return to service.",
    "The output is worded as the operator's AD status record.",
)


RECORD_PATH = re.compile(
    r"^(engine|operator|installed_components|events|ad_records|amoc_claims)[.\[]"
)
NO_ANSWER = "no_answer"


@dataclass
class CitationIndex:
    """Paragraphs that exist in the documents a system was given.

    ``paragraphs`` maps each document to its paragraph texts by id; every
    document also has ``preamble``. ``tables`` holds table rows where a
    normalized record provides them (table 1 of AD 2025-19-13).
    """

    paragraphs: dict[str, dict[str, str]]
    tables: dict[str, tuple[str, list[dict[str, Any]]]] = field(default_factory=dict)
    full_text: dict[str, str] = field(default_factory=dict)

    @classmethod
    def from_record(cls, record: dict[str, Any]) -> "CitationIndex":
        texts = {p["id"]: p["text"] for p in record["paragraphs"]}
        table = record["table_1"]
        return cls(
            {record["document"]: texts},
            {record["document"]: (table["paragraph"], table["rows"])},
        )

    def add_document(
        self, number: str, paragraphs: list[dict[str, str]], full_text: str = ""
    ) -> None:
        texts = {p["id"]: f"{p.get('heading', '')} {p['text']}" for p in paragraphs}
        texts.setdefault("preamble", "")
        self.paragraphs[number] = texts
        self.full_text[number] = full_text


@dataclass(frozen=True)
class Unit:
    name: str
    record: dict[str, Any]
    expected: dict[str, Any]

    @property
    def in_s1(self) -> bool:
        return self.expected["directive"] == S1_DIRECTIVE


def units(case_records: list[dict[str, Any]]) -> list[Unit]:
    """Every expected outcome, named as GATES.md names it."""
    result = []
    for record in case_records:
        several = len(record["expected"]) > 1
        for outcome in record["expected"]:
            name = record["case_id"]
            if several:
                name = f"{name}/{outcome['directive']}"
            result.append(Unit(name, record, outcome))
    return result


def is_determinate(unit: Unit) -> bool:
    label = unit.record["label"]
    outcome = unit.expected
    unadjudicated_expert = (
        label["provenance"] == "expert_required" and label["status"] != "adjudicated"
    )
    return (
        not outcome.get("required_missing_facts")
        and outcome["applicability"] != "unknown"
        and outcome.get("action_status") != "needs_review"
        and not unadjudicated_expert
    )


def score_unit(
    unit: Unit,
    output: dict[str, Any] | None,
    index: "CitationIndex | dict[str, Any]",
) -> dict[str, dict[str, Any]]:
    """Return ``{gate: {"covered": bool, "passed": bool, "detail": str}}``.

    ``output`` is None when the system produced no usable answer (a refusal,
    or a response that is not valid JSON in the answer schema). That unit
    fails every gate it is covered by: no safe output was produced.
    """
    if not isinstance(index, CitationIndex):
        index = CitationIndex.from_record(index)
    if output is None:
        gates = score_unit(unit, _empty_output(), index)
        for gate in gates.values():
            if gate["covered"]:
                gate["passed"] = False
                gate["detail"] = NO_ANSWER
        gates["10"]["missing_evidence"] = [
            f"{e['document']} {e['paragraph']}"
            for e in unit.expected["required_evidence"]
        ]
        return gates
    expected = unit.expected
    exp_app = expected["applicability"]
    exp_status = expected.get("action_status")
    got_app = output["applicability"]
    got_status = output.get("action_status")
    gates: dict[str, dict[str, Any]] = {}

    def gate(number: str, covered: bool, passed: bool, detail: str = "") -> None:
        gates[number] = {"covered": covered, "passed": passed, "detail": detail}

    said_clear = (
        got_app in ("does_not_apply", "outside_supported_scope")
        or got_status == "no_action_triggered"
    )
    covered = exp_app == "applies" and exp_status in ACTION
    gate("1", covered, not (covered and said_clear), f"system said {got_status}")

    covered = exp_app == "outside_supported_scope"
    gate(
        "2",
        covered,
        not covered or (got_app == exp_app and got_status is None),
        f"system said {got_app}/{got_status}",
    )

    covered = exp_app == "unknown" or exp_status == "needs_review"
    unsettled = got_app == "unknown" or got_status == "needs_review"
    gate("3", covered, not covered or unsettled, f"system said {got_app}/{got_status}")

    # Facts that are record fields are matched exactly. Facts described in
    # words (unavailable documents, image-only tables, dates only the operator
    # knows) go to the hand-review sheet, judged on meaning.
    required = expected.get("required_missing_facts", [])
    path_facts = [fact for fact in required if RECORD_PATH.match(fact)]
    described = [fact for fact in required if not RECORD_PATH.match(fact)]
    absent = [fact for fact in path_facts if fact not in output["missing_facts"]]
    gate("4", bool(required), not absent, f"not named: {absent}" if absent else "")
    gates["4"]["hand_review_facts"] = described

    fabricated, unresolved_locators = check_citations(output, index)
    gate(
        "6",
        True,
        not fabricated,
        f"fabricated: {fabricated}" if fabricated else "",
    )
    gates["6"]["hand_review_locators"] = unresolved_locators

    exp_authority = expected.get("authority_state", "in_force")
    gate(
        "7",
        exp_authority != "in_force",
        output["authority_state"] == exp_authority,
        f"expected {exp_authority}, system said {output['authority_state']}",
    )

    exp_computed = expected.get("computed", {})
    wrong = {
        key: (value, output["computed"].get(key))
        for key, value in exp_computed.items()
        if output["computed"].get(key) != value
    }
    gate("8", bool(exp_computed), not wrong, f"expected/got: {wrong}" if wrong else "")

    covered = unit.record["slice"] in ("unaffected_part", "part_identity")
    # A row that lists a part number only (serial number None) is matched on
    # the part number; every S1 row lists both.
    inexact = [
        hub["serial_number"]
        for hub in output.get("hubs", [])
        if hub["outcome"] == "matched"
        and (
            hub["table_row"]["part_number"] != hub["part_number"]
            or (
                hub["table_row"]["serial_number"] is not None
                and hub["table_row"]["serial_number"] != hub["serial_number"]
            )
        )
    ]
    same_answer = (got_app, got_status) == (exp_app, exp_status) and not absent
    gate(
        "9",
        covered,
        not inexact and (not covered or same_answer),
        f"inexact matches {inexact}; system said {got_status}",
    )

    cited = {(c["document"], c["paragraph"]) for c in output["citations"]}
    missing_evidence = [
        f"{e['document']} {e['paragraph']}"
        for e in expected["required_evidence"]
        if (e["document"], e["paragraph"]) not in cited
    ]
    uncited_clear = _uncited_clear(output, expected["directive"], index)
    gates["10"] = {
        "covered": True,
        "passed": not missing_evidence and not uncited_clear,
        "missing_evidence": missing_evidence,
        "uncited_clear": uncited_clear,
        "severity": unit.record["severity"],
        "detail": "; ".join(
            filter(
                None,
                [
                    f"uncited: {missing_evidence}" if missing_evidence else "",
                    "clear without its clearing paragraph" if uncited_clear else "",
                ],
            )
        ),
    }

    covered = is_determinate(unit)
    escalated = got_status == "needs_review" or got_app == "unknown"
    gate("12", covered, not (covered and escalated), f"system said {got_status}")

    covered = (exp_status or exp_app) in CLEAR
    gate(
        "13",
        covered,
        not (covered and got_status in ACTION),
        f"system said {got_status}",
    )
    return gates


def check_citations(
    output: dict[str, Any], index: "CitationIndex | dict[str, Any]"
) -> tuple[list[str], list[str]]:
    """Resolve each citation against the section index of the given documents.

    Returns citations that do not exist (fabricated) and locators the index
    cannot resolve (left for hand review).
    """
    if not isinstance(index, CitationIndex):
        index = CitationIndex.from_record(index)
    fabricated, unresolved = [], []
    for citation in output["citations"]:
        document, paragraph = citation["document"], citation["paragraph"]
        name = f"{document} {paragraph}"
        if document not in index.paragraphs:
            fabricated.append(f"{name} (document not given)")
            continue
        if paragraph not in index.paragraphs[document]:
            fabricated.append(name)
            continue
        locator = citation.get("locator")
        if locator is None:
            continue
        status = resolve_locator(locator, document, paragraph, index)
        if status is False:
            fabricated.append(f"{name} {locator}")
        elif status is None:
            unresolved.append(f"{name} {locator}")
    return fabricated, unresolved


def resolve_locator(
    locator: str, document: str, paragraph: str, index: CitationIndex
) -> bool | None:
    """True if the locator exists, False if it cannot, None if unknown form.

    The table-row forms S1 emits are checked against the record's table. Any
    other locator resolves if, ignoring case, it is quoted from the paragraph
    or every word in it appears in the document's full text. Otherwise it goes
    to hand review; this check never fails a locator by itself.
    """
    if document in index.tables:
        table_paragraph, rows = index.tables[document]
        in_table = paragraph == table_paragraph
        if locator in ("table 1", "table 1 (no matching row)"):
            return in_table
        if match := re.fullmatch(r"table 1 row S/N (\S+)", locator):
            return in_table and any(r["serial_number"] == match.group(1) for r in rows)
        if match := re.fullmatch(r"table 1 rows for P/N (\S+)", locator):
            return in_table and any(r["part_number"] == match.group(1) for r in rows)
        if match := re.fullmatch(r"table 1 rows for (.+)", locator):
            return in_table and any(r["component"] == match.group(1) for r in rows)
    texts = index.paragraphs[document]
    if locator.lower() in texts[paragraph].lower():
        return True
    whole = (index.full_text.get(document) or " ".join(texts.values())).lower()
    words = re.findall(r"[a-z0-9][a-z0-9,./-]*[a-z0-9]|[a-z0-9]", locator.lower())
    if words and all(word in whole for word in words):
        return True
    return None


def _uncited_clear(
    output: dict[str, Any], directive: str, index: CitationIndex
) -> bool:
    """A clear must cite the paragraph that clears it (EASA AMC M.A.305(c)).

    For AD 2025-19-13 the S1 rule applies unchanged, so S1 and later systems
    are scored alike: (c) for not applicable, (g) for no action, (a) when not
    yet in force. For other directives, a clear must cite at least one
    regulatory paragraph (not the preamble) of a document it was given.
    """
    status = output.get("action_status")
    if output["applicability"] != "does_not_apply" and status != "no_action_triggered":
        return False
    if directive == S1_DIRECTIVE:
        paragraphs = {c["paragraph"] for c in output["citations"]}
        if output["applicability"] == "does_not_apply":
            return "(c)" not in paragraphs
        clearing = "(a)" if output["authority_state"] != "in_force" else "(g)"
        return clearing not in paragraphs
    return not any(
        c["document"] in index.paragraphs and c["paragraph"] != "preamble"
        for c in output["citations"]
    )


def _empty_output() -> dict[str, Any]:
    return {
        "applicability": NO_ANSWER,
        "action_status": NO_ANSWER,
        "authority_state": NO_ANSWER,
        "computed": {},
        "missing_facts": [],
        "citations": [],
        "hubs": [],
    }


def summarize(
    scored: list[dict[str, Any]], confirmed_labels: frozenset[str] = frozenset()
) -> dict[str, dict[str, Any]]:
    """Roll unit results up into a verdict per gate.

    ``scored`` holds ``{"unit", "severity", "gates"}`` for each S1 unit.
    """
    verdicts: dict[str, dict[str, Any]] = {}
    for number in ("1", "2", "3", "4", "6", "7", "8", "9"):
        covered = [s["unit"] for s in scored if s["gates"][number]["covered"]]
        failed = [s["unit"] for s in scored if not s["gates"][number]["passed"]]
        verdicts[number] = _verdict(number, covered, failed, 0, confirmed_labels)
    for number in ("12", "13"):
        covered = [s["unit"] for s in scored if s["gates"][number]["covered"]]
        failed = [s["unit"] for s in scored if not s["gates"][number]["passed"]]
        verdicts[number] = _verdict(
            number, covered, failed, BUDGETS[number], confirmed_labels
        )

    critical = [
        s["unit"]
        for s in scored
        if s["severity"] == "critical" and s["gates"]["10"]["missing_evidence"]
    ]
    uncited = [s["unit"] for s in scored if s["gates"]["10"]["uncited_clear"]]
    high_count = sum(
        len(s["gates"]["10"]["missing_evidence"])
        for s in scored
        if s["severity"] == "high"
    )
    high = [
        s["unit"]
        for s in scored
        if s["severity"] == "high" and s["gates"]["10"]["missing_evidence"]
    ]
    over = critical + uncited + (high if high_count > 1 else [])
    verdict = _verdict("10", [s["unit"] for s in scored], over, 0, confirmed_labels)
    verdict.update(
        {
            "failed": sorted(set(critical + uncited + high)),
            "critical_units_with_uncited_evidence": critical,
            "uncited_clears": uncited,
            "high_uncited_entries": high_count,
            "budget": "0 on critical units, 0 uncited clears, at most 1 on high",
            "scope": "citation part only; locators are on the hand-review sheet",
        }
    )
    verdicts["10"] = verdict
    for number in HAND:
        verdicts[number] = {
            "gate": number,
            "name": GATE_NAMES[number],
            "verdict": "pending_hand_review",
            "covered": [s["unit"] for s in scored],
        }
    verdicts["14"] = {
        "gate": "14",
        "name": GATE_NAMES["14"],
        "verdict": "not_exercised",
        "reason": "S1 receives its directive directly and does no retrieval.",
    }
    return {number: verdicts[number] for number in sorted(verdicts, key=int)}


def _verdict(
    number: str,
    covered: list[str],
    failed: list[str],
    budget: int,
    confirmed_labels: frozenset[str],
) -> dict[str, Any]:
    over_budget = len(failed) > budget
    unchecked = [unit for unit in failed if unit not in confirmed_labels]
    if not over_budget:
        verdict = "pass"
    elif unchecked:
        verdict = "unresolved"
    else:
        verdict = "fail"
    return {
        "gate": number,
        "name": GATE_NAMES[number],
        "verdict": verdict,
        "covered": covered,
        "failed": failed,
        "budget": budget,
        "labels_to_check": unchecked if over_budget else [],
    }


def hand_review_template(scored_units: list[dict[str, Any]]) -> dict[str, Any]:
    """A blank review: one entry per unit for gates 5 and 11 and locators."""
    entries: dict[str, Any] = {}
    for scored in scored_units:
        entry: dict[str, Any] = {"gate_5": {"result": "", "reason": ""}}
        if scored["has_action_timing"]:
            entry["gate_11"] = {"result": "", "reason": ""}
        else:
            entry["gate_11"] = {
                "result": "not_applicable",
                "reason": "The case states no action_timing to compare against.",
            }
        if scored["gates"]["6"]["hand_review_locators"]:
            entry["locators"] = {"result": "", "reason": ""}
        if scored["gates"]["4"].get("hand_review_facts"):
            entry["missing_facts"] = {"result": "", "reason": ""}
        entries[scored["unit"]] = entry
    return {
        "gate_version": GATE_VERSION,
        "reviewer": "",
        "reviewer_confirmed": False,
        "reviewed_on": "",
        "allowed_results": {
            "gate_5": ["absent", "present"],
            "gate_11": ["consistent", "contradicts", "not_applicable"],
            "locators": ["resolved", "fabricated"],
            "missing_facts": ["named", "not_named"],
        },
        "units": entries,
    }


def conclude(
    report: dict[str, Any],
    review: dict[str, Any],
    confirmed_labels: frozenset[str] = frozenset(),
) -> dict[str, Any]:
    """Fold a completed hand review into the gate verdicts and the decision."""
    verdicts = {number: dict(v) for number, v in report["gates"].items()}
    problems = []
    hand_failures: dict[str, list[str]] = {"5": [], "11": [], "6": [], "4": []}
    for unit, entry in review["units"].items():
        for key, gate, bad in (
            ("gate_5", "5", "present"),
            ("gate_11", "11", "contradicts"),
            ("locators", "6", "fabricated"),
            ("missing_facts", "4", "not_named"),
        ):
            if key not in entry:
                continue
            result = entry[key]["result"]
            allowed = review["allowed_results"][key]
            if result not in allowed:
                problems.append(f"{unit} {key}: result {result!r} not in {allowed}")
            elif result == bad:
                hand_failures[gate].append(unit)
    if problems:
        raise ValueError("hand review is incomplete: " + "; ".join(problems))

    for gate in ("5", "11"):
        verdicts[gate] = _verdict(
            gate,
            verdicts[gate]["covered"],
            hand_failures[gate],
            0,
            confirmed_labels,
        )
    for gate in ("6", "4"):
        if hand_failures[gate]:
            merged = sorted(set(verdicts[gate]["failed"]) | set(hand_failures[gate]))
            verdicts[gate] = _verdict(
                gate, verdicts[gate]["covered"], merged, 0, confirmed_labels
            )

    protected = [verdicts[g]["verdict"] for g in PROTECTED]
    aggregate = [verdicts[g]["verdict"] for g in ("10", "11", "12", "13")]
    if "unresolved" in protected:
        decision = "unresolved"
        why = "A protected gate has a failing unit whose label is not yet checked."
    elif "fail" in protected:
        decision = "fix_or_switch"
        why = (
            "A protected gate failed. The failure taxonomy decides: a fixable "
            "defect is fixed and rerun; a limit of the approach means switch."
        )
    elif "unresolved" in aggregate:
        decision = "unresolved"
        why = "An aggregate gate is over budget on units whose labels are unchecked."
    elif "fail" in aggregate:
        decision = "constrain"
        why = "Protected gates pass, but an aggregate gate is over budget."
    else:
        decision = "go"
        why = "Every protected gate passes and every aggregate is within budget."
    return {
        "run_id": report["run_id"],
        "gate_version": report["gate_version"],
        "reviewer": review["reviewer"],
        "reviewer_confirmed": bool(review.get("reviewer_confirmed")),
        "provisional": not review.get("reviewer_confirmed"),
        "decision": decision,
        "why": why,
        "gates": verdicts,
    }
