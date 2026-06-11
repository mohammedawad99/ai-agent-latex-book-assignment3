"""Tests for the deterministic offline content QA scanner."""

from __future__ import annotations

from pathlib import Path

from agentic_latex_book.content_qa import (
    REQUIRED_TOPIC,
    check_text,
    scan,
)
from agentic_latex_book.crew.instructions import MANDATORY_PDF_ELEMENTS

_CANDIDATE_DIR = Path("results/stage8c7-full-gemini-20260611-173125/crew_outputs")

# A small, clean sample: all required positives + every mandatory element, no forbidden content.
_CLEAN = (
    f"{REQUIRED_TOPIC}\n"
    "Group MaRs-777. Authors: Mohamed Awad and Rawey Sleiman. Date: 2026-06-11.\n"
    + "\n".join(MANDATORY_PDF_ELEMENTS)
    + "\n"
)


def _write(tmp_path, text, name="content.md"):
    path = tmp_path / name
    path.write_text(text, encoding="utf-8")
    return path


def test_clean_sample_passes(tmp_path) -> None:
    report = scan(_write(tmp_path, _CLEAN))
    assert report.ok is True
    assert report.errors == []
    assert len(report.checked_files) == 1


def test_old_gradient_descent_fails() -> None:
    errors = check_text(_CLEAN + "\nUnderstanding and Implementing Gradient Descent")
    assert any("Understanding and Implementing Gradient Descent" in e for e in errors)


def test_placeholders_fail() -> None:
    errors = check_text(_CLEAN + "\nAuthor: [Your Name/Placeholder Name]\nOctober 2023")
    assert any("[Your Name/Placeholder Name]" in e for e in errors)
    assert any("October 2023" in e for e in errors)


def test_example_com_and_internal_publication_fail() -> None:
    errors = check_text(_CLEAN + "\nSee https://crewai-docs.example.com\nInternal Publication")
    assert any("example.com" in e for e in errors)
    assert any("Internal Publication" in e for e in errors)


def test_unsupported_metrics_fail() -> None:
    errors = check_text(_CLEAN + "\nThe run took 185 minutes, 99.1% valid, used 1.8M tokens.")
    for token in ("185 minutes", "99.1%", "1.8M tokens"):
        assert any(token in e for e in errors)


def test_unsupported_gpt4o_report_fails() -> None:
    errors = check_text(_CLEAN + "\nsee the GPT-4o Technical Report")
    assert any("GPT-4o Technical Report" in e for e in errors)


def test_conceptual_headers_footers_fail() -> None:
    errors = check_text(_CLEAN + "\nHeaders and footers would conceptually begin here.")
    assert any("conceptual-only headers/footers" in e for e in errors)


def test_missing_topic_group_authors_date_fail() -> None:
    errors = check_text("\n".join(MANDATORY_PDF_ELEMENTS))
    assert any("missing required topic" in e for e in errors)
    assert any("missing group code" in e for e in errors)
    assert any("missing author: Mohamed Awad" in e for e in errors)
    assert any("missing acceptable project date" in e for e in errors)


def test_missing_mandatory_element_fails() -> None:
    dropped = "a Hebrew-English BiDi section"
    text = _CLEAN.replace(dropped + "\n", "")
    errors = check_text(text)
    assert any(f"missing mandatory PDF element: {dropped}" in e for e in errors)


def test_directory_with_no_text_files_fails(tmp_path) -> None:
    (tmp_path / "data.json").write_text("{}", encoding="utf-8")
    report = scan(tmp_path)
    assert report.ok is False
    assert any("no .txt/.md files" in e for e in report.errors)


def test_scan_candidate_directory_reports_known_risks() -> None:
    """The committed Stage 8C.7 candidate fails the stricter scanner (evidence unread-only)."""
    if not _CANDIDATE_DIR.is_dir():
        return  # evidence not present in this checkout; nothing to assert
    report = scan(_CANDIDATE_DIR)
    assert report.ok is False
    assert len(report.checked_files) == 4
    assert any("example.com" in e for e in report.errors)
    assert any("185 minutes" in e for e in report.errors)
    assert any("GPT-4o Technical Report" in e for e in report.errors)
    assert any("conceptual-only headers/footers" in e for e in report.errors)


def test_scanner_is_deterministic() -> None:
    assert check_text(_CLEAN) == check_text(_CLEAN)
