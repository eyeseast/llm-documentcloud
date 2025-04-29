# llm-documentcloud

[![PyPI](https://img.shields.io/pypi/v/llm-documentcloud.svg)](https://pypi.org/project/llm-documentcloud/)
[![Changelog](https://img.shields.io/github/v/release/eyeseast/llm-documentcloud?include_prereleases&label=changelog)](https://github.com/eyeseast/llm-documentcloud/releases)
[![Tests](https://github.com/eyeseast/llm-documentcloud/actions/workflows/test.yml/badge.svg)](https://github.com/eyeseast/llm-documentcloud/actions/workflows/test.yml)
[![License](https://img.shields.io/badge/license-Apache%202.0-blue.svg)](https://github.com/eyeseast/llm-documentcloud/blob/main/LICENSE)

LLM integrations for DocumentCloud

## Installation

Install this plugin in the same environment as [LLM](https://llm.datasette.io/).

```bash
llm install llm-documentcloud
```

## Usage

Usage instructions go here.

## Development

To set up this plugin locally, first checkout the code. Then create a new virtual environment:

```bash
cd llm-documentcloud
python -m venv venv
source venv/bin/activate
```

Now install the dependencies and test dependencies:

```bash
python -m pip install -e '.[test]'
```

To run the tests:

```bash
python -m pytest
```
