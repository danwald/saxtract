#!/usr/bin/env python

"""Tests for `saxtract` package."""
import io
from pathlib import Path

import pytest
from click.testing import CliRunner

from saxtract import saxtract
from saxtract import cli


def test_command_line_interface(monkeypatch):
    """Test the CLI."""
    runner = CliRunner()
    in_path = Path(__file__).parent / 'data' / 'bars.xml'
    result = runner.invoke(cli.main, args=['--instream', f'{in_path.absolute()}'])
    assert not result.exception
    assert result.exit_code == 0
