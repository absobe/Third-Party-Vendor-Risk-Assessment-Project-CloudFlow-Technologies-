# Scripts README

**This is a fictional cybersecurity case study created for educational and portfolio purposes.**

This folder contains Python utilities that recalculate scores, generate charts, rebuild workbooks and evidence PDFs, and validate that the project package is complete.

## Environment

From the repository root:

```bash
python3 -m venv .venv
```

macOS / Linux:

```bash
source .venv/bin/activate
```

Windows (PowerShell):

```powershell
.venv\Scripts\activate
```

```bash
pip install -r requirements.txt
```

Packages actually used: `pandas` (available for analysis), `openpyxl` (workbooks), `matplotlib` (charts), `reportlab` (evidence PDFs).

## Commands

Recalculate inherent and residual scores, print High/Moderate/Low counts, and the overall vendor score:

```bash
python 14_Scripts/calculate_risk_scores.py
```

Generate scorecard bar chart and residual heat map:

```bash
python 14_Scripts/generate_scorecard.py
```

Rebuild Excel workbooks from `project_data.py` (overwrites xlsx files):

```bash
python 14_Scripts/generate_excel.py
```

Rebuild fictional evidence PDFs:

```bash
python 14_Scripts/generate_pdfs.py
```

Validate directories, files, unique risk IDs, formulas, treatments, owners, and final-report coverage:

```bash
python 14_Scripts/validate_project.py
```

Expected validation footer:

```text
PROJECT VALIDATION
------------------
Directories: PASS
Core Documents: PASS
Risk Register: PASS
Evidence Mapping: PASS
Remediation Mapping: PASS
Risk Treatment Mapping: PASS
Scorecard: PASS

OVERALL STATUS: PASS
```

## Canonical figures (do not drift)

| Item | Value |
| --- | --- |
| Overall vendor score | 74.4 |
| Overall residual risk | High |
| Recommendation | Conditional Approval |
| High residual risks | VR-001, VR-002, VR-003, VR-004 |

`project_data.py` is the source of truth for risk scores, treatments, remediation owners, and scorecard weights.
