# Final Findings

**This is a fictional cybersecurity case study created for educational and portfolio purposes.**

## Assessment outcome

| Item | Result |
| --- | --- |
| Vendor | CloudFlow Technologies |
| Product | CloudFlow CRM |
| Customer | Nexus Financial Services |
| Score | 74.4 |
| Overall residual risk | High |
| Recommendation | Conditional Approval |

## Major calculations

| ID | Inherent L×I | Residual L×I | Rating | Treatment |
| --- | --- | --- | --- | --- |
| VR-001 | 4×4=16 | 3×4=12 | High | Mitigate |
| VR-002 | 4×4=16 | 3×4=12 | High | Mitigate |
| VR-003 | 4×4=16 | 3×4=12 | High | Mitigate |
| VR-004 | 4×4=16 | 3×4=12 | High | Mitigate |
| VR-005 | 3×3=9 | 2×3=6 | Moderate | Accept |
| VR-006 | 3×3=9 | 2×3=6 | Moderate | Accept |
| VR-007 | 4×3=12 | 3×3=9 | Moderate | Accept |
| VR-008 | 4×4=16 | 3×3=9 | Moderate | Mitigate |

Scorecard: 0.10×78 + 0.10×82 + 0.15×88 + 0.10×74 + 0.10×72 + 0.15×62 + 0.10×70 + 0.10×85 + 0.10×58 = **74.4**.

## Lessons learned (case study)

1. Scorecards measure control coverage; residual risk measures remaining plausible harm.  
2. Point-in-time SOC 2 Type I is useful and insufficient as the only independent assurance.  
3. Daily backups without an approved RPO and without frequent restore tests leave recoverability weakly evidenced.  
4. “Without undue delay” is not a customer SLA.  
5. Fourth-party (subprocessor) governance is part of C-SCRM, not a paperwork afterthought.  
6. Label simulations clearly so a portfolio never impersonates a live audit.

## Lifecycle represented

Nexus Financial Services → Vendor Selection → CloudFlow Technologies → Security Questionnaire → Vendor Responses → Evidence Collection → Control Assessment → Risk Identification → Inherent Risk → Existing Controls → Residual Risk → Risk Register → Risk Treatment → Remediation Plan → Vendor Scorecard → Executive Review → **CONDITIONAL APPROVAL**.
