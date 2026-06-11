# Product Requirements Document (PRD)

## 1. Title and Document Status

**Project:** From PoC to Production — A CrewAI Multi-Agent Pipeline that Generates a ~15-Page Article/Book as a Polished LaTeX PDF.

**Working title of the generated artifact:** "From PoC to Production: Building Reliable AI Agent Systems with CrewAI, LaTeX, Observability, Security, and Cost Awareness."

**Repository:** `ai-agent-latex-book-assignment3`

**Document status:** Draft — Stage 1 (PRD). This document defines requirements only. No implementation, CrewAI agents, dependencies, or LaTeX sources exist yet. The PRD is expected to evolve as `docs/PLAN.md` and `docs/TODO.md` are written; changes will be tracked through normal Git history.

**Group code:** MaRs-777.

**Group members:**

- Mohamed Awad
- Rawey Sleiman

**Submission type:** Group submission by group MaRs-777. Mohamed Awad is the current repository maintainer; the work is owned jointly by the group members listed above.

**Last updated:** 2026-06-11.

---

## 2. Assignment Context

This is Assignment 3 for the AI Agents / Vibe Coding course. The task is to build a multi-agent system, orchestrated with CrewAI, that writes an approximately 15-page article/book on a chosen topic and compiles it into a professional PDF using LaTeX.

The course grades this work as a software engineering project, not only as a generated document. That means the repository must demonstrate a clear engineering process: planning documents, a real LaTeX project, reproducible runs, quality checks, and a meaningful commit history on GitHub.

The PDF is the central artifact that will be evaluated. Everything else in the repository exists to produce that PDF reliably and to prove that it was produced by an agent pipeline rather than written by hand.

This PRD is also shaped by feedback from Assignment 1, which is addressed explicitly in the requirements below.

---

## 3. Problem Statement

Writing a long, well-structured, correctly typeset document is time-consuming and error-prone when done manually. Doing it with a single large-language-model prompt tends to produce shallow, inconsistent output that does not satisfy strict formatting requirements (cover page, table of contents, headers/footers, figures, tables, formulas, bibliography, and bidirectional Hebrew–English text).

The assignment requires moving from a "proof of concept" mindset to a more disciplined, production-oriented one. A naive PoC can generate text, but it cannot reliably:

- coordinate multiple specialized writing and review steps,
- guarantee that every mandatory PDF element is present,
- compile LaTeX deterministically,
- produce evidence that the output meets the requirements, and
- track the cost and resources consumed.

The problem this project solves is: **how to orchestrate a set of cooperating agents that turn a topic into a complete, correctly formatted, evidence-backed LaTeX PDF, in a way that is reproducible and verifiable.**

---

## 4. Project Goal

Build a modular CrewAI pipeline that takes a topic (and configuration) as input and produces, as output, a polished ~15-page PDF that satisfies every mandatory content requirement, together with the supporting LaTeX project, logs, validation reports, and documentation needed to prove the result.

Secondary goal: do this in a way that is honest about its limitations. The system should be a credible step from PoC toward production practices (observability, validation, cost awareness, modular design) without claiming to be a finished production system.

---

## 5. Target Users / Evaluators

- **Primary:** The course lecturer and graders, who will evaluate the generated PDF and review the repository for engineering quality, process, and evidence.
- **Secondary:** The submitting group, who needs the system to be reproducible and debuggable while developing it.
- **Tertiary (hypothetical):** A future developer who might extend the pipeline to new topics or output formats. The design should make this plausible, even though no external user is expected during grading.

---

## 6. Scope

In scope for this project:

1. A CrewAI-based multi-agent pipeline that plans, writes, reviews, and assembles the document content.
2. Generation of LaTeX source for a ~15-page article/book on the working topic.
3. A Python step that generates at least one graph (figure) consumed by the LaTeX build.
4. Inclusion of at least one image, one table, one mathematical formula, and one section demonstrating Hebrew–English bidirectional (BiDi) text.
5. A bibliography with linked in-text citations.
6. A reproducible build that compiles the LaTeX sources into the final PDF.
7. Quality gates and validation checks that confirm the mandatory elements are present.
8. Documentation: PRD, PLAN, TODO, AI workflow, prompts, decisions, costs, quality, and submission checklist.
9. Evidence collection: logs, raw crew outputs, validation reports, and the final PDF, stored under `results/`.
10. A clean, professional Git history pushed to GitHub.

---

