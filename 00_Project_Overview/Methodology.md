# Assessment Methodology

**This is a fictional cybersecurity case study created for educational and portfolio purposes.**

## 1. Methodological notice

The assessment methodology combines concepts from recognized cybersecurity governance and supply-chain risk management frameworks. This simulated assessment does not constitute an ISO 27001 audit, SOC 2 audit, certification assessment, penetration test, or legal compliance opinion.

Reference frameworks used as **guidance**, not as a claim of certification or attested compliance:

- NIST Cybersecurity Framework (Identify, Protect, Detect, Respond, Recover).  
- NIST SP 800-161 concepts relating to Cybersecurity Supply Chain Risk Management.  
- ISO/IEC 27001 control concepts (ISMS, access, operations, supplier relationships, continuity).  
- SOC 2 Trust Services Criteria concepts (Security, Availability as examined in the fictional Type I).  
- CIS Controls concepts where relevant (IAM, data protection, vulnerability management, logging).

## 2. Process

1. **Relationship definition** — vendor, product, data, criticality.  
2. **Questionnaire** — 55 questions across domains A–T.  
3. **Evidence collection** — fictional policies, IR/BCP, backup, PT summary, SOC 2 Type I summary, subprocessor summary.  
4. **Control assessment** — Effective / Partially Effective / Ineffective / Not Applicable / Evidence Not Provided.  
5. **Gap analysis** — map weaknesses to risk IDs VR-001 through VR-008.  
6. **Inherent risk** — Likelihood × Impact before crediting controls.  
7. **Residual risk** — re-score only where controls demonstrably reduce likelihood or impact.  
8. **Treatment** — Mitigate, Accept, Transfer, or Avoid.  
9. **Remediation and contractual conditions**.  
10. **Scorecard and executive decision**.  
11. **Continuous monitoring plan**.

## 3. Control rating definitions

| Result | Meaning |
| --- | --- |
| Effective | Design and available evidence reasonably support the control objective for this use case. |
| Partially Effective | Control exists but is incomplete, inconsistently applied, or weakly evidenced. |
| Ineffective | Control objective is not met (for example, no documented RPO). |
| Not Applicable | Control is outside the system boundary. |
| Evidence Not Provided | Claimed or expected control could not be corroborated (for example, SOC 2 Type II). |

## 4. Why residual risk can remain High when the score is 74.4

Weighted domain scoring rewards breadth of a reasonably mature SaaS program (encryption, MFA for privileged cloud/CRM access, scanning, backups, logging). Residual risk asks a different question: can a realistic failure still cause Major impact to Nexus? Four issues still score 12 (High) after control credit: subprocessor scoring, restore-test cadence, undefined RPO, and incident notification SLA.

## 5. Independence and simulation

The assessor role is simulated. Evidence is authored as CloudFlow documents for the case study. In a live engagement, original vendor files, contract exhibits, and bridge letters would be used instead.
