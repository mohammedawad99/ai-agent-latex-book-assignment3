# TODO — Staged Task Plan

## 1. Title and Document Status

**Project:** From PoC to Production — A CrewAI Multi-Agent Pipeline that Generates a ~15-Page Article/Book as a Polished LaTeX PDF.

**Repository:** `ai-agent-latex-book-assignment3`

**Group:** MaRs-777 (Mohamed Awad, Rawey Sleiman). Mohamed Awad is the current repository maintainer.

**Document status:** Living task plan. Stages 0–8C.7 are complete and pushed; Stage 8C.6 hardened the topic/metadata (`0858c44`), and the second full Gemini run (8C.7, `0611993`) produced **candidate content** that passes the basic offline content gate (on-topic, real cover metadata, no placeholders). The candidate is **not final PDF-ready** (questionable citations, unsupported metrics, conceptual-only headers/footers). **No final accepted content and no LaTeX/PDF exist yet.** Stage 8C.8.0 (the cleanup plan) is committed (`dd18878`); Stage 8C.8.1 (the deterministic offline QA scanner) is committed and pushed (`dcac0eb`). Stage 8C.8.2/8C.8.3 (cleaned Markdown content under `latex_project/content/`) is **committed and pushed (`98a50f2`)** after human review — `book.md` and `README.md` are derived from the 8C.7 candidate and **pass the strict `content-qa` scanner (`ok: True`, exit 0)**; this is cleaned source only, so **no LaTeX and no PDF exist yet**. **Stage 9.x (LaTeX assembly from the cleaned content) is the current milestone:** the Stage 9.0 assembly plan is committed and pushed (`c3ca705`; D-030), and **Stage 9.1 (LaTeX skeleton + bibliography only) is committed and pushed (`af71265`)** after human review — `main.tex`, `preamble.tex`, nine skeleton chapter files (headings + TODO markers, not full text), and `references.bib` (transcribed from the cleaned bibliography only) now exist under `latex_project/`. **No compile has been attempted (TeX Live is not installed on this machine yet) and no PDF exists.** **Stage 9.2 (figure/graph generation) is committed and pushed (`6aa2cf1`)** after human review (including the matplotlib backend hardening fix) — two deterministic matplotlib scripts under `latex_project/scripts/` and the two generated PNGs under `latex_project/figures/` (`architecture.png`, `generation_time.png` — the graph clearly labelled illustrative); the chapter figure blocks reference the existing PNGs. Still no compile (TeX Live not installed) and **no PDF**. **Stage 9.3 (convert cleaned Markdown into full LaTeX chapters) is next.** The plan derives strictly from `docs/PRD.md` and `docs/PLAN.md`. Changes are tracked through normal Git history.

**Last updated:** 2026-06-12.

---

## 2. Current Project State

- [x] Stage 0 — Repository skeleton committed and pushed (`a0f8734`).
- [x] Stage 1 — PRD committed and pushed (`b501a36`).
- [x] Stage 2 — PLAN committed and pushed (`6baece3`).
- [x] Stage 3 — TODO committed and pushed (`a722f64`).
- [x] Stage 4 — Supporting documentation committed and pushed (`495f966`).
- [x] Stage 5 — Project setup committed and pushed (`d21b3c7`).
- [x] Stage 6 — Core deterministic foundation committed and pushed (`3e538af`).
- [x] Stage 7 — Offline CrewAI core committed and pushed (`aeb39dc`).
- [x] Stage 8A — Controlled-run scaffolding committed and pushed (`d9acbf7`).
- [x] Stage 8A.1 — Offline Gemini provider support committed and pushed (`a31f80a`).
- [x] Stage 8B.0 — Gemini provider dependency installed, committed and pushed (`7e28f01`).
- [x] Stage 8B.1 — First real minimal Gemini run executed by the student; evidence committed and pushed (`81e5b26`).
- [x] Stage 8C.1 — Offline full content-pipeline scaffolding committed and pushed (`20e1774`).
- [x] Stage 8C.3 — First real full Gemini run executed by the student (4 outputs produced; content rejected for final PDF).
- [x] Stage 8C.4 — First full-run evidence committed and pushed (`cf89e51`), as diagnostic/rejected content.
- [x] Stage 8C.5 — Documentation update after the rejected run, committed and pushed (`c2127f2`).
- [x] Stage 8C.6 — Offline topic/metadata hardening committed and pushed (`0858c44`).
- [x] Stage 8C.7 — Second real full Gemini run executed by the student; candidate evidence committed and pushed (`0611993`).
- [x] Stage 8C.8.0 — Content-QA cleanup plan committed and pushed (`dd18878`).
- [x] Stage 8C.8.1 — Deterministic offline QA scanner committed and pushed (`dcac0eb`).
- [x] Stage 8C.8.2 — cleaned Markdown content created (`book.md`, `README.md` under `latex_project/content/`, derived from the 8C.7 candidate); passes `content-qa` (`ok: True`, exit 0). Cleaned source only — no LaTeX/PDF. (Committed and pushed: `98a50f2`.)
- [x] Stage 8C.8.3 — cleaned content reviewed (human review, minor citation/source fixes) and committed/pushed (`98a50f2`).
- [x] Stage 9.0 — LaTeX assembly plan (docs only; D-030). (Committed and pushed: `c3ca705`.)
- [x] Stage 9.1 — LaTeX skeleton + bibliography (`main.tex`, `preamble.tex`, `chapters/` stubs, `references.bib`, `latex_project/README.md`). No compile attempted because TeX Live is not installed; no figures/scripts; **no PDF**. (Committed and pushed: `af71265`.)
- [x] Stage 9.2 — figure/graph generation (`scripts/generate_architecture.py`, `scripts/generate_graph.py` → `figures/architecture.png`, `figures/generation_time.png`; graph labelled illustrative). No compile and **no PDF**. (Committed and pushed: `6aa2cf1`.) **Stage 9.3 (full chapter conversion) is next.**
- [ ] Stages 9.2–16 — not started; no PDF exists yet.

Key constraints carried from PRD/PLAN: the PDF is the main evaluated artifact; CrewAI is mandatory; the LaTeX project must be included under `latex_project/`; the generated article PDF and the Moodle submission PDF (`MaRs-777-ex03.pdf`) are separate; the GitHub repo must be public or shared with rmisegal@gmail.com; evidence must come from real runs only with no fabrication; no overclaiming of production readiness; Python files stay short and maintainable; every important claim eventually points to evidence; commit history stays incremental and meaningful.

---

## 3. How to Use This TODO