## 7. Out of Scope

The following are explicitly not part of this project:

1. A production deployment, hosting, or public-facing service.
2. A graphical user interface or web frontend.
3. Real-time or streaming generation.
4. Multi-tenant usage, authentication, or user accounts.
5. Fine-tuning or training of models.
6. Guaranteed factual accuracy of every sentence in the generated book beyond reasonable review; the document is an illustrative article, not a peer-reviewed publication.
7. Support for arbitrary topics at grading time; the pipeline targets the chosen working topic, even if it is written to be reasonably reconfigurable.
8. Languages other than English and Hebrew (Hebrew is required only for the BiDi demonstration).

---

## 8. Final Deliverables

1. **The PDF** — the primary evaluated artifact — stored at `results/final_pdf/`.
2. **The LaTeX project** — all `.tex` sources, class/style files, bibliography, and asset references — under `latex_project/`.
3. **The CrewAI pipeline source code** under `src/agentic_latex_book/` (delivered in later stages).
4. **Helper scripts** under `scripts/` for building, validating, and reproducing runs.
5. **Tests** under `tests/`.
6. **Documentation** under `docs/`: `PRD.md`, `PLAN.md`, `TODO.md`, `AI_WORKFLOW.md`, `PROMPTS.md`, `DECISIONS.md`, `COSTS.md`, `QUALITY.md`, `SUBMISSION_CHECKLIST.md`.
7. **README.md** at the repository root.
8. **Evidence** under `results/`: `logs/`, `crew_outputs/`, `validation_reports/`, `final_pdf/`.
9. **A GitHub repository** with a meaningful, incremental commit history.
10. **The Moodle submission PDF** — a separate wrapper document created from the official Word template, named `MaRs-777-ex03.pdf`. It must contain the exercise number (03), the group code (MaRs-777), the GitHub link to this Assignment 3 repository, and the final self-assessment score. This is distinct from the generated LaTeX article/book PDF (deliverable 1) and is the document submitted on Moodle.

---

## 9. Functional Requirements

| ID | Requirement |
| --- | --- |
| FR-1 | The system shall accept a topic and configuration as input to the pipeline. |
| FR-2 | The system shall orchestrate multiple cooperating agents using CrewAI. |
| FR-3 | The pipeline shall produce a document outline/plan before writing full content. |
| FR-4 | The pipeline shall generate chapter/section content for an approximately 15-page document. |
| FR-5 | The pipeline shall include a content review/editing step before final assembly. |
| FR-6 | The system shall generate at least one graph from Python code and save it as an image asset. |
| FR-7 | The system shall assemble the content into LaTeX source files under `latex_project/`. |
| FR-8 | The system shall compile the LaTeX sources into a single PDF. |
| FR-9 | The system shall run validation checks confirming each mandatory PDF element exists. |
| FR-10 | The system shall write logs and raw agent outputs to `results/` during each run. |
| FR-11 | The system shall record cost/resource information (e.g., token usage and runtime) per run. |
| FR-12 | The system shall fail clearly (non-zero exit / explicit error report) if a mandatory element or the PDF build is missing. |
| FR-13 | The pipeline shall be runnable from the command line in a reproducible way. |

---

## 10. Non-Functional Requirements

| ID | Requirement |
| --- | --- |
| NFR-1 | **Modularity** — components (agents, LaTeX assembly, validation, cost tracking) shall be separable and independently replaceable, to address the extensibility weakness from Assignment 1. |
| NFR-2 | **Reproducibility** — a documented command sequence shall reproduce a run and its outputs from a clean checkout. |
| NFR-3 | **Observability** — runs shall produce logs sufficient to understand what each agent did and where failures occurred. |
| NFR-4 | **Evidence-first** — every important claim about the result shall be backed by a concrete artifact (log, report, generated file, or documented decision), not by description alone. |
| NFR-5 | **Honesty** — the project shall not overclaim production readiness; limitations shall be documented. |
| NFR-6 | **Maintainability** — code and documents shall be clear, consistently structured, and reasonably commented. |
| NFR-7 | **Portability** — the build shall work in a standard Linux/LaTeX environment with documented prerequisites. |
| NFR-8 | **Cost awareness** — the system shall make resource usage visible rather than hidden. |
| NFR-9 | **Security hygiene** — secrets (API keys) shall be kept out of the repository via environment variables and `.gitignore`. |

---

## 11. PDF Requirements Checklist

