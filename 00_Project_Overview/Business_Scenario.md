# Business Scenario

**This is a fictional cybersecurity case study created for educational and portfolio purposes.**

## Organizations

**Nexus Financial Services** is a fictional regional financial-services firm evaluating a SaaS customer-relationship platform to support sales, account management, and client-service teams. Nexus is the customer, organization, and vendor owner.

**CloudFlow Technologies** is a fictional third-party SaaS vendor. The product under review is **CloudFlow CRM**. CloudFlow stores and processes customer and employee information on behalf of Nexus.

## Why the assessment exists

Nexus wants a single system of record for pipeline, contacts, and support history. The data is Confidential: it is not payment-card data, but it is still personal and commercially sensitive. Onboarding a multi-tenant public-cloud CRM creates supply-chain, availability, and incident-notification risk. TPRM is required before production use.

## Data CloudFlow CRM will process for Nexus

- Customer names  
- Email addresses  
- Telephone numbers  
- Business contact information  
- Employee contact information  
- Customer support information  
- Sales records  
- Internal business information classified as Confidential  

## Data CloudFlow will not directly process

- Credit card information  
- Bank account credentials  
- Authentication secrets  
- Highly restricted financial records  

## Vendor characteristics (scenario facts used everywhere)

| Characteristic | Scenario value |
| --- | --- |
| Employees | Approximately 250 |
| Business customers | Approximately 500 |
| Delivery model | SaaS |
| Architecture | Multi-tenant |
| Hosting | Public cloud — AWS |
| Penetration testing | Annual (last simulated test October 2025) |
| Vulnerability scanning | Monthly authenticated |
| MFA | Required for privileged users (legacy admin utilities excepted) |
| Encryption | In transit (TLS 1.2+) and at rest (AES-256 / KMS) |
| Backups | Daily, encrypted, replicated |
| Incident response | Formal plan; customer SLA unclear |
| Independent assurance | SOC 2 Type I (Security and Availability) as of 30 September 2025 |
| ISO/IEC 27001 | Not certified |

## Decision context

The assessment must produce a risk-informed onboarding decision. A generally capable vendor can still be **High** residual risk if recoverability, notification, and supply-chain governance are incomplete. This case study’s outcome is **Conditional Approval** with overall residual risk **High**, not rejection and not unrestricted approval.
