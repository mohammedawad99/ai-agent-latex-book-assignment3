# Submission Checklist

## Purpose

This document tracks everything needed for a complete, correct submission of Assignment 3, across both GitHub and Moodle. It is the final gate before hand-in. Items are marked accurately: completed items are checked, and future work stays unchecked until it is genuinely done.

## Current Status

The project is at the documentation stage (Stage 4 of the staged plan). Planning and supporting documents exist; implementation, the LaTeX project, the generated PDF, and the Moodle wrapper PDF do not exist yet. Most items below are therefore intentionally unchecked.

## GitHub Requirements

- [ ] The submitted GitHub link points to the Assignment 3 repository `ai-agent-latex-book-assignment3` (not an earlier assignment).
- [ ] The repository is public, or shared with the lecturer at rmisegal@gmail.com.
- [x] The repository has a meaningful, incremental commit history (skeleton → PRD → PLAN → TODO → supporting documentation).
- [ ] The final state is pushed and `origin/main` is up to date at submission time.

## Moodle Requirements

- [ ] Each group member submits the assignment separately on Moodle.
- [ ] The submission PDF is created from the official Word template and converted to PDF.
- [ ] The submission PDF is named `MaRs-777-ex03.pdf`.
- [ ] The submission PDF states the exercise number: 03.
- [ ] The submission PDF states the group code: MaRs-777.
- [ ] The submission PDF lists the group members: Mohamed Awad and Rawey Sleiman.
- [ ] The submission PDF includes the Assignment 3 GitHub link.
- [ ] The submission PDF includes the final self-assessment score, decided honestly against the rubric.

Note: the Moodle submission PDF (`MaRs-777-ex03.pdf`) is a separate document from the generated article/book PDF. The article PDF is the main evaluated artifact; the wrapper carries submission metadata.

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
- [ ] Final article PDF in `results/final_pdf/`.
- [ ] Cost/runtime data recorded in `docs/COSTS.md`.

## Final Pre-Submit Verification Checklist

- [ ] All mandatory PDF gates pass on the real generated PDF.
- [ ] The local quality command passes from a clean checkout.
- [ ] No secrets, no fake outputs, and no stray build artifacts are committed.
- [ ] Documentation claims are linked to real evidence.
- [ ] Nothing overclaims production readiness; limitations are stated.
- [ ] Git commits use standard student authorship with no AI/bot metadata.
- [ ] `MaRs-777-ex03.pdf` is complete and submitted on Moodle by each member.
- [ ] The repository is shared/public and the link is correct.
