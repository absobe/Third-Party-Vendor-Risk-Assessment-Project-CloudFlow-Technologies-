# Risk Treatment Decisions

**This is a fictional cybersecurity case study created for educational and portfolio purposes.**

Treatment options used: **Mitigate**, **Accept**, **Transfer**, **Avoid**. None of the eight findings is Avoid (reject the vendor) or Transfer (e.g., insurance as the primary strategy). Insurance is unverified in the pack and is not used as a treatment.

| Risk ID | Decision | Rationale |
| --- | --- | --- |
| VR-001 | **Mitigate** | Fourth-party Confidential data exposure is not an acceptable standing design. |
| VR-002 | **Mitigate** | Annual restore tests do not evidence recoverability for a Tier-1 CRM. |
| VR-003 | **Mitigate** | Nexus cannot accept an undefined loss window. |
| VR-004 | **Mitigate** | Nexus regulatory/customer clocks need a 24-hour vendor notice commitment. |
| VR-005 | **Accept** (with conditions) | Type I plus internal controls are enough to start, if Type II is a 2026 monitoring condition. |
| VR-006 | **Accept** (with conditions) | Missing certification ≠ missing ISMS. Independent assurance still required. |
| VR-007 | **Accept** (with conditions) | 7-day Critical SLA and scanning/PT exist; negotiate 15-day internet-facing High. |
| VR-008 | **Mitigate** | Privileged-adjacent paths without MFA remain an actionable gap. |

Avoid was considered and rejected: strengths in encryption, privileged MFA, logging, backups, IR design, and scoped data (no PAN) make onboarding viable **with conditions**. Transfer was considered for VR-005/006 (rely solely on future certificates) and rejected as the sole strategy; acceptance is paired with monitoring.
