# Expanded Dataset Evaluation — Current Status

The dataset extension contains three new jobs, nine resumes, and 27 author-provisional relevance grades. The original Week 2 benchmark contains three jobs, eighteen resumes, and 54 relevance grades.

## Completed comparison

The original benchmark's stored lexical and semantic scores were recombined at lexical weights 0.0, 0.3, 0.5, 0.7, and 1.0. The output files in results/weight_comparison contain macro Precision@3 and NDCG@3, plus per-job rankings. The semantic-only configuration obtained the highest macro NDCG@3 (0.8231). The 0.3 and 0.5 lexical-weight blends each obtained 0.7449; 0.7 lexical weight obtained 0.7244.

## Outstanding extension experiment

The additional J4–J6 / R19–R27 cases have **not** been scored by TF-IDF or MiniLM. Consequently, the repository does not yet contain valid ranking metrics for this extension. Existing Week 2 scores cannot be reused for these new texts.

To finish the extension comparison, rerun the existing scoring procedure with the nine new resume texts as the candidate collection, compute the lexical and semantic component scores, form the three agreed hybrid combinations, and evaluate the resulting rankings against data/extension_1/relevance_labels.csv. Preserve the original benchmark and its recorded metrics.

The new labels have not been independently reviewed. Do not interpret the extension's future results as a held-out test or a general measure of hiring effectiveness.
