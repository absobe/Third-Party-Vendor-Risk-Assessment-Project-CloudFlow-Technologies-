# Risk Scoring Methodology

**This is a fictional cybersecurity case study created for educational and portfolio purposes.**

## Model

Simple 5×5. **Risk Score = Likelihood × Impact.**

### Likelihood

| Score | Label | Meaning in this assessment |
| ---: | --- | --- |
| 1 | Rare | Conceivable but not expected during the relationship |
| 2 | Unlikely | Could occur, but existing design makes it uncommon |
| 3 | Possible | Could occur at some point in a 12–36 month horizon |
| 4 | Likely | A realistic scenario given the gap, even if not frequent |
| 5 | Almost Certain | Expected unless the gap is closed |

### Impact

| Score | Label | Meaning for Nexus |
| ---: | --- | --- |
| 1 | Negligible | Immaterial operational or confidentiality effect |
| 2 | Minor | Limited, recoverable disruption or small data subset |
| 3 | Moderate | Noticeable operational, assurance, or limited Confidential exposure |
| 4 | Major | Significant Confidential CRM exposure, extended outage, or missed regulatory notice |
| 5 | Critical | Firm-wide or highly restricted financial / payments impact (out of this product’s data scope) |

### Rating

| Score | Rating |
| --- | --- |
| 1–4 | Low |
| 5–9 | Moderate |
| 10–16 | High |
| 17–25 | Critical |

Excel formulas in the risk register:

```text
Inherent Risk  = Likelihood * Impact
Residual Risk  = Residual Likelihood * Residual Impact
Rating         = IF(score<=4,"Low",IF(score<=9,"Moderate",IF(score<=16,"High","Critical")))
```

## Inherent versus residual

**Inherent risk** is scored as if existing controls were absent or failed. **Residual risk** credits only controls that change frequency, detectability, or blast radius. A policy binder does not automatically reduce impact. Example: VR-001 inherent 4×4=16 High; inventory/contracts reduce likelihood to 3; impact stays 4; residual 12 High.

## Overall vendor rating rule

The **highest residual rating among material findings that remain open without sufficient treatment in operation** drives the vendor roll-up. Four High residual risks remain, so overall residual risk is **High**, even though the weighted scorecard is 74.4 and no residual risk is Critical (17–25).
