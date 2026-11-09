# Week 1 Research Foundation

## Research question and hypothesis
Does combining semantic similarity with lexical matching improve identification of relevant resume-job qualifications compared with lexical matching alone? The working hypothesis is that semantic information may help with differently worded qualifications. The combined method remains to be implemented.

## Intended evidence
The planned comparison evaluates lexical and hybrid rankings against predefined relevance grades using Precision@K and NDCG. Week 1 establishes feasibility through input tables, integrity checks, and initial lexical rankings.

## Research inputs
The benchmark contains 3 fictional jobs and 9 fictional resumes spanning data analysis, web development, and IT support, giving 27 pairs. Each family includes direct wording, paraphrased wording, and partial qualifications. The rubric assigns grades before scoring: 2 for substantial intended task/tool coverage, 1 for partial coverage, and 0 for no relevant evidence in this toy scenario. These are author-defined judgments, not independent annotations or hiring suitability labels. No personal resumes are used.

## Environment and organization
The analysis is in src/week1_resume_job_foundation.ipynb. Dependencies are in src/requirements.txt. The recorded environment uses Python 3.12.8, NumPy 1.26.4, pandas 2.2.3, and scikit-learn 1.6.1. The notebook records versions in results/week_1/environment.json and saves inputs, rankings, and check results under results/week_1/. No separate Python script is required.

## Execution instructions
Install dependencies with python -m pip install -r src/requirements.txt from the repository root. Open the notebook in Jupyter from the root or src folder, restart the Python kernel and run through the Week 2 plan heading. The next section begins the Week 2 experiment. Outputs are overwritten under results/week_1/. No internet connection is needed after dependency installation.

## Current accomplishments
The notebook checks the inputs, fits unigram TF-IDF on the resumes, transforms jobs with that vocabulary, and calculates cosine similarity. The baseline uses the default tokenizer, retains stop words, and breaks ties by resume ID. The vocabulary has 81 terms. All 11 checks passed, covering IDs, text completeness, missing values, pair uniqueness and coverage, references and grades, bounded finite scores, self-similarity, and unknown vocabulary. Top pairs were J1-R1 (0.806630), J2-R4 (0.873329), and J3-R7 (0.879927). J1 ranked irrelevant R6 above partial R3. Semantic matching and comparative metrics belong to the Week 2 experiment.

## Problems and boundaries
The sample is small and constructed; labels simplify qualifications and lack independent validation. Generic words can distort rankings, paraphrases may be missed, and TF-IDF does not reliably interpret negation. Passing checks does not validate relevance judgments. These outputs do not establish real-world hiring effectiveness.

## Week 2 plan
The Week 2 plan calls for a frozen dataset and rubric, a documented pretrained encoder, predefined hybrid weights, and known-example tests for Precision@K and NDCG. Both methods use the same candidates. Failure analysis uses the predefined labels, and any future tuning takes place on separate development cases.
