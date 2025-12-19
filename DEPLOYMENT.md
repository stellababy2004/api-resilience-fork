# Deployment Runbook

## Prerequisites
- CI pipeline passing on main branch
- Environment variables configured
- Dependencies validated (no critical CVEs)

## Build & Test
```bash
pi## Local run
```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
uvicorn src.app:app --reloadp install -r requirements.txt
pytest


