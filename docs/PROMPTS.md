# Prompts Log

## Purpose

This document records the AI prompts used during the project so the workflow is transparent and reviewable, as required by the course. It is a running log: entries are added as work proceeds. To keep it readable and avoid leaking noise, entries are written as concise **summaries** of each prompt and its intent rather than full raw transcripts.

## Prompt Logging Policy

- Log a summary entry for each meaningful AI-assisted task (a document, a component, a review pass).
- Record what was asked for, the important constraints we imposed, what artifact resulted, and the result of our review.
- Do not paste secrets, API keys, or environment values into this log.
- Do not claim an artifact exists or works if it does not. Entries describe only work actually performed.
- Where a tool/model is not yet decided, record it as such rather than guessing. Planning and foundation stages used a general AI coding assistant; the concrete pipeline LLM model/provider is deferred until before the first real CrewAI execution (per decision D-014). Stage 7 added offline CrewAI agent/task specs and output-schema specs, but there is still no real crew run, no `kickoff`, no LLM/API call, no LaTeX, and no generated evidence.

## Prompt Record Template

Use this template for new entries:

| Field | Description |
| --- | --- |
| Stage | Project stage number |
| Date | Date of the prompt (YYYY-MM-DD) |
| Goal | What the prompt aimed to achieve |
| Tool/Model | The AI tool/model used, if known |
| Prompt summary | A short description of what was asked |
| Important constraints | Key rules imposed (e.g. docs-only, no code, no fake evidence) |
| Output artifact | The file(s) produced or changed |
| Review result | Outcome of group review (accepted / revised / rejected) |

## Logged Prompts (Stages 0–8C.5)

These entries summarize the AI-assisted work already completed. They are summaries, not raw prompts. Stages 0–4 produced repository structure and planning documentation only; Stages 5–6 added project setup and deterministic foundation code (config, paths, evidence, logging, runtime) with offline tests; Stage 7 added offline CrewAI agent/task specs and output-schema specs with a dry-run blueprint. No real crew run (`kickoff`), no LLM/API calls, no LaTeX, and no generated evidence have been produced yet.

