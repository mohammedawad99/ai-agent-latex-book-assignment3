"""Tests for the logging configuration helper. Uses tmp_path only."""

from __future__ import annotations

import logging

from agentic_latex_book.logging_setup import configure_logging


def test_console_logging_configured() -> None:
    """A console handler is attached at the requested level."""
    logger = configure_logging("test_console", level=logging.DEBUG)
    assert logger.level == logging.DEBUG
    assert any(isinstance(h, logging.StreamHandler) for h in logger.handlers)


def test_file_logging_writes(tmp_path) -> None:
    """A file handler writes log records to the given path."""
    log_file = tmp_path / "nested" / "run.log"
    logger = configure_logging("test_file", log_file=log_file)
    logger.info("hello evidence")
    for handler in logger.handlers:
        handler.flush()
    assert log_file.is_file()
    assert "hello evidence" in log_file.read_text(encoding="utf-8")


def test_no_duplicate_handlers() -> None:
    """Reconfiguring does not pile up duplicate handlers."""
    configure_logging("test_dup")
    logger = configure_logging("test_dup")
    assert len(logger.handlers) == 1
