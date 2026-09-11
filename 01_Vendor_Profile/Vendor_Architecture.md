# Vendor Architecture

**This is a fictional cybersecurity case study created for educational and portfolio purposes.**

## High-level design

CloudFlow CRM is a multi-tenant web application hosted on AWS in `us-east-1` across multiple availability zones. Compute runs in private subnets. A WAF sits in front of the HTTPS load balancer. Security groups restrict ingress. AWS IAM permission sets and a jump host protect privileged cloud administration. GuardDuty, CloudTrail (organization trail), and Security Hub are enabled. Encryption uses AWS KMS (AES-256). Backups replicate to a separate account in `us-east-2`.

## Shared responsibility (operationalized)

| Layer | Primary owner |
| --- | --- |
| Physical facilities, hypervisor | AWS |
| Host OS / managed data store patches (as configured) | CloudFlow / AWS shared per service |
| Application, tenant isolation, customer data, operator IAM | CloudFlow |
| Tenant user access, MFA for Nexus staff, data classification in fields | Nexus (complementary) |

## Isolation model

Logical isolation (`tenant_id`, row-level constraints, IAM-scoped application roles, S3 prefixes). Dedicated tenancy is not in the standard offering. This is acceptable for Confidential CRM data if application controls remain Effective; it is not equivalent to a single-tenant bank-grade partition.

## Trust boundaries relevant to findings

- **Subprocessors** sit outside CloudFlow’s AWS account boundary (VR-001).  
- **Backup restore** is the practical DR proof (VR-002, VR-003).  
- **Legacy admin utilities** are a separate identity path (VR-008).  
- **Customer IR notice** is a process boundary between CloudFlow IR and Nexus GRC (VR-004).
