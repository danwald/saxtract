#!/usr/bin/env python

"""Tests for `saxtract` package."""

import pytest

from click.testing import CliRunner

from saxtract import saxtract
from saxtract import cli

XML_DATA= """
<foo>
    <bar>
        <name>shamrocks<name>
        <address>lexington;ky;usa;</address>
    </bar>
    <bar>
        <name>irish-village<name>
        <address>gharoud;dubai;uae;</address>
    </bar>
    <bar>
        <name>garden-on-8<name>
        <address>dubai-internet-cit;ldubai;uae;</address>
    </bar>
</foo>
"""

@pytest.fixture
def response():
    """Sample pytest fixture.

    See more at: http://doc.pytest.org/en/latest/fixture.html
    """
    # import requests
    # return requests.get('https://github.com/audreyr/cookiecutter-pypackage')


def test_content(response):
    """Sample pytest test function with the pytest fixture as an argument."""
    # from bs4 import BeautifulSoup
    # assert 'GitHub' in BeautifulSoup(response.content).title.string


def test_command_line_interface():
    """Test the CLI."""
    runner = CliRunner()
    result = runner.invoke(cli.main, input=XML_DATA)
    pytest.set_trace()
    assert not result.exception
    assert result.exit_code == 0
    #assert '--help  Show this message and exit.' in help_result.output
