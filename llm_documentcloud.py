import os
import re
from urllib.parse import parse_qs, urlsplit
from typing import List

import llm
from documentcloud import DocumentCloud

DC_USERNAME = os.environ.get("DC_USERNAME")
DC_PASSWORD = os.environ.get("DC_PASSWORD")

PATH_RE = re.compile(r"^/documents/(\d+)-([-\w]+)/?")
PAGE_RE = re.compile(r"document/p(\d+)")

# normalize possible modes
MODES = {
    "document": "text",
    "text": "text",
    "image": "image",
    "images": "image",
    "grid": "image",
    "pdf": "pdf",
    "raw": "pdf",
}


class DCArgs:
    "Helper class for passing around args"

    def __init__(self, id: str | int, mode: str = "text", page: int = None):
        self.id = id
        self.mode = mode
        self.page = page

    def __repr__(self):
        return f"({self.id}, {self.mode}, {self.page})"

    def __iter__(self):
        return iter((self.id, self.mode, self.page))


@llm.hookimpl
def register_fragment_loaders(register):
    register("dc", load_document)


def load_document(
    argument: str,
) -> llm.Fragment | List[llm.Fragment] | llm.Attachment | List[llm.Attachment]:
    """
    Load a document by ID or URL and return a fragment or attachment, depending on the mode
    """

    source = f"dc:{argument}"
    client = DocumentCloud(DC_USERNAME, DC_PASSWORD)
    doc = client.documents.get(argument)  # let this error for Not Found

    return llm.Fragment(doc.full_text, source)


def parse_dc_url(url: str) -> DCArgs:
    """
    Parse a document URL into ID, mode and page

    >>> args = parse_dc_url("https://www.documentcloud.org/documents/25507045-20250118-ufc-intuit-dome-athlete-pay-and-weights-c-amico/?mode=images")
    >>> print(args)
    (25507045, image, None)
    """
    u = urlsplit(url)
    if not (m := PATH_RE.match(u.path)):
        raise ValueError(f"No ID found in URL: {url}")
    try:
        id = m.group(1)
    except IndexError:
        raise ValueError("Invalid URL")

    qs = parse_qs(u.query)
    mode = qs.get("mode", ["text"])[0]
    mode = MODES.get(mode, "text")

    page = None
    if u.fragment:
        if m := PAGE_RE.match(u.fragment):
            page = int(m.group(1))

    return DCArgs(id, mode, page)


def parse_dc_id(doc_id: str) -> DCArgs:
    """
    Parse an ID string, returning the ID, mode and page

    >>> args = parse_dc_id("25507045?mode=pdf&page=1")
    >>> print(args)
    (25507045, pdf, 1)
    """
    if not "?" in doc_id:
        return DCArgs(doc_id)

    doc_id, query = doc_id.split("?", 1)
    qs = parse_qs(query)
    mode = qs.get("mode", ["text"])[0]
    mode = MODES.get(mode, "text")

    # Get page number if specified
    page = None
    if "page" in qs:
        try:
            page = int(qs["page"][0])
        except ValueError:
            # If page is not a valid integer, keep it as None
            pass

    return DCArgs(doc_id, mode, page)
