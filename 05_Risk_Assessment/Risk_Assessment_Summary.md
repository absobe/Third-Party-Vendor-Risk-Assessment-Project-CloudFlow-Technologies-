# Risk Assessment Summary

**This is a fictional cybersecurity case study created for educational and portfolio purposes.**

## Result

| Metric | Value |
| --- | --- |
| Risks on register | 8 (VR-001–VR-008) |
| Critical residual | 0 |
| High residual | 4 (VR-001, VR-002, VR-003, VR-004) |
| Moderate residual | 4 (VR-005, VR-006, VR-007, VR-008) |
| Low residual | 0 |
| Overall residual risk | **High** |
| Overall vendor score | **74.4** |
| Recommendation | **Conditional Approval** |

## Primary risks requiring immediate attention

1. **Subprocessor governance (VR-001)** — no standardized scored assessments.  
2. **Backup recovery testing (VR-002)** — annual restore only.  
3. **Undefined RPO (VR-003)** — de facto ~24 hours, not approved.  
4. **Incident notification SLA (VR-004)** — “without undue delay” is not a clock.

## Workbooks

- `Inherent_Risk_Assessment.xlsx` — L×I formulas, no control credit.  
- `Residual_Risk_Assessment.xlsx` — control credit with written rationale per ID.  
- `06_Risk_Register/Vendor_Risk_Register.xlsx` — operational register with Excel formulas.

## Treatment snapshot

Mitigate: VR-001, VR-002, VR-003, VR-004, VR-008.  
Accept with conditions: VR-005, VR-006, VR-007.  
Transfer / Avoid: none. Rejection was not selected because encryption, privileged MFA, scanning, PT, backups, and IR design provide a workable baseline if High items are closed under contract.
