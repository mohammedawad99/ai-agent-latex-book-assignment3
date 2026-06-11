"""Lightweight runtime / cost tracker.

Records how long a run (or stage) took. It has slots for token/cost data, but it
never invents values: those stay ``None`` until a real provider reports them.
"""

from __future__ import annotations

import time
from dataclasses import asdict, dataclass, field


@dataclass
class RuntimeTracker:
    """Measure elapsed wall-clock time and hold optional cost placeholders."""

    label: str = "run"
    started_at: float | None = None
    ended_at: float | None = None
    elapsed_seconds: float | None = None
    # Cost/token fields stay None unless a real provider supplies them.
    prompt_tokens: int | None = None
    completion_tokens: int | None = None
    model: str | None = None
    _monotonic_start: float | None = field(default=None, repr=False)

    def start(self) -> RuntimeTracker:
        """Mark the start of the measured period."""
        self.started_at = time.time()
        self._monotonic_start = time.monotonic()
        return self

    def stop(self) -> RuntimeTracker:
        """Mark the end and compute elapsed seconds."""
        if self._monotonic_start is None:
            raise RuntimeError("stop() called before start().")
        self.ended_at = time.time()
        self.elapsed_seconds = time.monotonic() - self._monotonic_start
        return self

    def to_dict(self) -> dict:
        """Serialize to a plain dict for later evidence writing."""
        data = asdict(self)
        data.pop("_monotonic_start", None)
        return data
