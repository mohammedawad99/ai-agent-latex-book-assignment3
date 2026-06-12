# Technical Plan (PLAN)

## 1. Title and Document Status

**Project:** From PoC to Production — A CrewAI Multi-Agent Pipeline that Generates a ~15-Page Article/Book as a Polished LaTeX PDF.

**Repository:** `ai-agent-latex-book-assignment3`

**Group:** MaRs-777 (Mohamed Awad, Rawey Sleiman). Mohamed Awad is the current repository maintainer.

**Document status:** Draft — Stage 2 (PLAN). This is a design document only. No implementation, CrewAI agents, dependencies, or LaTeX sources exist yet. Every component described here is *proposed*, not built. The plan derives from `docs/PRD.md` and will be refined as implementation stages proceed; changes are tracked through normal Git history.

**Last updated:** 2026-06-11.

---

## 2. Purpose of this PLAN

The PRD says *what* the project must achieve and how success is judged. This PLAN says *how* we intend to build it: the architecture, the CrewAI design, the LaTeX and PDF strategy, the validation and evidence approach, and the order of implementation work. It is the bridge between requirements (`docs/PRD.md`) and the task breakdown (`docs/TODO.md`).

The PLAN deliberately stops at design. It does not add code, dependencies, or LaTeX. Where a concrete choice (engine, library, model) is still open, it is recorded as an open technical question (§27) rather than guessed.

---

## 3. PRD Requirements Summary

The PLAN must satisfy the following requirement groups from the PRD. Identifiers are kept consistent with the PRD so the two documents stay traceable.

- **Functional (FR-1…FR-13):** topic input; CrewAI orchestration of multiple agents; outline-before-writing; ~15 pages of content; review/edit step; Python-generated graph; LaTeX assembly; PDF compilation; validation of mandatory elements; logging; cost recording; clear failure on missing elements; reproducible CLI run.
- **Non-functional (NFR-1…NFR-9):** modularity, reproducibility, observability, evidence-first, honesty (no overclaiming), maintainability, portability, cost awareness, secrets hygiene.
- **PDF mandatory elements (PDF-1…PDF-11):** ~15 pages, cover page, table of contents, chapters/sections, headers/footers, image, Python-generated graph, table, math formula, Hebrew–English BiDi section, bibliography with linked citations.
- **CrewAI (CR-1…CR-7):** CrewAI is required; multiple distinct roles; structured task communication; persisted intermediate outputs; modular agent/task config; captured prompts and decisions; token/cost capture when available.
- **LaTeX (LR-1…LR-7):** all sources under `latex_project/`; organized multi-file project; headers/footers/ToC/figures/tables/math/bibliography; BiDi engine/package; managed references; reproducible build command; build artifacts ignored by Git.
- **Evidence/reproducibility (ER-1…ER-7):** logs, crew outputs, validation reports, final PDF under `results/`; documented reproduction commands; claims reference evidence; never fabricate evidence.
- **Quality (QR-1…QR-7):** automated gates per mandatory element; build + page-count check; tests; machine- and human-readable reports; fail-loud on gate failure; quality tooling and thresholds documented.
- **Cost (CO-1…CO-5):** token usage, runtime, summarized honestly in `docs/COSTS.md`.
- **Submission:** repo public or shared with rmisegal@gmail.com; correct Assignment 3 GitHub link.

---

## 4. Architecture Overview

The system is planned as a linear pipeline of small, single-responsibility components, coordinated so that the CrewAI crew handles content generation while deterministic Python components handle assembly, building, validation, and evidence. Keeping the agentic part and the deterministic part separate is the main architectural decision: agents are good at writing and reviewing, but PDF correctness must be guaranteed by deterministic code and checks, not left to a model.

Planned components (all proposed):

1. **CLI entry point** — parses arguments (topic, config path, flags) and invokes the pipeline.
2. **Configuration loader** — reads project settings (topic, model, page-count thresholds, paths) from a config file plus environment.
3. **Crew builder** — constructs the CrewAI agents, tasks, and process from configuration.
4. **Agents** — produce structured intermediate outputs (outline, chapter drafts, review notes, references).
5. **Content assembler** — converts approved structured content into LaTeX sources under `latex_project/`.
6. **Figure generator** — runs Python to create at least one graph image consumed by the LaTeX build.
7. **PDF builder** — compiles the LaTeX project into the article PDF.
8. **Validator** — checks the mandatory PDF and repository requirements and writes reports.
9. **Cost tracker** — records runtime and token/cost data where the provider exposes it.
10. **Evidence writer** — persists logs, crew outputs, and validation reports under `results/`.

