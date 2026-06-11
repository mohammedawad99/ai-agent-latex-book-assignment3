# Decision Log

## Purpose

This document records the significant decisions made during the project, so the reasoning behind the design is visible and can be revisited. Each decision is a numbered record with enough context to understand why it was made and what it implies. Decisions can be revised later; when that happens, we add a new record or update the status rather than silently rewriting history.

## Decision Record Format

Each record uses these fields:

- **ID** — `D-NNN`.
- **Date** — when the decision was made (YYYY-MM-DD).
- **Status** — Accepted / Superseded / Revisit at Stage N.
- **Context** — the situation that required a decision.
- **Decision** — what was decided.
- **Alternatives considered** — other options we weighed.
- **Rationale** — why we chose this option.
- **Consequences** — what follows from it.

---

## D-001 — Repository / Project Name

- **Date:** 2026-06-11
- **Status:** Accepted
- **Context:** Assignment 3 needs its own repository, clearly separated from earlier assignments.
- **Decision:** Use the repository/project name `ai-agent-latex-book-assignment3`.
- **Alternatives considered:** Reusing or renaming an earlier assignment repository; a shorter generic name.
- **Rationale:** A descriptive, assignment-specific name avoids confusion with Assignment 2 and makes the submission link unambiguous.
- **Consequences:** The submitted GitHub link and the Moodle wrapper PDF must reference this exact repository.

## D-002 — Documentation-First Workflow

- **Date:** 2026-06-11
- **Status:** Accepted
- **Context:** Assignment 1 feedback flagged weak planning and low visibility of process.
- **Decision:** Complete PRD, PLAN, TODO, and supporting documentation before writing implementation code.
- **Alternatives considered:** Start coding immediately and document afterwards.
- **Rationale:** Doc-first work makes scope, acceptance criteria, and the engineering process explicit, and directly addresses prior feedback.
- **Consequences:** Stages 0–4 produce no code; dependencies and implementation begin at Stage 5.

## D-003 — CrewAI as the Orchestration Mechanism

- **Date:** 2026-06-11
- **Status:** Accepted
- **Context:** The assignment requires a multi-agent system, and the course specifies CrewAI.
- **Decision:** Use CrewAI as the required orchestration mechanism for the agent pipeline.
- **Alternatives considered:** Other agent frameworks; a single-prompt approach.
- **Rationale:** CrewAI is the mandated framework and fits a multi-role writing/review pipeline.
- **Consequences:** The content-generation layer is built on CrewAI; the model/provider behind it is decided separately (see D-007).

## D-004 — Separate Agentic Generation from Deterministic Build/Validation

- **Date:** 2026-06-11
- **Status:** Accepted
- **Context:** PDF correctness must be guaranteed, but model output is not deterministic.
- **Decision:** Let CrewAI agents handle writing/review, and handle LaTeX assembly, PDF build, and validation with deterministic Python code.
- **Alternatives considered:** An all-agent pipeline that also assembles and validates.
- **Rationale:** Correctness of the mandatory PDF elements should be enforced by code and checks, not by trusting a model's claims; this supports the evidence-first principle.
- **Consequences:** Clear module boundaries; validation gates are independent, testable Python.

## D-005 — Include the LaTeX Project in the Repository

- **Date:** 2026-06-11
- **Status:** Accepted
- **Context:** The assignment requires the LaTeX sources used to build the PDF to be available.
- **Decision:** Keep all LaTeX sources under `latex_project/` in the repository; ignore only transient build artifacts.
- **Alternatives considered:** Committing only the final PDF; generating LaTeX outside the repo.
- **Rationale:** Including the sources is required and makes the build reproducible and reviewable.
- **Consequences:** `.gitignore` must exclude build artifacts while keeping sources and the final PDF tracked.

## D-006 — Article PDF and Moodle Wrapper PDF Are Separate