- Work top to bottom by stage. Do not start a stage until its **entry conditions** are met.
- A stage is finishable only when its **exit criteria**, **quality gates** (§6), and **evidence** (§7) are satisfied.
- Check a box `[x]` only when the task is genuinely done; leave future work `[ ]`.
- Stage numbers match the PLAN roadmap (`docs/PLAN.md` §25).
- Commit and push at meaningful increments per the policy in §8; never in a single final dump.
- Never check an evidence-related box unless the evidence came from a real run (no placeholders).

---

## 4. Stage Summary Table

| Stage | Title | Status | Entry condition | Primary exit artifact |
| --- | --- | --- | --- | --- |
| 0 | Repository skeleton + GitHub setup | Completed (`a0f8734`) | — | Skeleton on `main` |
| 1 | PRD | Completed (`b501a36`) | Stage 0 done | `docs/PRD.md` |
| 2 | PLAN | Completed (`6baece3`) | Stage 1 done | `docs/PLAN.md` |
| 3 | TODO | Completed (`a722f64`) | Stage 2 done | `docs/TODO.md` |
| 4 | Supporting documentation before code | Completed (`495f966`) | Stage 3 done | Doc set populated |
| 5 | Project setup (uv, deps, CLI skeleton) | Completed (`d21b3c7`) | Stage 4 done | `pyproject.toml`, runnable CLI stub |
| 6 | Core deterministic foundation | Completed (`3e538af`) | Stage 5 done | config/evidence/cost modules + tests |
| 7 | CrewAI core | Completed (`aeb39dc`) | Stage 6 done | crew specs/schemas/blueprint + builder |
| 8A | Controlled-run scaffolding | Completed (`d9acbf7`) | Stage 7 done | `run-minimal` + `--real` gate + tests |
| 8B/8C | Content planning and generation (real run) | Not started | Stage 8A done | outline→draft→review→refs flow |
| 9 | LaTeX assembler | Not started | Stage 8 done | `latex_project/` sources |
| 10 | Python-generated graph and assets | Not started | Stage 9 done | generated graph integrated |
| 11 | PDF build | Not started | Stage 10 done | article PDF in `results/final_pdf/` |
| 12 | Validation gates | Not started | Stage 11 done | passing gates + reports |
| 13 | Testing and quality hardening | Not started | Stage 12 done | coverage/length/clean-checkout green |
| 14 | Real end-to-end run and evidence | Not started | Stage 13 done | real run evidence in `results/` |
| 15 | Final documentation hardening | Not started | Stage 14 done | docs linked to evidence |
| 16 | Final submission preparation | Not started | Stage 15 done | `MaRs-777-ex03.pdf` + final push |

---

## 5. Detailed Staged Checklist

### Stage 0 — Repository Skeleton and Initial GitHub Setup (Completed, `a0f8734`)

Entry condition: none. Exit criteria: skeleton committed and pushed to `main`.

- [x] Create the project directory `ai-agent-latex-book-assignment3`.
- [x] Initialize Git and set the default branch to `main`.
- [x] Create the directory structure (`docs/`, `src/agentic_latex_book/`, `scripts/`, `tests/`, `latex_project/`, `results/` with subdirs, `assets/figures/`, `assets/generated/`).
- [x] Add placeholder documentation files under `docs/`.
- [x] Add `src/agentic_latex_book/__init__.py` (docstring only, no logic).
- [x] Add a professional `.gitignore` (Python, uv, venv, LaTeX artifacts, OS, IDE, logs, caches) that keeps sources, docs, and deliverables.
- [x] Preserve empty directories with `.gitkeep` markers.
- [x] Commit the skeleton (`a0f8734`) and push to GitHub.

### Stage 1 — PRD (Completed, `b501a36`)

Entry condition: Stage 0 done. Exit criteria: real PRD committed and pushed.

- [x] Write `docs/PRD.md` with all required sections (problem, goals, scope, requirements, acceptance criteria, traceability).
- [x] Add group identity (MaRs-777; Mohamed Awad, Rawey Sleiman) and group-submission wording.
- [x] Add the Moodle submission PDF deliverable (`MaRs-777-ex03.pdf`) as separate from the article PDF.
- [x] Add submission/GitHub access requirements (public or shared with rmisegal@gmail.com; correct Assignment 3 link).
- [x] Add the three submission rows to the traceability matrix.
- [x] Verify no Assignment 2 or wrong-exercise-number references remain.
- [x] Commit the PRD (`b501a36`) and push to GitHub with standard student authorship.

### Stage 2 — PLAN (Completed, `6baece3`)

Entry condition: Stage 1 done. Exit criteria: real technical PLAN committed and pushed.

- [x] Write `docs/PLAN.md` with all 27 required sections derived from the PRD.
- [x] Define architecture: agentic content layer + deterministic assembly/build/validation.
- [x] Define proposed agent roles, task graph, and artifact flow.
- [x] Define LaTeX, PDF build, graph, validation, evidence, cost, config, and security strategies.
- [x] Define the stage-by-stage roadmap and definition of done.
- [x] List open technical questions without guessing answers.
- [x] Verify no Assignment 2 or wrong-exercise-number references remain.
- [x] Commit the PLAN (`6baece3`) and push to GitHub with standard student authorship.

### Stage 3 — TODO (Completed, `a722f64`)

Entry condition: Stage 2 done and pushed. Exit criteria: this TODO is complete, reviewed, committed, and pushed.

- [x] Read `docs/PRD.md` and `docs/PLAN.md` and extract the work into staged tasks.
- [x] Write `docs/TODO.md` with the 11 required sections.
- [x] Include stages 0–16 matching the PLAN roadmap.
- [x] Mark Stages 0–2 completed with their commit hashes.
- [x] Provide at least 120 actionable checklist items.
- [x] Give each future stage clear entry conditions and exit criteria.
- [x] Self-review the TODO for vague tasks and remove any that are not executable as written.
- [x] Run the verification commands (`git diff`, `git status --short`, `wc -l`, checkbox count).
- [x] Confirm only `docs/TODO.md` changed and no code/deps/LaTeX/evidence were added.
- [x] Commit `docs/TODO.md` with a clear message and push to GitHub.

### Stage 4 — Supporting Documentation Before Code (Completed, `495f966`)

Entry condition: Stage 3 committed and pushed. Exit criteria: all doc files below are real (non-placeholder) and committed.

- [x] Write `docs/AI_WORKFLOW.md` describing how AI assistance is used across the project and how it is logged.
- [x] Write `docs/PROMPTS.md` with the prompt-capture format the pipeline will use (and seed it with the documentation-stage prompts).
- [x] Write `docs/DECISIONS.md` and record the first decisions (group setup, doc-first approach, deferral of dependencies to Stage 5).
- [x] Write `docs/COSTS.md` initial resource-awareness plan: what will be measured (runtime, tokens), how, and where summarized.
- [x] Write `docs/QUALITY.md` quality strategy: gates, tools, thresholds (page-count range, coverage target, file-length limit).
- [x] Write `docs/SUBMISSION_CHECKLIST.md` with the concrete Moodle + GitHub submission items.
- [x] Replace the root `README.md` placeholder with an initial professional version (overview, structure, planned usage, status).
- [x] Cross-link the documents (PRD ↔ PLAN ↔ TODO ↔ QUALITY ↔ COSTS) where helpful.
- [x] Verify no document overclaims production readiness or includes fake results.
- [x] Commit the documentation set in coherent increments and push.

