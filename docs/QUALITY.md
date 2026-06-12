# Quality Strategy

## Purpose

This document defines how quality is enforced in the project: the gates that confirm the generated PDF and the repository meet the mandatory requirements, and the code-quality tooling that keeps the implementation maintainable. Assignment 1 feedback noted that quality standards were not clearly established, so we set them out explicitly here and tie each gate to a concrete check. This is a planning-stage document; it describes the intended quality system, which is implemented across later stages.

## Current Status

As of Stage 8C.8.3 (cleaned Markdown content committed and pushed, `98a50f2`, passing the scanner):

- **pytest is configured** and the offline test suite passes (`uv run pytest`): **98 tests passing** (including the Stage 8C.6 hardening checks and the Stage 8C.8.1 scanner tests). The test suite remains offline and never calls a model or `kickoff`.
- **Stage 8C.7 candidate run passed the basic offline `content_checks` gate** — on-topic, no forbidden terms, no placeholders, no missing mandatory-element keywords (241,157 chars across the four outputs), recorded under `results/stage8c7-full-gemini-20260611-173125/`. The **previous failure modes are fixed** (no Gradient Descent topic, no placeholder author/date, correct group/authors/topic).
- The candidate is **not final PDF-ready.** Documented remaining content-QA risks (for Stage 8C.8): headers/footers described conceptually rather than implemented; questionable `example.com` / "Internal Publication" citations; unsupported in-text metrics (185 minutes / 99.1% / 1.8M tokens); and GPT-4o references although the run used Gemini.
- **No final accepted content, no LaTeX/PDF, and no PDF/LaTeX quality gate exist yet.** No claim of final readiness or PDF success is made.
- **Stage 8C.8.1 added the deterministic offline content-QA scanner** (`content_qa.py`, `content-qa` CLI): pure string checks for forbidden content (`example.com`, "Internal Publication", unsupported metrics 185 minutes / 99.1% / 1.8M tokens, "GPT-4o Technical Report", placeholders, the old Gradient Descent topic, conceptual-only headers/footers) and required positives (configured topic, group `MaRs-777`, both authors, an accepted date, and all mandatory PDF elements). It is offline, mutates nothing, and uses no model/API key. The committed Stage 8C.7 candidate **fails** this stricter scanner (8 blocking errors on its known risks), which is the intended signal that it is not final; a clean sample passes.
- **Stage 8C.8.2 produced the cleaned Markdown content** under `latex_project/content/` (`book.md`, `README.md`), derived from the 8C.7 candidate without editing the immutable run evidence. The cleaned content **passes the strict `content-qa` scanner** (`ok: True`, 0 errors, exit 0, 2 files): the 8 known risks were removed, only the measured run values from the 8C.7 `runtime.json` are stated (unmeasured metrics are labelled as proposed future evaluation), and the bibliography uses conservative real and project-local references. This is the gate that cleaned content must pass before LaTeX assembly; **no `.tex`/`.pdf` exists yet** and no claim of final PDF readiness is made. (Committed and pushed: `98a50f2`.)
- **Stage 9.0 planned the LaTeX/PDF validation gates (plan only — not implemented; still no `.tex`/`.pdf`):** for the Stage 9.5 validation pass, the PDF build must satisfy deterministic checks — compile exits 0; `latex_project/build/main.pdf` exists; page count 13–17; the PDF text layer contains the title, both authors, group `MaRs-777`, and the date; a ToC is present; all citations resolve (no `??`, no "Citation … undefined", no "Reference … undefined" in PDF text or compile log); the bibliography section appears with linked citations; both figure files (architecture diagram + Python-generated graph) exist on disk and are included; at least one `booktabs` table and the two equations appear; the Hebrew–English BiDi passage renders (Hebrew text present in the text layer); no overfull `\hbox` above ~50 pt; and the content-qa forbidden strings remain absent from the `.tex` sources. `content-qa latex_project/content/` stays mandatory as the pre-assembly gate. Engine and design rationale: D-030.
- **Stage 9.1 created the LaTeX skeleton and bibliography only** (`main.tex`, `preamble.tex`, nine chapter stubs with headings/TODO markers, `references.bib` transcribed strictly from the cleaned bibliography — Wooldridge URL-free, XeTeX via TUG). **No compile has been attempted**: TeX Live is not installed on this machine (`xelatex`/`biber` absent — environment limitation recorded; install command documented in `latex_project/README.md`), so the first syntax-check compile happens at Stage 9.4 after installation. The skeleton passes the same risk grep as the cleaned content (no `example.com`, no fabricated metrics, no `GPT-4o Technical Report`). **No PDF exists and no PDF gate has run.** (Committed and pushed: `af71265`.)
- **Stage 9.2 generated the two mandatory figures deterministically** (`figures/architecture.png` — the pipeline block diagram; `figures/generation_time.png` — the per-chapter chart) via two short matplotlib scripts under `latex_project/scripts/`, run with `uv run --with matplotlib` so no dependency was added. The chart's axis and title state explicitly that the values are **illustrative, not measured** — matching the cleaned content's own labelling — so no fake measured claims enter the PDF. Both scripts pass ruff lint/format. The chapter figure blocks now reference the existing PNGs. **Still no compile (TeX Live absent) and no PDF.** (Committed and pushed: `6aa2cf1`.)
- **Stage 9.3 converted the cleaned Markdown into the full LaTeX chapters.** All nine chapter files now carry the complete article text from `content/book.md` with no invented claims: measured values exact (`gemini/gemini-2.5-flash`, 300.68 s, 213,664 prompt / 235,436 completion tokens, 4 calls), unmeasured metrics labelled **proposed/not yet measured**, the graph labelled **illustrative**; booktabs tables 4.1/6.1, equations `eq:agent_utility`/`eq:quality`, plain-`verbatim` code listings (no new packages), the rendered Hebrew–English BiDi passage, and only citation keys that exist in `references.bib`. The whole `latex_project/` tree still passes the risk grep. **Still no compile (TeX Live absent), no PDF, and no PDF gate has run.** (Committed and pushed: `38f8c86`.)
- **Stage 9.4 ran the first real compile — it succeeds.** TeX Live was installed manually (the 9.4.0 gate first stopped on missing `bidi.sty`, fixed by `texlive-lang-arabic`). The XeLaTeX → biber → XeLaTeX ×2 sequence exits 0 and produces `latex_project/build/main.pdf` (19 pages) — a **gitignored build artifact, not committed and not final**. Two minimal log-driven source fixes: preamble package order (hyperref → polyglossia/bidi → biblatex) and `\path` for the two long bibliography paths. The final log shows **no LaTeX errors, no undefined citations, and no undefined references**; 5 minor overfull warnings (≤28 pt) and the 19-page count (target 13–17) are recorded for Stage 9.5, whose full PDF gates (page count, text-layer checks, BiDi render) still have NOT run and additionally need `poppler-utils` (`pdfinfo`/`pdftotext`). **No final PDF is claimed.** (Committed and pushed: `c7ce915`.)
- **Stage 9.5 ran the full deterministic PDF gate suite — all gates pass.** With `poppler-utils` 24.02 installed, a clean rebuild measures **16 pages (inside the 13–17 target)** with **0 overfull warnings** and a clean log (no errors, no undefined citations/references, no rerun-biber). All 14 text-layer gates pass via `pdftotext` (title, Mohamed Awad, Rawey Sleiman, MaRs-777, June 11 2026, Abstract, Contents, Bibliography, both figure captions, both table captions, the exact measured values, Hebrew BiDi text) and there are **0 unresolved `??` markers**. Rendered pages were inspected visually: cover, architecture figure, generation-time graph, Hebrew passage, and bibliography all render correctly (one float-induced sparse page, body p. 12, noted as harmless). Polish was minimal and content-preserving (margins 2.2 cm, 10pt, `\small` verbatim/table, `enumitem`, `\path`, biblatex URL penalties, figure widths); no mandatory element was removed and no metric changed. **`build/main.pdf` remains a gitignored build artifact: not committed, not copied to `results/final_pdf/`, and the Moodle submission PDF is not ready.** Stage 9.6 (final evidence commit) is the remaining step. (Committed and pushed: `899ebb8`.)
- **Stage 9.6 prepared the final article PDF evidence (in review before commit).** Human review blocked the first candidate over three stale "LaTeX assembly / PDF validation are future stages" statements (abstract, discussion, conclusion); these were corrected consistently in the cleaned source `content/book.md` **and** the matching chapter files (minimal consistency edits — no metric changed, nothing fabricated), the document was rebuilt cleanly, and every gate re-passed on the corrected PDF (16 pages, clean log, 0 overfulls, 14/14 text-layer gates, 0 unresolved `??`, 16/16 pages rendered, deterministic stale-statement grep clean). The corrected PDF was copied byte-identically (`cmp`-verified; SHA256 `b88fc2dd8768f2f3f972da98fdb4263b1eeee65baf617efdcd98cdc8ccccd3ee`) to `results/final_pdf/MaRs-777-article.pdf`, with gates, tool versions, the consistency-fix note, and a no-LLM statement recorded in `results/final_pdf/validation_report.md`. **This is the generated article PDF evidence only — the Moodle wrapper `MaRs-777-ex03.pdf` does not exist yet and submission packaging is a later step.** (Committed and pushed: `3fb8562` — the Stage 9.x LaTeX assembly milestone is complete; all deterministic gates passed on the committed evidence.)
- **ruff is configured** for linting and formatting; `uv run ruff check .` and `uv run ruff format --check .` both pass. Every Python file is under the 150-line limit.
- **The first real full run technically passed** (Stage 8C.3/8C.4): all four tasks (outline, draft, review, references) produced output, recorded under `results/stage8c3-full-gemini-20260611-164153/`; the **evidence secret scan was clean** (presence booleans only).
- **The generated content is rejected for the final PDF** — wrong topic ("Understanding and Implementing Gradient Descent" instead of the project topic), placeholder author/date (`[Your Name/Placeholder Name]`, "October 2023"), and only ~10 pages per the review output (target ~15). It is kept as **diagnostic evidence only**; no accepted final content exists.
- There are exactly two `kickoff` calls in the source, both in real-only paths (minimal + full runners); neither is exercised by tests.
- **No PDF/LaTeX quality gate has run, because no PDF or LaTeX exists.** No claim of full-pipeline or PDF success is made; the next step is prompt/config hardening before a second full run.
- All Python files are well under the 150-line course limit (largest is `config.py` at 131 lines; the CLI was split into `cli.py` and `cli_commands.py` to keep each small), though an automated **file-length check is not yet enforced**.
- There is still **no coverage measurement** yet.
- **mypy is deferred** (see decision D-013); it may be adopted in Stage 13.
- No PDF quality gate has been executed against a real PDF yet, because no pipeline or PDF exists.

