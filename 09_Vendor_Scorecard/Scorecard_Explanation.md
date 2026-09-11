# Scorecard Explanation

**This is a fictional cybersecurity case study created for educational and portfolio purposes.**

## How domain scores were set

Each domain is scored 0–100 from questionnaire completeness, control ratings, and evidence quality — not from residual risk bands. That separation is deliberate.

- **Data Protection 88:** TLS, KMS, classification, and a clean data-scope (no PAN) are strong.  
- **Cloud Security 85:** AWS baseline, detection, and logging are coherent.  
- **Access Control 82:** Privileged MFA and RBAC are strong; legacy MFA prevents the 90s.  
- **Governance 78:** Named CISO and policies; incomplete review packets and no ISO certificate.  
- **Vulnerability 74:** Scanning and PT good; 30-day High SLA.  
- **Incident Response 72:** Plan and tabletop exist; customer SLA does not.  
- **Compliance 70:** Type I only; Type II missing; no ISO 27001.  
- **Business Continuity 62:** Daily backups help; RPO and restore cadence do not.  
- **Third-Party Management 58:** Inventory without standardized scoring.

## Weighted overall 74.4

This sits in the requested realistic 70–80% band. It means “generally capable SaaS with material gaps,” not “Low risk.”

## Formula

`Overall = Σ (Weight × Domain Score)` implemented in Excel as `=B{row}*C{row}` with `=SUM` of weighted column. Weights must total 100%.

## Recalculation

```bash
python 14_Scripts/calculate_risk_scores.py
python 14_Scripts/generate_scorecard.py
```
