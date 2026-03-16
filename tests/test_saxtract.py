#!/usr/bin/env python
from __future__ import annotations

"""Tests for `saxtract` package."""
from pathlib import Path

import pytest
from click.testing import CliRunner

from saxtract import cli


@pytest.fixture(autouse=True)
def runner() -> CliRunner:
    return CliRunner()


@pytest.fixture
def test_file_path() -> Path:
    return (Path(__file__).parent / 'data' / 'bars.xml').absolute()


def test_cli_defaults(runner: CliRunner, test_file_path: Path) -> None:
    """Test the CLI."""
    result = runner.invoke(cli.main, args=['--instream', f'{test_file_path}'])
    assert not result.exception
    assert result.exit_code == 0
