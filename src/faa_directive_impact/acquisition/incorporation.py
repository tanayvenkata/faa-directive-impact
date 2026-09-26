"""Read the incorporated-material status stated in a directive's XML.

This is the minimum inspection acquisition needs to record explicit
dependencies. It does not interpret the listed material.
"""

import re
from dataclasses import dataclass
from xml.etree.ElementTree import Element

HEADING_PATTERN = re.compile(r"^\(([a-z]+)\)\s*Material Incorporated by Reference$")
LISTED_ITEM_PATTERN = re.compile(r"^\((?:[ivx]+)\)\s+(.+)$")
NONE_STATEMENT = "None."


@dataclass(frozen=True)
class IncorporatedMaterial:
    """What the directive's incorporation-by-reference paragraph states."""

    paragraph: str | None  # e.g. "l"; None when the heading is absent
    items: tuple[str, ...]

    @property
    def determined(self) -> bool:
        return self.paragraph is not None

    @property
    def required(self) -> bool:
        return bool(self.items)


def read_incorporated_material(root: Element) -> IncorporatedMaterial:
    """Find the "Material Incorporated by Reference" paragraph, any letter.

    ``None.`` yields no items. Otherwise each roman-numbered entry under the
    heading is returned verbatim as one named item.
    """
    elements = list(root.iter())
    for index, element in enumerate(elements):
        if element.tag != "HD":
            continue
        heading = _text(element)
        match = HEADING_PATTERN.fullmatch(heading)
        if not match:
            continue
        paragraphs = []
        for following in elements[index + 1 :]:
            if following.tag == "HD":
                break
            if following.tag == "P":
                paragraphs.append(_text(following))
        if paragraphs[:1] == [NONE_STATEMENT]:
            return IncorporatedMaterial(match.group(1), ())
        items = tuple(
            item.group(1)
            for text in paragraphs
            if (item := LISTED_ITEM_PATTERN.fullmatch(text))
        )
        # A non-"None" section with no recognizable items is still material.
        return IncorporatedMaterial(match.group(1), items or (heading,))
    return IncorporatedMaterial(None, ())


def _text(element: Element) -> str:
    return " ".join("".join(element.itertext()).split())