The final PDF must satisfy all of the following mandatory elements. Each will be validated and have associated evidence.

| ID | Mandatory element | Notes |
| --- | --- | --- |
| PDF-1 | Approximately 15 pages | Target ~15; small deviation acceptable, validated by page count. |
| PDF-2 | Cover page | Must include topic, author(s), course, lecturer, and date. |
| PDF-3 | Table of contents | Auto-generated from chapter/section structure. |
| PDF-4 | Chapters / sections | Logical, multi-section structure. |
| PDF-5 | Headers and footers | Running headers/footers with page numbering. |
| PDF-6 | At least one image | An included image asset. |
| PDF-7 | At least one Python-generated graph | A figure produced by Python code, not hand-drawn. |
| PDF-8 | At least one table | A real table with structured data. |
| PDF-9 | At least one mathematical formula | Typeset with LaTeX math. |
| PDF-10 | Hebrew–English BiDi section | A chapter/section demonstrating correct bidirectional handling. |
| PDF-11 | Bibliography with linked citations | References at the end with clickable in-text citations. |

---

## 12. CrewAI Pipeline Requirements

| ID | Requirement |
| --- | --- |
| CR-1 | CrewAI shall be the orchestration mechanism for the agents; it is required, not optional. |
| CR-2 | The pipeline shall define multiple agents with distinct roles (for example: planner/outliner, writer(s), reviewer/editor, and an assembler/validator). Exact roles to be finalized in `docs/PLAN.md`. |
| CR-3 | Agents shall communicate through well-defined tasks and structured outputs rather than ad-hoc free text where practical. |
| CR-4 | The pipeline shall persist intermediate agent outputs to `results/crew_outputs/` as evidence. |
| CR-5 | Agent and task configuration shall be modular so roles can be added or modified without rewriting the pipeline (supports NFR-1). |
| CR-6 | The pipeline shall capture prompts and key decisions for documentation in `docs/PROMPTS.md` and `docs/DECISIONS.md`. |
| CR-7 | The pipeline shall record token/cost usage where the model provider exposes it (supports cost awareness). |

---

## 13. LaTeX Project Requirements

| ID | Requirement |
| --- | --- |
| LR-1 | All LaTeX sources used to build the PDF shall be included under `latex_project/` in the repository. |
| LR-2 | The LaTeX project shall be organized (main file plus included chapters/sections and assets) rather than a single opaque file, where reasonable. |
| LR-3 | The project shall support headers/footers, table of contents, figures, tables, math, and bibliography. |
| LR-4 | Hebrew–English BiDi shall be handled with an appropriate engine/package (for example XeLaTeX/LuaLaTeX with a suitable BiDi package); the exact choice is recorded in `docs/DECISIONS.md`. |
| LR-5 | The bibliography shall use a managed references file with linked citations. |
| LR-6 | The build shall be invocable via a documented command/script and shall be reproducible. |
| LR-7 | LaTeX build artifacts (`.aux`, `.log`, etc.) shall be ignored by Git; sources and the final PDF shall be tracked. |

---

## 14. Evidence and Reproducibility Requirements

| ID | Requirement |
| --- | --- |
| ER-1 | Each pipeline run shall write execution logs to `results/logs/`. |
| ER-2 | Raw agent/crew outputs shall be stored in `results/crew_outputs/`. |
| ER-3 | Validation results shall be stored in `results/validation_reports/`. |
| ER-4 | The final PDF shall be stored in `results/final_pdf/`. |
| ER-5 | The repository shall document the exact commands needed to reproduce a run and the build. |
| ER-6 | Claims in documentation shall reference the specific evidence file that supports them. |
| ER-7 | No fake outputs or fabricated evidence shall ever be committed; evidence must come from real runs. |

---

## 15. Quality and Validation Requirements

| ID | Requirement |
| --- | --- |
| QR-1 | Automated quality gates shall verify that each mandatory PDF element (PDF-1…PDF-11) is present. |
| QR-2 | A validation step shall confirm the PDF compiles successfully and produces the expected page count range. |
| QR-3 | The project shall include tests under `tests/` for validation logic and key components. |
| QR-4 | Quality gates shall produce machine- and human-readable reports stored under `results/validation_reports/`. |
| QR-5 | A run that fails any mandatory quality gate shall be reported as failed, not silently accepted (supports FR-12). |
| QR-6 | Code quality tooling (formatting/linting) shall be defined in `docs/QUALITY.md` and applied (introduced in later stages, no dependencies added in Stage 1). |
| QR-7 | The quality criteria and their pass/fail thresholds shall be documented in `docs/QUALITY.md`. |

