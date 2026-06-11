# TODO — Staged Task Plan

## 1. Title and Document Status

**Project:** From PoC to Production — A CrewAI Multi-Agent Pipeline that Generates a ~15-Page Article/Book as a Polished LaTeX PDF.

**Repository:** `ai-agent-latex-book-assignment3`

**Group:** MaRs-777 (Mohamed Awad, Rawey Sleiman). Mohamed Awad is the current repository maintainer.

**Document status:** Draft — Stage 3 (TODO). This is a task plan only. Stages 0–2 are complete; Stage 3 is in progress; Stages 4–16 are future work and contain no implementation yet. The plan derives strictly from `docs/PRD.md` and `docs/PLAN.md`. Changes are tracked through normal Git history.

**Last updated:** 2026-06-11.

---

## 2. Current Project State

- [x] Stage 0 — Repository skeleton committed and pushed (`a0f8734`).
- [x] Stage 1 — PRD committed and pushed (`b501a36`).
- [x] Stage 2 — PLAN committed and pushed (`6baece3`).
- [ ] Stage 3 — TODO in progress (this document).
- [ ] Stages 4–16 — not started; no implementation code, dependencies, or LaTeX exist yet.

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
| 3 | TODO | In progress | Stage 2 done | `docs/TODO.md` |
| 4 | Supporting documentation before code | Not started | Stage 3 done | Doc set populated |
| 5 | Project setup (uv, deps, CLI skeleton) | Not started | Stage 4 done | `pyproject.toml`, runnable CLI stub |
| 6 | Core deterministic foundation | Not started | Stage 5 done | config/evidence/cost modules + tests |
| 7 | CrewAI core | Not started | Stage 6 done | crew builder + agents/tasks |
| 8 | Content planning and generation | Not started | Stage 7 done | outline→draft→review→refs flow |
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

### Stage 3 — TODO (Current Stage)

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

### Stage 4 — Supporting Documentation Before Code

Entry condition: Stage 3 committed and pushed. Exit criteria: all doc files below are real (non-placeholder) and committed.

- [ ] Write `docs/AI_WORKFLOW.md` describing how AI assistance is used across the project and how it is logged.
- [ ] Write `docs/PROMPTS.md` with the prompt-capture format the pipeline will use (and seed it with the documentation-stage prompts).
- [ ] Write `docs/DECISIONS.md` and record the first decisions (group setup, doc-first approach, deferral of dependencies to Stage 5).
- [ ] Write `docs/COSTS.md` initial resource-awareness plan: what will be measured (runtime, tokens), how, and where summarized.
- [ ] Write `docs/QUALITY.md` quality strategy: gates, tools, thresholds (page-count range, coverage target, file-length limit).
- [ ] Write `docs/SUBMISSION_CHECKLIST.md` with the concrete Moodle + GitHub submission items.
- [ ] Replace the root `README.md` placeholder with an initial professional version (overview, structure, planned usage, status).
- [ ] Cross-link the documents (PRD ↔ PLAN ↔ TODO ↔ QUALITY ↔ COSTS) where helpful.
- [ ] Verify no document overclaims production readiness or includes fake results.
- [ ] Commit the documentation set in coherent increments and push.

### Stage 5 — Project Setup

Entry condition: Stage 4 done. Exit criteria: project installs/runs a CLI stub reproducibly; dependency choices recorded.

- [ ] Decide the LLM provider/model for CrewAI and record it in `docs/DECISIONS.md` (resolves PLAN open question 1).
- [ ] Decide the plotting library and record it in `docs/DECISIONS.md`.
- [ ] Choose and record the initial test/lint tooling decision (pytest + ruff, and whether mypy is adopted) in `docs/DECISIONS.md`.
- [ ] Create a minimal `pyproject.toml` configured for uv with project metadata.
- [ ] Add the chosen runtime dependencies (CrewAI and required libraries) to `pyproject.toml`.
- [ ] Add pytest and ruff as dev dependencies in `pyproject.toml`.
- [ ] Add basic pytest configuration (test paths, options) when `pyproject.toml` is created.
- [ ] Add basic ruff configuration (rules, target version) when `pyproject.toml` is created.
- [ ] Create the uv environment and generate/commit the lock file.
- [ ] Add a `.env.example` template listing required environment variables (no real secrets).
- [ ] Add a project config file (e.g. topic, model, page-count thresholds, paths) under version control.
- [ ] Create a CLI entry point stub (`src/agentic_latex_book/cli.py`) that parses arguments and prints planned steps.
- [ ] Wire the CLI as a console script / runnable module.
- [ ] Add a package import sanity check (import the package and run the CLI `--help`).
- [ ] Add an initial local quality command/script that runs at least lint + tests (usable once the first tests exist).
- [ ] Add one trivial smoke test so the quality command has something to run.
- [ ] Document the exact setup, run, and quality-command instructions in `README.md`.
- [ ] Commit project setup and push.

