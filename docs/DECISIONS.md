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
- **Status:** Accepted (Stage 8A); extended by D-020, which adds Gemini in Stage 8A.1. Not reverted — the OpenAI path remains supported.
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

## D-020 — Stage 8A.1: Add Gemini Provider Support (Offline)

- **Date:** 2026-06-11
- **Status:** Accepted (extends D-018; does not revert it)
- **Context:** The student has a Gemini API key, not an OpenAI key. The resolver previously supported `openai` only (D-018).
- **Decision:** Extend `resolve_llm` to support `provider = "gemini"` alongside `openai`. The Gemini credential is read from the environment as `GEMINI_API_KEY` (preferred, matching the `gemini/` model prefix) with `GOOGLE_API_KEY` as the documented fallback; if both are set, `GEMINI_API_KEY` wins. The raw key is never logged or returned; `describe_llm_environment` still reports presence booleans only (and `base_url_present` is always `False` for Gemini, since no Gemini base-url path is supported here). The recommended Gemini model string is **`gemini/gemini-2.5-flash`**.
- **Alternatives considered:** Preferring `GOOGLE_API_KEY`; supporting a Gemini base_url; switching the whole project to Gemini and dropping OpenAI.
- **Rationale:** Adding Gemini lets the student run with the key they actually have, while keeping OpenAI available. Stage 8A.1 stays fully offline: **no real run, no `kickoff`, no LLM/API call, and no dependency added.**
- **Consequences:** Building a Gemini `LLM` requires the `crewai[google-genai]` provider package, which is **not installed** — constructing one offline raises `ImportError`, which `resolve_llm` wraps into a clear `LLMConfigError`. Installing that provider package is a **Stage 8B dependency decision** made by the student before the first real Gemini run. Gemini support is therefore only offline-tested in this stage (validation + safe-metadata paths); the construction/real path is validated at Stage 8B.

## D-021 — Stage 8B.0: Install the Gemini Provider Dependency

- **Date:** 2026-06-11
- **Status:** Accepted
- **Context:** D-020 wired Gemini support into the resolver, but building a Gemini `LLM` raised `ImportError` because the provider package was not installed. The student needs the Gemini path to actually work for the first real run.
- **Decision:** Add the Gemini provider extra via `uv add "crewai[google-genai]"`. uv updated the single existing dependency from `crewai>=0.80` to `crewai[google-genai]>=0.80` (no other dependency loosened) and refreshed `uv.lock` (added `google-genai`, `google-auth`, `pyasn1`, `pyasn1-modules`).
- **Alternatives considered:** Installing `litellm` to route Gemini; adding `google-genai` directly without the CrewAI extra; staying deferred.
- **Rationale:** The CrewAI `[google-genai]` extra is the supported, minimal way to enable CrewAI's native Gemini provider. It is the package CrewAI itself recommended in the earlier ImportError message.
- **Consequences:** A Gemini `LLM` now **constructs offline** (verified with a fake key, no model call), so the offline construction test is enabled. This stage installs the dependency only — **it runs nothing**: no `kickoff`, no LLM/API call, no tokens, no evidence. The first real Gemini run is Stage 8B.1, executed by the student with their own key in their own terminal.

## D-022 — Confirmed Provider/Model for Content Generation: Gemini 2.5 Flash

- **Date:** 2026-06-11
- **Status:** Accepted (provisional — may be revisited on quality/cost grounds)
- **Context:** Stage 8B.1 executed the first real minimal run and proved the Gemini path works end-to-end at minimal scale, with concrete evidence: a single `kickoff` to `gemini/gemini-2.5-flash` (3.18 s; 85 prompt + 33 completion tokens; secret scan clean) under `results/stage8b1-minimal-gemini-20260611-154559/`.
- **Decision:** Use `gemini/gemini-2.5-flash` (provider Gemini) as the confirmed provider/model for the next real content-generation stage (Stage 8C).
- **Alternatives considered:** Switching to OpenAI (the student does not have an OpenAI key); choosing a larger Gemini model now.
- **Rationale:** It is the path the student has credentials for and which is now proven to run; a small/fast model keeps cost low while the pipeline is built out.
- **Consequences:** Stage 8C proceeds with Gemini unless a later quality or cost problem forces a new decision. **A successful minimal run does not prove final PDF quality** — it only confirms the wiring; quality is judged at the full-generation and validation stages.

