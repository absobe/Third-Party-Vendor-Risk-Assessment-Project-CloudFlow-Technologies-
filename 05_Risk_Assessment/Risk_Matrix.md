# Risk Matrix

**This is a fictional cybersecurity case study created for educational and portfolio purposes.**

Likelihood increases upward; impact increases to the right. Residual positions for VR-001–VR-008:

| L \ I | 1 Negligible | 2 Minor | 3 Moderate | 4 Major | 5 Critical |
| ---: | --- | --- | --- | --- | --- |
| 5 Almost Certain | 5 Mod | 10 High | 15 High | 20 Crit | 25 Crit |
| 4 Likely | 4 Low | 8 Mod | 12 High | 16 High | 20 Crit |
| 3 Possible | 3 Low | 6 Mod | 9 Mod | 12 High | 15 High |
| 2 Unlikely | 2 Low | 4 Low | 6 Mod | 8 Mod | 10 High |
| 1 Rare | 1 Low | 2 Low | 3 Low | 4 Low | 5 Mod |

## Residual placements

| Risk ID | Residual L | Residual I | Score | Band | Heat-map cell |
| --- | ---: | ---: | ---: | --- | --- |
| VR-001 | 3 | 4 | 12 | High | Possible × Major |
| VR-002 | 3 | 4 | 12 | High | Possible × Major |
| VR-003 | 3 | 4 | 12 | High | Possible × Major |
| VR-004 | 3 | 4 | 12 | High | Possible × Major |
| VR-005 | 2 | 3 | 6 | Moderate | Unlikely × Moderate |
| VR-006 | 2 | 3 | 6 | Moderate | Unlikely × Moderate |
| VR-007 | 3 | 3 | 9 | Moderate | Possible × Moderate |
| VR-008 | 3 | 3 | 9 | Moderate | Possible × Moderate |

Inherent scores for VR-001, VR-002, VR-003, VR-004, and VR-008 were 16 (Likely × Major) before control credit. VR-007 inherent was 12 (Likely × Moderate). A PNG heat map is produced by `python 14_Scripts/generate_scorecard.py`.
