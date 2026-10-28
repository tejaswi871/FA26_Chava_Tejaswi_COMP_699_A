# Week 1 research progress

I generated 3 fictional job descriptions, 9 fictional resumes, and 27 labeled pairs. I assigned relevance grades before scoring: 2 for substantial intended task/tool coverage, 1 for partial coverage, and 0 for no relevant evidence in this constructed scenario.

I fitted unigram TF-IDF on resumes, transformed jobs using that vocabulary, and computed cosine similarities. I generated rankings with resume ID as the tie-breaker and saved inputs, labels, rankings, checks, and execution/environment summaries. The vocabulary contains 81 terms and all 11 checks passed.

Direct-wording candidates ranked first for each job. For J1, irrelevant R6 ranked above partial R3. I have not implemented semantic matching or comparative ranking metrics. My main limitations are the small synthetic sample, author-defined labels, simplified job families, generic words, and negation.

Next I will expand and freeze the dataset and rubric, add a documented sentence-embedding model, specify hybrid weights, and implement validated Precision@K and NDCG comparisons. Any tuning will be separated from evaluation.
