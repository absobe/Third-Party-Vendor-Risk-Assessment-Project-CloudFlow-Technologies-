# Vendor Profile — CloudFlow Technologies

**This is a fictional cybersecurity case study created for educational and portfolio purposes.**

| Attribute | Value |
| --- | --- |
| Legal name (fictional) | CloudFlow Technologies |
| Product | CloudFlow CRM |
| Relationship | Prospective SaaS processor for Nexus Financial Services |
| Assessment type | Initial Third-Party Vendor Security Assessment |
| Headquarters (fictional) | Austin, Texas, United States |
| Workforce | Approximately 250 employees |
| Customer base | Approximately 500 business customers |
| Delivery | SaaS, subscription, public cloud |
| Architecture | Multi-tenant |
| Hosting | Amazon Web Services (us-east-1 production; backup replication us-east-2) |
| Primary vendor contact | Jordan Hale, CISO |
| Security operations | Morgan Ellis, Director of Security |
| Infrastructure | Taylor Nguyen, Director of Infrastructure |
| Privacy | Avery Chen, Data Protection Officer |
| Independent assurance | SOC 2 Type I, Security and Availability, as of 30 September 2025 (simulated) |
| ISO/IEC 27001 | Not certified |
| Cyber insurance (claimed, not in pack) | USD 5 million cyber liability (certificate under NDA — Evidence Not Provided) |

## Service proposed to Nexus

CloudFlow CRM would be the system of record for Nexus sales pipeline, account contacts, and support notes. Nexus users would authenticate to the tenant; CloudFlow would process Confidential personal and business information as a processor under a DPA.

## Inherent relationship factors

- **Confidential data** in a multi-tenant SaaS.  
- **Availability** of a revenue-facing tool.  
- **Supply chain** via AWS and other subprocessors.  
- **Incident interdependence**: Nexus notification clocks depend on CloudFlow.

These factors, not the vendor’s size alone, drive a High inherent relationship before controls are credited. Residual overall risk remains **High** pending remediation of VR-001 through VR-004.