### Stage 5 — Project Setup (Completed, `d21b3c7`)

Entry condition: Stage 4 done. Exit criteria: project installs/runs a CLI stub reproducibly; dependency choices recorded.

- [ ] Decide the concrete LLM provider/model for CrewAI — explicitly deferred in Stage 5 (see D-014); to resolve before the first real CrewAI execution (Stage 7/8).
- [ ] Decide the plotting library — explicitly deferred in Stage 5 (see D-015); to resolve by Stage 10.
- [x] Choose and record the initial test/lint tooling decision (pytest + ruff, and whether mypy is adopted) in `docs/DECISIONS.md`.
- [x] Create a minimal `pyproject.toml` configured for uv with project metadata.
- [x] Add the chosen runtime dependencies (CrewAI and required libraries) to `pyproject.toml`.
- [x] Add pytest and ruff as dev dependencies in `pyproject.toml`.
- [x] Add basic pytest configuration (test paths, options) when `pyproject.toml` is created.
- [x] Add basic ruff configuration (rules, target version) when `pyproject.toml` is created.
- [x] Create the uv environment and generate/commit the lock file.
- [x] Add a `.env.example` template listing required environment variables (no real secrets).
- [x] Add a project config file (e.g. topic, model, page-count thresholds, paths) under version control.
- [x] Create a CLI entry point stub (`src/agentic_latex_book/cli.py`) that parses arguments and prints planned steps.
- [x] Wire the CLI as a console script / runnable module.
- [x] Add a package import sanity check (import the package and run the CLI `--help`).
- [x] Establish the initial quality command sequence (`uv run pytest`, `uv run ruff check .`, `uv run ruff format --check .`) that runs lint + tests. (A single consolidated quality script/command remains future Stage 13 work; none exists yet.)
- [x] Add one trivial smoke test so the quality command has something to run.
- [x] Document the exact setup, run, and quality-command instructions in `README.md`.
- [x] Commit project setup and push.

### Stage 6 — Core Deterministic Foundation (Completed, `3e538af`)

Entry condition: Stage 5 done. Exit criteria: deterministic modules exist with passing unit tests; no agentic code yet.

- [x] Implement the configuration loader (`config.py`) that resolves settings from config file + environment.
- [x] Implement a paths/constants module centralizing repository paths (`results/`, `latex_project/`, `assets/`).
- [x] Implement the evidence writer that creates per-run output locations under `results/`.
- [x] Implement structured logging that writes run logs to `results/logs/`.
- [x] Implement the cost/runtime tracker (timing now; token capture wired for later).
- [x] Ensure no secret values are ever written to logs or evidence.
- [x] Keep each module short and single-responsibility (respect the file-length limit).
- [x] Write unit tests for the config loader (valid, missing, and override cases).
- [x] Write unit tests for the paths/constants module.
- [x] Write unit tests for the evidence writer (creates expected structure).
- [x] Write unit tests for the cost/runtime tracker (records elapsed time).
- [x] Run pytest and confirm the test suite passes.
- [x] Run ruff lint/format checks and resolve any findings.
- [x] Run the quality command sequence (`uv run pytest`, `uv run ruff check .`, `uv run ruff format --check .`) and confirm it passes. (No single consolidated script exists yet; this is the command sequence.)
- [x] Commit the deterministic foundation and push.

### Stage 7 — CrewAI Core (Completed, `aeb39dc`)

Entry condition: Stage 6 done. Exit criteria (offline scope): offline agent/task specs, structured output-schema specs, a validated dry-run blueprint, a non-executing object builder, the `crew-plan` CLI command, and offline tests — all with no real crew run, no `kickoff`, and no LLM/API call. A real crew run and evidence persistence are explicitly out of Stage 7 scope (deferred below).

- [x] Define agent roles (planner/outliner, writer, reviewer/editor, reference curator) in small per-role modules.
- [x] Define task definitions for outline, drafting, review, and references.
- [x] Define structured output-schema specs for each task (offline dataclass contracts; not Pydantic, not yet LLM-enforced).
- [x] Implement the crew builder that assembles agents + tasks + process (sequential), with spec/schema validation and a dry-run blueprint.
- [x] Configure the crew process as sequential by default (parallelism deferred per PLAN open question 3).
- [x] Add the safe offline `crew-plan` CLI command and offline tests for specs, schemas, blueprint, and validation.
- [x] Add a smoke test that builds the crew object without executing a paid run (no `kickoff`).
- [x] Commit the CrewAI core and push.

Deferred to the controlled-run stage (Stage 8 wiring / Stage 14 real run), not Stage 7:

- [ ] Persist each intermediate crew output to `results/crew_outputs/` (needs a real run).
- [ ] Capture prompts used by each agent during runs into the prompts log (needs a real run).
- [ ] Record token/cost usage from the provider where exposed, via the cost tracker (needs a real run).
- [ ] Run a minimal real crew invocation to confirm wiring and output persistence (needs a chosen provider/model and credentials; see D-014, D-017).

### Stage 8A — Controlled-Run Scaffolding (Completed, `d9acbf7`)

Entry condition: Stage 7 done. Exit criteria (offline scope): safe `run-minimal` scaffolding with an explicit `--real` gate, an OpenAI-only LLM resolver that reads secrets from `os.environ` only, evidence/cost metadata format, and offline tests — with no real run, no `kickoff`, no LLM/API call, and `results/` still holding only `.gitkeep`.

- [x] Add config helpers `is_model_configured()` / `require_model_config()` (offline config still valid).
- [x] Add `crew/llm.py`: `resolve_llm()` (OpenAI-only, env-only secrets, never logs the key) and `describe_llm_environment()` (presence booleans only).
- [x] Add `crew/runner.py`: `run_minimal()` — dry-run by default (no LLM, no run, no files); single `kickoff` confined to the explicit `real=True` path; safe failure when unconfigured.
- [x] Add the `run-minimal` CLI command with `--dry-run` (default), `--real`, and `--run-id`.
- [x] Add offline tests for config helpers, LLM resolution, dry-run safety, no-file guarantee, and CLI gates.
- [x] Record D-018 (OpenAI-only provider strategy) and D-019 (controlled-run safety gates); document the run-cost metadata format in `docs/COSTS.md`.
- [x] Commit the controlled-run scaffolding and push.