### Stage 6 — Core Deterministic Foundation

Entry condition: Stage 5 done. Exit criteria: deterministic modules exist with passing unit tests; no agentic code yet.

- [ ] Implement the configuration loader (`config.py`) that resolves settings from config file + environment.
- [ ] Implement a paths/constants module centralizing repository paths (`results/`, `latex_project/`, `assets/`).
- [ ] Implement the evidence writer that creates per-run output locations under `results/`.
- [ ] Implement structured logging that writes run logs to `results/logs/`.
- [ ] Implement the cost/runtime tracker (timing now; token capture wired for later).
- [ ] Ensure no secret values are ever written to logs or evidence.
- [ ] Keep each module short and single-responsibility (respect the file-length limit).
- [ ] Write unit tests for the config loader (valid, missing, and override cases).
- [ ] Write unit tests for the paths/constants module.
- [ ] Write unit tests for the evidence writer (creates expected structure).
- [ ] Write unit tests for the cost/runtime tracker (records elapsed time).
- [ ] Run pytest and confirm the test suite passes.
- [ ] Run ruff lint/format checks and resolve any findings.
- [ ] Run the initial local quality command (lint + tests) and confirm it passes.
- [ ] Commit the deterministic foundation and push.

### Stage 7 — CrewAI Core

Entry condition: Stage 6 done. Exit criteria: a crew can be built and run end-to-end on a trivial input, persisting outputs.

- [ ] Define agent roles (planner/outliner, writer, reviewer/editor, reference curator) in small per-role modules.
- [ ] Define task definitions for outline, drafting, review, and references.
- [ ] Define structured output schemas for each task (typed, not free text).
- [ ] Implement the crew builder that assembles agents + tasks + process from config.
- [ ] Configure the crew process as sequential by default (parallelism deferred per PLAN open question 3).
- [ ] Persist each intermediate crew output to `results/crew_outputs/`.
- [ ] Capture prompts used by each agent into the `docs/PROMPTS.md` format / a prompts log.
- [ ] Record token/cost usage from the provider where exposed, via the cost tracker.
- [ ] Add a smoke test that builds the crew object without executing a paid run.
- [ ] Run a minimal real crew invocation to confirm wiring and output persistence.
- [ ] Commit the CrewAI core and push.

### Stage 8 — Content Planning and Generation

Entry condition: Stage 7 done. Exit criteria: the crew produces an outline, drafts, a reviewed draft, and a reference/citation map for the topic.

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
| 7 | Crew builds; smoke test passes; intermediate outputs persisted; prompts captured. |
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
| 7 | `results/crew_outputs/` sample outputs; prompts log; crew smoke test. |
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

- [ ] LLM provider/model for CrewAI and its cost/token-exposure characteristics (resolve by Stage 5).
- [ ] LaTeX engine + BiDi package combination most reliable for Hebrew–English (resolve by Stage 9/11).
- [ ] Sequential vs parallel chapter drafting (resolve by Stage 8).
- [ ] Exact page-count threshold for the page-count gate, e.g. 13–17 (resolve by Stage 12).
- [ ] Python plotting library for the generated graph (resolve by Stage 5/10).
- [ ] Per-gate detection methods (PDF text extraction vs source inspection) and their robustness (resolve by Stage 12).
- [ ] Reference sourcing: hand-curated vs agent-assembled with human review; how citation linking is verified (resolve by Stage 8/12).
- [ ] Test framework + quality tooling final selection, recorded in `docs/QUALITY.md` (resolve by Stage 5/13).
- [ ] Bound on re-draft iterations balancing quality against cost (resolve by Stage 8).
- [ ] Whether to add CI for the quality command (resolve by Stage 13).
