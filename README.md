# llm-documentcloud

[![PyPI](https://img.shields.io/pypi/v/llm-documentcloud.svg)](https://pypi.org/project/llm-documentcloud/)
[![Changelog](https://img.shields.io/github/v/release/eyeseast/llm-documentcloud?include_prereleases&label=changelog)](https://github.com/eyeseast/llm-documentcloud/releases)
[![Tests](https://github.com/eyeseast/llm-documentcloud/actions/workflows/test.yml/badge.svg)](https://github.com/eyeseast/llm-documentcloud/actions/workflows/test.yml)
[![License](https://img.shields.io/badge/license-Apache%202.0-blue.svg)](https://github.com/eyeseast/llm-documentcloud/blob/main/LICENSE)

LLM integrations for [DocumentCloud](https://www.documentcloud.org)

## Installation

Install this plugin in the same environment as [LLM](https://llm.datasette.io/).

```bash
llm install llm-documentcloud
```

## Usage

Use the `dc:` fragment to load documents hosted on DocumentCloud.

```sh
# run a basic prompt
llm -f dc:71072 'Summarize this document'

# extract tabular data
llm -f dc:25507045 'Extract the tables in this document as CSV'
```

Documents can be fetched based on ID alone, ID and slug or full URL. The following are equivalent:

```sh
llm -f dc:25507045 'Extract the tables in this document as CSV'
llm -f dc:25507045-20250118-ufc-intuit-dome-athlete-pay-and-weights-c-amico 'Extract the tables in this document as CSV'
llm -f dc:https://www.documentcloud.org/documents/25507045-20250118-ufc-intuit-dome-athlete-pay-and-weights-c-amico/ 'Extract the tables in this document as CSV'
```

In each case, a DocumentCloud API client will fetch the document's full text and store it as a fragment for `llm`.

### Using file attachments instead of text

DocumentCloud stores each document in several ways: a PDF file, its extracted text and each page as an image. You can feed each of these into `llm` using `mode` parameters:

```sh
# use the original PDF as an attachment
llm -f 'dc:https://www.documentcloud.org/documents/25507045-20250118-ufc-intuit-dome-athlete-pay-and-weights-c-amico/?mode=pdf'

# use each page image as an attachment
llm -f 'dc:https://www.documentcloud.org/documents/25507045-20250118-ufc-intuit-dome-athlete-pay-and-weights-c-amico/?mode=images'

# this is the same, since "grid" is the mode name used on the documentcloud frontend
llm -f 'dc:https://www.documentcloud.org/documents/25507045-20250118-ufc-intuit-dome-athlete-pay-and-weights-c-amico/?mode=grid'

# these are all equivalent and will extract full text
llm -f dc:https://www.documentcloud.org/documents/25507045-20250118-ufc-intuit-dome-athlete-pay-and-weights-c-amico/
llm -f 'dc:https://www.documentcloud.org/documents/25507045-20250118-ufc-intuit-dome-athlete-pay-and-weights-c-amico/?mode=document'
llm -f 'dc:https://www.documentcloud.org/documents/25507045-20250118-ufc-intuit-dome-athlete-pay-and-weights-c-amico/?mode=text'
```

### Getting specific pages

Sometimes you only want one page. DocumentCloud can link to specific pages, and those URLs can be used here:

```sh
# extract text, but only for page 2
llm -f 'dc:https://www.documentcloud.org/documents/25507045-20250118-ufc-intuit-dome-athlete-pay-and-weights-c-amico/?mode=document#document/p2'
```

Note that pages are 1-indexed. You can also get images:

```sh
# attach the image for page 2
llm -f 'dc:https://www.documentcloud.org/documents/25507045-20250118-ufc-intuit-dome-athlete-pay-and-weights-c-amico/?mode=images#document/p2'
```

There isn't a way to get a single page out of a PDF, so passing `mode=pdf` will set `page` to `None`.

## Development

To set up this plugin locally, first checkout the code. Then create a new virtual environment using `uv`:

```bash
cd llm-documentcloud
uv sync
```

To install the dependencies and test dependencies, include the `test` extras:

```bash
uv sync --extra test
```

To run the tests:

```bash
uv run pytest
```
