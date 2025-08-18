import pytest
from llm.plugins import pm, load_plugins
from llm_documentcloud import parse_dc_id, parse_dc_url, DCArgs

URLS = [
    (
        "https://www.documentcloud.org/documents/25507045-20250118-ufc-intuit-dome-athlete-pay-and-weights-c-amico/",
        DCArgs("25507045"),
    ),
    (
        "https://www.documentcloud.org/documents/25507045-20250118-ufc-intuit-dome-athlete-pay-and-weights-c-amico/?mode=pdf",
        DCArgs("25507045", "pdf"),
    ),
    (
        "https://www.documentcloud.org/documents/25507045-20250118-ufc-intuit-dome-athlete-pay-and-weights-c-amico/?mode=text",
        DCArgs("25507045", "text"),
    ),
    (
        "https://www.documentcloud.org/documents/25507045-20250118-ufc-intuit-dome-athlete-pay-and-weights-c-amico/?mode=image",
        DCArgs("25507045", "image"),
    ),
    (
        "https://www.documentcloud.org/documents/25507045-20250118-ufc-intuit-dome-athlete-pay-and-weights-c-amico/?mode=images",
        DCArgs("25507045", "image"),
    ),
    (
        "https://www.documentcloud.org/documents/25507045-20250118-ufc-intuit-dome-athlete-pay-and-weights-c-amico/?mode=grid",
        DCArgs("25507045", "image"),
    ),
    (
        "https://www.documentcloud.org/documents/25507045-20250118-ufc-intuit-dome-athlete-pay-and-weights-c-amico/?mode=document#document/p2",
        DCArgs("25507045", "text", 2),
    ),
    (
        "https://www.documentcloud.org/documents/25507045-20250118-ufc-intuit-dome-athlete-pay-and-weights-c-amico/?mode=images#document/p2",
        DCArgs("25507045", "image", 2),
    ),
    (
        "https://www.documentcloud.org/documents/25507045-20250118-ufc-intuit-dome-athlete-pay-and-weights-c-amico/?mode=pdf#document/p2",
        DCArgs("25507045", "pdf", 2),
    ),
]

IDS = [
    ("25507045", DCArgs("25507045")),
    (
        "25507045-20250118-ufc-intuit-dome-athlete-pay-and-weights-c-amico",
        DCArgs("25507045-20250118-ufc-intuit-dome-athlete-pay-and-weights-c-amico"),
    ),
    (
        "25507045-20250118-ufc-intuit-dome-athlete-pay-and-weights-c-amico?mode=pdf",
        DCArgs(
            "25507045-20250118-ufc-intuit-dome-athlete-pay-and-weights-c-amico", "pdf"
        ),
    ),
    ("25507045?mode=images", DCArgs("25507045", "image")),
    ("25507045?mode=images&page=2", DCArgs("25507045", "image", 2)),
]


def setup_module(module):
    load_plugins()


def test_plugin_is_installed():
    names = [mod.__name__ for mod in pm.get_plugins()]
    assert "llm_documentcloud" in names


@pytest.mark.parametrize(["id_str", "expected"], IDS)
def test_parse_dc_id(id_str, expected: DCArgs):
    args = parse_dc_id(id_str)

    assert args.id == expected.id
    assert args.mode == expected.mode
    assert args.page == expected.page


@pytest.mark.parametrize(["url", "expected"], URLS)
def test_parse_dc_url(url, expected: DCArgs):
    args = parse_dc_url(url)

    assert args.id == expected.id
    assert args.mode == expected.mode
    assert args.page == expected.page