Data flows in one direction (topic → content → LaTeX → PDF → validation → evidence), with the cost tracker and evidence writer observing the run throughout.

---

## 5. Proposed Repository Structure

The Stage 0 skeleton already provides the top-level layout. The planned population of each area (created in later stages, not now):

```
src/agentic_latex_book/
  __init__.py            # exists (placeholder docstring only)
  cli.py                 # planned: CLI entry point
  config.py              # planned: configuration loader / settings model
  crew.py                # planned: crew builder (agents, tasks, process)
  agents/                # planned: agent role definitions (one concern per file)
  tasks/                 # planned: task definitions and structured schemas
  assembly/              # planned: content -> LaTeX assembler
  figures/               # planned: Python figure/graph generators
  build/                 # planned: LaTeX -> PDF build script
  validation/            # planned: quality gates and checks
  cost/                  # planned: cost/runtime tracker
  evidence/              # planned: logging and artifact writers
latex_project/           # planned: main.tex, chapters/, refs, class/style, assets refs
scripts/                 # planned: run, build, validate, reproduce helpers
tests/                   # planned: tests for validation logic and components
results/                 # evidence (logs, crew_outputs, validation_reports, final_pdf)
assets/figures/          # authored images
assets/generated/        # Python-generated graph output
docs/                    # PRD, PLAN, TODO, AI_WORKFLOW, PROMPTS, DECISIONS, COSTS, QUALITY, SUBMISSION_CHECKLIST
```

This is a proposed structure; module names may change during implementation and any change will be recorded in `docs/DECISIONS.md`. The intent is one clear responsibility per module to honour NFR-1 (modularity) and the course guideline of short, maintainable Python files.

---

## 6. Main Pipeline Flow

The planned end-to-end flow for a single run:

1. **Invoke** — user runs the CLI with a topic and config.
2. **Load config** — resolve settings, paths, thresholds, and model selection; load secrets from environment.
3. **Start evidence + cost capture** — open a run log and begin timing.
4. **Build crew** — construct agents, tasks, and the CrewAI process.
5. **Run crew** — produce an outline, then chapter drafts, then a review/edit pass, then a references set. Persist each structured output to `results/crew_outputs/`.
6. **Generate figures** — run the Python graph generator; write the image to `assets/generated/`.
7. **Assemble LaTeX** — convert approved content + figures + references into `latex_project/` sources.
8. **Build PDF** — compile the LaTeX project into the article PDF.
9. **Validate** — run all quality gates against the PDF and the repository; write reports to `results/validation_reports/`.
10. **Finalize evidence + cost** — copy the final PDF to `results/final_pdf/`, write the cost summary, close logs.
11. **Report result** — succeed only if every mandatory gate passes; otherwise fail clearly with the failing gate(s).

---

## 7. CrewAI Orchestration Design

CrewAI is the required orchestration mechanism (CR-1) and is the only agentic layer in the system. Plan:

- A **crew builder** constructs agents, tasks, and the process from configuration so roles can be added or changed without rewriting the pipeline (CR-5, NFR-1).
- The crew runs as a **sequential process** by default: outline → draft → review → references. Sequential is preferred initially for coherence and predictable cost; parallel chapter drafting is an open question (§27, mirrors PRD open question).
- Agents communicate through **well-defined tasks with structured outputs** (CR-3) — for example, the outline task returns a typed structure (chapter titles, intended length, key points), not free text, so downstream assembly is deterministic.
- Every intermediate output is **persisted** to `results/crew_outputs/` as evidence (CR-4, ER-2).
- Prompts and notable decisions are **captured** for `docs/PROMPTS.md` and `docs/DECISIONS.md` (CR-6).
- **Token/cost usage** is recorded where the provider exposes it (CR-7, CO-1).

The model/provider is not chosen in this PLAN; it is an open question resolved before implementation and recorded in `docs/DECISIONS.md`.

---

