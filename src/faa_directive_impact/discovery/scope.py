"""Decide each discovered directive's coverage state.

Coverage states (ROADMAP.md, "Directive Coverage State"):

- ``evaluated``: rules verified and covered by passing cases. Only AD
  2025-19-13 (Federal Register document 2025-18469).
- ``not_yet_evaluated``: within the supported IAE V2500-A5/D5/E5 boundary but
  not yet covered by cases. Shown as new; never enters the evaluated queues.
- ``outside_supported_scope``: searchable only; no impact determination.

The title only decides which directives are worth reading in full: those
naming International Aero Engines. The boundary itself is read from the
models paragraph (c) "Applicability" of the directive's XML. Anything that
cannot be read confidently is sent to review and kept out of scope.
"""

import re
from dataclasses import dataclass
from xml.etree.ElementTree import Element

from defusedxml import ElementTree as SafeElementTree

from faa_directive_impact.directives.hpt_hub_record import DOCUMENT_NUMBER, MODEL

EVALUATED = "evaluated"
NOT_YET_EVALUATED = "not_yet_evaluated"
OUTSIDE_SUPPORTED_SCOPE = "outside_supported_scope"
COVERAGE_STATES = (EVALUATED, NOT_YET_EVALUATED, OUTSIDE_SUPPORTED_SCOPE)

# Documents whose rules are verified and covered by passing seed cases.
EVALUATED_DOCUMENTS = frozenset({DOCUMENT_NUMBER})
IAE_TITLE = "International Aero Engines"
APPLICABILITY_HEADING = re.compile(r"^\(c\)\s*Applicability$")
# Any V2500-series designation, to catch variants the family pattern rejects.
V2500_TOKEN = re.compile(r"\bV25\d\d[A-Za-z0-9-]*")
HYPHEN_SPACE = re.compile(r"-\s+")


@dataclass(frozen=True)
class ScopeDecision:
    """A coverage state, the models behind it, and whether a person must look."""

    coverage_state: str
    basis: str
    detail: str
    models: tuple[str, ...] = ()
    needs_review: bool = False

    def as_record(self) -> dict:
        return {
            "coverage_state": self.coverage_state,
            "basis": self.basis,
            "detail": self.detail,
            "models": list(self.models),
            "needs_review": self.needs_review,
        }


def names_international_aero_engines(title: str) -> bool:
    """Whether the title names IAE, so the directive is read in full."""
    return IAE_TITLE in title


def outside_by_title() -> ScopeDecision:
    return ScopeDecision(
        OUTSIDE_SUPPORTED_SCOPE,
        "title",
        "The title does not name International Aero Engines; only the API "
        "metadata is kept.",
    )


def needs_review(detail: str) -> ScopeDecision:
    """Unclassifiable: kept out of scope and listed for a person to check."""
    return ScopeDecision(OUTSIDE_SUPPORTED_SCOPE, "review", detail, needs_review=True)


def classify_applicability(xml_bytes: bytes, document_number: str) -> ScopeDecision:
    """Classify an IAE directive from the models its paragraph (c) lists.

    In scope only when every V2500 designation in the paragraph's first
    statement is an A5/D5/E5 model. A mixture, an unrecognized V2500
    designation, or a missing paragraph goes to review. A paragraph naming no
    V2500 model at all (for example PW1100G-JM engines) is outside the
    boundary.
    """
    try:
        root = SafeElementTree.fromstring(xml_bytes)
    except Exception as error:  # defusedxml raises parse and security errors
        return needs_review(f"XML did not parse: {type(error).__name__}")
    statement = applicability_statement(root)
    if statement is None:
        return needs_review("No (c) Applicability paragraph was found.")
    text = HYPHEN_SPACE.sub("-", statement)
    tokens = [token.rstrip("-") for token in V2500_TOKEN.findall(text)]
    in_family = sorted({token for token in tokens if MODEL.fullmatch(token)})
    other = sorted({token for token in tokens if not MODEL.fullmatch(token)})
    if other:
        return needs_review(
            "Paragraph (c) names V2500 designations outside A5/D5/E5: "
            + ", ".join(other)
        )
    if in_family:
        state = (
            EVALUATED if document_number in EVALUATED_DOCUMENTS else NOT_YET_EVALUATED
        )
        return ScopeDecision(
            state,
            "applicability_paragraph",
            "Paragraph (c) lists only V2500-A5/D5/E5 models.",
            tuple(in_family),
        )
    if "applies to" not in text:
        return needs_review("Paragraph (c) does not state what the AD applies to.")
    return ScopeDecision(
        OUTSIDE_SUPPORTED_SCOPE,
        "applicability_paragraph",
        "Paragraph (c) lists no V2500 model.",
    )


def applicability_statement(root: Element) -> str | None:
    """Return the first paragraph under the "(c) Applicability" heading."""
    elements = list(root.iter())
    for index, element in enumerate(elements):
        if element.tag != "HD" or not APPLICABILITY_HEADING.fullmatch(_text(element)):
            continue
        for following in elements[index + 1 :]:
            if following.tag == "HD":
                return None
            if following.tag == "P":
                return _text(following)
    return None


def _text(element: Element) -> str:
    return " ".join("".join(element.itertext()).split())
