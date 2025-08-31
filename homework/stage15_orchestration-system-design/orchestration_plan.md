# Orchestration Plan — Mock Analysis Project

## 1. Project Task Decomposition

| Task            | Inputs               | Outputs            | Idempotent |
|-----------------|-------------------|------------------|------------|
| ingest          | /data/raw.ext      | prices_raw.json  | True       |
| clean           | prices_raw.json    | prices_clean.json | True       |
| train_or_score  | prices_clean.json  | model.json       | True       |
| report          | model.json         | report.txt       | True       |

**Notes:**  
- Tasks are designed to be idempotent: rerunning will produce the same outputs given the same inputs.

---

## 2. Dependencies (DAG)
**Description:**  
- `ingest` must complete before `clean`.  
- `clean` outputs feed into `train_or_score`.  
- `report` depends on the trained model output.  
- Tasks are mostly sequential; parallelization is limited in this small workflow.

---

## 3. Logging & Checkpoints Plan

| Task            | Log Messages                       | Checkpoint Artifact       |
|-----------------|-----------------------------------|--------------------------|
| ingest          | start/end, rows processed, source URI | prices_raw.json          |
| clean           | start/end, rows in/out             | prices_clean.json        |
| train_or_score  | start/end, params, metrics         | model.json               |
| report          | start/end, artifact path           | report.txt               |

**Notes:**  
- Logging is written to console or file; critical metrics (row counts, MAE, AUC) included.  
- Checkpoints allow recovery if later tasks fail.

---

## 4. Right-Sizing Automation

- **Automate now:**  
  - `ingest`, `clean`, `train_or_score` tasks. These are repetitive, deterministic, and suitable for automation.  
- **Manual:**  
  - `report` generation may include narrative commentary and visual inspection; automating fully may reduce interpretability.  

**Rationale:** Focus automation on deterministic, repeatable tasks to reduce human error, while leaving interpretive or descriptive tasks semi-manual.

---

## 5. (Stretch) Refactor One Task into Function + CLI

```python
import argparse, json, logging, sys
from datetime import datetime
from pathlib import Path

def ingest_task(input_path: str, output_path: str) -> None:
    """Ingest raw data → save JSON."""
    logging.info('[ingest_task] start: %s', input_path)
    # TODO: implement actual ingestion logic
    result = {'run_at': datetime.utcnow().isoformat(), 'note': 'replace with real output'}
    Path(output_path).parent.mkdir(parents=True, exist_ok=True)
    Path(output_path).write_text(json.dumps(result, indent=2))
    logging.info('[ingest_task] wrote %s', output_path)

def main(argv=None):
    parser = argparse.ArgumentParser(description='Ingest Task CLI')
    parser.add_argument('--input', required=True)
    parser.add_argument('--output', required=True)
    args = parser.parse_args(argv)
    logging.basicConfig(level=logging.INFO, handlers=[logging.StreamHandler(sys.stdout)])
    ingest_task(args.input, args.output)

if __name__ == '__main__':
    main(['--input', 'data/raw.ext', '--output', 'data/prices_raw.json'])
