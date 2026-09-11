# Criticality Assessment

**This is a fictional cybersecurity case study created for educational and portfolio purposes.**

## Inherent criticality of the relationship

| Factor | Rating | Rationale |
| --- | --- | --- |
| Data sensitivity | High | Confidential personal and commercial CRM data |
| Volume | Moderate | Regional financial-services firm; not a global retail dump of PAN |
| Availability dependence | High | Sales and service operations would run on the CRM |
| Substitutability | Moderate | Other CRMs exist, but switching cost after data load is material |
| Regulatory adjacency | High | Nexus is a financial-services firm; vendor incidents can trigger Nexus notices |
| Fourth-party exposure | High | AWS plus utility subprocessors |

**Overall inherent vendor criticality: High.**

## Why this is not “Critical” in the 5×5 Critical band (17–25)

CloudFlow will not process cards, bank credentials, or highly restricted financial records. A complete CRM compromise would still be Major (impact 4) for confidentiality and operations, not automatically a 5 (Critical) firm-wide payments outage. Several inherent scores use impact 4 for that reason.

## Residual criticality after this assessment

Until VR-001–VR-004 are mitigated, the vendor remains **High** residual risk for onboarding. Conditional Approval is appropriate: the service is important enough to proceed with conditions, not important-plus-uncontrolled enough to Avoid by default.

## Nexus internal classification of the vendor (recommended)

Tier 1 (High) third party — annual reassessment, contractual security exhibit, and monitoring of incidents, subprocessors, PT summaries, and assurance reports.