#### Stage 8A.1 — Add Gemini Provider Support (Completed, `a31f80a`; offline)

The student has a Gemini key, not OpenAI. This sub-stage adds Gemini support to the
resolver while staying fully offline — no real run, no `kickoff`, no LLM/API call,
and no dependency added (see decision D-020).

- [x] Extend `resolve_llm` to support `provider = "gemini"` (alongside `openai`), reading `GEMINI_API_KEY` (preferred) or `GOOGLE_API_KEY` from `os.environ`; raw key never logged/returned.
- [x] Keep `describe_llm_environment` safe (presence booleans only; `base_url_present` is `False` for Gemini).
- [x] Add offline tests: Gemini metadata for both key vars (no leak), and a safe failure when no Gemini key is set; document why Gemini construction is not unit-tested (needs `crewai[google-genai]`).
- [x] Record D-020 and note the recommended Gemini model string `gemini/gemini-2.5-flash`.
- [x] Commit the Gemini provider support and push.

#### Stage 8B.0 — Install the Gemini Provider Dependency (Completed, `7e28f01`; offline)

Dependency-only sub-stage: install `crewai[google-genai]` so a Gemini `LLM` can be
constructed. Still fully offline — no real run, no `kickoff`, no LLM/API call, no
evidence (see decision D-021).

- [x] Run `uv add "crewai[google-genai]"` (updates the single dependency to `crewai[google-genai]>=0.80`; refreshes `uv.lock`).
- [x] Verify a Gemini `LLM` now constructs offline with a fake key (no model call) and add the offline construction test.
- [x] Record D-021; note no real Gemini call/cost occurred.
- [x] Commit the Gemini provider dependency and push.

#### Stage 8B.1 — First Real Minimal Gemini Run (Completed, `81e5b26`)

The student executed a single controlled minimal run (`run-minimal --real`) against
`gemini/gemini-2.5-flash` in their own terminal with their own key, reviewed the
evidence for secrets, and committed it.

- [x] Execute one real minimal Gemini run (`gemini/gemini-2.5-flash`); a single `kickoff`, no loops, no retries.
- [x] Review the run evidence; confirm the secret scan is clean (only presence booleans, no raw key).
- [x] Commit the four evidence files under `results/stage8b1-minimal-gemini-20260611-154559/` and push (`81e5b26`).
- [x] Record the measured runtime/token data in `docs/COSTS.md` (3.18s; 85 prompt + 33 completion tokens).

Evidence: `results/stage8b1-minimal-gemini-20260611-154559/` (`runtime.json`, `logs/run.log`, `crew_outputs/minimal_task.txt`, `validation_reports/run_note.md`). This proves the agentic path works at minimal scale only — **no LaTeX, no PDF, and no full content-generation run exist yet**.

#### Stage 8C.1 — Offline Full Content-Pipeline Scaffolding (Completed, `20e1774`)

Offline scaffolding for the full pipeline runner — no real run, no `kickoff` at
runtime, no LLM/API call, no evidence (see decision D-023).

- [x] Add `crew/full_runner.py` (`run_full`, dry-run default) and `crew/persist.py` (per-task evidence writer).
- [x] Add the `run-full` CLI command with mutually-exclusive `--dry-run`/`--real` and `--run-id`.
- [x] Add offline tests: dry-run no-file, gating conflict (exit 2), safe failure when unconfigured, ordered task output mapping, and fake persistence (all files + schema names, no secrets).
- [x] Confirm exactly two `kickoff` calls exist, both in real-only paths (minimal + full runners).
- [x] Record D-023.
- [x] Commit the offline full-pipeline scaffolding and push.

#### Stage 8C.3 / 8C.4 — First Real Full Gemini Run + Evidence (Completed, `cf89e51`)

The student executed one real full run; all four tasks produced output, committed as
diagnostic evidence under `results/stage8c3-full-gemini-20260611-164153/`.

- [x] Execute one real full run (`gemini/gemini-2.5-flash`); ~249 s; 153,748 prompt + 200,472 completion tokens.
- [x] Review the evidence; secret scan clean (presence booleans only, no raw key).
- [x] Commit the eight evidence files (8C.4, `cf89e51`).
- [x] Record the content-quality verdict: **rejected for final PDF** — wrong topic ("Gradient Descent"), placeholder author/date, and only ~10 pages (per the review output).

#### Stage 8C.5 — Documentation After the Rejected Run (Completed, `c2127f2`)

- [x] Record the run cost/resource data in `docs/COSTS.md` (real run row).
- [x] Update `docs/QUALITY.md`: full runner technically passed; content rejected; no PDF/LaTeX gate yet; no accepted content yet.
- [x] Record D-024 (reject first full content; harden topic/prompt controls before another run).
- [x] Commit the documentation update and push.

#### Stage 8C.6 — Offline Topic/Metadata Hardening (Completed, `0858c44`)

Bind the crew to the configured topic and real cover metadata before a second run —
offline only, no real run, no `kickoff`, no LLM/API call, no evidence (see D-025).

- [x] Add project metadata to the config (`authors`, `assignment_context`, `project_date`) with strict validation; set the topic to the assignment topic.
- [x] Add `crew/context.py` (`ProjectContext`) and `crew/instructions.py` (context-bound task instructions forbidding wrong topics, placeholders, stale dates, and short length).
- [x] Bind `build_task_specs(context)` / `build_crew(llm, context)` / `crew_blueprint(context)` and the full runner to the configured context.
- [x] Add `crew/content_checks.py` (offline helper flagging forbidden terms, placeholders, off-topic text, and missing mandatory elements).
- [x] Add offline tests (config metadata validation, topic binding in blueprint/instructions, content checks); confirm exactly two `kickoff` calls remain (both real-only paths).
- [x] Record D-025.
- [x] Commit the offline hardening and push (`0858c44`).

#### Stage 8C.7 — Second Real Full Gemini Run + Candidate Evidence (Completed, `0611993`)

The student executed a second real full run after the 8C.6 hardening; all four
tasks produced output, committed as **candidate** evidence under
`results/stage8c7-full-gemini-20260611-173125/`.

- [x] Execute one real full run (`gemini/gemini-2.5-flash`); ~300.7 s; 213,664 prompt + 235,436 completion tokens.
- [x] Run the offline `content_checks` gate: on-topic, no forbidden terms, no placeholders, no missing mandatory elements (basic gate passes).
- [x] Confirm the previous failure modes are fixed (no Gradient Descent topic, no `[Your Name]` placeholder, no stale date; correct group/authors/topic appear).
- [x] Commit the eight evidence files (`0611993`).
- [x] Record the verdict: **candidate content accepted, not final PDF-ready** — remaining risks: conceptual-only headers/footers, questionable `example.com` citations, unsupported metrics (185 minutes / 99.1% / 1.8M tokens), GPT-4o references despite the Gemini run, and "Internal Publication" citations.