- **Date:** 2026-06-11
- **Status:** Accepted
- **Context:** The submission requires a Moodle wrapper document distinct from the generated article.
- **Decision:** Treat the generated article/book PDF (the main evaluated artifact) and the Moodle submission PDF (`MaRs-777-ex03.pdf`) as two separate deliverables.
- **Alternatives considered:** Submitting only the article PDF; merging both into one file.
- **Rationale:** They serve different purposes — the article is the evaluated output; the wrapper carries submission metadata (exercise number, group code, GitHub link, self-score).
- **Consequences:** The wrapper is created manually from the official Word template, not produced by the pipeline.

## D-007 — Defer Dependencies and Model/Provider Choice to Stage 5

- **Date:** 2026-06-11
- **Status:** Revisit at Stage 5
- **Context:** Choosing dependencies and an LLM provider early would lock in decisions before setup.
- **Decision:** Add no dependencies and choose no model/provider until Stage 5 (Project Setup).
- **Alternatives considered:** Selecting the model and libraries during planning.
- **Rationale:** Keeps the planning stages clean and avoids premature commitment; the choice has cost and BiDi implications best handled at setup.
- **Consequences:** No `pyproject.toml` exists yet; the model/provider, plotting library, and LaTeX engine are open questions tracked in PLAN §27 and TODO §11.

## D-008 — Evidence Only From Real Runs

- **Date:** 2026-06-11
- **Status:** Accepted
- **Context:** Assignment feedback emphasized that claims must be backed by evidence, not description.
- **Decision:** Commit evidence (logs, crew outputs, validation reports, final PDF) only when produced by a real run; never fabricate placeholder results.
- **Alternatives considered:** Adding sample/mock evidence to illustrate structure.
- **Rationale:** Fabricated evidence would be dishonest and would undermine the whole submission.
- **Consequences:** `results/` holds only `.gitkeep` markers until Stage 14 produces real artifacts.

## D-009 — Incremental GitHub Commit History

- **Date:** 2026-06-11
- **Status:** Accepted
- **Context:** A professional process should be visible in the repository history.
- **Decision:** Commit and push at meaningful increments throughout the project, not in a single final dump.
- **Alternatives considered:** Developing locally and pushing everything at the end.
- **Rationale:** Incremental history demonstrates the engineering process and makes review easier.
- **Consequences:** Each stage is its own commit (or coherent set of commits) with standard student authorship.

## D-010 — uv as Dependency / Environment Manager

- **Date:** 2026-06-11
- **Status:** Accepted
- **Context:** Stage 5 needs a reproducible Python environment and dependency lock.
- **Decision:** Use `uv` for environment creation, dependency resolution, and locking (`uv.lock`).
- **Alternatives considered:** pip + venv + requirements.txt; Poetry; PDM.
- **Rationale:** uv is fast, produces a deterministic lock file, and is the course-aligned tool; `uv sync` reproduces the environment from a clean checkout.
- **Consequences:** `uv.lock` is committed and only modified through uv; setup commands are `uv sync` / `uv run ...`.

## D-011 — Initial Runtime and Dev Dependencies

- **Date:** 2026-06-11
- **Status:** Accepted
- **Context:** The setup stage should declare only what is needed now, without implementing the pipeline.
- **Decision:** Runtime dependency: `crewai` (declared, not yet used). Dev dependencies: `pytest` and `ruff`.
- **Alternatives considered:** Adding LLM client libraries, plotting, or LaTeX-related packages now.
- **Rationale:** CrewAI is the required framework and is declared so the environment is ready; pytest/ruff enable quality from the start. Other libraries are deferred until the stage that needs them, to avoid premature commitment.
- **Consequences:** The environment installs CrewAI's dependency tree; no agents/tasks exist yet. TOML config is read with the standard-library `tomllib`, so no TOML dependency is needed.

## D-012 — Configuration Format

