# Submission Checklist

## Purpose

This document tracks everything needed for a complete, correct submission of Assignment 3 for the GitHub repository. It is the final gate before hand-in. Items are marked accurately: completed items are checked, and future work stays unchecked until it is genuinely done.

## Current Status

The implementation, the LaTeX project, and the validated generated article PDF (`results/final_pdf/MaRs-777-article.pdf`, Stage 9.6) all exist and are committed. Remaining unchecked items are the final repository review / submission readiness review.

## GitHub Requirements

- [ ] The submitted GitHub link points to the Assignment 3 repository `ai-agent-latex-book-assignment3` (not an earlier assignment).
- [ ] The repository is public, or shared with the lecturer at rmisegal@gmail.com.
- [x] The repository has a meaningful, incremental commit history (skeleton → PRD → PLAN → TODO → supporting documentation).
- [ ] The final state is pushed and `origin/main` is up to date at submission time.

## Final Article / Book PDF Requirements Checklist

The generated PDF must satisfy every mandatory element (to be confirmed by validation reports in Stage 14):

- [ ] Approximately 15 pages.
- [ ] Cover page with topic, author(s), course, lecturer, and date.
- [ ] Table of contents.
- [ ] Chapters / sections.
- [ ] Headers and footers.
- [ ] At least one image.
- [ ] At least one Python-generated graph.
- [ ] At least one table.
- [ ] At least one mathematical formula.
- [ ] Hebrew–English bidirectional (BiDi) section.
- [ ] Bibliography with linked citations.

## Repository Completeness Checklist

- [x] `README.md` at the repository root (initial professional version).
- [x] `docs/PRD.md`.
- [x] `docs/PLAN.md`.
- [x] `docs/TODO.md`.
- [x] `docs/AI_WORKFLOW.md`, `docs/PROMPTS.md`, `docs/DECISIONS.md`, `docs/COSTS.md`, `docs/QUALITY.md`, `docs/SUBMISSION_CHECKLIST.md` (initial versions).
- [ ] `latex_project/` with the LaTeX sources used to build the PDF.
- [ ] `src/agentic_latex_book/` implementation.
- [ ] `tests/` with the test suite.
- [ ] `scripts/` with run/build/validate helpers.

## Evidence Checklist

All evidence must come from real runs (no fabrication):

- [ ] Execution logs in `results/logs/`.
- [ ] Raw crew outputs in `results/crew_outputs/`.
- [ ] Validation reports in `results/validation_reports/`.
- [x] Final article PDF in `results/final_pdf/` (`MaRs-777-article.pdf`, 16 pages, validated + `validation_report.md`; committed and pushed in Stage 9.6, `3fb8562`).
- [ ] Cost/runtime data recorded in `docs/COSTS.md`.

## Final Pre-Submit Verification Checklist

- [ ] All mandatory PDF gates pass on the real generated PDF.
- [ ] The local quality command passes from a clean checkout.
- [ ] No secrets, no fake outputs, and no stray build artifacts are committed.
- [ ] Documentation claims are linked to real evidence.
- [ ] Nothing overclaims production readiness; limitations are stated.
- [ ] Git commits use standard student authorship with no AI/bot metadata.
- [ ] The repository is shared/public and the link is correct.