#### Stage 8C.8.0 — Content QA Cleanup Plan (Completed, `dd18878`; plan only)

Deterministic / human-reviewed cleanup of the Stage 8C.7 candidate into final source
content, before LaTeX assembly. See decision D-027. **Plan only — no cleaned content,
LaTeX, or PDF is created here; the candidate evidence stays immutable; no real run.**

**Evidence immutability:** `results/stage8c7-full-gemini-20260611-173125/` must remain
unchanged. Cleaned content is a *derived* artifact created later under
`latex_project/content/` (chosen so the cleaned source lives inside the LaTeX project
that builds the PDF; D-027), never by editing the evidence.

**Cleanup rules (applied later, to the derived content):**

- [ ] Replace fake-looking bibliography links with real, verified sources or remove them; no `*.example.com`.
- [ ] Replace `crewai-docs.example.com` only with a verified official CrewAI source; otherwise remove.
- [ ] Remove `mars777.example.com` unless replaced by a real project file/reference.
- [ ] Remove/rewrite "Internal Publication" references unless the referenced file exists in the repo and is linked as project evidence.
- [ ] Replace unsupported metrics with measured values from committed runtime evidence (8C.7: provider/model Gemini `gemini/gemini-2.5-flash`, `elapsed_seconds` 300.68034328000067, `prompt_tokens` 213664, `completion_tokens` 235436).
- [ ] Convert "185 minutes" / "99.1%" / "1.8M tokens" into either clearly-labelled *proposed* evaluation metrics, or remove them.
- [ ] Replace GPT-4o-specific wording with neutral "LLM" wording, or Gemini-specific wording only where grounded by the actual run.
- [ ] Keep the core topic, authors, group code, date, BiDi section, table, formula, graph concept, and architecture content; headers/footers become real LaTeX (not prose).
- [ ] Keep the page target around 13–17 final PDF pages.

**Citation policy:** prefer course materials already in the project; official docs for
CrewAI / LaTeX / CTAN / polyglossia / bidi / XeLaTeX / LuaLaTeX where needed; project
evidence files for measured runtime/token claims. No fake URLs, no fabricated reports,
no invented internal publications; any external source is verified before final use.

**Deterministic checks (offline scanner, Stage 8C.8.1) over the Stage 8C.8.2 cleaned content — all passing:**

- [x] no `example.com`; no `Internal Publication`; no `185 minutes` / `99.1%` / `1.8M tokens`; no unsupported `GPT-4o Technical Report`.
- [x] no old-failure topic/placeholders; required topic present; group/authors/date present.
- [x] mandatory PDF elements present; measured runtime/token values present correctly (from the 8C.7 `runtime.json`) with unmeasured metrics labelled as proposed; bibliography uses conservative real/project-local references, no fake-looking links.

**Staged plan after this:**

- [x] Stage 8C.8.1 — implement the deterministic offline QA scanner for candidate/cleaned content (`content_qa.py`, `content-qa` CLI, offline tests). The committed Stage 8C.7 candidate **fails** the scanner on its known risks (example.com, 185 minutes/99.1%/1.8M tokens, GPT-4o Technical Report, conceptual headers/footers); a clean sample passes. (Committed and pushed: `dcac0eb`.)
- [x] Stage 8C.8.2 — created cleaned Markdown content under `latex_project/content/` (`book.md`, `README.md`) from the candidate, preserving evidence immutability; passes `content-qa` (`ok: True`, exit 0). (Committed and pushed: `98a50f2`.)
- [x] Stage 8C.8.3 — reviewed the cleaned content (scanner green, human review with minor citation/source fixes) and committed/pushed it (`98a50f2`).
- [x] Stage 9.0 — LaTeX assembly plan (docs only; D-030). (Committed and pushed: `c3ca705`.)
- [x] Stage 9.1 — LaTeX skeleton + bibliography (no compile — TeX Live not installed; no PDF). (Committed and pushed: `af71265`.)
- [ ] Stages 9.2–9.6 — LaTeX assembly implementation (see the Stage 9.0 plan section below).
- [ ] Later — PDF compile + validation gates.

### Stage 8C — Content Planning and Generation

Entry condition: Stage 8A scaffolding done and a real minimal run (8B) confirmed. Exit criteria: the crew produces an outline, drafts, a reviewed draft, and a reference/citation map for the topic.

- [ ] Implement outline generation sized for ~15 pages, including where each mandatory element will live.
- [ ] Implement chapter/section drafting that follows the outline and target lengths.
- [ ] Implement the review/edit pass that checks coherence, length, and mandatory-element coverage.
- [ ] Implement reference/citation-map generation (entries + in-text citation points).
- [ ] Implement the bounded re-draft policy (limited iterations before failing) per PLAN §20.
- [ ] Ensure the outline explicitly assigns the image, graph, table, formula, BiDi section, and bibliography.
- [ ] Persist outline, drafts, review notes, and references to `results/crew_outputs/`.
- [ ] Manually review one generated outline+draft for sanity (length and coverage).
- [ ] Record content-generation decisions in `docs/DECISIONS.md`.
- [ ] Commit content planning/generation and push.

### Stage 9.0 — LaTeX Assembly Plan (plan only; D-030)

Converts the committed cleaned Markdown (`latex_project/content/book.md`, `98a50f2`) into a polished ~15-page article PDF. This section is the roadmap; nothing below exists yet (no `.tex`, no `.bib`, no images, no scripts, no PDF). Design decisions and rationale are recorded in D-030.

**Proposed structure** (under `latex_project/`; `content/` stays the immutable cleaned source):

```
latex_project/
├── main.tex          # document class, includes, titlepage, \tableofcontents
├── preamble.tex      # packages, fonts, polyglossia/bidi, fancyhdr, listings, biblatex
├── chapters/         # 00-abstract.tex, 01-introduction.tex … 08-conclusion.tex
├── figures/          # architecture diagram + Python-generated graph (created in 9.2)
├── scripts/          # generate_architecture.py, generate_graph.py (created in 9.2)
├── references.bib    # transcribed from book.md bibliography only (created in 9.1)
├── build/            # compile output (already gitignored)
├── README.md         # build prerequisites + exact commands (created in 9.1)
└── content/          # cleaned Markdown source — never edited by assembly
```

**Engine and fonts:** XeLaTeX + `fontspec` + `polyglossia` (loads `bidi` for Hebrew); main font DejaVu Sans — verified installed and Hebrew-capable (`fc-list :lang=he`); LuaLaTeX is the fallback. TeX Live is **not installed yet** — installing `texlive-xetex`, `texlive-latex-extra`, `texlive-bibtex-extra`, `biber`, `fonts-dejavu` (system packages, no repo change) is the Stage 9.1 entry step, plus a font-availability check before any compile.