- **Date:** 2026-06-11
- **Status:** Accepted
- **Context:** The project needs a non-secret configuration file for topic, paths, thresholds, and model placeholders.
- **Decision:** Use TOML (`config/default.toml`), read with the standard-library `tomllib`.
- **Alternatives considered:** YAML (requires an extra dependency); JSON (no comments); Python config module.
- **Rationale:** TOML is readable, supports comments, and needs no extra dependency on Python 3.11+.
- **Consequences:** Config is loaded via `tomllib`; secrets stay out of this file and come from the environment.

## D-013 — mypy Deferred

- **Date:** 2026-06-11
- **Status:** Deferred (revisit at Stage 13)
- **Context:** Static typing could be adopted now or later.
- **Decision:** Do not add mypy in Stage 5; revisit during Stage 13 quality hardening.
- **Alternatives considered:** Adopting mypy immediately.
- **Rationale:** The Stage 5 surface is tiny (a CLI skeleton); type-checking adds little value now and would add tooling overhead. The codebase uses type hints already, so adopting mypy later is straightforward.
- **Consequences:** No mypy config yet; the decision is recorded so it is a deliberate deferral, not an omission.

## D-014 — Concrete LLM Provider/Model Deferred

- **Date:** 2026-06-11
- **Status:** Deferred (revisit before the first real CrewAI run, Stage 7/8)
- **Context:** Stage 5 sets up the project but performs no real CrewAI execution and makes no LLM calls. The config and `.env.example` carry provider/model placeholders only.
- **Decision:** Do not select a concrete LLM provider/model in Stage 5; defer the choice until just before the first real CrewAI execution.
- **Alternatives considered:** Choosing a provider/model now to "lock it in" during setup.
- **Rationale:** No code calls a model yet, so a concrete choice would add no value and would risk committing to a provider before its cost/token-exposure characteristics are evaluated against the pipeline's needs. The placeholders keep the setup runnable offline.
- **Consequences:** `config/default.toml` `[model]` and `.env.example` stay as placeholders; the choice and its rationale are recorded as a new decision when made (Stage 7/8). This supersedes the Stage 5 timing implied earlier for PLAN open question 1.

## D-015 — Plotting Library Deferred

- **Date:** 2026-06-11
- **Status:** Deferred (revisit at Stage 10, graph generation)
- **Context:** The Python-generated graph is produced in Stage 10; Stage 5 generates no graphs.
- **Decision:** Do not add or select a plotting library in Stage 5; defer until the graph-generation stage.
- **Alternatives considered:** Adding a plotting dependency now.
- **Rationale:** Adding a plotting dependency before any graph code exists would be premature and would enlarge the environment without need. Deferring keeps Stage 5 dependencies minimal.
- **Consequences:** No plotting dependency is declared yet; the library is chosen and recorded when Stage 10 begins.

## D-016 — Deterministic Foundation: Stdlib-First, Temp-Only Evidence Tests

- **Date:** 2026-06-11
- **Status:** Accepted
- **Context:** Stage 6 builds the deterministic foundation (config, paths, evidence, logging, runtime) that the later pipeline depends on.
- **Decision:** Implement these modules with the Python standard library only (`tomllib`, `dataclasses`, `pathlib`, `logging`, `time`) and test the evidence/logging helpers exclusively against pytest `tmp_path`, never writing committed evidence under `results/`.
- **Alternatives considered:** Pydantic for config/validation; third-party logging or settings libraries; testing evidence helpers by writing into the real `results/` tree.
- **Rationale:** The needs are small, so stdlib keeps the dependency surface minimal and the code easy to read. Temp-only tests keep `results/` holding only `.gitkeep` markers and honor the evidence-only-from-real-runs rule (D-008).
- **Consequences:** No new dependencies were added in Stage 6; `results/` stays clean; the runtime tracker keeps token/cost fields as `None` until a real provider supplies values.

## D-017 — CrewAI Core: Offline Specs/Blueprint First, Real Kickoff Deferred