## D-023 — Stage 8C.1: Full-Pipeline Runner and Evidence Format (Offline Scaffolding)

- **Date:** 2026-06-11
- **Status:** Accepted
- **Context:** The minimal runner proved the wiring (Stage 8B.1). The full content pipeline (outline → draft → review → references) needs a runner that executes the existing `build_crew()` crew and persists each task's output.
- **Decision:** Add `crew/full_runner.py` (`run_full`) and `crew/persist.py`, plus a `run-full` CLI command. `run_full` is dry-run by default (reports the blueprint, constructs no LLM, writes nothing). The single new `kickoff` lives only in `_run_real_full` (`real=True`); the minimal runner's `kickoff` is unchanged — so exactly two `kickoff` calls now exist, both in real-only paths. A real run persists per-task raw outputs (`crew_outputs/{outline,draft,review,references}.txt`), `crew_outputs/_index.json` (task → file → `output_schema` → length → non-empty), `runtime.json`, `logs/run.log` (presence booleans only), and `validation_reports/run_note.md`, under a fresh `create_run_directory` (no overwrite). Future run-id format: `stage8c3-full-gemini-<UTC-YYYYMMDD-HHMMSS>`.
- **Alternatives considered:** Extending the minimal runner; enforcing Pydantic output schemas now; writing a combined single output file instead of per-task files.
- **Rationale:** A separate runner keeps the minimal path untouched and the files small. Per-task raw outputs keep results reviewable; `_index.json` records the contract without enforcing it yet.
- **Consequences:** **Stage 8C.1 is offline scaffolding only — no real run, no `kickoff` at runtime, no LLM/API call, no evidence created.** The first real full run is Stage 8C.3, executed by the student with their own Gemini key; structured-output enforcement and the LaTeX/PDF stages remain future work.

## D-024 — Reject First Full Gemini Content for Final PDF; Harden Topic/Prompt Controls

- **Date:** 2026-06-11
- **Status:** Accepted
- **Context:** Stage 8C.3 executed the first real full run (`stage8c3-full-gemini-20260611-164153`; ~249 s; 153,748 + 200,472 tokens). It proved the full runner and per-task persistence work end-to-end, but the generated content is unsuitable: it produced a "Gradient Descent" article instead of the intended project topic, included placeholder author/date fields (`[Your Name/Placeholder Name]`, "October 2023"), and the review itself states the draft is only ~10 pages (target ~15).
- **Decision:** Keep the run's output as **diagnostic evidence only** (committed at `cf89e51`); do **not** use it for the final PDF. Before any second full run, add prompt/config hardening: make the topic configurable and actually passed to the crew, remove placeholder author/date (wire group/date from config), and steer the outline/draft toward ~15 pages.
- **Alternatives considered:** Editing the generated text by hand (rejected — evidence must come from real runs, not hand-edits); building LaTeX from the wrong content anyway (rejected — wasted effort on off-topic content); switching model/provider (not warranted — the issue is prompt/config, not the model).
- **Consequences:** Another real full run will be needed after hardening, adding token cost; this avoids building LaTeX from wrong content. The evidence stays in the repository as an honest record of what the first full run produced.

## D-025 — Stage 8C.6: Bind the Crew to the Configured Topic and Cover Metadata

