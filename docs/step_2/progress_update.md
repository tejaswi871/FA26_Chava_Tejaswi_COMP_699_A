# Coursework Progress Update — Dataset and Evidence Review

Tejaswi Chava | NLP-Based Resume–Job Alignment | COMP 699 A

## Dataset expansion (Task 1)

Added a separate synthetic extension at data/extension_1 containing three additional job descriptions, nine additional resumes, and 27 relevance pairs. The examples cover operations coordination, customer support, and marketing assistance. Each family includes a direct match, a partial match, and a keyword-heavy negative example. The Week 2 frozen benchmark (three jobs, eighteen resumes, 54 pairs) remains untouched.

## Relevance-label refinement (Task 2)

Retained the Week 2 grading rubric (0 = no task coverage, 1 = partial, 2 = substantial). The new label_review.csv records the rationale for the nine central constructed cases. Cross-domain pairs are graded zero because the written resumes do not demonstrate the target job's tasks. These are provisional author judgments, not independent reviewer assessments. Independent validation remains a limitation, not a completed activity.

## Ranking-error review (Task 5)

The previously recorded Week 3 experiment identified keyword-heavy negative cases. For J1, R12 (sales of software, without hands-on analysis) ranked second under lexical, semantic, and hybrid methods. For J3, R18 (marketing equipment without troubleshooting experience) ranked third under all three methods. At K=3, keyword-negative appearances totaled 3 for lexical, 2 for semantic, and 3 for hybrid; at K=5, all three methods had 3. These observations are from the original frozen benchmark only.

This suggests that topical word overlap can outrank evidence of actually performing the requested work. It does not establish the same behavior on real resumes or on the new extension. The new examples deliberately test similar ambiguities, but no new ranking experiment has yet been run.

## Interpretation and limitations

On the original benchmark, semantic-only achieved the strongest macro NDCG@3 (0.823093), compared with lexical (0.724399) and the equal-weight hybrid (0.744880). The sample is small and synthetic, relevance judgments are author-assigned, and the ranking cutoffs reuse the same candidates. Results are descriptive rather than generalizable. Expanding the dataset increases coverage but does not by itself improve the validity of the measured model performance.

## Reproducibility and next step

Original results remain in results/week_2 and results/week_3; rerun the existing Week 3 analysis with python src/run_week3_evidence.py. The new extension is intentionally separate. The next modest coursework experiment is to score the extension with the existing three methods, report the same ranking metrics, and document whether the previously observed error patterns recur. No new model or application architecture is required.

## Task tracking

Task 1 — Expanded sample dataset: completed as a separate, unscored extension.
Task 2 — Refined relevance labels: completed for documented author-provisional grading; independent validation not performed.
Task 5 — Document ranking errors and limitations: completed for existing recorded evidence; extension results not yet available.
Task 7 — Repository documentation: updated with this progress note and dataset documentation.
