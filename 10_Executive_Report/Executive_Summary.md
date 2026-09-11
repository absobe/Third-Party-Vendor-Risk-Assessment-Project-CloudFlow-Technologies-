# Executive Summary

**This is a fictional cybersecurity case study created for educational and portfolio purposes.**

**To:** Daniel Okonkwo, CISO, Nexus Financial Services  
**From:** Priya Mehta, Third-Party Risk Analyst (simulated role)  
**Date:** 6 March 2026  
**Subject:** Initial Third-Party Vendor Security Assessment of CloudFlow Technologies (CloudFlow CRM)  
**Assessment ID:** NEX-TPRM-2026-014  

## Who is the vendor, and what do they provide?

CloudFlow Technologies is a fictional SaaS company of about 250 employees serving about 500 business customers. The product, CloudFlow CRM, is a multi-tenant application hosted on AWS. Nexus Financial Services is considering it as the firm’s CRM.

## What data will they process?

Customer and employee contact details, emails, telephone numbers, support information, sales records, and other Confidential business information. CloudFlow will **not** process credit cards, bank credentials, authentication secrets, or highly restricted financial records.

## Why was the vendor assessed?

Nexus requires cybersecurity due diligence before onboarding a processor of Confidential data. This is an Initial Third-Party Vendor Security Assessment.

## Strengths

CloudFlow presents a recognizable SaaS control environment: named CISO, MFA for privileged AWS and CRM operator access, TLS 1.2+, encryption at rest, monthly authenticated scanning, annual penetration testing, daily encrypted backups, centralized logging, and a formal incident response plan. A SOC 2 Type I report (Security and Availability, as of 30 September 2025) supports control design at a point in time.

## Important weaknesses

The program is not uniformly mature. Subprocessor security reviews are informal and not scored. Backup restoration is tested only annually. No Recovery Point Objective is approved (daily backups imply up to about 24 hours of data loss). Customer incident notification is “without undue delay,” with no hour-based SLA. Assurance is Type I rather than Type II, and there is no ISO/IEC 27001 certification. High-severity vulnerabilities may remain open 30 days. Some legacy internal admin tools lack MFA.

## Overall risk rating and score

**Overall residual risk: High.**  
**Overall vendor security score: 74.4 / 100.**  
A mid-70s score and High residual risk can coexist: the platform is generally capable, but recoverability, notification, and fourth-party governance still present Major impact scenarios.

## Risks requiring immediate attention

VR-001 Weak Subprocessor Governance; VR-002 Insufficient Backup Recovery Testing; VR-003 Undefined RPO; VR-004 Unclear Incident Notification SLA. All four remain **High** residual (score 12) and must be **mitigated**, not accepted.

## Recommended decision

**Conditional Approval.** CloudFlow may be onboarded only with documented security conditions: remediation of High findings; contractual 24-hour incident notice and defined recovery objectives; subprocessor review rights; evidence updates; and annual reassessment.

## What happens next

Legal should attach a security exhibit covering notice and RPO. TPRM should track CAP-001–CAP-008. Production load of Confidential data should wait on contractual commitment of CAP-003 and CAP-004 and agreed plans for CAP-001, CAP-002, and CAP-008. Reassess by 6 March 2027, or earlier if a material incident or subprocessor change occurs.
