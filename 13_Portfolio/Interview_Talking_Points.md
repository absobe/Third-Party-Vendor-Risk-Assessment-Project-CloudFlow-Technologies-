# Interview Talking Points

**This is a fictional cybersecurity case study created for educational and portfolio purposes.**  
Answers are written for a third-year software-engineering / GRC internship interview. They are technically accurate and do not overclaim professional employment.

---

### What is third-party risk management?

Third-party risk management is the process of identifying, assessing, treating, and monitoring security and related risks introduced by vendors and other external parties. In this project, Nexus would depend on CloudFlow to protect Confidential CRM data, stay available, and notify Nexus of material incidents.

### Why did you assess the vendor?

Nexus was considering CloudFlow CRM before onboarding. Any processor of Confidential customer and employee information needs due diligence. The assessment answers whether onboarding is acceptable and under what conditions.

### How did you calculate risk?

I used a 5×5 model: Likelihood (1–5) times Impact (1–5). Scores 1–4 Low, 5–9 Moderate, 10–16 High, 17–25 Critical. Excel formulas compute the products and ratings so the register is reproducible.

### What is inherent risk?

Risk before crediting existing controls — as if the control failed or did not exist. Example: informal subprocessor governance scored 4×4=16 High inherent.

### What is residual risk?

Risk remaining after existing controls. Controls do not automatically reduce scores. For VR-001, an inventory and some contracts lowered likelihood to 3, but impact stayed 4, so residual 12 remained High.

### Why did you recommend conditional approval?

The vendor had a workable SaaS baseline (encryption, privileged MFA, scanning, backups, IR plan) and would not process payments data. High gaps were remediable with procedures and contract language. That supports onboarding with conditions rather than a blanket yes.

### Why wasn't the vendor rejected?

Rejection (Avoid) is for unacceptable risk that cannot be reasonably treated. Missing ISO 27001 or a Type II report, by themselves, did not mean controls were absent. High findings had credible mitigations. Avoid remained available if CAP dates were missed.

### What was the highest risk?

Four findings share the highest residual band: VR-001 subprocessor governance, VR-002 restore testing, VR-003 undefined RPO, and VR-004 notification SLA, each residual 12 High. I would discuss VR-004 and VR-001 first with executives because they affect Nexus’s own regulatory notice and fourth-party exposure.

### How did you evaluate vendor evidence?

I mapped each artifact to control IDs, checked internal consistency (for example, BCP without RPO), and refused to rate a control Effective without evidence. SOC 2 Type II was Evidence Not Provided. Subprocessor scoring was Partially Effective because the vendor disclosed an informal process.

### What is the difference between SOC 2 Type I and Type II?

Type I is point-in-time design suitability. Type II tests operating effectiveness over a period. VR-005 exists because Type I gives less assurance that controls actually ran as described for six or twelve months.

### Why is subprocessor risk important?

CloudFlow’s subprocessors are fourth parties to Nexus. A weak email or analytics provider can still see Confidential data. NIST SP 800-161 concepts emphasize supply-chain C-SCRM, not only the prime vendor’s policies.

### How would you improve this assessment with a real vendor?

Request original SOC reports under NDA, sample access-review tickets, restore-test logs, vulnerability SLA metrics, insurance certificates, and a live architecture walkthrough. Add targeted technical testing only with authorization. Involve legal on the actual MSA. Recalculate residual risk from real evidence, which might differ from this simulation.

### What limitations did your project have?

It is fictional. I authored both the questionnaire answers and the evidence, so independence is simulated. There is no live testing, no real regulatory opinion, and no certification. Scores are a teaching model, not an actuarial loss forecast.