- **Date:** 2026-06-11
- **Status:** Accepted
- **Context:** The first full run (D-024) produced off-topic content ("Gradient Descent"), placeholder author/date fields, and only ~10 pages. The root cause is that the task descriptions were generic and not bound to the assignment topic or real cover metadata.
- **Decision:** Harden the pipeline offline before a second run: add project metadata to the config (`authors`, `assignment_context`, `project_date`; topic set to *"From PoC to Production: A CrewAI Multi-Agent Pipeline for Generating a LaTeX Book"*), with strict validation (non-empty topic/authors/date). Introduce a `ProjectContext` and context-bound task instructions (`crew/context.py`, `crew/instructions.py`) so outline/draft/review/references are written about the configured topic with the real group/authors/date, explicitly forbidding the failure modes (unrelated topics such as Gradient Descent, placeholder author fields, stale dates like "October 2023", too-short content). The review task must check topic, placeholders, length, mandatory PDF elements, and citation quality; references must be relevant to CrewAI/LaTeX/software-engineering, not ML. Add an offline `content_checks` helper that flags forbidden terms, placeholders, off-topic text, and missing mandatory elements.
- **Alternatives considered:** Re-running with the same prompts and hoping for better luck; hardcoding the topic into the prompts (less flexible than config-driven); enforcing Pydantic output schemas now (deferred).
- **Consequences:** The next real run (Stage 8C.7) is strongly bound to the assignment topic and metadata. This is offline scaffolding only — **no real run, no `kickoff`, no LLM/API call, and no evidence are produced in 8C.6.** The `content_checks` helper can gate future evidence before acceptance.

## D-026 — Accept Second Full Gemini Run as Candidate Evidence, Not Final PDF-Ready Content

- **Date:** 2026-06-11
- **Status:** Accepted
- **Context:** After the 8C.6 hardening, the second full run (`stage8c7-full-gemini-20260611-173125`; ~300.7 s; 213,664 + 235,436 tokens) produced on-topic content with the real cover metadata and passed the basic offline `content_checks` gate (no forbidden terms, no placeholders, no missing mandatory-element keywords). It fixes the previous off-topic/placeholder failure (D-024). However, it still contains questionable citations (`example.com` links, "Internal Publication"), unsupported in-text metrics (185 minutes / 99.1% / 1.8M tokens), GPT-4o references despite the Gemini run, and headers/footers described only conceptually.
- **Decision:** Accept the run as a **candidate content source** (committed at `0611993`), but do **not** treat it as final content. Perform Stage 8C.8 content QA — deterministic/human-reviewed cleanup — before LaTeX assembly: implement real headers/footers in LaTeX, replace/remove fake citations with real project files or valid references, remove unsupported metrics, and correct GPT-4o→Gemini references.
- **Alternatives considered:** Rejecting it outright and re-running (costly, and the basics are now correct); accepting it as-is for the PDF (dishonest — fabricated citations/metrics); editing the evidence by hand (rejected — evidence stays as produced).
- **Consequences:** Avoids another immediate expensive real run; shifts effort to deterministic/human cleanup before PDF work. A constrained re-run remains possible if QA finds gaps that cleanup cannot fix.

## D-027 — Content QA Cleanup Plan: Derived Cleaned Content, Evidence Immutable

- **Date:** 2026-06-12
- **Status:** Accepted (plan)
- **Context:** The Stage 8C.7 candidate (`results/stage8c7-full-gemini-20260611-173125/`) passes the basic content gate but is not final PDF-ready: questionable `example.com`/"Internal Publication" citations, unsupported in-text metrics (185 minutes / 99.1% / 1.8M tokens), GPT-4o references despite the Gemini run, and conceptual-only headers/footers (D-026).
- **Decision:** Clean the candidate into final source content **without editing the committed evidence**. The run evidence under `results/` is immutable diagnostic record. Curated, human-reviewed content is created later as a **separate derived artifact** under `latex_project/content/` (chosen over `content/cleaned/` because the cleaned content is the direct input to the LaTeX assembler, so it belongs inside the LaTeX project that produces the PDF — keeping the build self-contained per LR-1/LR-2). An offline deterministic QA scanner gates the cleaned content. Measured claims use the committed `runtime.json` values only (Gemini, ~300.7 s, 213,664 + 235,436 tokens); unmeasured metrics are removed or turned into clearly-labelled *proposed* evaluation metrics. Citations follow a conservative policy: course materials, official CrewAI/LaTeX/CTAN docs, and project evidence files only — no fake URLs, no fabricated reports, no invented internal publications; any external source is verified before final use.
- **Alternatives considered:** Editing the evidence in place (rejected — breaks evidence immutability); accepting the candidate as-is for the PDF (rejected — dishonest citations/metrics); regenerating via another paid run (deferred — the basics are correct; cleanup is cheaper and deterministic).
- **Consequences:** No further token cost for cleanup itself; the LaTeX project gains a `latex_project/content/` source tree later; the QA scanner becomes a reusable gate. This is **plan-only** — no cleaned content, LaTeX, or PDF is created in 8C.8.0, and no real run occurs.

