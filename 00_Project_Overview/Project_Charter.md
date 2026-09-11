# Project Charter

**This is a fictional cybersecurity case study created for educational and portfolio purposes.**

| Field | Content |
| --- | --- |
| Project title | Third-Party Vendor Risk Assessment — CloudFlow Technologies |
| Subtitle | A Simulated SaaS Vendor Cybersecurity Risk Assessment and GRC Case Study |
| Assessment ID | NEX-TPRM-2026-014 |
| Assessment type | Initial Third-Party Vendor Security Assessment |
| Requesting organization | Nexus Financial Services (fictional customer / vendor owner) |
| Vendor | CloudFlow Technologies (fictional third-party SaaS vendor) |
| Product | CloudFlow CRM |
| Sponsor (simulated) | Daniel Okonkwo, CISO, Nexus Financial Services |
| Assessment lead (simulated) | Priya Mehta, Third-Party Risk Analyst |
| Business owner (simulated) | Elena Voss, VP of Revenue Operations |
| Window | 3 February 2026 – 28 February 2026 |
| Report date | 6 March 2026 |

## 1. Purpose

This charter authorizes a simulated cybersecurity due-diligence assessment of CloudFlow CRM before a proposed onboarding by Nexus Financial Services. The charter exists so the case study has a defined owner, scope, success criteria, and decision rights, matching how a GRC function would open a TPRM engagement.

## 2. Business driver

Revenue Operations intends to replace a fragmented set of spreadsheets and a legacy contact tool with a multi-tenant SaaS CRM. The platform will hold Confidential customer and employee contact data and sales records. Cybersecurity due diligence is required before contract signature and production data load.

## 3. In-scope question

Should Nexus Financial Services onboard CloudFlow Technologies, and under what conditions?

## 4. Success criteria

- Scope, data types, and system boundary documented.  
- Questionnaire with at least 50 questions completed with vendor responses.  
- Evidence reviewed and mapped to controls.  
- Inherent and residual risk scored on a 5×5 model.  
- Risk register, treatment, and remediation recorded.  
- Weighted scorecard produced.  
- Executive recommendation issued (in this case study: Conditional Approval, overall residual risk High).

## 5. Out of scope for this engagement

- Hands-on penetration testing by Nexus.  
- Vulnerability scanning of CloudFlow by Nexus.  
- Legal privilege review of a real contract.  
- On-site data-center inspection.  
- Assessment of Nexus internal CRM configuration after go-live (covered under continuous monitoring).

## 6. Decision rights

The Nexus CISO (simulated) issues the vendor security recommendation. Business may still decline commercially. Conditional Approval in this package means security will support onboarding only if listed conditions are accepted.

## 7. Key deliverables

All folders `00_` through `15_` in this repository, including Excel workbooks, fictional evidence PDFs, Python scoring/validation, and the final report.

## 8. Constraints and assumptions

See `Scope_and_Assumptions.md`. Evidence and responses are created for educational simulation. CloudFlow is assumed to be in AWS, approximately 250 employees, approximately 500 business customers, multi-tenant SaaS, SOC 2 Type I, no ISO 27001 certification.

## 9. Approval (simulated)

| Role | Name | Decision | Date |
| --- | --- | --- | --- |
| CISO, Nexus | Daniel Okonkwo | Charter approved | 20 January 2026 |
| VP Revenue Operations | Elena Voss | Business need confirmed | 20 January 2026 |
| TPRM Lead | Priya Mehta | Assessment opened | 3 February 2026 |