---

## 16. Cost / Resource Awareness Requirements

| ID | Requirement |
| --- | --- |
| CO-1 | The system shall record token usage (prompt/completion where available) per run. |
| CO-2 | The system shall record wall-clock runtime per run and, where practical, per stage. |
| CO-3 | Cost/resource data shall be summarized in `docs/COSTS.md` with reference to the underlying evidence. |
| CO-4 | Cost reporting shall be honest and based on measured data, not estimates presented as facts. |
| CO-5 | The documentation shall note the model(s) used and any assumptions behind cost figures. |

---

## 17. Risks and Mitigations

| ID | Risk | Mitigation |
| --- | --- | --- |
| RK-1 | Hebrew–English BiDi rendering is fragile in LaTeX. | Choose a BiDi-capable engine early; isolate the BiDi section; validate its build explicitly. |
| RK-2 | Agent output is inconsistent or too short/long for ~15 pages. | Use structured tasks, an outline-first step, and a page-count validation gate with iteration. |
| RK-3 | LaTeX compilation is non-deterministic or environment-dependent. | Pin the build command/engine, document prerequisites, and run the build in a reproducible script. |
| RK-4 | API/model cost grows during iteration. | Track cost per run, cache intermediate outputs, and avoid unnecessary full re-runs. |
| RK-5 | Scope creep beyond assignment requirements. | Keep an explicit out-of-scope list and map work to requirements via the traceability matrix. |
| RK-6 | Overclaiming production readiness. | State limitations explicitly; frame the work as PoC-to-production progress, not a finished product. |
| RK-7 | Evidence not captured during runs. | Make logging and artifact storage part of the pipeline, not an afterthought. |
| RK-8 | Secrets accidentally committed. | Use environment variables and `.gitignore`; never hardcode keys. |

---

## 18. Acceptance Criteria

The project is acceptable when all of the following hold:

1. A single, reproducible command sequence runs the CrewAI pipeline and produces the final PDF.
2. The final PDF satisfies every mandatory element PDF-1 through PDF-11, confirmed by validation reports.
3. The PDF is approximately 15 pages.
4. The LaTeX project that produced the PDF is present in `latex_project/`.
5. `README.md`, `docs/PRD.md`, `docs/PLAN.md`, and `docs/TODO.md` exist and are real, non-placeholder documents.
6. Evidence (logs, crew outputs, validation reports, final PDF) exists under `results/` and comes from real runs.
7. Cost/resource usage is recorded and summarized in `docs/COSTS.md`.
8. The repository has a meaningful, incremental commit history pushed to GitHub.
9. AI-assisted workflow, prompts, and decisions are documented.
10. No fabricated evidence and no overclaiming of production readiness are present.
11. The GitHub repository is public, or shared with the lecturer at rmisegal@gmail.com, per the assignment instructions.
12. The submitted GitHub link points to this Assignment 3 repository (`ai-agent-latex-book-assignment3`), not the older Assignment 2 repository.
13. The Moodle submission PDF (`MaRs-777-ex03.pdf`) is created from the official Word template and includes exercise number 03, group code MaRs-777, the Assignment 3 GitHub link, and the final self-assessment score.

---

## 19. Assumptions

1. The student has access to a working CrewAI-compatible LLM API and a LaTeX toolchain (with a BiDi-capable engine) in a standard Linux environment.
2. "Approximately 15 pages" allows minor deviation as long as the document is clearly around that length.
3. The chosen working topic is acceptable for the assignment; it can be refined without changing the architecture.
4. Hebrew content for the BiDi demonstration can be a short, self-contained section rather than a full bilingual book.
5. Grading focuses on the PDF plus the engineering process and evidence, consistent with the assignment summary.
6. Model/provider details and exact dependencies will be decided in `docs/PLAN.md`; Stage 1 deliberately adds none.
7. The build environment used for grading is similar enough to the development environment that documented prerequisites are sufficient.

---

## 20. Open Questions

