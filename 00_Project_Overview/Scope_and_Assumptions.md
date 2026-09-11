# Scope and Assumptions

**This is a fictional cybersecurity case study created for educational and portfolio purposes.**

## 1. Assessment type

Initial Third-Party Vendor Security Assessment of CloudFlow Technologies / CloudFlow CRM, performed for Nexus Financial Services (all fictional).

## 2. In-scope environment

- CloudFlow CRM SaaS application (multi-tenant).  
- Supporting AWS accounts used to host the production CRM, logs, and backups (as described by the vendor).  
- Identity and access management for CloudFlow operators.  
- Backup, recovery, incident response, and subprocessor management as they affect Nexus Confidential data.  
- Independent assurance artifacts provided (SOC 2 Type I summary; penetration-test summary).

## 3. In-scope data

Customer names, emails, telephone numbers, business and employee contact information, support information, sales records, and other Confidential internal business information stored in the CRM.

## 4. Explicitly out of scope

- Nexus corporate network, endpoints, and identity (except complementary user-entity controls).  
- Payment card processing, core banking systems, and highly restricted financial ledgers.  
- Hands-on testing against live CloudFlow systems.  
- Physical inspection of AWS facilities.  
- Legal determination of regulatory applicability beyond TPRM commentary.

## 5. Assumptions

1. Vendor questionnaire answers and PDFs are simulated and internally consistent.  
2. AWS shared-responsibility model applies: CloudFlow owns the application, tenant isolation, IAM, and customer data handling; AWS owns underlying physical and hypervisor controls.  
3. Nexus will require MFA for its own CRM users as a complementary control.  
4. Daily backups imply a de facto ~24-hour loss potential until RPO is documented.  
5. “Without undue delay” is not equivalent to a 24-hour notification SLA.  
6. Absence of ISO/IEC 27001 certification is an assurance gap, not automatic evidence that controls are absent.  
7. SOC 2 Type I is point-in-time design assurance, not period-of-time operating effectiveness.  
8. Overall residual risk is **High** because four findings remain High after credit for existing controls.  
9. Overall score **74.4** reflects domain capability and does not override residual risk.  
10. Final security recommendation is **Conditional Approval**.

## 6. Limitations statement (required)

The assessment methodology combines concepts from recognized cybersecurity governance and supply-chain risk management frameworks. This simulated assessment does not constitute an ISO 27001 audit, SOC 2 audit, certification assessment, penetration test, or legal compliance opinion.

This project is fictional, simulated, educational, not a real vendor assessment, not a penetration test, not a vulnerability assessment, not an ISO audit, not a SOC audit, not a legal opinion, and not a certification. All evidence and vendor responses were created for educational simulation.
