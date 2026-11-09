"""Export the original Week 2 synthetic benchmark to a new directory."""

import argparse
import csv
import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
INPUT_FIELDS = {
    "jobs.csv": ("job_id", "title", "text"),
    "resumes.csv": ("resume_id", "text"),
    "relevance_labels.csv": ("job_id", "resume_id", "relevance"),
    "added_scenarios.csv": ("resume_id", "scenario", "intended_family", "rationale"),
}
SCENARIOS = [
    ('R10',
     'Used Python and SQL to clean sales datasets, build dashboards, and explain trends to managers.',
     'J1', 2, 'direct'),
    ('R11',
     'Prepared monthly business charts in spreadsheets; learning to query tables but no completed database projects.',
     'J1', 1, 'partial'),
    ('R12',
     'Sold software subscriptions to clients seeking Python SQL data analysis and dashboards; no hands-on analysis experience.',
     None, 0, 'keyword_negative'),
    ('R13',
     'Implemented JavaScript components with HTML and CSS, tested mobile layouts and responsive web pages.',
     'J2', 2, 'direct'),
    ('R14',
     'Created page wireframes and visual prototypes; collaborated with developers without implementing browser code.',
     'J2', 1, 'partial'),
    ('R15',
     'Recruited JavaScript HTML CSS web developers; reviewed applicants but did not build or test websites.',
     None, 0, 'keyword_negative'),
    ('R16',
     'Diagnosed Windows workstation failures, repaired network connections and resolved help desk support tickets.',
     'J3', 2, 'direct'),
    ('R17',
     'Helped colleagues reset account passwords and install desktop apps; escalated network faults to technicians.',
     'J3', 1, 'partial'),
    ('R18',
     'Marketed Windows computers and network equipment to help desk departments; did not troubleshoot technical issues.',
     None, 0, 'keyword_negative'),

]
RATIONALES = {
    2: "Substantial task/tool coverage",
    1: "Partial task coverage",
    0: "Mentions target tools in nontechnical role; explicitly lacks task experience",
}


def read_week1(name):
    with (ROOT / "results/week_1" / name).open(encoding="utf-8", newline="") as source:
        return list(csv.DictReader(source))


def export_benchmark(destination):
    manifest_path = ROOT / "data/week_2/manifest.json"
    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    jobs = read_week1("jobs.csv")
    resumes = read_week1("resumes.csv")
    labels = read_week1("relevance_labels.csv")
    metadata = []
    for resume_id, text, family, grade, scenario in SCENARIOS:
        resumes.append({"resume_id": resume_id, "text": text})
        metadata.append({
            "resume_id": resume_id,
            "scenario": scenario,
            "intended_family": family or "none",
            "rationale": RATIONALES[grade],
        })
        for job in jobs:
            job_id = job["job_id"]
            labels.append({
                "job_id": job_id,
                "resume_id": resume_id,
                "relevance": grade if job_id == family else 0,
            })

    destination.mkdir()
    for name, rows in zip(INPUT_FIELDS, (jobs, resumes, labels, metadata)):
        with (destination / name).open("w", encoding="utf-8", newline="") as output:
            writer = csv.DictWriter(output, fieldnames=INPUT_FIELDS[name])
            writer.writeheader()
            writer.writerows(rows)
    manifest["sha256"] = {
        name: hashlib.sha256((destination / name).read_bytes()).hexdigest()
        for name in sorted(INPUT_FIELDS)
    }
    with (destination / "manifest.json").open("w", encoding="utf-8", newline="\n") as output:
        output.write(json.dumps(manifest, indent=2) + "\n")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("destination", type=Path, help="New output directory with an existing parent")
    args = parser.parse_args()
    try:
        export_benchmark(args.destination)
    except FileExistsError:
        parser.exit(1, f"Destination already exists: {args.destination}\n")
    print(f"Exported benchmark to {args.destination}")
