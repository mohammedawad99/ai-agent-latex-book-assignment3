"""Generate the pipeline architecture diagram for Chapter 3 (fig:architecture).

Deterministic matplotlib drawing of the block diagram described in
content/book.md section 3.1. Run from the repository root with:

    uv run --with matplotlib python latex_project/scripts/generate_architecture.py
"""

from pathlib import Path

import matplotlib

# Select the headless backend before pyplot is imported, so the script is
# deterministic in environments without a display.
matplotlib.use("Agg")

import matplotlib.pyplot as plt  # noqa: E402
from matplotlib.patches import FancyBboxPatch  # noqa: E402

OUTPUT = Path(__file__).resolve().parent.parent / "figures" / "architecture.png"

STAGES = [
    "User Input\n(topic, outline request)",
    "Planner Agent\n(detailed outline)",
    "Writer Agent\n(chapter draft)",
    "Reviewer Agent\n(content & structure review)",
    "Reference Curator Agent\n(citations)",
    "Structured Content\n(input to LaTeX assembly)",
]

BOX_FACE = "#e8eef7"
BOX_EDGE = "#1f3a5f"
BOX_WIDTH = 0.8
BOX_HEIGHT = 0.62


def main() -> None:
    fig, ax = plt.subplots(figsize=(5.0, 7.5))
    ax.set_xlim(0.0, 1.0)
    ax.set_ylim(0.0, float(len(STAGES)))
    ax.axis("off")

    for index, label in enumerate(STAGES):
        # Rows are laid out top to bottom in pipeline order.
        y_center = len(STAGES) - index - 0.5
        box = FancyBboxPatch(
            ((1.0 - BOX_WIDTH) / 2, y_center - BOX_HEIGHT / 2),
            BOX_WIDTH,
            BOX_HEIGHT,
            boxstyle="round,pad=0.02",
            facecolor=BOX_FACE,
            edgecolor=BOX_EDGE,
            linewidth=1.2,
        )
        ax.add_patch(box)
        ax.text(0.5, y_center, label, ha="center", va="center", fontsize=11)
        if index > 0:
            ax.annotate(
                "",
                xy=(0.5, y_center + BOX_HEIGHT / 2 + 0.02),
                xytext=(0.5, y_center + 1 - BOX_HEIGHT / 2 - 0.02),
                arrowprops={"arrowstyle": "-|>", "color": BOX_EDGE, "linewidth": 1.4},
            )

    ax.set_title("CrewAI multi-agent pipeline", fontsize=13)
    fig.savefig(OUTPUT, dpi=150, bbox_inches="tight")
    plt.close(fig)
    print(f"wrote {OUTPUT}")


if __name__ == "__main__":
    main()
