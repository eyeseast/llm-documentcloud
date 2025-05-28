import pytest
from llm.plugins import pm, load_plugins
from documentcloud import DocumentCloud
from llm_documentcloud import parse_dc_id, parse_dc_url, DCArgs

URLS = [
    "https://www.documentcloud.org/documents/25507045-20250118-ufc-intuit-dome-athlete-pay-and-weights-c-amico/",
    "https://www.documentcloud.org/documents/25507045-20250118-ufc-intuit-dome-athlete-pay-and-weights-c-amico/?mode=pdf",
    "https://www.documentcloud.org/documents/25507045-20250118-ufc-intuit-dome-athlete-pay-and-weights-c-amico/?mode=text",
    "https://www.documentcloud.org/documents/25507045-20250118-ufc-intuit-dome-athlete-pay-and-weights-c-amico/?mode=image",
    "https://www.documentcloud.org/documents/25507045-20250118-ufc-intuit-dome-athlete-pay-and-weights-c-amico/?mode=images",
    "https://www.documentcloud.org/documents/25507045-20250118-ufc-intuit-dome-athlete-pay-and-weights-c-amico/?mode=grid",
    "https://www.documentcloud.org/documents/25507045-20250118-ufc-intuit-dome-athlete-pay-and-weights-c-amico/?mode=document#document/p2",
    "https://www.documentcloud.org/documents/25507045-20250118-ufc-intuit-dome-athlete-pay-and-weights-c-amico/?mode=images#document/p2",
    "https://www.documentcloud.org/documents/25507045-20250118-ufc-intuit-dome-athlete-pay-and-weights-c-amico/?mode=pdf#document/p2",
]

IDS = [
    "25507045",
    "25507045-20250118-ufc-intuit-dome-athlete-pay-and-weights-c-amico",
    "25507045-20250118-ufc-intuit-dome-athlete-pay-and-weights-c-amico?mode=pdf",
    "25507045?mode=images",
    "25507045?mode=images&page=2",
]


def setup_module(module):
    load_plugins()


def test_plugin_is_installed():
    names = [mod.__name__ for mod in pm.get_plugins()]
    assert "llm_documentcloud" in names
