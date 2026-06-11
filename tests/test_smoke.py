"""Smoke tests for the Stage 5 setup skeleton.

These tests are deterministic and offline: they never call an LLM, CrewAI, or
any network service, and they create no artifacts.
"""

from __future__ import annotations

import agentic_latex_book
from agentic_latex_book.cli import main


def test_package_imports() -> None:
    """The package imports and exposes a version string."""
    assert isinstance(agentic_latex_book.__version__, str)
    assert agentic_latex_book.__version__


def test_cli_status_returns_zero(capsys) -> None:
    """The default/status command runs offline and returns exit code 0."""
    exit_code = main(["status"])
    captured = capsys.readouterr()
    assert exit_code == 0
    assert "not implemented yet" in captured.out.lower()


def test_cli_default_returns_zero(capsys) -> None:
    """Invoking with no subcommand prints status and returns 0."""
    exit_code = main([])
    captured = capsys.readouterr()
    assert exit_code == 0
    assert "agentic-latex-book" in captured.out


def test_cli_help_exits_zero() -> None:
    """`--help` exits with code 0 (argparse raises SystemExit(0))."""
    try:
        main(["--help"])
    except SystemExit as exc:
        assert exc.code == 0
    else:  # pragma: no cover - argparse always exits on --help
        raise AssertionError("--help should raise SystemExit")
