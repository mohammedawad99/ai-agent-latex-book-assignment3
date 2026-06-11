"""Tests for the runtime/cost tracker. Deterministic and offline."""

from __future__ import annotations

import pytest

from agentic_latex_book.runtime import RuntimeTracker


def test_records_elapsed_time() -> None:
    """start()/stop() produce a non-negative elapsed time."""
    tracker = RuntimeTracker(label="unit").start().stop()
    assert tracker.elapsed_seconds is not None
    assert tracker.elapsed_seconds >= 0
    assert tracker.started_at is not None
    assert tracker.ended_at is not None


def test_stop_before_start_raises() -> None:
    """Calling stop() before start() is an error."""
    with pytest.raises(RuntimeError):
        RuntimeTracker().stop()


def test_to_dict_has_no_fake_cost_data() -> None:
    """Serialization keeps token/cost fields as None (never invented)."""
    data = RuntimeTracker(label="unit").start().stop().to_dict()
    assert data["label"] == "unit"
    assert data["prompt_tokens"] is None
    assert data["completion_tokens"] is None
    assert data["model"] is None
    assert "_monotonic_start" not in data
