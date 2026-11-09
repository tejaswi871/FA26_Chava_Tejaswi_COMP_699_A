# Week 1 Progress

The benchmark contains 3 fictional job descriptions, 9 fictional resumes, and 27 labeled pairs. Grades were set before scoring. A grade of 2 indicates substantial task and tool coverage, 1 indicates partial coverage, and 0 indicates no relevant evidence in the scenario.

The lexical baseline fits unigram TF-IDF on resumes, transforms jobs using the same vocabulary, and ranks candidates by cosine similarity with resume ID as the tie-breaker. The run saved inputs, labels, rankings, checks, and environment details. The vocabulary contains 81 terms, and all 11 checks passed.

Direct-wording candidates ranked first for each job. For J1, irrelevant R6 ranked above partially relevant R3. The small synthetic sample, author-defined labels, and simplified job families limit the comparison. Generic words and negation can also affect the rankings.

The Week 2 plan adds a frozen benchmark, a pretrained sentence encoder, a fixed hybrid rule, and known-example tests for Precision@K and NDCG. Any later tuning uses separate development cases.