## D-028 — Deterministic Offline Scanner as the Content Gate Before LaTeX

- **Date:** 2026-06-12
- **Status:** Accepted
- **Context:** D-027 requires cleaning the candidate into final content under `latex_project/content/`. We need an objective, repeatable way to decide whether content is acceptable before LaTeX assembly.
- **Decision:** Add `src/agentic_latex_book/content_qa.py` — a deterministic, offline scanner (`scan`, `check_text`, `collect_text_files`) that reads a file, a list of files, or a directory of `.txt`/`.md` content and returns a `QAReport` (`ok`, `errors`, `warnings`, `checked_files`). It applies pure string checks: blocking errors for forbidden content (`example.com`, "Internal Publication", the unsupported metrics 185 minutes / 99.1% / 1.8M tokens, "GPT-4o Technical Report", placeholders, the old Gradient Descent topic, conceptual-only headers/footers) and required positives (the configured topic, group `MaRs-777`, both authors, an accepted date, and all mandatory PDF elements). A `content-qa <path>` CLI command runs it and exits non-zero on any blocking error. No network, no model, no API key, and no file is mutated.
- **Alternatives considered:** Trusting the basic `content_checks` gate (too lenient — it missed citations/metrics); an LLM judge (non-deterministic, costs tokens, not offline); regex-heavy parsing (over-engineered for now).
- **Consequences:** The committed Stage 8C.7 candidate **fails** this stricter scanner (it still contains the known risks), which is the intended signal that it is not final. Cleaned content (Stage 8C.8.2) must pass the scanner before commit and LaTeX assembly. This stage is offline and adds no dependency and no LLM/API cost.

---

## D-029 — Derived Cleaned Markdown as the Source for LaTeX Assembly

- **Date:** 2026-06-12
- **Status:** Accepted
- **Context:** The Stage 8C.7 run evidence is immutable and still contains the known content risks, so it cannot be fed directly into LaTeX assembly. We need a clean, reviewable, scanner-passing source for the document.
- **Decision:** Create cleaned Markdown under `latex_project/content/` (`book.md` plus a `README.md`), **derived** from the 8C.7 candidate (`crew_outputs/` outline and draft) but edited by the students, and use that as the single source for LaTeX assembly — not the raw LLM evidence. The cleaning removed the 8 known risks (fabricated `example.com`/internal links, the unsupported 185 minutes / 99.1% / 1.8M tokens metrics, the GPT-4o report reference, and conceptual-only header/footer wording), replaced unmeasured metrics with the actual `runtime.json` values (labelling unmeasured ones as proposed future evaluation), used a conservative real/project-local bibliography, and stated explicitly that headers/footers are implemented in LaTeX assembly. The cleaned content must pass `content-qa` (it does: `ok: True`, exit 0) before commit and assembly.
- **Alternatives considered:** Feeding raw evidence straight into LaTeX (fails the scanner and would publish fabricated claims); re-running the crew with stricter prompts to avoid manual cleaning (costs tokens and is non-deterministic — deferred unless cleaning proves insufficient); editing the evidence in place (rejected — evidence must stay immutable).
- **Consequences:** Evidence under `results/stage8c7-full-gemini-20260611-173125/` stays untouched; the cleaned content is a separate derived artifact. This stage is offline and human-reviewed: no real run, no `kickoff`, no LLM/API call, no tokens, and no dependency change. LaTeX/PDF assembly remains a future stage.

---

## Open Decisions (To Be Recorded Later)

The following are not yet decided and will become decision records when resolved (sourced from PLAN §27 / TODO §11). The LLM provider/model and plotting-library deferrals are now recorded explicitly above (D-014, D-015):

- LaTeX engine and BiDi package (Stage 9/11).
- Sequential vs parallel chapter drafting (Stage 8).
- Page-count threshold for the page-count gate (Stage 12).
- Whether to adopt mypy and whether to add CI (Stage 13).