**Packages (minimal):** `geometry` (a4, ~2.5 cm margins), `fontspec`, `polyglossia`, `amsmath`, `booktabs`, `graphicx`, `fancyhdr`, `listings`+`xcolor`, `biblatex` (biber backend, numeric), `hyperref` last.

**Mapping from `book.md`:** cover page → `titlepage` with title/group `MaRs-777`/authors/course/lecturer/date; the "Mandatory PDF Elements", "Note on headers and footers", and hand-written ToC sections are assembly instructions — not typeset; ToC → `\tableofcontents`; `## n.`→`\chapter`, `### n.m`→`\section`; the two tables → `booktabs`; the two equations → `equation` environments; code blocks → `listings`; ASCII pipeline diagram → generated architecture figure; BiDi snippet → an actually rendered Hebrew–English passage; `[n]` markers → `\cite{key}` (numbers regenerated by biblatex). No manual page numbers; all numbering is automatic.

**Figures (Stage 9.2):** both Python-generated to `figures/` by scripts under `scripts/` run with `uv run --with matplotlib python …` (no dependency change): the Chapter 3 architecture diagram (chosen over TikZ for first-compile safety; D-030) and the Chapter 6 illustrative graph (the script already shown in `book.md` §6.2, labelled illustrative).

**Headers/footers (Stage 9.1):** `fancyhdr` — short title in header, `MaRs-777` opposite, automatic page numbers in footer; `plain` on chapter pages.

**Page target 13–17:** `report`/11pt/a4/2.5 cm margins; tune figure widths (0.7–0.9`\textwidth`) and listing font size at 9.5; no artificial padding.

**Build sequence (executed only from Stage 9.4 on):**

```
uv run --with matplotlib python latex_project/scripts/generate_architecture.py
uv run --with matplotlib python latex_project/scripts/generate_graph.py
cd latex_project
xelatex -interaction=nonstopmode -halt-on-error -output-directory=build main.tex
biber build/main
xelatex -interaction=nonstopmode -halt-on-error -output-directory=build main.tex
xelatex -interaction=nonstopmode -halt-on-error -output-directory=build main.tex
```

**Validation gates (Stage 9.5; deterministic, see QUALITY.md):** compile exits 0; `build/main.pdf` exists; page count 13–17; pdftotext contains title/authors/group/date; ToC present; no `??` / no "Citation … undefined" / no "Reference … undefined" in output or log; bibliography section present; both figure files exist and are included; table + formulas + Hebrew BiDi text present in the PDF text layer; overfull `\hbox` warnings above ~50 pt: zero; the content-qa risk strings stay absent from the `.tex` sources; `content-qa latex_project/content/` stays green as the pre-assembly gate.

**Sub-stages:**

- [x] 9.0 — this plan (docs only). (Committed and pushed: `c3ca705`.)
- [~] 9.1 — LaTeX skeleton + bibliography setup (font check done — DejaVu Sans confirmed via `fc-match`; `main.tex`/`preamble.tex`/`chapters/` stubs, `references.bib`, fancyhdr, titlepage, `latex_project/README.md` created; committed and pushed: `af71265`). **Environment limitation:** TeX Live is still not installed (`xelatex`/`biber` absent), so no syntax-check compile was attempted; the install command is documented in `latex_project/README.md` and runs before Stage 9.4.
- [~] 9.2 — figure/graph generation scripts + generated images under `figures/` (two deterministic matplotlib scripts run via `uv run --with matplotlib` — no dependency change; `architecture.png` 611×928, `generation_time.png` 1200×750, both PNG; graph values labelled illustrative, not measured; chapter figure blocks uncommented to reference the existing PNGs; includes the Agg-backend-before-pyplot hardening fix; committed and pushed: `6aa2cf1`).
- [ ] 9.3 — convert cleaned Markdown into LaTeX chapters (full mapping above) (**next stage**).
- [ ] 9.4 — first compile; fix compile errors (build sequence above).
- [ ] 9.5 — PDF validation and polish (gates above; 13–17 pages).
- [ ] 9.6 — commit final LaTeX sources + PDF evidence (final PDF to `results/final_pdf/` per Stage 11).

These sub-stages absorb the older Stage 9/10/11/12 checklists below: 9.1/9.3 ≈ Stage 9, 9.2 ≈ Stage 10 (figures under `latex_project/figures/`, not `assets/`; D-030), 9.4/9.6 ≈ Stage 11, 9.5 ≈ Stage 12 gates. The original checklist items are ticked as the matching sub-stage completes.

### Stage 9 — LaTeX Assembler

Entry condition: Stage 8 done. Exit criteria: approved content assembles into an organized `latex_project/` that contains every mandatory structural element.

- [ ] Design the `latex_project/` structure (main + chapters + refs + style/preamble).
- [ ] Implement the assembler that converts structured content into LaTeX sources.
- [ ] Create `main.tex` that includes the chapter files and sets document class/options.
- [ ] Generate per-chapter `.tex` files from the drafted content.
- [ ] Implement the cover page (topic, author(s) = group members, course, lecturer, date).
- [ ] Enable the table of contents.
- [ ] Configure running headers/footers with page numbering.
- [ ] Insert at least one table with real structured data.
- [ ] Insert at least one mathematical formula.
- [ ] Set up the bibliography with a managed references file and linked in-text citations.
- [ ] Implement the Hebrew–English BiDi section as an isolated chapter/section.
- [ ] Ensure agent text is escaped/mapped so it does not break LaTeX compilation.
- [ ] Keep build artifacts out of Git (rely on `.gitignore`).
- [ ] Commit the LaTeX assembler and generated sources and push.

### Stage 10 — Python-Generated Graph and Assets

Entry condition: Stage 9 done. Exit criteria: a Python-generated graph and an authored image are integrated and referenced in the LaTeX sources.

- [ ] Implement the figure generator that creates at least one graph from Python code.
- [ ] Write the generated graph image to `assets/generated/`.
- [ ] Add at least one authored image under `assets/figures/`.
- [ ] Keep authored vs generated assets clearly separated so the "Python-generated" requirement is provable.
- [ ] Reference the generated graph from the LaTeX sources so it appears in the PDF.
- [ ] Reference the authored image from the LaTeX sources.
- [ ] Make the figure generator deterministic/reproducible where practical.
- [ ] Add a test that the figure generator produces the expected output file.
- [ ] Commit the graph generator and assets and push.

### Stage 11 — PDF Build

Entry condition: Stage 10 done. Exit criteria: the LaTeX project compiles via a pinned script and the article PDF lands in `results/final_pdf/`.

