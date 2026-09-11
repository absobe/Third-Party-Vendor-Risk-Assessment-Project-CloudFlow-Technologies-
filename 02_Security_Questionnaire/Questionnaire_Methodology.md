# Questionnaire Methodology

**This is a fictional cybersecurity case study created for educational and portfolio purposes.**

## Purpose

The questionnaire is the structured intake for CloudFlow Technologies. It is not a certification checklist. It is mapped to control IDs and, where gaps appear, to risk IDs VR-001–VR-008.

## Design

- **55 questions** across domains A–T (Governance through Risk Management).  
- Each item records: Question ID, Domain, Control area, Question, Vendor Response, Evidence Requested, Evidence Received, Assessment Status, Assessor Notes, Risk Impact.  
- Linked Risk ID is added in the Excel workbook for traceability.

## Status values used

| Status | Meaning |
| --- | --- |
| Complete | Response and evidence reasonably support the answer |
| Partial | Claim is plausible but evidence is thin |
| Gap | Documentation or operating practice incomplete |
| Finding | Directly feeds a risk register item |
| Evidence not provided | Could not be corroborated in the pack (e.g., insurance certificate) |

## Vendor response principles (simulation)

Responses are intentionally imperfect. Strengths include MFA for privileged AWS/CRM access, encryption, scanning, annual PT, daily backups, IR plan, logging, and awareness training. Weaknesses match the required findings: no ISO 27001, SOC 2 Type I, informal subprocessor scoring, annual restore tests, undocumented RPO, unclear notification SLA, incomplete policy review packets, annual training, legacy MFA gap, and a 30-day High vulnerability window.

## How to use the workbooks

1. Open `Vendor_Security_Questionnaire.xlsx` sheet `Questionnaire`.  
2. Filter `Assessment Status` = Finding to jump to register inputs.  
3. Use `Vendor_Response_Summary.xlsx` for a shorter strength/weakness view.  
4. Confirm the same Question IDs in `15_Final_Checks/Evidence_Traceability_Matrix.xlsx`.
