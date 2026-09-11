# Remediation Prioritization

**This is a fictional cybersecurity case study created for educational and portfolio purposes.**

## Sequencing logic

1. **Contractual clocks first (March 2026):** RPO (VR-003) and incident notification (VR-004). These are documentation and legal instruments Nexus can enforce even before CloudFlow finishes engineering work.  
2. **Recoverability proof (April 2026):** quarterly restore testing (VR-002) and subprocessor scoring procedure (VR-001).  
3. **Access path hygiene (May 2026):** legacy MFA (VR-008).  
4. **Assurance upgrades (June–December 2026):** vulnerability SLA tightening (VR-007) and SOC 2 Type II (VR-005).  
5. **Optional certification (2027):** ISO 27001 (VR-006).

## Priority versus residual rating

| Priority | Items | Why |
| --- | --- | --- |
| High | VR-001, VR-002, VR-003, VR-004, VR-008 | Open High residual, or Moderate residual with a clear production-path gap (MFA) |
| Moderate | VR-005, VR-007 | Accepted with dated monitoring conditions |
| Low | VR-006 | Assurance preference, not a control vacuum |

## Dependency

RPO definition (CAP-003) should precede interpreting restore-test success (CAP-002), because “successful restore” is only meaningful against an approved loss window.