- [ ] Decide the LaTeX engine (BiDi-capable, e.g. XeLaTeX/LuaLaTeX) and record it in `docs/DECISIONS.md` (resolves PLAN open question 2).
- [ ] Implement the PDF builder wrapping a single pinned build command/engine.
- [ ] Create a build script under `scripts/` that compiles the project reproducibly.
- [ ] Handle multi-pass compilation needed for ToC and bibliography/citations.
- [ ] Treat a failed compilation as a hard, non-zero failure.
- [ ] Write build artifacts to a working/build directory that is gitignored.
- [ ] Copy the final compiled PDF to `results/final_pdf/`.
- [ ] Document the build prerequisites and command in `README.md`.
- [ ] Verify the BiDi section renders correctly in the produced PDF.
- [ ] Commit the build script/builder and push.

### Stage 12 — Validation Gates

Entry condition: Stage 11 done. Exit criteria: all mandatory gates run, pass on the real PDF, and write reports.

- [ ] Implement the build gate (LaTeX compiles successfully).
- [ ] Implement the page-count gate (PDF ~15 pages; threshold recorded in `docs/QUALITY.md`).
- [ ] Implement the cover-page gate (topic, author(s), course, lecturer, date present).
- [ ] Implement the table-of-contents gate.
- [ ] Implement the structure gate (multiple chapters/sections present).
- [ ] Implement the header/footer gate (running headers/footers and page numbers).
- [ ] Implement the image gate (at least one image present).
- [ ] Implement the Python-generated-graph gate.
- [ ] Implement the table gate (at least one table present).
- [ ] Implement the formula gate (at least one math formula present).
- [ ] Implement the BiDi gate (Hebrew–English section present and rendered).
- [ ] Implement the bibliography/citation-link gate (references present with linked citations).
- [ ] Implement the repository gate (README, PRD, PLAN, TODO, `latex_project/`, `results/` present).
- [ ] Make each gate an independent check so new gates can be added without touching others.
- [ ] Write machine- and human-readable reports to `results/validation_reports/`.
- [ ] Ensure any failing mandatory gate causes a reported failure (no silent pass).
- [ ] Commit the validation gates and reports tooling and push.

### Stage 13 — Testing and Quality Hardening

Entry condition: Stage 12 done. Basic pytest, ruff, and the initial quality command already exist from Stage 5 and have been run each stage since Stage 6; this stage hardens and finalizes them rather than introducing them. Exit criteria: coverage, file-length, optional mypy, and the consolidated quality command all pass from a clean checkout.

- [ ] Review and consolidate the existing pytest configuration and test organization under `tests/`.
- [ ] Review and tighten the existing ruff rules for the now-complete codebase.
- [ ] Finalize the mypy decision; if adopted, configure it and resolve type issues across the codebase.
- [ ] Set and enforce a coverage target; measure coverage and close important gaps.
- [ ] Add a file-length check enforcing short, maintainable Python files (record the limit in `docs/QUALITY.md`).
- [ ] Harden the local quality command to run lint + types (if adopted) + tests + coverage + length check.
- [ ] Document the final quality command and all thresholds in `docs/QUALITY.md`.
- [ ] Decide whether to add a CI workflow that runs the same checks; record the decision.
- [ ] Validate that the consolidated quality command passes from a clean checkout.
- [ ] Commit the quality hardening and push.

### Stage 14 — Real End-to-End Run and Evidence

Entry condition: Stage 13 done. Exit criteria: one full real run produces the PDF plus real evidence; nothing fabricated.

- [ ] Run the full CrewAI pipeline end-to-end from the CLI on the chosen topic.
- [ ] Collect execution logs into `results/logs/`.
- [ ] Collect raw crew outputs into `results/crew_outputs/`.
- [ ] Produce the article PDF into `results/final_pdf/`.
- [ ] Run all validation gates and collect reports into `results/validation_reports/`.
- [ ] Collect cost/runtime data and record it (for `docs/COSTS.md`).
- [ ] Confirm the PDF satisfies every mandatory element (PDF-1…PDF-11).
- [ ] Verify all committed evidence comes from this/real runs (no placeholders or fabricated files).
- [ ] If any gate fails, fix and re-run rather than editing evidence by hand.
- [ ] Commit the real evidence and push.

### Stage 15 — Final Documentation Hardening

Entry condition: Stage 14 done with passing gates. Exit criteria: all docs reflect the real system and link claims to evidence.

- [ ] Update `README.md` with the final overview, reproduction steps, and results summary.
- [ ] Update `docs/AI_WORKFLOW.md` to reflect the actual workflow used.
- [ ] Update `docs/PROMPTS.md` with the prompts actually used.
- [ ] Update `docs/DECISIONS.md` with all final decisions and dates.
- [ ] Update `docs/COSTS.md` with measured runtime/token data and stated assumptions.
- [ ] Update `docs/QUALITY.md` with the final gates, tools, thresholds, and results.
- [ ] Update `docs/SUBMISSION_CHECKLIST.md` to its final state.
- [ ] Link every important claim to a specific evidence file under `results/`.
- [ ] Re-check that nothing overclaims production readiness; state limitations honestly.
- [ ] Commit documentation hardening and push.

### Stage 16 — Final Submission Preparation

Entry condition: Stage 15 done. Exit criteria: repository is share-ready and the Moodle PDF is prepared and submitted.

- [ ] Verify the GitHub repository is public or shared with rmisegal@gmail.com.
- [ ] Verify the submitted GitHub link points to `ai-agent-latex-book-assignment3` (not Assignment 2).
- [ ] Prepare `MaRs-777-ex03.pdf` from the official Word template.
- [ ] Ensure `MaRs-777-ex03.pdf` contains exercise number 03, group code MaRs-777, the Assignment 3 GitHub link, and the final self-assessment score.
- [ ] Decide the final self-assessment score with the group and justify it against the rubric.
- [ ] Perform final repository cleanup (no stray artifacts, no secrets, no fake outputs).
- [ ] Confirm the commit history is incremental and meaningful.
- [ ] Do the final push and confirm `origin/main` is up to date.
- [ ] Submit `MaRs-777-ex03.pdf` on Moodle.
- [ ] Record submission completion in `docs/SUBMISSION_CHECKLIST.md`.

---

## 6. Quality Gates Per Stage

