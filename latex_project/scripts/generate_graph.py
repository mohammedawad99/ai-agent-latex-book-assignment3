"""Generate the illustrative per-chapter generation-time chart for Chapter 6
(fig:generation_time).

The values are ILLUSTRATIVE inputs for the chart, exactly as labelled in
content/book.md section 6.2 — they are not measured results. Run from the
repository root with:

    uv run --with matplotlib python latex_project/scripts/generate_graph.py
"""

from pathlib import Path

import matplotlib

# Select the headless backend before pyplot is imported, so the script is
# deterministic in environments without a display.
matplotlib.use("Agg")

import matplotlib.pyplot as plt  # noqa: E402

OUTPUT = Path(__file__).resolve().parent.parent / "figures" / "generation_time.png"

# Illustrative example values for the figure (not measured results); these are
# the same values shown in content/book.md section 6.2.
CHAPTER_LABELS = ["Ch 1", "Ch 2", "Ch 3", "Ch 4", "Ch 5"]
EXAMPLE_TIMES = [15, 20, 30, 45, 60]


def main() -> None:
    fig, ax = plt.subplots(figsize=(8.0, 5.0))
    ax.bar(CHAPTER_LABELS, EXAMPLE_TIMES, color="steelblue")
    ax.set_xlabel("Chapter")
    ax.set_ylabel("Illustrative generation time (minutes)")
    ax.set_title("Illustrative generation time per chapter (not measured)")
    fig.tight_layout()
    fig.savefig(OUTPUT, dpi=150)
    plt.close(fig)
    print(f"wrote {OUTPUT}")


if __name__ == "__main__":
    main()
