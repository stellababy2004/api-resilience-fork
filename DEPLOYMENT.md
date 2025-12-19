# Deployment Runbook

## Prerequisites
- CI pipeline passing on main branch
- Environment variables configured
- Dependencies validated (no critical CVEs)

## Build & Test
```bash
pip install -r requirements.txt
pytest
