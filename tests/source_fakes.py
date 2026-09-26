"""Minimal but realistic offline stand-ins for Federal Register and GovInfo."""

import hashlib
import json

PNG_SIGNATURE = b"\x89PNG\r\n\x1a\n"


def make_pdf(text: str) -> bytes:
    """Return a one-page PDF whose extractable text is ``text``."""
    content = f"BT /F1 12 Tf 72 720 Td ({text}) Tj ET".encode("cp1252")
    objects = [
        b"<< /Type /Catalog /Pages 2 0 R >>",
        b"<< /Type /Pages /Kids [3 0 R] /Count 1 >>",
        b"<< /Type /Page /Parent 2 0 R /MediaBox [0 0 612 792] "
        b"/Contents 4 0 R /Resources << /Font << /F1 5 0 R >> >> >>",
        b"<< /Length %d >>\nstream\n" % len(content) + content + b"\nendstream",
        b"<< /Type /Font /Subtype /Type1 /BaseFont /Helvetica "
        b"/Encoding /WinAnsiEncoding >>",
    ]
    output = b"%PDF-1.7\n"
    offsets = []
    for number, body in enumerate(objects, start=1):
        offsets.append(len(output))
        output += b"%d 0 obj\n" % number + body + b"\nendobj\n"
    xref_at = len(output)
    output += b"xref\n0 %d\n0000000000 65535 f \n" % (len(objects) + 1)
    output += b"".join(b"%010d 00000 n \n" % offset for offset in offsets)
    output += b"trailer\n<< /Size %d /Root 1 0 R >>\n" % (len(objects) + 1)
    output += b"startxref\n%d\n%%%%EOF\n" % xref_at
    return output


def directive_xml(
    number: str, root: str = "RULE", incorporated: tuple[str, ...] = ()
) -> bytes:
    if incorporated:
        items = "".join(
            f"<P>({roman}) {item}</P>"
            for roman, item in zip(("i", "ii", "iii", "iv"), incorporated, strict=False)
        )
        section = f"<P>(1) The Director approved the IBR.</P>{items}"
    else:
        section = "<P>None.</P>"
    return (
        f"<{root}><PREAMB><AGENCY>DEPARTMENT OF TRANSPORTATION</AGENCY></PREAMB>"
        f"<HD>(k) Additional Information</HD><P>Contact the FAA.</P>"
        f"<HD>(l) Material Incorporated by Reference</HD>{section}"
        f"<FRDOC>[FR Doc. {number} Filed 9-23-25; 8:45 am]</FRDOC></{root}>"
    ).encode()


def graphic_bytes(identifier: str) -> bytes:
    return PNG_SIGNATURE + identifier.encode()


def api_url(number: str) -> str:
    return f"https://www.federalregister.gov/api/v1/documents/{number}.json"


def document_pages(
    number: str,
    document_type: str = "Rule",
    publication_date: str = "2025-09-24",
    docket_ids: tuple[str, ...] = ("Docket No. FAA-2025-0926",),
    images: tuple[str, ...] = (),
    incorporated: tuple[str, ...] = (),
) -> dict[str, bytes | None]:
    """Return URL → body for every representation of one document."""
    package = f"FR-{publication_date}"
    base = f"https://www.federalregister.gov/documents/full_text/{number}"
    urls = {
        "full_text_xml_url": f"{base}.xml",
        "body_html_url": f"{base}.html",
        "raw_text_url": f"{base}.txt",
        "pdf_url": f"https://www.govinfo.gov/content/pkg/{package}/pdf/{number}.pdf",
        "mods_url": (
            f"https://www.govinfo.gov/metadata/granule/{package}/{number}/mods.xml"
        ),
    }
    root = "PRORULE" if document_type == "Proposed Rule" else "RULE"
    pages: dict[str, bytes | None] = {
        urls["full_text_xml_url"]: directive_xml(number, root, incorporated),
        urls[
            "body_html_url"
        ]: f"\n  <div><p id='p-1'>FR Doc. {number}</p></div>".encode(),
        urls["raw_text_url"]: f"[FR Doc. {number} Filed]".encode(),
        urls["pdf_url"]: make_pdf(f"[FR Doc. {number.replace('-', '\u2013')} Filed]"),
        urls["mods_url"]: f"<mods><identifier>{number}</identifier></mods>".encode(),
    }
    images_field = {}
    images_metadata = {}
    for identifier in images:
        url = f"https://img.federalregister.gov/{identifier}/{identifier}_original_size.png"
        body = graphic_bytes(identifier)
        pages[url] = body
        images_field[identifier] = {"original_size": url}
        images_metadata[identifier] = {
            "original_size": {
                "identifier": identifier,
                "size": len(body),
                "sha": hashlib.md5(body, usedforsecurity=False).hexdigest(),
                "url": url,
            }
        }
    record = {
        "document_number": number,
        "type": document_type,
        "publication_date": publication_date,
        "docket_ids": list(docket_ids),
        "images": images_field,
        "images_metadata": images_metadata,
        "page_views": {"count": 1},
        **urls,
    }
    pages[api_url(number)] = json.dumps(record).encode()
    return pages


def edit_api_record(pages: dict[str, bytes | None], number: str, **changes) -> None:
    """Rewrite fields of a served API record; ``None`` deletes the field."""
    record = json.loads(pages[api_url(number)] or b"")
    for key, value in changes.items():
        if value is None:
            record.pop(key, None)
        else:
            record[key] = value
    pages[api_url(number)] = json.dumps(record).encode()
