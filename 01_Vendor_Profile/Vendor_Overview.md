# Vendor Overview

**This is a fictional cybersecurity case study created for educational and portfolio purposes.**

CloudFlow Technologies operates CloudFlow CRM, a multi-tenant SaaS application used by mid-market professional-services and financial-adjacent teams to manage contacts, opportunities, and support cases.

## Security narrative (as presented by the vendor)

CloudFlow describes a named CISO, documented policies, AWS hosting with encryption in transit and at rest, MFA for privileged production and cloud administration, monthly authenticated vulnerability scanning, annual independent penetration testing, daily encrypted backups, centralized logging, and a formal incident response plan. A SOC 2 Type I report addresses Security and Availability as of 30 September 2025. ISO/IEC 27001 certification has not been obtained.

## Material caveats discovered in this simulated review

1. Subprocessor reviews are not consistently scored (VR-001).  
2. Backup restoration tests are annual, not quarterly (VR-002).  
3. RPO is not formally documented (VR-003).  
4. Customer incident notification has no hour-based SLA (VR-004).  
5. Assurance is Type I, not Type II (VR-005).  
6. No ISO 27001 certificate (VR-006).  
7. High-severity vulnerabilities may remain 30 days (VR-007).  
8. Some legacy internal admin utilities lack MFA (VR-008).

## What CloudFlow does well

Privileged MFA on AWS/CRM, TLS 1.2+, AES-256/KMS, logging, daily backups, IR plan existence, annual PT, monthly scanning, and a coherent cloud baseline. Those strengths support Conditional Approval rather than Avoid/reject — provided High findings are contractually and operationally addressed.

## Strategic fit

The product scope excludes card data and core banking records, which lowers inherent impact relative to a payments processor. Confidential CRM data still warrants High residual attention on recoverability, notification, and fourth-party governance.
