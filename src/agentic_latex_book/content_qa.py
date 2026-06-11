"""Deterministic offline content QA scanner.

Scans candidate or cleaned content (a single file, a list of files, or a
directory of ``.txt``/``.md`` files) for blocking quality risks and required
positive markers before LaTeX assembly. Pure string checks: no network, no
model, no API key, and no file is ever modified (see decision D-028).
"""

from __future__ import annotations

from collections.abc import Iterable
from dataclasses import dataclass, field
from pathlib import Path

from agentic_latex_book.crew.instructions import MANDATORY_PDF_ELEMENTS

REQUIRED_TOPIC = "From PoC to Production: A CrewAI Multi-Agent Pipeline for Generating a LaTeX Book"
REQUIRED_GROUP = "MaRs-777"
REQUIRED_AUTHORS = ("Mohamed Awad", "Rawey Sleiman")
ACCEPTED_DATES = ("2026-06-11", "June 11, 2026")

# Blocking content that must never appear in accepted content.
FORBIDDEN_SUBSTRINGS = (
    "example.com",  # covers crewai-docs.example.com and mars777.example.com
    "Internal Publication",
    "185 minutes",
    "99.1%",
    "1.8M tokens",
    "GPT-4o Technical Report",
    "October 2023",
    "[Your Name]",
    "[Your Name/Placeholder Name]",
    "[Optional Affiliation/Institution]",
    "Understanding and Implementing Gradient Descent",
)

# Headers/footers described conceptually instead of implemented.
CONCEPTUAL_HEADER_PHRASES = (
    "would conceptually begin",
    "conceptually begin from this point",
)

_TEXT_SUFFIXES = (".txt", ".md")


@dataclass
class QAReport:
    """Result of a content QA scan. ``errors`` are blocking; ``warnings`` advisory."""

    ok: bool = True
    errors: list[str] = field(default_factory=list)
    warnings: list[str] = field(default_factory=list)
    checked_files: list[str] = field(default_factory=list)

    def to_dict(self) -> dict:
        return {
            "ok": self.ok,
            "errors": self.errors,
            "warnings": self.warnings,
            "checked_files": self.checked_files,
            "error_count": len(self.errors),
            "warning_count": len(self.warnings),
            "files_checked": len(self.checked_files),
        }


def collect_text_files(target: Path) -> list[Path]:
    """Return sorted ``.txt``/``.md`` files for a file or directory target."""
    if target.is_dir():
        return sorted(
            p for p in target.rglob("*") if p.is_file() and p.suffix.lower() in _TEXT_SUFFIXES
        )
    if target.is_file():
        return [target]
    return []


def _resolve_files(target) -> list[Path]:
    if isinstance(target, (str, Path)):
        return collect_text_files(Path(target))
    if isinstance(target, Iterable):
        found: list[Path] = []
        for item in target:
            found.extend(collect_text_files(Path(item)))
        return sorted(set(found))
    return []


def check_text(text: str) -> list[str]:
    """Return the list of blocking errors for one combined text. Pure string checks."""
    errors: list[str] = []
    lowered = text.lower()

    for token in FORBIDDEN_SUBSTRINGS:
        if token.lower() in lowered:
            errors.append(f"forbidden content: {token!r}")
    for phrase in CONCEPTUAL_HEADER_PHRASES:
        if phrase.lower() in lowered:
            errors.append(f"conceptual-only headers/footers: {phrase!r}")

    if REQUIRED_TOPIC.lower() not in lowered:
        errors.append("missing required topic")
    if REQUIRED_GROUP.lower() not in lowered:
        errors.append("missing group code")
    for author in REQUIRED_AUTHORS:
        if author.lower() not in lowered:
            errors.append(f"missing author: {author}")
    if not any(date.lower() in lowered for date in ACCEPTED_DATES):
        errors.append("missing acceptable project date")
    for element in MANDATORY_PDF_ELEMENTS:
        if element.lower() not in lowered:
            errors.append(f"missing mandatory PDF element: {element}")

    return errors


def scan(target) -> QAReport:
    """Scan a file, a list of files, or a directory and return a QAReport."""
    files = _resolve_files(target)
    report = QAReport()
    if not files:
        report.ok = False
        report.errors.append(f"no .txt/.md files found at {target}")
        return report

    combined = []
    for path in files:
        report.checked_files.append(str(path))
        combined.append(path.read_text(encoding="utf-8"))
    report.errors.extend(check_text("\n\n".join(combined)))
    report.ok = not report.errors
    return report
