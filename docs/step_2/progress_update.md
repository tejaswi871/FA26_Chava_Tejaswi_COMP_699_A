# Research Progress Update — Dataset and Evidence Review

Tejaswi Chava | NLP-Based Resume–Job Alignment | COMP 699 A

## Dataset expansion (Task 1)

Extended the research dataset in data/extension_1 with three job descriptions, nine resume profiles, and 27 resume–job relevance pairs. The additional examples cover operations coordination, customer support, and marketing assistance. Each job family includes strong, partial, and keyword-overlap cases. The original Week 2 benchmark (three jobs, eighteen resumes, 54 pairs) remains unchanged to preserve the existing evaluation results.

## Resume–job relevance labels (Task 2)

Applied the existing relevance rubric: 0 for no demonstrated task coverage, 1 for partial task coverage, and 2 for substantial task and tool coverage. The label_review.csv file records the rationale for nine representative cases. Other cross-domain pairs receive grade 0 because their profiles do not demonstrate the target job's tasks. The labels are based on the constructed examples; independent assessment has not yet been conducted.

## Ranking-error analysis (Task 5)

The Week 3 results identify cases in which technical terminology appears in resumes without evidence of the corresponding job duties. For J1, R12 ranked second under lexical, semantic, and hybrid matching despite describing software sales rather than hands-on data analysis. For J3, R18 ranked third under all three methods despite describing equipment marketing rather than technical troubleshooting.

At K=3, keyword-negative appearances totaled 3 for lexical, 2 for semantic, and 3 for hybrid matching. At K=5, all three methods recorded 3. These results apply to the original benchmark. The new examples have not yet been scored.

## Results and limitations

On the original benchmark, macro NDCG@3 was 0.724399 for lexical matching, 0.823093 for semantic matching, and 0.744880 for equal-weight hybrid matching. Semantic matching produced the highest value on this dataset. The benchmark uses a small number of synthetic job descriptions and author-assigned relevance labels, limiting conclusions beyond the evaluated examples.

## Reproducibility and next experiment

The original evaluation outputs remain in results/week_2 and results/week_3. The existing cutoff analysis can be reproduced with `python src/run_week3_evidence.py`. The dataset extension is stored separately to preserve the original benchmark.

The next experiment is to evaluate the additional resume–job pairs with the existing lexical, semantic, and hybrid methods, compare ranking metrics, and examine whether the previously observed ranking errors also appear in the expanded dataset.

## Progress status

Task 1 — Extend research dataset: completed.
Task 2 — Refine resume–job relevance labels: completed for the new examples; independent assessment pending.
Task 5 — Analyze ranking errors and limitations: completed for the existing experimental results.
Task 7 — Update research documentation: completed for this stage.