| Stage | Quality gate(s) that must hold before exit |
| --- | --- |
| 0–3 | Each doc/skeleton change committed and pushed; no Assignment 2 or wrong-exercise-number references; standard student authorship. |
| 4 | All listed docs are real (non-placeholder); no overclaiming; no fake results. |
| 5 | `pyproject.toml` valid; environment builds; CLI `--help` runs; dependency decisions recorded. |
| 6 | Unit tests for config/evidence/cost/paths pass; no secrets in logs; files within length limit. |
| 7 | Specs/schemas/blueprint validate; crew object construction smoke test passes; no `kickoff`/LLM/API; no generated evidence. |
| 8 | Outline assigns all mandatory elements; bounded re-draft policy in place; outputs persisted. |
| 9 | LaTeX project organized; all mandatory structural elements present in sources. |
| 10 | Python-generated graph and authored image produced and referenced in LaTeX. |
| 11 | LaTeX compiles via pinned script; final PDF copied to `results/final_pdf/`; BiDi renders. |
| 12 | All mandatory gates implemented and passing on the real PDF; reports written; fail-loud verified. |
| 13 | Lint + (types) + tests + coverage + file-length check pass via one command. |
| 14 | Full real run completes; PDF meets PDF-1…PDF-11; evidence is real, not fabricated. |
| 15 | All docs updated; every important claim linked to evidence; limitations stated. |
| 16 | Repo shared/public; correct A3 link; `MaRs-777-ex03.pdf` complete; final push done. |

---

## 7. Evidence Expected Per Stage

| Stage | Evidence produced (location) |
| --- | --- |
| 0 | Skeleton commit `a0f8734` on `main`. |
| 1 | `docs/PRD.md`; commit `b501a36`. |
| 2 | `docs/PLAN.md`; commit `6baece3`. |
| 3 | `docs/TODO.md`; this stage's commit. |
| 4 | Populated `docs/*.md` and `README.md`; commits. |
| 5 | `pyproject.toml`, lock file, `.env.example`, config, CLI stub; commit. |
| 6 | Deterministic modules + passing tests; test output. |
| 7 | Code/tests/docs only: crew specs, schema specs, blueprint, `crew-plan` CLI, passing tests. Real crew outputs deferred to the Stage 8/14 controlled run. |
| 8 | Outline/draft/review/references in `results/crew_outputs/`. |
| 9 | `latex_project/` sources with all mandatory elements. |
| 10 | `assets/generated/` graph + `assets/figures/` image; LaTeX references. |
| 11 | Article PDF in `results/final_pdf/`; build script. |
| 12 | Validation reports in `results/validation_reports/`. |
| 13 | Passing quality-command output; coverage report. |
| 14 | Real run logs, crew outputs, validation reports, final PDF, cost data — all under `results/`. |
| 15 | Updated docs with explicit links to the above evidence. |
| 16 | `MaRs-777-ex03.pdf`; submission record; final `origin/main` state. |

Evidence is committed only after a real run produces it. Until a stage runs for real, `results/` holds only `.gitkeep` markers.

---

## 8. Commit / Push Policy

- [ ] Commit at meaningful increments (per stage or per coherent sub-task), never in a single final dump.
- [ ] Use clear, descriptive commit messages in standard student style.
- [ ] Never add Claude/AI/bot/co-author/generated-by metadata to commits or files.
- [ ] Keep `main` buildable; avoid committing broken intermediate states where avoidable.
- [ ] Never commit secrets, `.env` files, or transient build artifacts.
- [ ] Never commit fabricated outputs or evidence.
- [ ] Push after each stage so `origin/main` stays current and the history is visible.

---

## 9. Definition of Done

The project is done when all of the following hold (mirrors PRD §18 and PLAN §26):

- [ ] A single, reproducible command sequence runs the CrewAI pipeline and produces the final PDF.
- [ ] The final PDF satisfies every mandatory element PDF-1…PDF-11, confirmed by validation reports.
- [ ] The PDF is approximately 15 pages.
- [ ] The LaTeX project that produced the PDF is present in `latex_project/`.
- [ ] `README.md`, `docs/PRD.md`, `docs/PLAN.md`, and `docs/TODO.md` are real, non-placeholder documents.
- [ ] Evidence under `results/` exists and comes from real runs.
- [ ] Cost/resource usage is recorded and summarized in `docs/COSTS.md`.
- [ ] The repository has a meaningful, incremental commit history on GitHub.
- [ ] AI-assisted workflow, prompts, and decisions are documented.
- [ ] No fabricated evidence and no overclaiming of production readiness are present.
- [ ] The repository is public or shared with rmisegal@gmail.com, with the correct Assignment 3 link.
- [ ] `MaRs-777-ex03.pdf` is prepared from the official template and submitted on Moodle.

---

## 10. Final Submission Checklist

- [ ] Final article PDF present in `results/final_pdf/` and passing all gates.
- [ ] LaTeX sources present and building under `latex_project/`.
- [ ] README, PRD, PLAN, TODO complete and consistent.
- [ ] Supporting docs (AI_WORKFLOW, PROMPTS, DECISIONS, COSTS, QUALITY, SUBMISSION_CHECKLIST) complete.
- [ ] Real evidence under `results/` (logs, crew outputs, validation reports, final PDF).
- [ ] Cost/runtime data recorded honestly in `docs/COSTS.md`.
- [ ] Quality command passes from a clean checkout.
- [ ] No secrets, no fake outputs, no stray build artifacts in the repo.
- [ ] GitHub repository public or shared with rmisegal@gmail.com.
- [ ] Submitted GitHub link points to `ai-agent-latex-book-assignment3`.
- [ ] `MaRs-777-ex03.pdf` created from the official Word template with all required fields.
- [ ] Final self-assessment score decided and included in `MaRs-777-ex03.pdf`.
- [ ] `MaRs-777-ex03.pdf` submitted on Moodle.
- [ ] `origin/main` up to date after the final push.

---

## 11. Open Blockers / Unresolved Decisions

These carry over from `docs/PLAN.md` §27 and must be resolved at the stage noted; none are guessed here.

- [ ] LLM provider/model for CrewAI and its cost/token-exposure characteristics — deferred in Stage 5 (see D-014); resolve before the first real CrewAI execution (Stage 7/8).
- [ ] LaTeX engine + BiDi package combination most reliable for Hebrew–English (resolve by Stage 9/11).
- [ ] Sequential vs parallel chapter drafting (resolve by Stage 8).
- [ ] Exact page-count threshold for the page-count gate, e.g. 13–17 (resolve by Stage 12).
- [ ] Python plotting library for the generated graph — deferred in Stage 5 (see D-015); resolve by Stage 10 (graph generation).
- [ ] Per-gate detection methods (PDF text extraction vs source inspection) and their robustness (resolve by Stage 12).
- [ ] Reference sourcing: hand-curated vs agent-assembled with human review; how citation linking is verified (resolve by Stage 8/12).
- [ ] Test framework + quality tooling final selection, recorded in `docs/QUALITY.md` (resolve by Stage 5/13).
- [ ] Bound on re-draft iterations balancing quality against cost (resolve by Stage 8).
- [ ] Whether to add CI for the quality command (resolve by Stage 13).
