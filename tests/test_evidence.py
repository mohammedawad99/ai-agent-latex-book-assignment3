"""Tests for the evidence run-directory helper. Uses tmp_path only."""

from __future__ import annotations

import pytest

from agentic_latex_book.evidence import RUN_SUBDIRS, create_run_directory


def test_creates_expected_structure(tmp_path) -> None:
    """A run directory and all standard subdirectories are created."""
    run = create_run_directory(tmp_path, "run-001")
    assert run.root == tmp_path / "run-001"
    for sub in RUN_SUBDIRS:
        assert (run.root / sub).is_dir()
    assert run.logs.is_dir()
    assert run.final_pdf.is_dir()


def test_refuses_overwrite_by_default(tmp_path) -> None:
    """Re-creating an existing run directory raises unless exist_ok=True."""
    create_run_directory(tmp_path, "run-001")
    with pytest.raises(FileExistsError):
        create_run_directory(tmp_path, "run-001")


def test_exist_ok_allows_reuse(tmp_path) -> None:
    """exist_ok=True reuses the directory without error."""
    create_run_directory(tmp_path, "run-001")
    run = create_run_directory(tmp_path, "run-001", exist_ok=True)
    assert run.root.is_dir()


@pytest.mark.parametrize(
    "bad_id",
    ["", ".", "..", "bad id", "../bad", "bad/id", "bad\\id", "tab\tid"],
)
def test_unsafe_run_id_rejected(tmp_path, bad_id) -> None:
    """Empty, reserved, separator, and whitespace run IDs are rejected."""
    with pytest.raises(ValueError):
        create_run_directory(tmp_path, bad_id)


def test_valid_run_id_accepted(tmp_path) -> None:
    """A safe run_id with letters, digits, dash, underscore, dot is accepted."""
    run = create_run_directory(tmp_path, "run-2026_06.11")
    assert run.root == tmp_path / "run-2026_06.11"
    assert run.logs.is_dir()
