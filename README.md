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

## Week 2: method implementation and baseline experiment
I extended my Week 1 notebook with pretrained MiniLM semantic scoring, an equal-weight lexical/semantic hybrid, and a controlled comparison with the lexical baseline. My fixed synthetic benchmark contains 3 jobs, 18 resumes and 54 labeled pairs. I use Precision@3 and NDCG@3 to record initial evidence rather than final research conclusions.

### Reproduce Week 2
Install dependencies in the same environment as the notebook kernel:
```bash
python -m pip install -r src/requirements_week2.txt
```
Open `src/week1_resume_job_foundation.ipynb` from the repository root or src folder, restart the kernel and run all cells in order. Week 2 starts after the original Week 2 plan. Its first model download requires internet and approximately 91 MB; subsequent runs reuse `.cache/minilm/`. No separate scoring scripts are required. Generated files under data/week_2/ and results/week_2/ are recreated when the notebook runs.

### Initial measurements
| Method | Macro Precision@3 | Macro NDCG@3 |
|---|---:|---:|
| Lexical | 0.666667 | 0.724399 |
| Semantic | 0.777778 | 0.823093 |
| Hybrid | 0.666667 | 0.744880 |

All 10 method tests passed. Hybrid NDCG@3 improves on one job, with no Precision@3 improvement. Semantic-only performs best on this small constructed benchmark. Keyword-negative failures remain. My inputs and labels are synthetic; these actual computational measurements do not establish real-world hiring effectiveness.

### Week 2 files
- `src/week1_resume_job_foundation.ipynb`: implemented methods, experiment, validation and observations; original Week 1 cells preserved.
- `src/requirements_week2.txt`: tested dependencies; Jupyter and ipykernel can be installed separately if needed.
- `data/week_2/`: frozen synthetic inputs, relevance rubric, scenario rationales and protocol manifest.
- `results/week_2/`: complete rankings, metrics, validation log, repeatability evidence and exact execution environment.
- `docs/step_2/week_2/method_and_baseline.pdf`: required milestone report, with editable Markdown.
- `src/build_week2_report.py`: optional report renderer; run from any directory after results exist.

The saved Week 2 outputs were generated in the recorded Python environment; rerunning on another operating system may change timing or floating-point details. Model weights are excluded from Git. I used AI assistance during implementation and reviewed the notebook and computed evidence. Week 3 experiments, independent evaluation and the final combined submission remain planned.