The pytest/ruff results above are real (the tests actually pass). Everything related to a real crew run, the generated PDF, coverage, mypy, and an enforced file-length check is still planned, and no passing result is claimed for them.

## Planned Quality Gates (Mandatory PDF and Repository Checks)

Each gate is an independent check that produces a pass/fail with evidence, implemented in Stage 12 and run for real in Stage 14. The planned gates:

| Gate | What it checks | Requirement |
| --- | --- | --- |
| Build gate | The LaTeX project compiles successfully | FR-8 / PDF build |
| Page-count gate | The PDF is approximately 15 pages (threshold TBD, e.g. 13–17) | PDF-1 |
| Cover-page gate | Cover present with topic, author(s), course, lecturer, date | PDF-2 |
| ToC gate | Table of contents present | PDF-3 |
| Structure gate | Multiple chapters/sections present | PDF-4 |
| Headers/footers gate | Running headers/footers with page numbers | PDF-5 |
| Image gate | At least one image present | PDF-6 |
| Python-generated graph gate | A Python-generated graph present | PDF-7 |
| Table gate | At least one table present | PDF-8 |
| Formula gate | At least one mathematical formula present | PDF-9 |
| BiDi gate | Hebrew–English bidirectional section present and rendered | PDF-10 |
| Bibliography / citation-link gate | Bibliography present with linked in-text citations | PDF-11 |
| Repository gate | Required files exist (README, PRD, PLAN, TODO, `latex_project/`, `results/`) | Repository requirements |

