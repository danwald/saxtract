#!/usr/bin/env python

"""Tests for `saxtract` package."""
import io
from pathlib import Path

import pytest
from click.testing import CliRunner

from saxtract import saxtract
from saxtract import cli


@pytest.fixture
def test_file_path():
    return (Path(__file__).parent / 'data' / 'bars.xml').absolute()


def test_cli_defaults(test_file_path):
    """Test the CLI."""
    runner = CliRunner()
    result = runner.invoke(cli.main, args=['--instream', f'{test_file_path}'])
    assert not result.exception
    assert result.exit_code == 0


def test_cli_show_tags(test_file_path):
    """Test the CLI."""
    runner = CliRunner()
    result = runner.invoke(cli.main, args=['--instream', f'{test_file_path}', '--show-tags'])
    assert not result.exception
    assert result.exit_code == 0
