"""Generate scorecard charts and a text summary."""

from __future__ import annotations

import sys
from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch

sys.path.insert(0, str(Path(__file__).resolve().parent))
from project_data import ASSESSMENT, DISCLAIMER, OVERALL_SCORE, RISKS, SCORECARD_DOMAINS, ROOT, rating


def main() -> int:
    out_dir = ROOT / "09_Vendor_Scorecard"
    out_dir.mkdir(parents=True, exist_ok=True)

    domains = [d["domain"] for d in SCORECARD_DOMAINS]
    scores = [d["score"] for d in SCORECARD_DOMAINS]
    weights = [d["weight"] * 100 for d in SCORECARD_DOMAINS]

    fig, ax = plt.subplots(figsize=(11, 5.5))
    bars = ax.bar(domains, scores, color="#1B365D", edgecolor="#C4A35A", linewidth=0.8)
    ax.axhline(OVERALL_SCORE, color="#8B1E3F", linestyle="--", linewidth=1.2, label=f"Weighted overall {OVERALL_SCORE}")
    ax.set_ylim(0, 100)
    ax.set_ylabel("Domain score (0–100)")
    ax.set_title("CloudFlow Technologies — Vendor Security Scorecard (Simulated)")
    ax.legend()
    plt.xticks(rotation=28, ha="right")
    for b, s in zip(bars, scores):
        ax.text(b.get_x() + b.get_width() / 2, s + 1.5, str(s), ha="center", va="bottom", fontsize=8)
    fig.tight_layout()
    chart1 = out_dir / "scorecard_domain_chart.png"
    fig.savefig(chart1, dpi=140)
    plt.close()

    fig, ax = plt.subplots(figsize=(7, 6))
    ax.set_xlim(0.5, 5.5)
    ax.set_ylim(0.5, 5.5)
    ax.set_xlabel("Impact")
    ax.set_ylabel("Likelihood")
    ax.set_title("Residual risk heat map (simulated)")
    ax.set_xticks([1, 2, 3, 4, 5])
    ax.set_yticks([1, 2, 3, 4, 5])
    # background bands
    from matplotlib.colors import ListedColormap
    import numpy as np

    grid = np.zeros((5, 5))
    for i in range(5):
        for j in range(5):
            grid[i, j] = (i + 1) * (j + 1)
    cmap = ListedColormap(["#C8E6C9", "#FFF3B0", "#FFCC80", "#EF9A9A"])
    # map scores to 0-3
    def band(v):
        if v <= 4:
            return 0
        if v <= 9:
            return 1
        if v <= 16:
            return 2
        return 3

    banded = np.vectorize(band)(grid)
    ax.imshow(banded, origin="lower", extent=[0.5, 5.5, 0.5, 5.5], cmap=cmap, alpha=0.85, vmin=0, vmax=3)
    for r in RISKS:
        ax.scatter(r["residual_impact"], r["residual_likelihood"], c="#1B365D", s=80, zorder=3)
        ax.annotate(r["id"], (r["residual_impact"] + 0.08, r["residual_likelihood"] + 0.08), fontsize=8, color="#1B365D")
    fig.tight_layout()
    chart2 = out_dir / "residual_heatmap.png"
    fig.savefig(chart2, dpi=140)
    plt.close()

    summary = out_dir / "scorecard_generated_summary.txt"
    lines = [
        DISCLAIMER,
        "",
        f"Overall vendor score: {OVERALL_SCORE}",
        f"Overall residual risk: {ASSESSMENT['overall_risk']}",
        f"Recommendation: {ASSESSMENT['recommendation']}",
        "",
        "Domain scores:",
    ]
    for d in SCORECARD_DOMAINS:
        lines.append(f"  {d['domain']}: {d['score']} (weight {d['weight']:.0%}, contribution {d['weight']*d['score']:.1f})")
    lines.append("")
    lines.append("Residual ratings:")
    for r in RISKS:
        lines.append(f"  {r['id']} {r['title']}: {r['residual_risk']} {rating(r['residual_risk'])} ({r['treatment']})")
    summary.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"Wrote {chart1.relative_to(ROOT)}")
    print(f"Wrote {chart2.relative_to(ROOT)}")
    print(f"Wrote {summary.relative_to(ROOT)}")
    print(f"Overall vendor score: {OVERALL_SCORE}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
