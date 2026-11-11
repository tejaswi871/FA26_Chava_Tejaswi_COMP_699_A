# Preliminary Evidence

**NLP-Based Resume-Job Alignment**

Tejaswi Chava | COMP 699 A | Step 2, Week 3

## 1. Research question and working hypothesis

Does combining semantic similarity with lexical matching improve the ranking of relevant resumes over lexical matching alone? Semantic similarity may help with differently worded qualifications. The fixed blend is expected to help in some cases.

## 2. Preliminary analysis

The cutoff analysis compares lexical, MiniLM semantic, and equal-weight hybrid rankings at K = 1, 3, and 5. It also traces the ranks of three keyword-heavy negative resumes across all jobs.

## 3. Inputs, conditions, and measurements

The source inputs are 3 synthetic job descriptions, 18 synthetic resumes, and 54 author-graded pairs frozen in data/week_2. The analysis reads Week 2 rankings, retaining the candidate pool, scores, and resume-ID tie break. The hybrid weights remain 0.50 lexical and 0.50 semantic.

Precision@K treats grades 1 and 2 as relevant. NDCG@K discounts gains of 2^grade - 1 by log2(rank + 1), normalized to the ideal order for each job. Macro values average the three jobs equally. Keyword-negative counts sum appearances among the top K across jobs.

## 4. Preliminary results

| Method | K | Precision | NDCG | Keyword negatives |
| --- | --- | --- | --- | --- |
| Lexical | 1 | 1.0000 | 1.0000 | 0 |
| Semantic | 1 | 1.0000 | 1.0000 | 0 |
| Hybrid | 1 | 1.0000 | 1.0000 | 0 |
| Lexical | 3 | 0.6667 | 0.7244 | 3 |
| Semantic | 3 | 0.7778 | 0.8231 | 2 |
| Hybrid | 3 | 0.6667 | 0.7449 | 3 |
| Lexical | 5 | 0.6000 | 0.7337 | 3 |
| Semantic | 5 | 0.8000 | 0.9049 | 3 |
| Hybrid | 5 | 0.8000 | 0.8892 | 3 |

Source: cutoff_metrics_macro.csv. Per-job metrics and individual negative ranks are saved alongside it.

## 5. Evidence and interpretation

All three methods tie at K = 1. At K = 5, the hybrid improves macro precision from 0.6000 to 0.8000 and NDCG from 0.7337 to 0.8892 versus lexical scoring. Semantic-only ties hybrid precision and leads NDCG at both K = 3 and 5. The blend therefore adds value over the lexical baseline at some depths, while semantic-only remains the strongest ranking reference on this sample.

At K = 3, semantic scoring returns two keyword negatives across the three jobs, compared with three for the other methods. At K = 5, each method returns three. R12 remains second for J1 and R18 remains third for J3 under all three methods. These examples point to persistent sensitivity to technical wording.

## 6. Validity and reproducibility

The script verifies the input hashes, checks candidate coverage and rank/grade alignment, and reproduces all nine Week 2 per-job top-three measurements within 1e-12. Run python src/run_week3_evidence.py from the repository root with Python 3.12. This deterministic analysis uses the checked-in ranks and labels. Reproducing the underlying scores requires the Week 2 notebook and pinned model.

Three constructed queries and author-assigned grades limit inference. Cutoffs reuse the same rankings and are correlated. The negative cases were built to diagnose topical overlap and may be more obvious than real resumes. The results support descriptive claims about this benchmark.

## 7. Research design revision

Keep the research question and make semantic-only a required reference. Report performance across prespecified cutoffs and track keyword negatives separately. Reserve weight selection for a separate development set. The current claim is limited to the observed ranking depths and benchmark.

## 8. Prioritized next research tasks

1. Add job queries and more varied qualification and negation examples.

2. Collect independent relevance judgments with a documented rubric.

3. Freeze a held-out set and predeclare evaluation cutoffs.

4. Compare candidate blend weights on development data and evaluate the chosen rule on held-out queries.
