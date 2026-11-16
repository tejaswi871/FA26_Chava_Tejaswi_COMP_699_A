# Step 2 — Consolidated Research Report

**NLP-Based Resume–Job Alignment Using Lexical and Semantic Matching**  
Tejaswi Chava | COMP 699 A | November 2026

## 1. Research Foundation

**Research question.** Does combining semantic similarity with lexical matching improve the ranking of resumes relevant to a job description compared with lexical matching alone?

The research evaluates text-based relevance rankings rather than hiring suitability. The working hypothesis is that semantic representations may recognize relevant qualifications expressed using different wording. Evidence consists of candidate rankings, graded relevance labels, Precision@3, NDCG@3, and case-level error observations.

The initial research inputs were three synthetic job descriptions and nine synthetic resume profiles (27 pairs), representing data analysis, web development, and IT support. Relevance grades were assigned before scoring using 0 for no demonstrated task coverage, 1 for partial coverage, and 2 for substantial task and tool coverage. These labels are author judgments rather than independent assessments. Week 1 established the computational environment, checked input integrity, and generated TF-IDF cosine-similarity rankings. Eleven initial checks passed. The original benchmark exposed lexical-matching weaknesses involving paraphrases and irrelevant terminology.

## 2. Method and Baseline

Week 2 expanded and froze the benchmark to three jobs, eighteen resumes, and 54 labeled pairs. Input hashes are recorded in data/week_2/manifest.json. The methods are (1) unigram TF-IDF cosine similarity, (2) pretrained MiniLM sentence embeddings with cosine similarity, and (3) an equal-weight hybrid of those scores. The MiniLM model uses a pinned full-precision ONNX export, attention-mask mean pooling, and L2 normalization. No model fine-tuning or supervised training was conducted.

Each method ranks the same candidates for each job. Ties are broken by resume identifier. Precision@3 counts grade-1 and grade-2 resumes in the first three results. NDCG@3 uses exponential relevance gains and logarithmic rank discounting, normalized by the ideal ranking. Macro results average equally across the three job descriptions.

**Recorded Week 2 baseline results:**

| Method | Precision@3 | NDCG@3 |
| --- | ---: | ---: |
| Lexical | 0.6667 | 0.7244 |
| Semantic | 0.7778 | 0.8231 |
| Equal-weight hybrid | 0.6667 | 0.7449 |

The equal-weight hybrid improved NDCG@3 slightly over lexical matching, but semantic-only scoring performed best overall. The Week 2 implementation passed ten automated numerical and scoring checks. Source code, requirements, recorded rankings, and evaluation outputs are preserved in the repository.

## 3. Preliminary Evidence

Week 3 examined rankings at cutoffs K = 1, 3, and 5. All methods achieved Precision@1 and NDCG@1 of 1.0 on the three constructed jobs. At K = 5, lexical Precision was 0.6000 and NDCG was 0.7337; semantic Precision was 0.8000 and NDCG was 0.9049; hybrid Precision was 0.8000 and NDCG was 0.8892.

The error analysis identified misleading keyword overlap. For the data analyst job, resume R12 described software sales rather than hands-on analysis but ranked second under all three methods. For IT support, resume R18 described equipment marketing rather than troubleshooting but ranked third under all three methods. This illustrates that similarity scores may reward related terminology without establishing actual task experience.

An additional dataset extension includes three job descriptions (operations coordination, customer service, and marketing assistance), nine resumes, and 27 provisional relevance labels. The extension is stored separately from the frozen benchmark. **It has not yet been scored with the lexical, semantic, or hybrid models**, so no new performance results are claimed for it.

A follow-up analysis combined the **previously recorded** lexical and semantic component scores with alternative weights. These are post-hoc comparisons on the original benchmark, not a held-out model-selection experiment:

| Lexical weight | Semantic weight | Precision@3 | NDCG@3 |
| ---: | ---: | ---: | ---: |
| 0.0 | 1.0 | 0.7778 | 0.8231 |
| 0.3 | 0.7 | 0.6667 | 0.7449 |
| 0.5 | 0.5 | 0.6667 | 0.7449 |
| 0.7 | 0.3 | 0.6667 | 0.7244 |
| 1.0 | 0.0 | 0.6667 | 0.7244 |

The additional weight settings did not outperform semantic-only ranking on the original three jobs. These comparisons use the same job descriptions and relevance judgments as the initial experiment and therefore do not establish out-of-sample performance.

## 4. Project Completion Plan

The next experiment will apply the existing TF-IDF and pinned MiniLM procedures to the separate extension dataset, generate its component scores, and calculate Precision@3 and NDCG@3 for each method. The experiment should document the different candidate pool and refrain from treating raw cosine scores across datasets as directly comparable.

Further work will review provisional relevance labels independently where feasible, investigate keyword-heavy negative examples, and compare weight settings on a development set distinct from any final evaluation set. Findings will be reported with per-job results and explicit limitations. The current evidence supports a reproducible computational comparison but does not establish general effectiveness for real applicant screening.

## Reproducibility and References

The repository retains the original notebook in src/week1_resume_job_foundation.ipynb, pinned dependencies in src/requirements_week2.txt, Week 3 analysis in src/run_week3_evidence.py, and the additional weight comparison in src/run_weight_comparison.py. Results are in results/week_2, results/week_3, and results/weight_comparison.

Relevant background includes Reimers and Gurevych (2019), *Sentence-BERT*, EMNLP-IJCNLP, https://aclanthology.org/D19-1410/; the all-MiniLM-L6-v2 model card at https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2; and scikit-learn documentation for TfidfVectorizer and ndcg_score.

**Research limitation.** The experiments rely on small, deliberately constructed synthetic data, author-assigned relevance judgments, and repeated evaluation on the same benchmark. The results are descriptive and preliminary, not a final conclusion.