## 8. Proposed Agent Roles

Proposed roles (final set confirmed in `docs/DECISIONS.md` during implementation):

| Role | Responsibility | Primary output |
| --- | --- | --- |
| Planner / Outliner | Turn the topic into a structured outline sized for ~15 pages, including where the mandatory elements (image, graph, table, formula, BiDi section, bibliography) will live. | Outline structure |
| Writer(s) | Draft chapter/section content following the outline and target lengths. | Chapter drafts |
| Reviewer / Editor | Check coherence, length, and that planned mandatory elements are present in the content; request fixes. | Edited content + review notes |
| Reference Curator | Assemble the bibliography entries and the in-text citation points (with human review per PRD open question). | References + citation map |

An **assembler/validator** step exists in the architecture but is planned as deterministic Python (not an agent), because PDF correctness must be guaranteed by code and checks, not by a model. This keeps the evidence-first and honesty principles intact (NFR-4, NFR-5).

---

## 9. Proposed Task Graph and Context Flow

Planned task sequence and what context each task consumes/produces:

1. **Outline task** — input: topic + config. Output: structured outline (chapters, target lengths, placement of mandatory elements).
2. **Drafting task(s)** — input: outline + topic. Output: chapter drafts. May be one task per chapter or one combined task (open question on parallelism).
3. **Review/edit task** — input: drafts + outline. Output: revised content + review notes confirming planned elements are covered.
4. **Reference task** — input: topic + outline + content. Output: bibliography entries + citation points.

Context flows forward only; each task receives the prior structured outputs it needs. The deterministic assembler then consumes the approved content + references + generated figure. If the review task reports missing mandatory coverage, the plan allows a bounded re-draft loop before failing (ties to error handling, §20, and RK-2).

---

## 10. Data / Artifact Flow

Planned artifacts and their destinations:

| Stage | Produces | Location |
| --- | --- | --- |
| Crew run | Outline, drafts, review notes, references (structured) | `results/crew_outputs/` |
| Figure generator | Graph image | `assets/generated/` |
| Assembler | LaTeX sources (main, chapters, refs, style) | `latex_project/` |
| PDF builder | Article PDF + build artifacts (artifacts gitignored) | build dir → final copied to `results/final_pdf/` |
| Validator | Validation reports (machine + human readable) | `results/validation_reports/` |
| Cost tracker | Runtime + token/cost summary | run record → summarized in `docs/COSTS.md` |
| Evidence writer | Run logs | `results/logs/` |

Sources (LaTeX, generated figure) and the final PDF are tracked in Git; transient build artifacts (`.aux`, `.log`, etc.) are ignored (LR-7). All evidence comes from real runs only (ER-7) — no placeholder files will be committed as if they were results.

---

## 11. LaTeX Generation Strategy

- The assembler converts approved structured content into an **organized multi-file LaTeX project** under `latex_project/` (LR-1, LR-2): a `main.tex` that includes per-chapter `.tex` files, a references file, and a class/style or preamble holding headers/footers, ToC, and package setup.
- The preamble provides the mandatory structural elements (LR-3): cover page (topic, author(s)=group members, course, lecturer, date — PDF-2), table of contents (PDF-3), running headers/footers with page numbers (PDF-5), figure/table support (PDF-6, PDF-7, PDF-8), math (PDF-9), and bibliography (PDF-11).
- The **Hebrew–English BiDi section** (PDF-10) is isolated into its own chapter/section so it can be built and validated independently, reducing the risk that BiDi issues break the whole document (RK-1). The exact engine/package is an open question recorded for `docs/DECISIONS.md` (LR-4).
- The assembler keeps content and presentation separate where practical, so agent-written text maps cleanly into LaTeX without the agent having to emit raw LaTeX control sequences (reduces breakage and keeps modules short).

---

## 12. PDF Build Strategy

- A **PDF builder** wraps a single, pinned build command/engine so the build is reproducible (LR-6, NFR-2). The engine choice must support BiDi (e.g. a Unicode-aware engine such as XeLaTeX or LuaLaTeX) and is finalized in `docs/DECISIONS.md`.
- The build runs through a documented **script** under `scripts/` so it can be reproduced from a clean checkout (ER-5).
- Build artifacts are written to a working/build directory and **gitignored**; only the final PDF is copied to `results/final_pdf/` and tracked (LR-7).
- A failed compilation is a hard failure: the builder returns a non-zero result and the run is reported as failed (FR-12, QR-5).

