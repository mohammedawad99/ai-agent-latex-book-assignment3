"""Persist full-pipeline run evidence (per-task outputs + safe metadata).

Writes only secret-free files. Used by the full runner's real path and exercised
directly by offline tests with fake outputs (no real CrewAI run happens here).
"""

from __future__ import annotations

import json

from agentic_latex_book.crew.tasks import task_specs


def _schema_by_task() -> dict[str, str]:
    return {task.name: task.output_schema_name for task in task_specs()}


def build_index(task_outputs: dict) -> dict:
    """Map each task to its file, schema name, length, and non-empty flag."""
    schemas = _schema_by_task()
    index: dict[str, dict] = {}
    for name, text in task_outputs.items():
        index[name] = {
            "file": f"crew_outputs/{name}.txt",
            "output_schema": schemas.get(name, "unknown"),
            "length": len(text),
            "non_empty": bool(text.strip()),
        }
    return index


def persist_full_run(run_dir, task_outputs: dict, runtime: dict, env_meta: dict) -> None:
    """Write per-task outputs, an index, runtime, a log line, and a run note.

    ``env_meta`` must contain presence booleans only (no raw key/base-url value).
    """
    for name, text in task_outputs.items():
        (run_dir.crew_outputs / f"{name}.txt").write_text(text, encoding="utf-8")

    (run_dir.crew_outputs / "_index.json").write_text(
        json.dumps(build_index(task_outputs), indent=2), encoding="utf-8"
    )

    runtime_record = dict(runtime)
    runtime_record["llm_environment"] = env_meta
    (run_dir.root / "runtime.json").write_text(
        json.dumps(runtime_record, indent=2), encoding="utf-8"
    )

    (run_dir.logs / "run.log").write_text(
        f"provider={env_meta['provider']} model={env_meta['model']} "
        f"api_key_present={env_meta['api_key_present']} "
        f"base_url_present={env_meta['base_url_present']}\n",
        encoding="utf-8",
    )

    (run_dir.validation_reports / "run_note.md").write_text(
        "# Full run note\n\nA single controlled full content-generation run executed.\n"
        "Outputs: outline, draft, review, references (raw text, for human review).\n",
        encoding="utf-8",
    )
