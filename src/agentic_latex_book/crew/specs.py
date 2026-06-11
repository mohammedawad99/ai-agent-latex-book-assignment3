"""Plain-data specifications for the crew's agents and tasks.

These dataclasses describe the planned crew without constructing any CrewAI
object or calling an LLM, so they are fully serializable and testable offline.
"""

from __future__ import annotations

from dataclasses import dataclass, field


@dataclass(frozen=True)
class AgentSpec:
    """A description of one agent's role and behaviour."""

    name: str
    role: str
    goal: str
    backstory: str
    allow_delegation: bool = False
    verbose: bool = False


@dataclass(frozen=True)
class TaskSpec:
    """A description of one task and the tasks that feed it context."""

    name: str
    description: str
    expected_output: str
    agent_name: str
    output_schema_name: str
    context_task_names: tuple[str, ...] = field(default_factory=tuple)
