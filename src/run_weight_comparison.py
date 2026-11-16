"""Recalculate hybrid weight comparisons from the frozen Week 2 component scores.

This analysis does not rerun the MiniLM model. It combines previously saved
lexical and semantic scores for the same resume-job pairs.
"""
import csv
from collections import defaultdict
from math import log2
from pathlib import Path
from statistics import mean

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "results/week_2/rankings.csv"
OUTPUT = ROOT / "results/weight_comparison"
WEIGHTS = (0.0, 0.3, 0.5, 0.7, 1.0)

def dcg(grades):
    return sum((2 ** g - 1) / log2(i + 2) for i, g in enumerate(grades))

def write_csv(path, rows):
    with path.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=list(rows[0]), lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)

def main():
    with SOURCE.open(newline="", encoding="utf-8") as f:
        source = list(csv.DictReader(f))
    scores = defaultdict(dict)
    labels = {}
    for r in source:
        key = (r["job_id"], r["resume_id"])
        scores[key][r["method"]] = float(r["score"])
        grade = int(r["relevance"])
        if key in labels and labels[key] != grade:
            raise ValueError("Inconsistent relevance grades")
        labels[key] = grade
    if not labels or any(set(v) != {"lexical", "semantic", "hybrid"} for v in scores.values()):
        raise ValueError("Missing component scores")
    jobs = sorted({j for j, _ in labels})
    details = []
    for weight in WEIGHTS:
        for job in jobs:
            ranked = sorted(
                ((rid, labels[j, rid], weight * scores[j, rid]["lexical"] +
                  (1 - weight) * scores[j, rid]["semantic"])
                 for j, rid in labels if j == job),
                key=lambda x: (-x[2], x[0])
            )
            if len(ranked) < 3:
                raise ValueError("Insufficient candidates")
            top = ranked[:3]
            ideal = dcg(sorted((g for _, g, _ in ranked), reverse=True)[:3])
            details.append(dict(
                lexical_weight=weight, job_id=job,
                precision_at_3=sum(g >= 1 for _, g, _ in top) / 3,
                ndcg_at_3=dcg([g for _, g, _ in top]) / ideal if ideal else 0,
                top_3_resume_ids="|".join(rid for rid, _, _ in top)))
    summary = []
    for weight in WEIGHTS:
        subset = [r for r in details if r["lexical_weight"] == weight]
        summary.append(dict(lexical_weight=weight, semantic_weight=1 - weight,
                            precision_at_3=mean(r["precision_at_3"] for r in subset),
                            ndcg_at_3=mean(r["ndcg_at_3"] for r in subset)))
    OUTPUT.mkdir(parents=True, exist_ok=True)
    write_csv(OUTPUT / "metrics_by_job.csv", details)
    write_csv(OUTPUT / "metrics_summary.csv", summary)
    print("Compared five weighting configurations across", len(jobs), "jobs")

if __name__ == "__main__":
    main()
