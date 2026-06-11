"""Small logging configuration helper.

Configures a named logger with a console handler and, optionally, a file
handler. Kept deliberately simple. Callers must not pass secret values into log
messages; this helper does not handle redaction.
"""

from __future__ import annotations

import logging
from pathlib import Path

_LOG_FORMAT = "%(asctime)s %(levelname)s %(name)s: %(message)s"


def configure_logging(
    name: str = "agentic_latex_book",
    level: int = logging.INFO,
    log_file: Path | None = None,
) -> logging.Logger:
    """Return a configured logger.

    Handlers are reset on each call so repeated configuration does not attach
    duplicate handlers. If ``log_file`` is given, its parent directory is
    created and a file handler is added alongside the console handler.
    """
    logger = logging.getLogger(name)
    logger.setLevel(level)
    logger.propagate = False

    # Reset to avoid duplicate handlers when reconfigured.
    for handler in list(logger.handlers):
        logger.removeHandler(handler)
        handler.close()

    formatter = logging.Formatter(_LOG_FORMAT)

    console = logging.StreamHandler()
    console.setLevel(level)
    console.setFormatter(formatter)
    logger.addHandler(console)

    if log_file is not None:
        log_file.parent.mkdir(parents=True, exist_ok=True)
        file_handler = logging.FileHandler(log_file, encoding="utf-8")
        file_handler.setLevel(level)
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)

    return logger
