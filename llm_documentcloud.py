import os
import llm
from documentcloud import DocumentCloud

DC_USERNAME = os.environ.get("DC_USERNAME")
DC_PASSWORD = os.environ.get("DC_PASSWORD")


@llm.hookimpl
def register_fragment_loaders(register):
    register("dc", load_document)


def load_document(argument: str) -> llm.Fragment:
    """Load a document by ID or URL and return a fragment"""
    source = f"dc:{argument}"
    client = DocumentCloud(DC_USERNAME, DC_PASSWORD)
    doc = client.documents.get(argument)  # let this error for Not Found

    return llm.Fragment(doc.full_text, source)
