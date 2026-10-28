# NLP-Based Resume-Job Alignment

## Research question
I am investigating whether combining semantic similarity with lexical matching improves identification of relevant resume-job qualifications compared with lexical matching alone. My working hypothesis is that semantic information may help with differently worded qualifications.

## Week 1 progress
I created 3 fictional job descriptions, 9 fictional resumes, and 27 labeled pairs. I implemented unigram TF-IDF cosine similarity and generated initial rankings. All 11 validation checks passed. Semantic matching, hybrid scoring, and comparative ranking metrics remain planned.

## Run
Install dependencies with `python -m pip install -r src/requirements.txt`. Open `src/week1_resume_job_foundation.ipynb` in Jupyter from the repository root or src folder. Select the Python kernel, restart it, run all cells, and save the notebook. Outputs are recreated under `results/week_1/`. No separate Python script or internet connection is required after dependency installation.

## Organization
- `src/`: executed notebook and dependencies.
- `results/week_1/`: inputs, labels, rankings, checks, and execution/environment summaries.
- `docs/step_2/week_1/`: research foundation report and progress note.

## Limitations and next work
My small synthetic sample and author-defined grades do not establish hiring suitability or real-world effectiveness. I will expand and freeze the inputs and rubric, add sentence embeddings, predeclare hybrid weights, and implement validated Precision@K and NDCG comparisons. Any tuning will be separated from evaluation.
