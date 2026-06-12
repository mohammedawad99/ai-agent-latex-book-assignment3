# Final PDF Evidence Validation Report

**Group:** MaRs-777
**Authors:** Mohamed Awad, Rawey Sleiman
**Date of validation:** 2026-06-12 (Stage 9.6)

## Source and artifacts

- **Source commit used for validation:** commit `899ebb8` ("Polish and
  validate LaTeX PDF") plus the uncommitted Stage 9.6 content-consistency fix
  (see note below); the latest docs commit at validation time was `2e0f8fa`.
- **Article PDF (this evidence):** `results/final_pdf/MaRs-777-article.pdf`
- **Build source:** `latex_project/build/main.pdf` (gitignored build output;
  the evidence file is a byte-identical copy — verified with `cmp`).

## Compile command sequence (from `latex_project/`)

```
xelatex -interaction=nonstopmode -halt-on-error -file-line-error -output-directory=build main.tex
biber --input-directory build --output-directory build main
xelatex -interaction=nonstopmode -halt-on-error -file-line-error -output-directory=build main.tex
xelatex -interaction=nonstopmode -halt-on-error -file-line-error -output-directory=build main.tex
```

All four steps exited 0 on a clean rebuild (`rm -rf latex_project/build` first).

## Validation summary

| Gate | Result |
| :--- | :--- |
| Pages | **16** (target: 13–17) |
| Compile status | success (all steps exit 0) |
| Overfull `\hbox` warnings | 0 |
| Undefined citations/references | 0 |
| Rerun-biber warnings | 0 |
| Unresolved `??` markers in PDF text | 0 |
| PDF text-layer gates (14 checks) | all passed — title, both authors, group MaRs-777, date June 11 2026, Abstract, Contents, Bibliography, both figure captions, both table captions, measured values (`gemini/gemini-2.5-flash`, 300.68 s, 213,664 / 235,436 tokens) |
| Hebrew–English BiDi section | present in the PDF text layer and visually confirmed in the Stage 9.5/9.6 page renderings (right-to-left rendering correct) |
| Rendered page images | 16/16 pages rendered via `pdftoppm` |

## Checksum

```
SHA256(results/final_pdf/MaRs-777-article.pdf) =
b88fc2dd8768f2f3f972da98fdb4263b1eeee65baf617efdcd98cdc8ccccd3ee
```

## Content-consistency note

Before this evidence was finalised, human review found three stale statements
in the article (abstract, discussion, conclusion) still describing LaTeX
assembly / PDF validation as *future* stages. These were corrected
consistently in the cleaned source (`latex_project/content/book.md`) and the
matching chapter files, the document was rebuilt cleanly, and every gate was
re-run on the corrected PDF (the results above are from the corrected build).
A deterministic stale-statement grep over the final PDF text layer now
confirms the old claims are gone.

## Scope note

This file is the **generated LaTeX article/book PDF evidence** produced by the
project's LaTeX assembly pipeline. The Moodle wrapper PDF
(`MaRs-777-ex03.pdf`) is a **separate submission artifact and is not created
here**; submission packaging remains a later step.

## Tool versions

- XeTeX 3.141592653-2.6-0.999995 (TeX Live 2023/Debian)
- biber 2.19
- pdfinfo (poppler) 24.02.0

## No-LLM statement

Stage 9.6 is deterministic local build and evidence packaging only: no CrewAI
run, no `kickoff`, no LLM/API call, and no API key were used.