| Stage | Date | Goal | Tool/Model | Prompt summary | Important constraints | Output artifact | Review result |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 0 | 2026-06-11 | Create a clean repository skeleton | AI coding assistant | Asked to create the directory structure, placeholder docs, `.gitignore`, and package init, with no implementation | Skeleton only; no code; no fake outputs; preserve empty dirs | Repository skeleton (commit `a0f8734`) | Accepted |
| 1 | 2026-06-11 | Write a professional PRD | AI coding assistant | Asked to write a full PRD (problem, goals, scope, requirements, acceptance criteria, traceability) from the assignment brief | Plan only; no implementation; evidence-first; group submission | `docs/PRD.md` (commit `b501a36`) | Accepted after targeted submission fixes |
| 2 | 2026-06-11 | Write a technical PLAN | AI coding assistant | Asked to design the architecture and strategy strictly from the PRD | Design only; no code/deps/LaTeX; do not invent features | `docs/PLAN.md` (commit `6baece3`) | Accepted |
| 3 | 2026-06-11 | Write a detailed staged TODO | AI coding assistant | Asked to break the PLAN into staged, actionable checklist tasks | Task plan only; ≥120 checkboxes; match PLAN roadmap | `docs/TODO.md` (commit `a722f64`) | Accepted after quality-timing correction |
| 4 | 2026-06-11 | Write supporting documentation | AI coding assistant | Asked to write AI_WORKFLOW, PROMPTS, DECISIONS, COSTS, QUALITY, SUBMISSION_CHECKLIST, and an initial README | Docs only; planned-status wording; no implementation claims | This document and the other Stage 4 files | Accepted for initial Stage 4 documentation after review |
| 5 | 2026-06-11 | Project setup (uv, deps, CLI skeleton) | AI coding assistant | Asked to create `pyproject.toml`, uv lock, `.env.example`, config, a safe CLI skeleton, and a smoke test | Setup only; no agents/LLM; no secrets; pytest+ruff pass | Stage 5 setup files | Accepted (commit `d21b3c7`) |
| 6 | 2026-06-11 | Deterministic foundation modules | AI coding assistant | Asked to implement config/paths/evidence/logging/runtime modules and their offline tests | Deterministic only; no CrewAI/LLM; temp-only evidence; files under the line limit | `config.py`, `paths.py`, `evidence.py`, `logging_setup.py`, `runtime.py`, and their tests | Accepted (commit `3e538af`) |
| 7 | 2026-06-11 | CrewAI core (offline specs + schemas + blueprint) | AI coding assistant | Asked to define agent/task specs, output-schema specs, a validated dry-run blueprint, a deferred object builder, and a `crew-plan` CLI command | Offline only; no kickoff; no LLM/API; no real run/evidence | `crew/specs.py`, `crew/schemas.py`, `crew/agents.py`, `crew/tasks.py`, `crew/builder.py`, CLI `crew-plan`, and tests | Accepted (commit `aeb39dc`) |
| 8A | 2026-06-11 | Controlled-run scaffolding (no real run) | AI coding assistant | Asked to add the LLM resolver, minimal runner, `run-minimal` CLI with an explicit `--real` gate, and offline safety tests | Offline only; OpenAI-only; env-only secrets; no `.env` auto-load; no kickoff/LLM/API; no real run/evidence | `config.py`, `crew/llm.py`, `crew/runner.py`, `cli.py`, `cli_commands.py`, tests, and docs | Accepted (commit `d9acbf7`) |
| 8A.1 | 2026-06-11 | Add Gemini provider support (offline) | AI coding assistant | Asked to extend the resolver to support `provider="gemini"` with `GEMINI_API_KEY`/`GOOGLE_API_KEY`, plus offline tests | Offline only; env-only secrets; no `.env` auto-load; no kickoff/LLM/API; no dependency added; no real run/evidence | `crew/llm.py`, `tests/test_crew_llm.py`, and docs | Accepted (commit `a31f80a`) |
| 8B.0 | 2026-06-11 | Install Gemini provider dependency (offline) | AI coding assistant | Asked to add `crewai[google-genai]` via uv and an offline Gemini construction test | Dependency only; offline; no kickoff/LLM/API; no real run/evidence; no source-logic change | `pyproject.toml`, `uv.lock`, `tests/test_crew_llm.py`, and docs | Accepted (commit `7e28f01`) |
| 8B.1 | 2026-06-11 | Commit first real minimal Gemini run evidence | AI coding assistant | Asked to review and commit the evidence the student produced by running `run-minimal --real` against Gemini | Student executed the real run manually with their own key in their own terminal; no key logged or used by the assistant; evidence reviewed (secret scan clean) and committed; assistant ran no real call | `results/stage8b1-minimal-gemini-20260611-154559/` (evidence only) | Accepted (commit `81e5b26`) |
| 8C.1 | 2026-06-11 | Offline full content-pipeline scaffolding | AI coding assistant | Asked to add the full runner, per-task persistence, the `run-full` CLI, and offline tests | Offline only; dry-run default; single new `kickoff` only in the full real path; no real run/LLM/API/evidence; no dependency added | `crew/full_runner.py`, `crew/persist.py`, `cli.py`, `cli_commands.py`, `tests/test_full_runner.py`, and docs | Accepted (commit `20e1774`) |
| 8C.4 | 2026-06-11 | Commit first full Gemini run evidence | AI coding assistant | Asked to review and commit the evidence the student produced by running `run-full --real` against Gemini | Student executed the real run manually with their own key; no key logged/used by the assistant; evidence reviewed (secret scan clean) and committed; assistant ran no real call | `results/stage8c3-full-gemini-20260611-164153/` (evidence only) | Evidence accepted (commit `cf89e51`); content **rejected for final PDF** (wrong topic, placeholders, ~10 pages) |
| 8C.5 | 2026-06-11 | Document the rejected first full run | AI coding assistant | Asked to update docs to record the full run worked technically but its content is rejected; next step is prompt/config hardening | Docs only; no real run/LLM/API; no evidence/source/dependency change | `docs/TODO.md`, `docs/PROMPTS.md`, `docs/COSTS.md`, `docs/QUALITY.md`, `docs/DECISIONS.md` | In review |

## Future Prompts

Project setup (Stage 5) and the deterministic foundation including the config loader (Stage 6) are already logged in the table above. Further implementation-stage prompts will be added here as the project proceeds — for example prompts used to draft the crew builder, the LaTeX assembler, the figure generator, the PDF builder, and the validation gates. No claim is made that any not-yet-built component exists. This log will grow alongside the actual work.