---

## 13. Python-Generated Graph Strategy

- A dedicated **figure generator** module produces at least one graph from Python code (FR-6, PDF-7) and writes the image to `assets/generated/`.
- The generated image is referenced from the LaTeX sources so it appears in the PDF, and the validator confirms both that the generator ran and that the figure is present in the document (QR-1).
- The plotting library is an open question (recorded for `docs/DECISIONS.md`); no dependency is added in this PLAN. The generator is kept separate from authored images in `assets/figures/` so the "Python-generated" requirement is unambiguous and provable.

---

## 14. Validation and Quality-Gate Strategy

Planned automated gates, each producing a pass/fail with evidence (QR-1…QR-5). The gates check at least:

| Gate | Checks | Maps to |
| --- | --- | --- |
| Build gate | LaTeX compiles successfully | FR-8, QR-2 |
| Page-count gate | PDF is approximately 15 pages (threshold TBD, e.g. 13–17) | PDF-1, QR-2 |
| Cover-page gate | Cover present with topic, author(s), course, lecturer, date | PDF-2 |
| ToC gate | Table of contents present | PDF-3 |
| Structure gate | Multiple chapters/sections present | PDF-4 |
| Header/footer gate | Running headers/footers and page numbers present | PDF-5 |
| Image gate | At least one image present | PDF-6 |
| Graph gate | Python-generated graph present | PDF-7 |
| Table gate | At least one table present | PDF-8 |
| Formula gate | At least one math formula present | PDF-9 |
| BiDi gate | Hebrew–English BiDi section present and rendered | PDF-10 |
| Bibliography gate | Bibliography with linked citations present | PDF-11 |
| Repository gate | Required files exist (README, PRD, PLAN, TODO, latex_project/, results/) | §8, ER-* |

Gates write **machine- and human-readable reports** to `results/validation_reports/` (QR-4). A run failing any mandatory gate is reported as failed, not silently accepted (QR-5, FR-12). Exact detection methods (PDF text extraction, source inspection, page counting) and thresholds are decided during implementation and documented in `docs/QUALITY.md` (QR-7).

---

## 15. Evidence and Reproducibility Strategy

- Each run writes **execution logs** to `results/logs/` (ER-1), **raw crew outputs** to `results/crew_outputs/` (ER-2), **validation reports** to `results/validation_reports/` (ER-3), and the **final PDF** to `results/final_pdf/` (ER-4).
- The README and PLAN/TODO document the **exact commands** to reproduce a run and the build (ER-5, NFR-2).
- Documentation claims reference the **specific evidence file** that supports them (ER-6, NFR-4).
- **No fabricated evidence**: results are committed only after a real run produces them (ER-7). Until then, `results/` holds only structural `.gitkeep` markers.

---

## 16. Cost / Resource Tracking Strategy

- A **cost tracker** records wall-clock runtime per run and, where practical, per stage (CO-2), and token usage (prompt/completion) where the provider exposes it (CO-1).
- Cost/resource data is summarized in `docs/COSTS.md` with references to the underlying run records (CO-3), reported honestly from measured data rather than estimates presented as facts (CO-4), and annotated with the model(s) used and any assumptions (CO-5).
- If the provider does not expose token counts, this limitation is stated plainly rather than filled with invented numbers (supports NFR-5).

---

## 17. Configuration Strategy

- A **configuration loader** centralizes settings: topic, model/provider selection, page-count thresholds, paths, and feature flags.
- Configuration comes from a versioned config file plus environment variables for anything secret. No secrets are stored in the config file or the repository (NFR-9, §18).
- Centralizing configuration keeps modules small and makes the pipeline reconfigurable for a different topic without code changes, supporting modularity (NFR-1) and the "reasonably reconfigurable" scope note in the PRD.

---

## 18. Security and Secrets Handling

- API keys and other secrets are read from **environment variables** only and never hardcoded or committed (NFR-9, RK-8).
- The existing `.gitignore` ignores `.env` files (while allowing a future `.env.example` template) and secret-like files.
- No credentials appear in logs or evidence; the evidence writer must avoid persisting secret values.
- This is basic secrets hygiene appropriate to a course project; the PLAN does not claim a hardened production security posture (NFR-5).

