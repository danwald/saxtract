#!/usr/bin/env python

"""Tests for `saxtract` package."""
import io
from pathlib import Path

import pytest
from click.testing import CliRunner

from saxtract import saxtract
from saxtract import cli


@pytest.fixture
def test_file_path(autouse=True):
    return (Path(__file__).parent / 'data' / 'bars.xml').absolute()


def test_cli_defaults():
    """Test the CLI."""
    runner = CliRunner()
    fp = (Path(__file__).parent / 'data' / 'bars.xml').absolute()
    result = runner.invoke(cli.main, args=['--instream', f'{fp}'])
    assert not result.exception
    assert result.exit_code == 0


def test_cli_show_tags():
    """Test the CLI."""
    runner = CliRunner()
    fp = (Path(__file__).parent / 'data' / 'bars.xml').absolute()
    result = runner.invoke(cli.main, args=['--instream', f'{fp}', '--show-tags'])
    assert not result.exception
    assert result.exit_code == 0