A run that fails any mandatory gate is reported as failed, not silently accepted. Exact detection methods (PDF text extraction, source inspection, page counting) and the page-count threshold are finalized during implementation and recorded here.

## Planned Code Quality

- **pytest** — unit tests, focused first on the deterministic components (config, evidence, cost tracker, validation gates).
- **ruff** — linting and formatting with project rules.
- **mypy** — optional; the decision to adopt it is made and recorded in Stage 5/13.
- **Coverage target** — a coverage goal for the deterministic modules, enforced in Stage 13 (exact target recorded then).
- **File-length check** — enforce short, maintainable Python files; the limit is recorded here once chosen.
- **Local quality command** — for now, a command *sequence* run from a clean checkout: `uv run pytest`, `uv run ruff check .`, `uv run ruff format --check .`. A single consolidated command/script (adding types + coverage + length check) may be introduced during Stage 13; none exists yet.

## Quality Timeline

To avoid bolting quality on at the end, basic tooling starts early:

- **Stage 5** — basic pytest and ruff configuration are added when `pyproject.toml` is created, plus the initial quality command sequence and a trivial smoke test.
- **Stage 6** — the first deterministic tests are written, and the quality command sequence (pytest + ruff check + ruff format check) is run on every deterministic increment.
- **Stages 7–12** — tests accompany the components they cover; validation gates are implemented and tested.
- **Stage 13** — final quality hardening: coverage enforcement, optional mypy finalization, file-length check, command consolidation, and clean-checkout validation.

## No Fake Passing Claims

We do not record a gate or check as passing unless it has actually run and passed on real output. Planned gates are clearly labeled as planned. Real results, with their evidence locations, are added once the checks run.

## Quality Report Locations

- Validation gate reports (machine- and human-readable): `results/validation_reports/`
- Test, lint, and coverage output: produced by the local quality command; key results summarized in this document once available.
- Build logs relevant to the build gate: `results/logs/`
