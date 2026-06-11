# LaTeX Project (`latex_project/`)

This directory holds the LaTeX sources for the article *From PoC to
Production: A CrewAI Multi-Agent Pipeline for Generating a LaTeX Book*
(group MaRs-777; Mohamed Awad, Rawey Sleiman).

**Status: skeleton only (Stage 9.1).** The chapter files contain headings and
TODO markers, not the full text. **No final PDF exists yet.** Full chapter
conversion (Stage 9.3), figure/graph generation (Stage 9.2), compilation
(Stage 9.4), and PDF validation (Stage 9.5) are future stages — see
`docs/TODO.md` (Stage 9.0 plan) and `docs/DECISIONS.md` (D-030).

## Structure

```
latex_project/
├── main.tex          # entry point: cover page, abstract, ToC, chapters, bibliography
├── preamble.tex      # packages, fonts, Hebrew/English (polyglossia), fancyhdr, biblatex
├── chapters/         # one skeleton file per chapter (00_abstract … 08_conclusion)
├── figures/          # (empty) architecture diagram + Python-generated graph land here in 9.2
├── scripts/          # (empty) the figure-generation Python scripts land here in 9.2
├── references.bib    # bibliography transcribed from content/book.md only
├── build/            # compile output directory (gitignored; created at build time)
└── content/          # cleaned Markdown source — immutable input, never edited here
```

`content/book.md` is the single source of truth for all article text. The
LaTeX sources are derived from it; the original CrewAI run evidence under
`results/` is never modified.

## Build prerequisites (not yet installed on this machine)

Engine: **XeLaTeX** with polyglossia/bidi for the Hebrew–English section and
DejaVu Sans as the Hebrew font (decision D-030; LuaLaTeX is the fallback).

```bash
sudo apt update
sudo apt install -y texlive-xetex texlive-latex-extra texlive-bibtex-extra biber fonts-dejavu
```

Verify afterwards:

```bash
xelatex --version | head -3
biber --version
fc-match "DejaVu Sans"
```

## Build plan (executed from Stage 9.4 on — do not expect a PDF yet)

```bash
# 1. Generate figures (Stage 9.2 creates these scripts):
uv run --with matplotlib python scripts/generate_architecture.py
uv run --with matplotlib python scripts/generate_graph.py

# 2. Compile from this directory (multi-pass for ToC + citations):
mkdir -p build
xelatex -interaction=nonstopmode -halt-on-error -output-directory=build main.tex
biber --input-directory build --output-directory build main
xelatex -interaction=nonstopmode -halt-on-error -output-directory=build main.tex
xelatex -interaction=nonstopmode -halt-on-error -output-directory=build main.tex
```

Build artifacts stay in `build/` (gitignored). The final validated PDF is
copied to `results/final_pdf/` only at Stage 9.6.
