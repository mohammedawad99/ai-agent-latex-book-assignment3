"""Safe builder for the crew core.

Provides the agent/task specs, a validation check, and a dry-run blueprint used
by the CLI and tests. A real CrewAI object builder is included but it never runs
the crew: ``kickoff`` and any LLM/API call are deferred to a later, controlled
stage once a provider/model is chosen (see decision D-017).
"""

from __future__ import annotations

from agentic_latex_book.crew.agents import agent_specs
from agentic_latex_book.crew.context import ProjectContext
from agentic_latex_book.crew.schemas import output_schema_specs
from agentic_latex_book.crew.specs import AgentSpec, TaskSpec
from agentic_latex_book.crew.tasks import build_task_specs, task_specs


class CrewSpecError(ValueError):
    """Raised when the agent/task specifications are inconsistent."""


def crew_specs() -> tuple[tuple[AgentSpec, ...], tuple[TaskSpec, ...]]:
    """Return the planned (agents, tasks) specifications."""
    return agent_specs(), task_specs()


def validate_specs(agents: tuple[AgentSpec, ...], tasks: tuple[TaskSpec, ...]) -> None:
    """Validate that tasks reference known agents, earlier context, and known schemas."""
    agent_names = {a.name for a in agents}
    schema_names = {s.name for s in output_schema_specs()}
    seen_tasks: set[str] = set()
    for task in tasks:
        if task.agent_name not in agent_names:
            raise CrewSpecError(f"Task {task.name!r} references unknown agent {task.agent_name!r}.")
        if task.output_schema_name not in schema_names:
            raise CrewSpecError(
                f"Task {task.name!r} references unknown output schema {task.output_schema_name!r}."
            )
        for ctx in task.context_task_names:
            if ctx not in seen_tasks:
                raise CrewSpecError(f"Task {task.name!r} context {ctx!r} is not an earlier task.")
        seen_tasks.add(task.name)


def crew_blueprint(context: ProjectContext | None = None) -> dict:
    """Return a validated dry-run blueprint of the crew (no objects, no run).

    When a ``context`` is given, the blueprint records the bound topic.
    """
    agents = agent_specs()
    tasks = build_task_specs(context) if context is not None else task_specs()
    validate_specs(agents, tasks)
    blueprint = {
        "process": "sequential",
        "agents": [{"name": a.name, "role": a.role} for a in agents],
        "tasks": [
            {
                "name": t.name,
                "agent": t.agent_name,
                "output_schema": t.output_schema_name,
                "context": list(t.context_task_names),
            }
            for t in tasks
        ],
    }
    if context is not None:
        blueprint["topic"] = context.topic
    return blueprint


def build_crew(llm=None, context: ProjectContext | None = None):
    """Construct real CrewAI objects without running them.

    Building Agent/Task/Crew objects is safe offline; only ``kickoff`` needs an
    LLM/provider. This function therefore constructs the objects and returns the
    Crew, but never calls ``kickoff``. The ``llm`` argument is passed through to
    the agents when provided so a controlled run can be wired up later.
    """
    from crewai import Agent, Crew, Process, Task

    agents = agent_specs()
    tasks = build_task_specs(context) if context is not None else task_specs()
    validate_specs(agents, tasks)

    agent_objs = {}
    for spec in agents:
        kwargs = dict(
            role=spec.role,
            goal=spec.goal,
            backstory=spec.backstory,
            allow_delegation=spec.allow_delegation,
            verbose=spec.verbose,
        )
        if llm is not None:
            kwargs["llm"] = llm
        agent_objs[spec.name] = Agent(**kwargs)

    task_objs: dict[str, Task] = {}
    for spec in tasks:
        task_objs[spec.name] = Task(
            description=spec.description,
            expected_output=spec.expected_output,
            agent=agent_objs[spec.agent_name],
            context=[task_objs[c] for c in spec.context_task_names],
        )

    return Crew(
        agents=list(agent_objs.values()),
        tasks=list(task_objs.values()),
        process=Process.sequential,
    )
