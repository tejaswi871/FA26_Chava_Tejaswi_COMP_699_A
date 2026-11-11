"""Measure cutoff sensitivity using the frozen Week 2 rankings and labels."""

import csv
import hashlib
import json
from collections import defaultdict
from math import isclose, log2
from pathlib import Path
from statistics import mean

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data/week_2"
BASELINE = ROOT / "results/week_2"
OUT = ROOT / "results/week_3"
METHODS = ("lexical", "semantic", "hybrid")
CUTOFFS = (1, 3, 5)


def read_rows(path):
    with path.open(encoding="utf-8", newline="") as source:
        return list(csv.DictReader(source))


def write_rows(name, rows):
    with (OUT / name).open("w", encoding="utf-8", newline="") as output:
        writer = csv.DictWriter(output, fieldnames=list(rows[0]), lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)


def discounted_gain(grades):
    return sum((2**grade - 1) / log2(i + 2) for i, grade in enumerate(grades))


def run():
    manifest = json.loads((DATA / "manifest.json").read_text())
    for name, digest in manifest["sha256"].items():
        if hashlib.sha256((DATA / name).read_bytes()).hexdigest() != digest:
            raise ValueError(f"Frozen benchmark file changed: {name}")
    labels = defaultdict(dict)
    for row in read_rows(DATA / "relevance_labels.csv"):
        job_labels = labels[row["job_id"]]
        grade = int(row["relevance"])
        if row["resume_id"] in job_labels or grade not in (0, 1, 2):
            raise ValueError(f"Duplicate or invalid label: {row}")
        job_labels[row["resume_id"]] = grade

    negative_ids = {
        row["resume_id"] for row in read_rows(DATA / "added_scenarios.csv")
        if row["scenario"] == "keyword_negative"
    }
    rankings = defaultdict(list)
    for row in read_rows(BASELINE / "rankings.csv"):
        rankings[row["method"], row["job_id"]].append(row)
    if rankings.keys() != {(method, job) for method in METHODS for job in labels}:
        raise ValueError("Missing or unexpected method/job groups")

    original = {(r["method"], r["job_id"]): r for r in read_rows(BASELINE / "metrics_by_job.csv")}
    metrics = []
    negatives = []
    for method in METHODS:
        for job, expected in sorted(labels.items()):
            rows = sorted(rankings[method, job], key=lambda r: int(r["rank"]))
            ids = [r["resume_id"] for r in rows]
            if len(ids) != len(expected) or set(ids) != expected.keys() or len(ids) < max(CUTOFFS):
                raise ValueError(f"Incomplete or duplicated candidate pool: {method}, {job}")
            grades = [expected[rid] for rid in ids]
            if any(int(r["rank"]) != i or int(r["relevance"]) != g
                   for i, (r, g) in enumerate(zip(rows, grades), 1)):
                raise ValueError(f"Ranks or labels disagree: {method}, {job}")
            for k in CUTOFFS:
                ideal = discounted_gain(sorted(grades, reverse=True)[:k])
                precision = sum(g >= 1 for g in grades[:k]) / k
                ndcg = discounted_gain(grades[:k]) / ideal if ideal else 0.0
                if k == 3 and not all(
                    isclose(value, float(original[method, job][name]), rel_tol=0, abs_tol=1e-12)
                    for name, value in (("precision_at_3", precision), ("ndcg_at_3", ndcg))
                ):
                    raise ValueError(f"Week 2 top-three metrics disagree: {method}, {job}")
                metrics.append(dict(method=method, job_id=job, k=k, precision=precision, ndcg=ndcg))
            for rank, (rid, grade) in enumerate(zip(ids, grades), 1):
                if rid in negative_ids:
                    negatives.append(dict(method=method, job_id=job, resume_id=rid, rank=rank, grade=grade))
    macro = []
    for method in METHODS:
        for k in CUTOFFS:
            group = [r for r in metrics if r["method"] == method and r["k"] == k]
            macro.append(dict(method=method, k=k, jobs=len(group),
                              precision=mean(r["precision"] for r in group),
                              ndcg=mean(r["ndcg"] for r in group),
                              keyword_negatives_in_top_k=sum(
                                  r["method"] == method and r["rank"] <= k for r in negatives)))
    OUT.mkdir(parents=True, exist_ok=True)
    write_rows("cutoff_metrics_by_job.csv", metrics)
    write_rows("cutoff_metrics_macro.csv", macro)
    write_rows("keyword_negative_ranks.csv", negatives)
    print("Checked frozen inputs, complete rankings, and nine Week 2 top-three metric rows.")


if __name__ == "__main__":
    run()
