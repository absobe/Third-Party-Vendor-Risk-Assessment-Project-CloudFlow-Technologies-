# Third-Party Vendor Risk Assessment Report

**CloudFlow Technologies — CloudFlow CRM**  
**Prepared for:** Nexus Financial Services (fictional)  
**Prepared by:** Priya Mehta, Third-Party Risk Analyst (simulated role)  
**Reviewed by:** Daniel Okonkwo, CISO, Nexus Financial Services (simulated role)  
**Project type:** Initial Third-Party Vendor Security Assessment (educational portfolio case study)  
**Assessment ID:** NEX-TPRM-2026-014  
**Assessment window:** 3–28 February 2026  
**Report date:** 6 March 2026  
**Classification:** Confidential — Simulated Case Study  

---

**This is a fictional cybersecurity case study created for educational and portfolio purposes.**

This report is fictional, simulated, and educational. It is not a real vendor assessment, not a penetration test, not a vulnerability assessment, not an ISO audit, not a SOC audit, not a legal opinion, and not a certification. All evidence and vendor responses were created for educational simulation. Do not represent this document as an assessment of any real company.

---

## Cover endorsement

| Item | Value |
| --- | --- |
| Vendor | CloudFlow Technologies |
| Product | CloudFlow CRM |
| Customer | Nexus Financial Services |
| Overall vendor score | 74.4 |
| Overall residual risk | **High** |
| Recommendation | **Conditional Approval** |

---

## 1. Executive Summary

Nexus Financial Services evaluated CloudFlow Technologies before a proposed purchase of CloudFlow CRM. The platform would process Confidential contact, support, and sales information. It would not process payment cards, bank credentials, authentication secrets, or highly restricted financial records.

CloudFlow operates a generally capable SaaS control environment on AWS: privileged MFA, encryption, scanning, annual penetration testing, daily backups, logging, and a documented incident response plan. Independent assurance is limited to a SOC 2 Type I report as of 30 September 2025. ISO/IEC 27001 is not certified.

Material gaps remain in subprocessor scoring, backup restoration testing, formal RPO, and customer incident notification. Those four findings (VR-001–VR-004) retain **High** residual risk (score 12). Overall residual risk is therefore **High** despite a 74.4 scorecard. The security recommendation is **Conditional Approval**, not rejection and not unrestricted go-live.

Immediate attention: VR-001, VR-002, VR-003, VR-004. Next steps: security exhibit (24-hour notice, RPO), CAP tracker, and annual reassessment.

---

## 2. Business Context

Revenue Operations at Nexus intends to consolidate pipeline and client-service records. A multi-tenant public-cloud CRM creates supply-chain and availability dependence. TPRM opened NEX-TPRM-2026-014 under a charter dated 20 January 2026. CloudFlow is described as approximately 250 employees and 500 business customers.

The decision Nexus needs is: *Should we onboard CloudFlow, and under what conditions?*

---

## 3. Assessment Scope

**In scope:** CloudFlow CRM SaaS; AWS hosting as described; operator IAM; backup/IR/BCP/subprocessor processes; questionnaire and provided evidence.

**In-scope data:** names, emails, telephone numbers, business and employee contacts, support information, sales records, Confidential internal business information.

**Out of scope:** Nexus enterprise IT (except complementary user-entity controls); card/bank/core-banking systems; live technical testing; physical AWS inspection; legal privilege analysis.

Assumptions and limitations: see Appendix D and `00_Project_Overview/Scope_and_Assumptions.md`.

---

## 4. Assessment Methodology

The assessment methodology combines concepts from recognized cybersecurity governance and supply-chain risk management frameworks. This simulated assessment does not constitute an ISO 27001 audit, SOC 2 audit, certification assessment, penetration test, or legal compliance opinion.

Process: relationship definition → 55-question questionnaire (domains A–T) → evidence review → control rating → inherent 5×5 → residual re-score with written control credit → treatment → remediation → weighted scorecard → executive decision → monitoring plan.

Control results: Effective, Partially Effective, Ineffective, Not Applicable, Evidence Not Provided. Risk score = Likelihood × Impact. Ratings: 1–4 Low, 5–9 Moderate, 10–16 High, 17–25 Critical.

---

## 5. Vendor Overview

