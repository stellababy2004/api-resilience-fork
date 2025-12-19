# API Resilience Fork – CVE Remediation & CI/CD Gates

This repository is a **resilience fork of a production API**, maintained with a strict security-first approach.

## Objectives
- Maintain a **stable, deploy-ready branch** at any time
- Integrate **security patches and CVE remediations**
- Enforce **CI/CD quality gates** (tests, coverage, vulnerability scanning)
- Ensure full **traceability** between vulnerabilities, fixes and commits

## Key Deliverables
- **Code & Artifacts:** secured fork with clean commit history dedicated to security fixes
- **Process:** CI pipeline failing on new CVEs or coverage regression
- **Documentation:** deployment runbook and CVE catalog (impact → fix → commit)

## Documentation
- [CVE Catalog](CVE_CATALOG.md)
- [Deployment Runbook](DEPLOYMENT.md)
- [Security Policy](SECURITY.md)

## Status
This repository is actively maintained as a security-focused resilience branch.
