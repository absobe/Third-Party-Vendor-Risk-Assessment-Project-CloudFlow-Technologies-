"""Calculate inherent/residual risk scores and print assessment statistics."""

from __future__ import annotations

import sys
from collections import Counter
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from project_data import ASSESSMENT, DISCLAIMER, OVERALL_SCORE, RISKS, SCORECARD_DOMAINS, rating


def main() -> int:
    print(DISCLAIMER)
    print()
    print("RISK SCORE CALCULATION")
    print("----------------------")
    print("Formula: Risk Score = Likelihood × Impact")
    print("Ratings: 1–4 Low | 5–9 Moderate | 10–16 High | 17–25 Critical")
    print()
    print(f"{'ID':<8}{'Title':<36}{'Inh L×I':>8}{'Inh':>10}{'Res L×I':>8}{'Res':>10}{'Treat':>10}")
    counts = Counter()
    for r in RISKS:
        inh = r["likelihood"] * r["impact"]
        res = r["residual_likelihood"] * r["residual_impact"]
        inh_r = rating(inh)
        res_r = rating(res)
        assert inh == r["inherent_risk"]
        assert res == r["residual_risk"]
        assert res_r == r["residual_rating"]
        counts[res_r] += 1
        print(
            f"{r['id']:<8}{r['title'][:34]:<36}{r['likelihood']}x{r['impact']}={inh:<4}{inh_r:>10}"
            f"{r['residual_likelihood']}x{r['residual_impact']}={res:<4}{res_r:>10}{r['treatment']:>10}"
        )
    print()
    print("SUMMARY STATISTICS")
    print("------------------")
    print(f"Number of Critical risks : {counts.get('Critical', 0)}")
    print(f"Number of High risks     : {counts.get('High', 0)}")
    print(f"Number of Moderate risks  : {counts.get('Moderate', 0)}")
    print(f"Number of Low risks       : {counts.get('Low', 0)}")
    print(f"Overall vendor score      : {OVERALL_SCORE}")
    print(f"Overall residual risk     : {ASSESSMENT['overall_risk']}")
    print(f"Recommendation            : {ASSESSMENT['recommendation']}")
    print()
    print("WEIGHTED SCORECARD CHECK")
    print("------------------------")
    total = 0.0
    for d in SCORECARD_DOMAINS:
        w = d["weight"] * d["score"]
        total += w
        print(f"  {d['domain']:<28} weight={d['weight']:.0%}  score={d['score']:>3}  weighted={w:5.1f}")
    print(f"  {'TOTAL':<28}                  {total:5.1f}")
    if abs(total - OVERALL_SCORE) > 0.05:
        print("INCONSISTENCY: overall score does not match domain weights.")
        return 1
    high = [r["id"] for r in RISKS if r["residual_rating"] == "High"]
    print()
    print("High residual risks requiring immediate attention:")
    print("  " + ", ".join(high))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
