"""Command-line entry point for the agentic LaTeX book project.

This is a Stage 5 setup skeleton. It is intentionally safe: it does not run
CrewAI, does not call any LLM, and does not create any output artifacts. Its
only job for now is to confirm the package is installed and to report the
current project status.
"""

from __future__ import annotations

import argparse
import sys
import tomllib
from pathlib import Path

from agentic_latex_book import __version__

# Repository root, resolved from this file's location (src/agentic_latex_book/cli.py).
_REPO_ROOT = Path(__file__).resolve().parents[2]
_DEFAULT_CONFIG = _REPO_ROOT / "config" / "default.toml"

_NOT_IMPLEMENTED_NOTICE = (
    "The CrewAI pipeline is not implemented yet. This command only reports "
    "project status; it does not generate content, call an LLM, or build a PDF."
)


def _load_config(config_path: Path) -> dict:
    """Load the non-secret TOML config if present; return {} if it is missing."""
    if not config_path.is_file():
        return {}
    with config_path.open("rb") as handle:
        return tomllib.load(handle)


def _print_status(config_path: Path) -> int:
    """Print a safe project-status summary. Performs no external calls."""
    config = _load_config(config_path)
    project = config.get("project", {})
    topic = project.get("topic", "<not configured>")
    group = project.get("group_code", "<not configured>")

    print(f"agentic-latex-book version {__version__}")
    print(f"group: {group}")
    print(f"topic: {topic}")
    print(f"config: {config_path if config_path.is_file() else '<not found>'}")
    print("stage: project setup (Stage 5)")
    print(_NOT_IMPLEMENTED_NOTICE)
    return 0


def main(argv: list[str] | None = None) -> int:
    """Parse arguments and dispatch. Returns a process exit code."""
    parser = argparse.ArgumentParser(
        prog="agentic-latex-book",
        description=(
            "Setup skeleton for the CrewAI LaTeX book pipeline. No pipeline is implemented yet."
        ),
    )
    parser.add_argument(
        "--version",
        action="version",
        version=f"agentic-latex-book {__version__}",
    )
    parser.add_argument(
        "--config",
        type=Path,
        default=_DEFAULT_CONFIG,
        help="Path to the TOML config file (default: config/default.toml).",
    )
    subparsers = parser.add_subparsers(dest="command")
    subparsers.add_parser(
        "status",
        help="Print current project status and exit (safe, offline).",
    )

    args = parser.parse_args(argv)

    # Default behavior (no subcommand) is the safe status report.
    if args.command in (None, "status"):
        return _print_status(args.config)

    parser.print_help()
    return 0


if __name__ == "__main__":
    sys.exit(main())