---

## 19. Modularity and Extensibility Plan

- Each component (config, crew builder, agents, assembler, figure generator, builder, validator, cost tracker, evidence writer) is a **separate module with one responsibility** (NFR-1), so any one can be replaced without rewriting the others.
- Agent and task configuration is **data-driven** where practical, so new roles or tasks are added through configuration rather than structural rewrites (CR-5).
- Python files are kept **short and maintainable** per the course guideline; large concerns are split across small modules under `src/agentic_latex_book/`.
- Validation gates are written as **independent checks** so new mandatory elements can be added as new gates without touching existing ones.

---

## 20. Error Handling and Failure Reporting

- The pipeline **fails loudly**: any missing mandatory element, failed LaTeX build, or failed gate causes a non-zero exit and an explicit report of what failed (FR-12, QR-5).
- A **bounded re-draft loop** is allowed when the review step finds missing mandatory coverage or the page-count gate is not met, to avoid infinite cost while still self-correcting (ties to RK-2, RK-4).
- Errors are written to `results/logs/` with enough context to locate the failing stage (NFR-3, observability).
- The system never papers over a failure by emitting a partial or fake PDF and calling it success (NFR-4, NFR-5, ER-7).

---

## 21. Testing Strategy

- Tests live under `tests/` (QR-3) and focus first on the **deterministic** parts that guard correctness: validation gates, the page-count check, repository-file checks, and the assembler's content→LaTeX mapping.
- Validation logic is tested against small **fixture inputs** (e.g. a minimal known-good and known-bad sample) so gates are proven to pass and fail correctly — without fabricating run evidence.
- Agent behaviour is hard to unit-test deterministically; the plan favours testing the **contracts** (structured output shapes) the agents must satisfy rather than the model's wording.
- The testing framework and any tooling are chosen at implementation time and recorded in `docs/QUALITY.md`; no dependency is added in this PLAN.

---

## 22. Submission Strategy

- The **article/book PDF** (the main evaluated artifact) is produced by the pipeline and stored in `results/final_pdf/`, together with its validation report.
- The **GitHub repository** must be public or shared with the lecturer at rmisegal@gmail.com (PRD §18.11), and the submitted link must point to `ai-agent-latex-book-assignment3`, not the Assignment 2 repository (PRD §18.12).
- A meaningful, incremental **commit history** is maintained throughout (PRD §18.8); commits use standard student authorship with no AI/bot metadata.
- `docs/SUBMISSION_CHECKLIST.md` will track these submission items before final hand-in.

---

## 23. Technical Decisions and Alternatives

Decisions recorded here are *provisional directions*, not final; each is confirmed and dated in `docs/DECISIONS.md` during implementation.

| Topic | Provisional direction | Alternatives considered | Rationale |
| --- | --- | --- | --- |
| Agentic vs deterministic split | Agents write/review; Python assembles/builds/validates | All-agent pipeline | PDF correctness must be guaranteed by code, not a model (NFR-4). |
| Crew process | Sequential first | Parallel chapter drafting | Coherence and predictable cost; parallel is an open question. |
| LaTeX engine | A Unicode/BiDi-capable engine (e.g. XeLaTeX/LuaLaTeX) | pdfLaTeX + workarounds | BiDi support (PDF-10) needs a modern engine. |
| BiDi handling | Isolated BiDi section + suitable package | Fully bilingual document | Lowers risk; meets the requirement without overreach. |
| Structured agent outputs | Typed/structured task outputs | Free-text passing | Deterministic downstream assembly (CR-3). |
| Graph library | Python plotting library (TBD) | Hand-drawn/static image | Requirement is explicitly a Python-generated graph (PDF-7). |
| Config source | Config file + environment | Hardcoded constants | Reconfigurability and secrets hygiene (NFR-1, NFR-9). |

Model/provider, exact engine, exact libraries, and test framework are intentionally left open here (§27).

---

## 24. Risks Inherited from PRD and Technical Mitigations

