# NLP-Based Resume-Job Alignment

## Research question
Does combining semantic similarity with lexical matching improve the ranking of relevant resumes compared with lexical matching alone? The working hypothesis is that semantic similarity may help when resumes and job descriptions express the same qualifications in different words.

## Week 1 progress
The Week 1 baseline used unigram TF-IDF cosine similarity to rank 9 fictional resumes for 3 fictional job descriptions. All 11 validation checks passed across the 27 labeled pairs.

### Reproduce Week 1
Install dependencies with `python -m pip install -r src/requirements.txt`. Open `src/week1_resume_job_foundation.ipynb` in Jupyter from the repository root or `src/`. Run the cells through the **Week 2 plan** heading and stop before the Week 2 implementation. Week 1 recreates its outputs under `results/week_1/` and can run offline after dependency installation.

## Organization
- `src/`: executed notebook and dependencies.
- `results/week_1/`: inputs, labels, rankings, checks, and execution/environment summaries.
- `docs/step_2/week_1/`: research foundation report and progress note.

## Week 2: method implementation and baseline experiment
Week 2 compares pretrained MiniLM semantic scoring and an equal-weight lexical/semantic hybrid with the lexical baseline. The fixed synthetic benchmark contains 3 jobs, 18 resumes, and 54 labeled pairs. Precision@3 measures how many of the first three results are relevant, and NDCG@3 gives more weight to highly relevant resumes near the top.

### Reproduce Week 2
Install dependencies in the same environment as the notebook kernel:
```bash
python -m pip install -r src/requirements_week2.txt
```
Open `src/week1_resume_job_foundation.ipynb` from the repository root or src folder, restart the kernel and run all cells in order. Week 2 starts after the original Week 2 plan. Its first model download requires internet and approximately 91 MB; subsequent runs reuse `.cache/minilm/`. No separate scoring scripts are required. The notebook verifies the committed inputs in `data/week_2/` before model setup and recreates outputs in `results/week_2/`. To regenerate the benchmark explicitly, run `python src/export_week2_benchmark.py path/to/new-directory` from the repository root. Choose a new directory with an existing parent.

### Initial measurements
| Method | Macro Precision@3 | Macro NDCG@3 |
|---|---:|---:|
| Lexical | 0.666667 | 0.724399 |
| Semantic | 0.777778 | 0.823093 |
| Hybrid | 0.666667 | 0.744880 |

All 10 method tests passed. The hybrid improved NDCG@3 on one job and tied the lexical baseline on Precision@3. Semantic scoring led on both macro averages. Some resumes that explicitly lacked a qualification still ranked highly. The measurements describe a small synthetic benchmark with author-assigned labels.

### Week 2 files
- `src/week1_resume_job_foundation.ipynb`: methods, validation, and observations for the Week 1 baseline followed by the Week 2 comparison.
- `src/requirements_week2.txt`: tested dependencies; Jupyter and ipykernel can be installed separately if needed.
- `data/week_2/`: frozen synthetic inputs, relevance rubric, scenario rationales and protocol manifest.
- `results/week_2/`: complete rankings, metrics, validation log, repeatability evidence and exact execution environment.
- `docs/step_2/week_2/method_and_baseline.pdf`: required milestone report, with editable Markdown.
- `src/build_week2_report.py`: optional report renderer; run from any directory after results exist.

The execution summary records the Python environment used to produce the saved outputs. Model weights are cached locally and excluded from Git. Next steps include expanding the benchmark and collecting independent relevance judgments before any tuning.

## Week 3 preliminary evidence

The cutoff analysis compares lexical, MiniLM semantic, and equal-weight hybrid rankings at K = 1, 3, and 5. It also traces the ranks of three keyword-heavy negative resumes across all jobs.

Run `python src/run_week3_evidence.py` from the repository root to recreate the tables in `results/week_3/`. The script uses only the Python standard library. The notebook also contains an executable Week 3 section with the same analysis and recorded observations.

- [Preliminary evidence report](docs/step_2/week_3/preliminary_evidence.pdf)
- [Editable report](docs/step_2/week_3/preliminary_evidence.md)
