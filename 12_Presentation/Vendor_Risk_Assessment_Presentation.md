# Vendor Risk Assessment Presentation

**This is a fictional cybersecurity case study created for educational and portfolio purposes.**  
Use these 12 slides in PowerPoint, Google Slides, or a PDF export. Keep the disclaimer on every slide footer.

---

## Slide 1 — Project Title

**Third-Party Vendor Risk Assessment — CloudFlow Technologies**  
A Simulated SaaS Vendor Cybersecurity Risk Assessment and GRC Case Study  

Nexus Financial Services (fictional customer) → CloudFlow Technologies / CloudFlow CRM (fictional vendor)  
Assessment ID NEX-TPRM-2026-014 | 6 March 2026  
Prepared by: Priya Mehta, TPRM Analyst (simulated)  

Footer: *This is a fictional cybersecurity case study created for educational and portfolio purposes.*

---

## Slide 2 — Business Scenario

- Nexus wants a SaaS CRM for sales and service.  
- Data: Confidential contacts, support, sales records.  
- Not in scope: cards, bank credentials, secrets, highly restricted financial records.  
- Question: Should Nexus onboard CloudFlow, and under what conditions?

---

## Slide 3 — Vendor Overview

- ~250 employees, ~500 business customers, multi-tenant SaaS on AWS.  
- Strengths claimed: MFA (privileged), TLS, AES-256, monthly scanning, annual PT, daily backups, IR plan, SOC 2 Type I.  
- Not certified to ISO/IEC 27001.

---

## Slide 4 — Assessment Scope

- Initial Third-Party Vendor Security Assessment.  
- In: CRM, AWS as described, IAM, BCP/IR/backups/subprocessors, evidence pack.  
- Out: live PT/scanning by Nexus, physical DC review, legal opinion.

---

## Slide 5 — Assessment Methodology

- References: NIST CSF, NIST SP 800-161 concepts, ISO/IEC 27001 concepts, SOC 2 TSC, CIS concepts.  
- Not an audit or certification.  
- Flow: Questionnaire → Evidence → Controls → Inherent → Residual → Register → Treatment → Scorecard → Decision.  
- 5×5: Score = Likelihood × Impact.

---

## Slide 6 — Vendor Security Strengths

- Privileged MFA (AWS + CRM operators)  
- Encryption in transit and at rest  
- Monthly authenticated scanning; annual PT with High items closed  
- Daily encrypted backups; SIEM logging  
- Formal IR plan and named CISO  

---

## Slide 7 — Major Risk Findings

| ID | Finding | Residual |
| --- | --- | --- |
| VR-001 | Weak subprocessor governance | 12 High |
| VR-002 | Insufficient backup recovery testing | 12 High |
| VR-003 | Undefined RPO | 12 High |
| VR-004 | Unclear incident notification SLA | 12 High |
| VR-005–007 | Type I only; no ISO; 30-day High SLA | Moderate (Accept w/ conditions) |
| VR-008 | Legacy MFA gap | 9 Moderate (Mitigate) |

---

## Slide 8 — Risk Heat Map

Plot residual points: VR-001–004 at (Impact 4, Likelihood 3); VR-007/008 at (3,3); VR-005/006 at (3,2).  
Caption: Four High cells drive overall **High** vendor risk.  
(Insert `09_Vendor_Scorecard/residual_heatmap.png`.)

---

## Slide 9 — Vendor Risk Scorecard

Overall score **74.4**. Lowest: Third-Party 58, BC 62. Highest: Data Protection 88, Cloud 85.  
Message: **70s score ≠ Low risk.**

---

## Slide 10 — Remediation Plan

- Mar 2026: RPO + 24-hour notice in contract  
- Apr 2026: scored subprocessors; quarterly restore test  
- May 2026: legacy MFA  
- 2026 monitoring: 15-day High SLA; SOC 2 Type II  

---

## Slide 11 — Management Decision

# CONDITIONAL APPROVAL

Overall residual risk: **High**  
Conditions: High-finding remediation, contractual security, annual reassessment, evidence updates, 24-hour notice, defined RPO, subprocessor review rights.

---

## Slide 12 — Lessons Learned / Conclusion

- TPRM must separate scorecards from residual risk.  
- Type I ≠ Type II; no ISO 27001 ≠ no ISMS.  
- Fourth parties, restore tests, and notification clocks are typical SaaS deal-breakers if left unconditioned.  
- This package is a **simulated** student/professional portfolio case study — never present it as a live assessment.

**Thank you.** Questions.