CloudFlow Technologies (fictional) delivers CloudFlow CRM as multi-tenant SaaS on AWS (us-east-1, backup replication us-east-2). CISO: Jordan Hale. SOC 2 Type I (Security and Availability) as of 30 September 2025. No ISO/IEC 27001. Annual PT (October 2025, fictional Northbridge Labs). See `01_Vendor_Profile/`.

---

## 6. Data and System Context

Data flows from Nexus users over TLS into a tenant-isolated data store encrypted with KMS. Logs go to SIEM. Daily backups replicate off-account. Email and telemetry subprocessors may handle limited data. Logical isolation (not dedicated tenancy) is the tenancy model. Complementary control: Nexus must require MFA for its own users.

---

## 7. Control Assessment

Representative results:

| Control ID | Control | Result |
| --- | --- | --- |
| CTRL-AC-001 | MFA for privileged users | Effective |
| CTRL-AC-004 | MFA on legacy admin paths | Partially Effective |
| CTRL-DP-002 / 003 | Encryption transit / rest | Effective |
| CTRL-VM-001 | Monthly authenticated scanning | Effective |
| CTRL-VM-002 | High vuln SLA | Partially Effective |
| CTRL-IR-001 | IR plan | Effective |
| CTRL-IR-002 | Customer notification SLA | Partially Effective |
| CTRL-BC-002 | RPO | Ineffective |
| CTRL-BU-001 | Daily encrypted backups | Effective |
| CTRL-BU-002 | Restoration testing | Partially Effective |
| CTRL-CM-001 | SOC 2 Type I | Partially Effective |
| CTRL-CM-002 | SOC 2 Type II | Evidence Not Provided |
| CTRL-CM-003 | ISO 27001 certification | Ineffective |
| CTRL-TPRM-004 | Formal subprocessor risk assessment | Partially Effective |

Full ratings: `04_Control_Assessment/Control_Assessment.xlsx`.

---

## 8. Key Findings

### VR-001 — Weak Subprocessor Governance

CloudFlow lacks a consistently documented and formally scored process for evaluating security risks associated with subprocessors. Inventory and some flow-down exist. Residual 3×4=12 High. Mitigate (CAP-001).

### VR-002 — Insufficient Backup Recovery Testing

Restoration testing is annual (12 November 2025, 6h 40m on a non-production snapshot). Residual 3×4=12 High. Mitigate (CAP-002).

### VR-003 — Undefined Recovery Point Objective

No formally documented RPO. Daily backups imply ~24 hours potential loss. Residual 3×4=12 High. Mitigate (CAP-003).

### VR-004 — Unclear Incident Notification SLA

Customer notice is “without undue delay.” Residual 3×4=12 High. Mitigate (CAP-004) — 24-hour contractual clock.

### VR-005 — SOC 2 Type I Only

Type I provides less assurance of operating effectiveness over time than Type II. Residual 2×3=6 Moderate. Accept with Type II condition.

### VR-006 — No ISO 27001 Certification

No accredited certification; ISMS is still operated. Residual 2×3=6 Moderate. Accept with continued assurance.

### VR-007 — Vulnerability Remediation Window

High-severity items may remain 30 days. Residual 3×3=9 Moderate. Accept with 15-day internet-facing High target.

### VR-008 — Legacy MFA Gap

Some legacy internal admin utilities lack MFA (password + VPN). Production CRM/AWS privileged MFA is Effective. Residual 3×3=9 Moderate. Mitigate (CAP-008).

---

## 9. Risk Analysis

Inherent scores treat controls as absent. Residual scores credit only demonstrated reduction. Example: VR-001 inherent 4×4=16; inventory/contracts reduce likelihood to 3; impact remains 4 because a weak fourth party can still expose Confidential data. Similar reasoning applies to VR-002–VR-004 (backups/IR internals reduce likelihood, not Major impact). VR-008 residual drops to 9 because production/AWS MFA and VPN reduce both likelihood and blast radius. See `05_Risk_Assessment/Residual_Risk_Assessment.xlsx` for per-ID narratives.

Overall residual **High** because open High residuals exist. No residual Critical (17–25).

---

## 10. Risk Register

See `06_Risk_Register/Vendor_Risk_Register.xlsx` (formulas for L×I and rating) and `Risk_Register_Summary.md`. All eight IDs, owners, due dates, treatments, and evidence references are populated.