| PRD risk | Technical mitigation in this PLAN |
| --- | --- |
| RK-1 BiDi fragility | Choose a BiDi-capable engine; isolate the BiDi section; dedicated BiDi gate (§11, §14). |
| RK-2 Inconsistent length | Outline-first sizing; page-count gate; bounded re-draft loop (§9, §14, §20). |
| RK-3 Non-deterministic build | Pinned engine/command via a build script; documented prerequisites (§12). |
| RK-4 Growing cost | Sequential default; bounded loops; cost tracking to catch regressions (§7, §16, §20). |
| RK-5 Scope creep | Plan strictly maps to PRD requirements; out-of-scope list respected (§3). |
| RK-6 Overclaiming readiness | Honest limitations stated throughout; deterministic checks, not model claims (§4, §16, §18). |
| RK-7 Missing evidence | Evidence writer integrated into the pipeline, not added afterwards (§4, §15). |
| RK-8 Leaked secrets | Env-only secrets; `.gitignore`; secrets kept out of logs (§18). |

---

## 25. Stage-by-Stage Implementation Roadmap

Proposed order of future work (each stage is a separate, reviewable increment with its own commits):

1. **Stage 3 — TODO:** turn this PLAN into an actionable task list in `docs/TODO.md`.
2. **Stage 4 — Project setup:** minimal `pyproject.toml` and chosen dependencies (the first point where dependencies are added), config loader, CLI skeleton.
3. **Stage 5 — Crew core:** crew builder, agent roles, structured task outputs; persist crew outputs as evidence.
4. **Stage 6 — Content → LaTeX assembler:** build the organized `latex_project/` from structured content.
5. **Stage 7 — Figure generator:** Python-generated graph into `assets/generated/`.
6. **Stage 8 — PDF builder:** pinned LaTeX build via script; produce the article PDF.
7. **Stage 9 — Validation gates:** implement all mandatory gates + reports; tests for gates.
8. **Stage 10 — Cost + evidence:** finalize cost tracking and evidence writing; populate `docs/COSTS.md` from real runs.
9. **Stage 11 — BiDi hardening:** ensure the Hebrew–English section builds and passes its gate reliably.
10. **Stage 12 — Documentation + submission:** complete `AI_WORKFLOW.md`, `PROMPTS.md`, `DECISIONS.md`, `QUALITY.md`, `SUBMISSION_CHECKLIST.md`; confirm repo sharing/link.

Order may adjust; changes are recorded in `docs/DECISIONS.md`.

---

## 26. Definition of Done for Implementation Stages

A stage is considered done when:

1. Its planned components exist and run from the CLI/scripts as described.
2. Relevant tests pass under `tests/` where the stage adds testable logic.
3. Any evidence it produces comes from a **real run** and is stored under `results/`.
4. No mandatory quality gate that the stage is responsible for is failing or silently skipped.
5. Documentation affected by the stage (DECISIONS, QUALITY, COSTS, etc.) is updated, with claims pointing to evidence.
6. Changes are committed with standard student authorship (no AI/bot metadata) and pushed to GitHub with a clear message.
7. The repository remains clean: no fake outputs, no committed secrets, no leftover build artifacts.

The overall project is done when the PRD acceptance criteria (PRD §18) all hold.

---

## 27. Open Technical Questions

1. **Model/provider:** which CrewAI-compatible LLM and provider, and what are its cost/token-exposure characteristics? (Carried from PRD; decided before Stage 5.)
2. **LaTeX engine + BiDi package:** which combination is most reliable for Hebrew–English in the target environment? (Validated before Stage 6/11.)
3. **Crew process shape:** sequential vs parallel chapter drafting, given coherence and cost trade-offs?
4. **Page-count threshold:** exact acceptable range for the page-count gate (e.g. 13–17)?
5. **Graph library:** which Python plotting library for the generated graph?
6. **Validation detection methods:** how each gate detects its element (PDF text extraction vs source inspection) and how robust that is?
7. **Reference sourcing:** are bibliography entries curated by hand or assembled by an agent with human review, and how is citation linking verified?
8. **Test framework + quality tooling:** which testing and lint/format tools, recorded in `docs/QUALITY.md`?
9. **Re-draft loop bounds:** how many re-draft iterations are allowed before failing, balancing quality against cost?

These are resolved and recorded in `docs/DECISIONS.md` as implementation proceeds; none are guessed in this PLAN.