- **Date:** 2026-06-11
- **Status:** Accepted
- **Context:** Stage 7 builds the CrewAI core, but a real crew run needs a chosen LLM provider/model and credentials, which are deferred (D-014).
- **Decision:** Model the crew as plain `AgentSpec`/`TaskSpec` dataclasses plus offline `OutputSchemaSpec` output-schema specs (in `crew/schemas.py`), with a validated dry-run blueprint, and keep all execution out of Stage 7. The schema specs are plain data (no Pydantic, no dependency) describing the structure each task output is intended to follow; they are not yet enforced against real LLM output. A `build_crew()` function constructs real CrewAI `Agent`/`Task`/`Crew` objects (which is safe offline in the installed version) but never calls `kickoff` and passes only the text `expected_output` to tasks (no structured-output enforcement yet); running the crew is deferred to a later controlled stage once a provider/model is chosen.
- **Alternatives considered:** Building and running the crew now with a default provider; using Pydantic schemas with enforced structured output immediately; or not constructing any CrewAI objects until the run stage.
- **Rationale:** Specs + schema specs + blueprint give a fully testable, offline, reviewable core that names its output contracts explicitly. Constructing real objects (without running) proves the wiring works without spending tokens or requiring a key. This keeps the stage safe and honest.
- **Consequences:** No tokens are spent and no evidence is produced in Stage 7; the `crew-plan` CLI command and tests rely only on the offline blueprint. Real structured-output enforcement, intermediate-output persistence, prompt/token capture, and the first real invocation move to the run stage.

## D-018 — Stage 8A Provider Strategy: OpenAI / OpenAI-Compatible Only

- **Date:** 2026-06-11
- **Status:** Accepted (for Stage 8A; broader providers revisited later)
- **Context:** The first real run needs a provider, but the installed environment has the `openai` SDK only — `litellm`, `anthropic`, and `google-generativeai` are not installed.
- **Decision:** Stage 8A supports the `openai` provider only (`crewai.LLM` with `model`, optional `base_url`). An OpenAI-compatible local endpoint is supported via `OPENAI_BASE_URL` so a real run can be exercised at zero cost without a cloud key.
- **Alternatives considered:** Adding `litellm` or other provider SDKs to support Anthropic/Gemini/Ollama-native now.
- **Rationale:** Using the already-present OpenAI path adds no dependency (Stage 8A forbids dependency changes). The `base_url` escape hatch keeps a cost-free local option open.
- **Consequences:** `resolve_llm` rejects non-OpenAI providers with a clear error; supporting other providers later will be its own decision and may add a dependency.

## D-019 — Controlled-Run Safety Gates

- **Date:** 2026-06-11
- **Status:** Accepted
- **Context:** A real CrewAI run spends tokens and needs credentials; it must never happen by accident.
- **Decision:** A real run requires the explicit `run-minimal --real` flag *and* a configured provider/model *and* credentials in the environment. Secrets are read only from `os.environ` (no `.env` auto-loading, no `python-dotenv`); the raw key is never printed, logged, or written to evidence (only presence booleans). The single `kickoff` call lives solely in the runner's `real=True` path. Stage 8A performs no real run; it ships only the scaffolding, gates, and offline tests.
- **Alternatives considered:** Auto-loading `.env`; allowing a real run as the default; logging the key for debugging.
- **Rationale:** Explicit opt-in plus env-only secrets minimizes accidental spend and leakage and keeps the default experience safe and offline.
- **Consequences:** The student runs the first real minimal run themselves (Stage 8B) after exporting env vars in their own terminal; evidence is reviewed for secrets before being committed.

---

## Open Decisions (To Be Recorded Later)

The following are not yet decided and will become decision records when resolved (sourced from PLAN §27 / TODO §11). The LLM provider/model and plotting-library deferrals are now recorded explicitly above (D-014, D-015):

- LaTeX engine and BiDi package (Stage 9/11).
- Sequential vs parallel chapter drafting (Stage 8).
- Page-count threshold for the page-count gate (Stage 12).
- Whether to adopt mypy and whether to add CI (Stage 13).
