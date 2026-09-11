# Executive Report

**This is a fictional cybersecurity case study created for educational and portfolio purposes.**

## 1. Engagement snapshot

Nexus Financial Services completed a simulated Initial Third-Party Vendor Security Assessment of CloudFlow Technologies for CloudFlow CRM (NEX-TPRM-2026-014), 3–28 February 2026, report 6 March 2026. Methodological references: NIST CSF, NIST SP 800-161 concepts, ISO/IEC 27001 concepts, SOC 2 TSC concepts, CIS Control concepts. This is not an audit, certification, or penetration test.

## 2. Inherent relationship

High criticality vendor: Confidential data, revenue-facing availability, financial-services customer with notification duties, AWS-hosted multi-tenant SaaS. Impact is Major rather than Critical because payments and core banking data are out of product scope.

## 3. Control posture in brief

Effective controls include privileged MFA on production/AWS, RBAC, encryption, monthly scanning, annual PT (High PT items closed), daily encrypted backups, logging, and an IR plan with internal escalation. Partially effective or ineffective areas concentrate in TPRM scoring, RPO, restore testing, customer IR SLA, Type II assurance, ISO certification, High vuln SLA, and legacy MFA.

## 4. Risk results

Eight findings. Residual: 0 Critical, 4 High, 4 Moderate, 0 Low. Treatments: five Mitigate, three Accept with conditions. Scorecard 74.4. Overall residual **High**.

## 5. Conditions of approval (management view)

1. Remediate High-risk findings VR-001–VR-004 on the CAP dates.  
2. Execute contractual security requirements (24-hour notice; RPO; audit/evidence rights).  
3. Annual reassessment.  
4. Evidence updates (PT summary, vulnerability metrics, restore tests, subprocessor assessments).  
5. Incident notification requirements as in the IR exhibit.  
6. Defined recovery objectives.  
7. Subprocessor review requirements and notice of material fourth-party changes.

## 6. Recommendation

**Conditional Approval** — support onboarding under the conditions above. Do not issue unrestricted approval. Do not reject solely for missing ISO 27001 or Type II, given compensating design evidence and data scope.

## 7. Continuous monitoring (see also final report §16)

Annual reassessment; questionnaire refresh; certification/PT review; material incident review; subprocessor change monitoring; contractual security reviews; risk score updates.
