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
    return Path(__file__).parent / 'data' / 'bars.xml'.absolute()


def test_command_line_runs():
    """Test the CLI."""
    runner = CliRunner()
    result = runner.invoke(cli.main, args=['--instream', f'{test_file_path}'])
    assert not result.exception
    assert result.exit_code == 0