1. Which exact LLM/model and provider will be used, and what are its cost characteristics? (To be decided in PLAN.)
2. Which LaTeX engine and BiDi package give the most reliable Hebrew–English handling in the target environment? (To be validated.)
3. What is the final set of CrewAI agent roles and the task graph between them? (To be finalized in PLAN.)
4. How many writing/review iterations are needed to reliably hit ~15 pages without excessive cost?
5. Should chapters be generated in parallel or sequentially, given cost and coherence trade-offs?
6. What is the precise pass/fail threshold for the page-count gate (e.g., 13–17 pages)?
7. How will citations and the bibliography be sourced — curated by hand, or assembled by an agent with human review?

---

## 21. Traceability Matrix

Maps assignment requirements to the planned evidence that will demonstrate them. Evidence artifacts are produced in later stages; this matrix defines where each will live.

| Assignment requirement | PRD reference | Planned evidence / location |
| --- | --- | --- |
| ~15-page PDF | PDF-1 | Final PDF in `results/final_pdf/`; page-count check in `results/validation_reports/`. |
| Cover page (topic, author, course, lecturer, date) | PDF-2 | LaTeX cover source in `latex_project/`; rendered cover in final PDF; validation report. |
| Table of contents | PDF-3 | `latex_project/` ToC source; rendered ToC; validation report. |
| Chapters / sections | PDF-4 | Chapter `.tex` files in `latex_project/`; structure check in validation report. |
| Headers and footers | PDF-5 | Header/footer config in `latex_project/`; rendered pages; validation report. |
| At least one image | PDF-6 | Image asset in `assets/figures/`; reference in LaTeX; validation report. |
| At least one Python-generated graph | PDF-7 | Generator code in `src/`/`scripts/`; output in `assets/generated/`; validation report. |
| At least one table | PDF-8 | Table source in `latex_project/`; validation report. |
| At least one math formula | PDF-9 | Math source in `latex_project/`; validation report. |
| Hebrew–English BiDi section | PDF-10 | BiDi section source in `latex_project/`; rendered section; build/validation evidence. |
| Bibliography with linked citations | PDF-11 | References file in `latex_project/`; rendered bibliography; citation-link check. |
| CrewAI orchestration | CR-1…CR-7 | Pipeline code in `src/agentic_latex_book/`; intermediate outputs in `results/crew_outputs/`. |
| LaTeX project included | LR-1…LR-7 | `latex_project/` sources; `.gitignore` rules; build script in `scripts/`. |
| README + PRD + PLAN + TODO | §8 | `README.md`, `docs/PRD.md`, `docs/PLAN.md`, `docs/TODO.md`. |
| Reproducibility | ER-1…ER-7, NFR-2 | `results/` artifacts; documented commands in README/PLAN. |
| Quality gates / validation | QR-1…QR-7 | `tests/`; reports in `results/validation_reports/`; `docs/QUALITY.md`. |
| Cost / resource awareness | CO-1…CO-5 | Per-run cost records; `docs/COSTS.md`. |
| AI workflow documentation | NFR-4, CR-6 | `docs/AI_WORKFLOW.md`, `docs/PROMPTS.md`, `docs/DECISIONS.md`. |
| Professional engineering process | §2, §8, NFR-* | Git history on GitHub; documentation set; `docs/SUBMISSION_CHECKLIST.md`. |
| Moodle template PDF submission | §8 (deliverable 10), Acceptance §18.13 | `MaRs-777-ex03.pdf` from the official Word template; tracked in submission checklist. |
| GitHub sharing / public access | Acceptance §18.11 | Repository public or shared with rmisegal@gmail.com; recorded in `docs/SUBMISSION_CHECKLIST.md`. |
| Correct Assignment 3 repository link | Acceptance §18.12 | GitHub link to `ai-agent-latex-book-assignment3`; verified in `MaRs-777-ex03.pdf` and `docs/SUBMISSION_CHECKLIST.md`. |

---

## Explicit Statements

The following statements are binding for this project:

- **The PDF is the main evaluated artifact.** All other components exist to produce and substantiate it.
- **CrewAI is required as the orchestration mechanism.** The multi-agent pipeline must be built with CrewAI.
- **The LaTeX project must be included in the repository**, under `latex_project/`, including all sources used to build the PDF.
- **PRD, PLAN, TODO, and README are mandatory** and must be real, non-placeholder documents.
- **The system must not overclaim production readiness.** It is a credible PoC-to-production step; its limitations are documented.
- **Every important claim must be supported by evidence** — logs, validation reports, generated files, or documented decisions — never by description alone.
- **The repository must maintain a meaningful commit history** and be updated on GitHub throughout the project, not in a single final dump.