---

## 11. Risk Treatment

| ID | Treatment |
| --- | --- |
| VR-001, VR-002, VR-003, VR-004, VR-008 | Mitigate |
| VR-005, VR-006, VR-007 | Accept with conditions |
| — | Transfer: none; Avoid: none |

---

## 12. Remediation Plan

CAP-001–CAP-008 in `07_Remediation/`. High-priority due dates cluster 31 March–15 May 2026. Success criteria are evidence-based (approved procedure, restore report with timing, signed RPO, executed notice clause, MFA coverage report).

---

## 13. Vendor Scorecard

Weighted overall **74.4**. Domain scores: Governance 78, Access 82, Data Protection 88, Vulnerability 74, IR 72, BC 62, Compliance 70, Cloud 85, Third-Party 58. Interpretation: capable SaaS with concentrated BC and TPRM weakness. Score ≠ Low risk.

---

## 14. Risk Acceptance Decisions

CISO (simulated) may accept VR-005, VR-006, VR-007 with dated conditions. High residuals are not accepted. See `08_Risk_Treatment/`.

---

## 15. Management Recommendation

**CONDITIONAL APPROVAL.** CloudFlow may be onboarded only under documented security conditions:

1. Remediation of high-risk findings.  
2. Formal contractual security requirements.  
3. Annual reassessment.  
4. Evidence updates.  
5. Incident notification requirements (24 hours from confirmation of a material incident).  
6. Defined recovery objectives.  
7. Subprocessor review requirements.

---

## 16. Continuous Monitoring

After onboarding, Nexus TPRM should:

- Perform annual vendor reassessment (first: 6 March 2027).  
- Refresh the security questionnaire.  
- Review certifications and SOC reports (Type II when issued).  
- Review penetration-testing summaries each cycle.  
- Review material incidents and tabletop outcomes.  
- Monitor subprocessor changes (14-day vendor notice plus Nexus risk review).  
- Conduct contractual security reviews at renewal.  
- Update residual risk scores when CAP evidence arrives — never auto-reduce scores.

Trigger an off-cycle review if: Sev1 incident, missed CAP dates, loss of independent assurance, or material architecture change.

---

## 17. Conclusion

CloudFlow CRM is a reasonable SaaS candidate for Confidential (non-payments) CRM data, provided Nexus treats High residual issues as onboarding conditions rather than paperwork. The simulated evidence supports **Conditional Approval** at **High** overall residual risk and a **74.4** control scorecard. Unrestricted approval would understate recoverability, notification, and fourth-party risk. Rejection would overstate the meaning of missing ISO 27001 and Type II relative to the observed design strengths.

This conclusion is educational only.

---

## Appendix A — Questionnaire Summary

55 questions, domains A–T. Findings concentrated in Q-S-050 (subprocessor scoring), Q-M-037 (restore testing), Q-L-033 (RPO), Q-J-028 (notification SLA), Q-O-041 (SOC 2 Type I), Q-O-042 (ISO 27001), Q-F-018 (30-day High), Q-C-009 (legacy MFA). Workbook: `02_Security_Questionnaire/Vendor_Security_Questionnaire.xlsx`.

---

## Appendix B — Evidence Mapping

Ten fictional PDFs in `03_Vendor_Evidence/` map to control IDs as in `04_Control_Assessment/Evidence_Mapping.xlsx` and `15_Final_Checks/Evidence_Traceability_Matrix.xlsx`. Each PDF is labeled SIMULATED / FICTIONAL EVIDENCE — FOR EDUCATIONAL USE ONLY.

---

## Appendix C — Risk Scoring Methodology

Likelihood 1–5, Impact 1–5, product 1–25, bands Low/Moderate/High/Critical as in `05_Risk_Assessment/Risk_Scoring_Methodology.md`. Recalculate with `python 14_Scripts/calculate_risk_scores.py`.

---

## Appendix D — Assumptions and Limitations

This project is fictional, simulated, educational, not a real vendor assessment, not a penetration test, not a vulnerability assessment, not an ISO audit, not a SOC audit, not a legal opinion, and not a certification. Frameworks are references only. All CloudFlow and Nexus names, people, dates, SOC extracts, and penetration-test counts are invented for a student GRC portfolio.
