# Risk Register Summary

**This is a fictional cybersecurity case study created for educational and portfolio purposes.**

The live register is `Vendor_Risk_Register.xlsx`. Scores in columns Inherent Risk, Residual Risk, and Risk Rating are **formulas**, not hand-typed products.

## Register contents (residual)

| Risk ID | Title | Inh. | Residual | Rating | Treatment | Due | Acceptance required |
| --- | --- | ---: | ---: | --- | --- | --- | --- |
| VR-001 | Weak Subprocessor Governance | 16 | 12 | High | Mitigate | 2026-04-30 | No |
| VR-002 | Insufficient Backup Recovery Testing | 16 | 12 | High | Mitigate | 2026-04-30 | No |
| VR-003 | Undefined Recovery Point Objective | 16 | 12 | High | Mitigate | 2026-03-31 | No |
| VR-004 | Unclear Incident Notification SLA | 16 | 12 | High | Mitigate | 2026-03-31 | No |
| VR-005 | SOC 2 Type I Only | 9 | 6 | Moderate | Accept | 2026-12-31 | Yes |
| VR-006 | No ISO 27001 Certification | 9 | 6 | Moderate | Accept | 2027-06-30 | Yes |
| VR-007 | Vulnerability Remediation Window | 12 | 9 | Moderate | Accept | 2026-06-30 | Yes |
| VR-008 | Legacy MFA Gap | 16 | 9 | Moderate | Mitigate | 2026-05-15 | No |

Owners, evidence references, and status text are in the workbook and in `14_Scripts/project_data.py`. Dashboard sheet counts High/Moderate/Low using `COUNTIF` on the rating column.

## Consistency rule

Risk IDs never change across the questionnaire, evidence mapping, treatment records, remediation tracker, scorecard narrative, executive pack, or final report.
