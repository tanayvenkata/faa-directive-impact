from datetime import date

from defusedxml import ElementTree

from faa_directive_impact.directives.hpt_hub_record import index_paragraphs
from faa_directive_impact.directives.source_text import (
    Relationship,
    SourceDocument,
    documents_for,
    render_text,
)

XML = b"""<RULE><PREAMB><AGENCY>FAA</AGENCY></PREAMB><SUPLINF>
<HD SOURCE="HD1">(g) Required Actions</HD>
<P>(1) Inspect the disk listed in Table 1.</P>
<GPH SPAN="3" DEEP="168"><PRTPAGE P="1"/><GID>ER02JY21.000</GID></GPH>
<HD SOURCE="HD1">Note 1 to paragraph (g)(1):</HD>
<P>A note.</P>
<P>(2) Then remove it.</P>
<GPOTABLE><TTITLE>Table 2</TTITLE><BOXHD><CHED>P/N</CHED><CHED>S/N</CHED></BOXHD>
<ROW><ENT>2A5001</ENT><ENT>PKLB1</ENT></ROW></GPOTABLE>
<SIG><NAME>Signer</NAME></SIG></SUPLINF></RULE>"""


def test_image_tables_are_marked_not_dropped() -> None:
    text = render_text(ElementTree.fromstring(XML))

    assert "[Image ER02JY21.000 is not included in this text." in text
    assert "Table 2\nP/N | S/N\n2A5001 | PKLB1" in text
    assert "(1) Inspect the disk listed in Table 1." in text


def test_note_headings_do_not_end_the_paragraph_index() -> None:
    ids = [p["id"] for p in index_paragraphs(ElementTree.fromstring(XML))]

    assert ids == ["(g)", "(g)(1)", "(g)(2)"]


def document(number: str, published: date) -> SourceDocument:
    return SourceDocument(number, "Rule", published, None, number, b"<RULE/>")


def test_thread_includes_related_documents_published_by_the_question_date() -> None:
    documents = {
        "final": document("final", date(2026, 8, 20)),
        "correction": document("correction", date(2026, 9, 10)),
        "proposal": document("proposal", date(2025, 11, 18)),
        "unrelated": document("unrelated", date(2025, 1, 1)),
    }
    links = [
        Relationship("proposal_final", "proposal", "final"),
        Relationship("corrects", "correction", "final"),
    ]

    early = documents_for("final", date(2026, 9, 1), documents, links)
    late = documents_for("final", date(2026, 10, 6), documents, links)
    proposal_only = documents_for("proposal", date(2026, 1, 15), documents, links)

    assert [d.number for d in early] == ["proposal", "final"]
    assert [d.number for d in late] == ["proposal", "final", "correction"]
    assert [d.number for d in proposal_only] == ["proposal"]
