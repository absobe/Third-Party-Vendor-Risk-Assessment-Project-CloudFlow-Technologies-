"""Canonical fictional assessment data for CloudFlow Technologies.

This is a fictional cybersecurity case study created for educational
and portfolio purposes. It is not an assessment of a real company.
"""

from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

DISCLAIMER = (
    "This is a fictional cybersecurity case study created for educational "
    "and portfolio purposes."
)

ASSESSMENT = {
    "assessment_id": "NEX-TPRM-2026-014",
    "assessment_type": "Initial Third-Party Vendor Security Assessment",
    "customer": "Nexus Financial Services",
    "vendor": "CloudFlow Technologies",
    "product": "CloudFlow CRM",
    "assessor": "Priya Mehta, Third-Party Risk Analyst (simulated role)",
    "reviewer": "Daniel Okonkwo, Chief Information Security Officer, Nexus Financial Services",
    "vendor_ciso": "Jordan Hale, Chief Information Security Officer, CloudFlow Technologies",
    "start_date": "2026-02-03",
    "end_date": "2026-02-28",
    "report_date": "2026-03-06",
    "overall_risk": "High",
    "recommendation": "Conditional Approval",
    "overall_score": 74.4,
}

# Likelihood/Impact 1-5. Residual scores consider existing controls without
# automatically reducing every score just because a control exists.
RISKS = [
    {
        "id": "VR-001",
        "title": "Weak Subprocessor Governance",
        "description": (
            "CloudFlow Technologies lacks a consistently documented and formally "
            "scored process for evaluating security risks associated with subprocessors."
        ),
        "business_impact": (
            "A weakly governed subprocessor could expose Nexus Confidential CRM data "
            "to unauthorized access, availability disruption, or delayed incident awareness."
        ),
        "affected_asset": "CloudFlow CRM customer and employee contact data; subprocessor chain",
        "control_domain": "Third-Party / Subprocessor Management",
        "likelihood": 4,
        "impact": 4,
        "existing_controls": (
            "Subprocessor inventory exists; contractual flow-down clauses for core AWS "
            "and selected SaaS utilities; annual review of named subprocessors without "
            "standardized risk scoring."
        ),
        "residual_likelihood": 3,
        "residual_impact": 4,
        "owner": "Jordan Hale, CISO, CloudFlow Technologies (Nexus TPRM owner: Priya Mehta)",
        "treatment": "Mitigate",
        "due_date": "2026-04-30",
        "status": "Open — remediation required before unrestricted production use",
        "acceptance_required": "No — mitigate; residual High until remediation complete",
        "evidence": "Subprocessor_Management_Summary.pdf; Q-S-048; CTRL-TPRM-004",
        "questionnaire_ids": "Q-S-047, Q-S-048, Q-S-049",
        "control_ids": "CTRL-TPRM-001, CTRL-TPRM-004",
        "remediation_id": "CAP-001",
        "primary": True,
    },
    {
        "id": "VR-002",
        "title": "Insufficient Backup Recovery Testing",
        "description": (
            "Backup restoration testing is performed annually only and may not provide "
            "sufficient evidence that critical CRM services can be recovered within expected timeframes."
        ),
        "business_impact": (
            "Nexus sales operations, customer support, and relationship records could remain "
            "unavailable longer than business tolerance after a destructive incident."
        ),
        "affected_asset": "CloudFlow CRM production data stores and backup media",
        "control_domain": "Business Continuity / Backup Management",
        "likelihood": 4,
        "impact": 4,
        "existing_controls": (
            "Daily encrypted backups; 30-day operational retention plus 12-month archive; "
            "annual restoration test of a non-production snapshot completed 2025-11-12."
        ),
        "residual_likelihood": 3,
        "residual_impact": 4,
        "owner": "Taylor Nguyen, Director of Infrastructure, CloudFlow Technologies",
        "treatment": "Mitigate",
        "due_date": "2026-04-30",
        "status": "Open — quarterly restoration testing required",
        "acceptance_required": "No — mitigate; residual High until testing cadence improves",
        "evidence": "Backup_and_Recovery_Summary.pdf; Business_Continuity_Plan.pdf; Q-M-037",
        "questionnaire_ids": "Q-L-034, Q-M-036, Q-M-037",
        "control_ids": "CTRL-BC-003, CTRL-BU-002",
        "remediation_id": "CAP-002",
        "primary": True,
    },
    {
        "id": "VR-003",
        "title": "Undefined Recovery Point Objective",
        "description": (
            "The vendor does not have a formally documented Recovery Point Objective (RPO) "
            "for the CloudFlow CRM platform."
        ),
        "business_impact": (
            "Nexus cannot confirm maximum acceptable data loss. Daily backups imply up to "
            "approximately 24 hours of potential data loss, which may exceed Confidential "
            "CRM recovery expectations."
        ),
        "affected_asset": "CloudFlow CRM platform availability and data integrity",
        "control_domain": "Business Continuity / Disaster Recovery",
        "likelihood": 4,
        "impact": 4,
        "existing_controls": (
            "Daily backups provide a de facto recovery point of approximately 24 hours; "
            "RTO of 8 hours is stated for the production CRM tier in the BCP, but RPO is "
            "not formally approved by business and technology owners."
        ),
        "residual_likelihood": 3,
        "residual_impact": 4,
        "owner": "Taylor Nguyen, Director of Infrastructure, CloudFlow Technologies",
        "treatment": "Mitigate",
        "due_date": "2026-03-31",
        "status": "Open — RPO must be documented and contractually committed",
        "acceptance_required": "No — mitigate",
        "evidence": "Business_Continuity_Plan.pdf; Backup_and_Recovery_Summary.pdf; Q-L-033",
        "questionnaire_ids": "Q-K-032, Q-L-033",
        "control_ids": "CTRL-BC-001, CTRL-DR-001",
        "remediation_id": "CAP-003",
        "primary": True,
    },
    {
        "id": "VR-004",
        "title": "Unclear Incident Notification SLA",
        "description": (
            "The customer notification timeframe following a material cybersecurity incident "
            "is not clearly defined. Vendor language uses 'without undue delay' without a clock."
        ),
        "business_impact": (
            "Nexus may be unable to meet its own regulatory, contractual, and customer "
            "notification obligations if CloudFlow delays notice after a material incident."
        ),
        "affected_asset": "Nexus incident response and regulatory notification obligations",
        "control_domain": "Incident Response",
        "likelihood": 4,
        "impact": 4,
        "existing_controls": (
            "Formal incident response plan; severity classification; internal 24-hour executive "
            "escalation for Severity 1 events; customer notice described as 'without undue delay' "
            "and 'as required by law'."
        ),
        "residual_likelihood": 3,
        "residual_impact": 4,
        "owner": "Morgan Ellis, Director of Security, CloudFlow Technologies",
        "treatment": "Mitigate",
        "due_date": "2026-03-31",
        "status": "Open — contractual 24-hour material incident notice required",
        "acceptance_required": "No — mitigate",
        "evidence": "Incident_Response_Plan.pdf; Q-J-028, Q-J-029",
        "questionnaire_ids": "Q-J-027, Q-J-028, Q-J-029",
        "control_ids": "CTRL-IR-002, CTRL-IR-004",
        "remediation_id": "CAP-004",
        "primary": True,
    },
    {
        "id": "VR-005",
        "title": "SOC 2 Type I Only",
        "description": (
            "The available SOC 2 evidence is a Type I report dated 2025-09-30. Type I "
            "describes control design at a point in time and provides less assurance about "
            "operating effectiveness over a period than a Type II report."
        ),
        "business_impact": (
            "Nexus has reduced independent assurance that described controls operated "
            "effectively throughout a review period."
        ),
        "affected_asset": "Independent assurance over CloudFlow CRM control environment",
        "control_domain": "Compliance",
        "likelihood": 3,
        "impact": 3,
        "existing_controls": (
            "SOC 2 Type I (Security and Availability TSC) issued 2025-09-30; no qualified "
            "opinion on design; Type II examination in progress targeting 2026-Q4."
        ),
        "residual_likelihood": 2,
        "residual_impact": 3,
        "owner": "Jordan Hale, CISO, CloudFlow Technologies",
        "treatment": "Accept",
        "due_date": "2026-12-31",
        "status": "Accepted with conditions — Type II required as continuous monitoring evidence",
        "acceptance_required": "Yes — CISO Nexus acceptance with Type II monitoring condition",
        "evidence": "SOC2_TypeI_Summary.pdf; Q-O-041",
        "questionnaire_ids": "Q-O-041, Q-O-042",
        "control_ids": "CTRL-CM-001, CTRL-CM-002",
        "remediation_id": "CAP-005",
        "primary": False,
    },
    {
        "id": "VR-006",
        "title": "No ISO 27001 Certification",
        "description": (
            "CloudFlow Technologies does not hold ISO/IEC 27001 certification. An internal "
            "ISMS exists and maps selected ISO 27001 control concepts, but no accredited "
            "certification has been obtained."
        ),
        "business_impact": (
            "Absence of certification is not by itself a control failure, but it reduces "
            "external validation of the information security management system."
        ),
        "affected_asset": "Information security management system assurance",
        "control_domain": "Security Governance / Compliance",
        "likelihood": 3,
        "impact": 3,
        "existing_controls": (
            "Documented information security policy; named CISO; annual policy review cycle; "
            "SOC 2 Type I; internal control mapping to ISO/IEC 27001 Annex A concepts."
        ),
        "residual_likelihood": 2,
        "residual_impact": 3,
        "owner": "Jordan Hale, CISO, CloudFlow Technologies",
        "treatment": "Accept",
        "due_date": "2027-06-30",
        "status": "Accepted with conditions — ISMS evidence accepted in lieu of certification",
        "acceptance_required": "Yes — accepted provided annual independent assurance continues",
        "evidence": "Information_Security_Policy.pdf; Q-O-042; Q-A-003",
        "questionnaire_ids": "Q-A-001, Q-O-042",
        "control_ids": "CTRL-GOV-001, CTRL-CM-003",
        "remediation_id": "CAP-006",
        "primary": False,
    },
    {
        "id": "VR-007",
        "title": "Vulnerability Remediation Window",
        "description": (
            "High-severity vulnerabilities may remain open for up to 30 days under the "
            "vendor vulnerability management policy. Critical findings target 7 days, but "
            "high-severity internet-facing issues can remain for a full month."
        ),
        "business_impact": (
            "Known exploitable weaknesses in the CRM stack could persist long enough to be "
            "targeted, increasing the chance of confidentiality or availability impact."
        ),
        "affected_asset": "CloudFlow CRM application and supporting AWS infrastructure",
        "control_domain": "Vulnerability Management",
        "likelihood": 4,
        "impact": 3,
        "existing_controls": (
            "Monthly authenticated vulnerability scanning; annual independent penetration test; "
            "WAF and security groups; 7-day target for Critical; 30-day target for High; "
            "exception process with CISO approval."
        ),
        "residual_likelihood": 3,
        "residual_impact": 3,
        "owner": "Morgan Ellis, Director of Security, CloudFlow Technologies",
        "treatment": "Accept",
        "due_date": "2026-06-30",
        "status": "Accepted with conditions — 15-day High SLA requested for internet-facing assets",
        "acceptance_required": "Yes — accepted if internet-facing High findings meet 15-day target",
        "evidence": "Vulnerability_Management_Policy.pdf; Penetration_Test_Summary.pdf; Q-F-018",
        "questionnaire_ids": "Q-F-016, Q-F-018, Q-G-020",
        "control_ids": "CTRL-VM-002, CTRL-VM-003",
        "remediation_id": "CAP-007",
        "primary": False,
    },
    {
        "id": "VR-008",
        "title": "Legacy MFA Gap",
        "description": (
            "Some legacy internal systems do not support multi-factor authentication. Privileged "
            "access to CloudFlow CRM production and AWS is MFA-enforced, but a small set of "
            "legacy administrative utilities still rely on password plus VPN."
        ),
        "business_impact": (
            "Compromise of a legacy administrative credential could provide a pathway toward "
            "production support tooling if network segmentation fails."
        ),
        "affected_asset": "Legacy internal admin utilities (not customer-facing CRM UI)",
        "control_domain": "Identity and Access Management",
        "likelihood": 4,
        "impact": 4,
        "existing_controls": (
            "MFA for production CRM, AWS IAM (privileged), and corporate SSO; VPN required "
            "for legacy tools; quarterly access reviews; privileged access via jump host for AWS."
        ),
        "residual_likelihood": 3,
        "residual_impact": 3,
        "owner": "Morgan Ellis, Director of Security, CloudFlow Technologies",
        "treatment": "Mitigate",
        "due_date": "2026-05-15",
        "status": "Open — MFA or compensating control required on remaining legacy admin tools",
        "acceptance_required": "No — mitigate",
        "evidence": "Access_Control_Policy.pdf; Q-C-009",
        "questionnaire_ids": "Q-C-008, Q-C-009, Q-C-011",
        "control_ids": "CTRL-AC-001, CTRL-AC-004",
        "remediation_id": "CAP-008",
        "primary": False,
    },
]


def rating(score: int) -> str:
    if score <= 4:
        return "Low"
    if score <= 9:
        return "Moderate"
    if score <= 16:
        return "High"
    return "Critical"


for r in RISKS:
    r["inherent_risk"] = r["likelihood"] * r["impact"]
    r["inherent_rating"] = rating(r["inherent_risk"])
    r["residual_risk"] = r["residual_likelihood"] * r["residual_impact"]
    r["residual_rating"] = rating(r["residual_risk"])
    r["risk_rating"] = r["residual_rating"]


SCORECARD_DOMAINS = [
    {"domain": "Security Governance", "weight": 0.10, "score": 78},
    {"domain": "Access Control", "weight": 0.10, "score": 82},
    {"domain": "Data Protection", "weight": 0.15, "score": 88},
    {"domain": "Vulnerability Management", "weight": 0.10, "score": 74},
    {"domain": "Incident Response", "weight": 0.10, "score": 72},
    {"domain": "Business Continuity", "weight": 0.15, "score": 62},
    {"domain": "Compliance", "weight": 0.10, "score": 70},
    {"domain": "Cloud Security", "weight": 0.10, "score": 85},
    {"domain": "Third-Party Management", "weight": 0.10, "score": 58},
]

OVERALL_SCORE = round(sum(d["weight"] * d["score"] for d in SCORECARD_DOMAINS), 1)
assert abs(OVERALL_SCORE - 74.4) < 0.05

REMEDIATION = [
    {
        "id": "CAP-001",
        "finding_id": "VR-001",
        "finding": "Weak Subprocessor Governance",
        "action": "Establish documented risk-based security assessments for all critical subprocessors, including a scored questionnaire, residual-risk rating, and approval record.",
        "recommended_control": "Formal subprocessor risk assessment procedure aligned to NIST SP 800-161 concepts",
        "owner": "Jordan Hale, CISO, CloudFlow Technologies",
        "priority": "High",
        "due_date": "2026-04-30",
        "success_criteria": "Approved subprocessor assessment procedure and completed assessments for all critical subprocessors, with scores retained for Nexus review.",
        "evidence_required": "Procedure document, completed assessments, residual-risk ratings, and contract flow-down evidence",
        "status": "Open",
    },
    {
        "id": "CAP-002",
        "finding_id": "VR-002",
        "finding": "Insufficient Backup Recovery Testing",
        "action": "Perform documented restoration testing at least quarterly for critical CRM data stores and record recovery timing against RTO/RPO.",
        "recommended_control": "Quarterly backup restoration tests for production-equivalent datasets",
        "owner": "Taylor Nguyen, Director of Infrastructure, CloudFlow Technologies",
        "priority": "High",
        "due_date": "2026-04-30",
        "success_criteria": "Successful restoration test report with measured recovery timing for at least one production-equivalent restore.",
        "evidence_required": "Restoration test report, timestamps, issues log, and sign-off",
        "status": "Open",
    },
    {
        "id": "CAP-003",
        "finding_id": "VR-003",
        "finding": "Undefined Recovery Point Objective",
        "action": "Define and formally approve a platform-specific RPO for CloudFlow CRM and reflect it in the BCP, customer contract, and backup design.",
        "recommended_control": "Documented and approved RPO (recommended: <= 4 hours for Confidential CRM data or compensating continuous backup)",
        "owner": "Taylor Nguyen, Director of Infrastructure, CloudFlow Technologies",
        "priority": "High",
        "due_date": "2026-03-31",
        "success_criteria": "Documented RPO approved by CloudFlow technology and business owners and committed in the Nexus MSA/DPA addendum.",
        "evidence_required": "Approved RPO statement, BCP update, and contractual exhibit",
        "status": "Open",
    },
    {
        "id": "CAP-004",
        "finding_id": "VR-004",
        "finding": "Unclear Incident Notification SLA",
        "action": "Commit to a contractual customer notification SLA of 24 hours from confirmation of a material cybersecurity incident affecting Nexus data or services.",
        "recommended_control": "Contractual 24-hour material incident notification clause with named contacts",
        "owner": "Morgan Ellis, Director of Security, CloudFlow Technologies; Samira Patel, Legal Counsel, Nexus",
        "priority": "High",
        "due_date": "2026-03-31",
        "success_criteria": "Executed contract language specifying 24-hour notice, severity definitions, and communication channels.",
        "evidence_required": "Signed MSA/DPA security exhibit and updated IR plan notification matrix",
        "status": "Open",
    },
    {
        "id": "CAP-005",
        "finding_id": "VR-005",
        "finding": "SOC 2 Type I Only",
        "action": "Provide a SOC 2 Type II report covering Security and Availability for a minimum six-month period, or an equivalent independent examination.",
        "recommended_control": "SOC 2 Type II (Security, Availability) as continuous monitoring evidence",
        "owner": "Jordan Hale, CISO, CloudFlow Technologies",
        "priority": "Moderate",
        "due_date": "2026-12-31",
        "success_criteria": "Unqualified Type II report covering the production CRM environment provided to Nexus TPRM.",
        "evidence_required": "SOC 2 Type II report (or documented delay with compensating evidence)",
        "status": "Monitoring — accepted with conditions",
    },
    {
        "id": "CAP-006",
        "finding_id": "VR-006",
        "finding": "No ISO 27001 Certification",
        "action": "Maintain mapped ISMS evidence and provide annual independent assurance. ISO 27001 certification is encouraged but not a go-live blocker.",
        "recommended_control": "Continued SOC 2 / independent assurance and ISMS control mapping",
        "owner": "Jordan Hale, CISO, CloudFlow Technologies",
        "priority": "Low",
        "due_date": "2027-06-30",
        "success_criteria": "Annual independent assurance package received; optional ISO 27001 roadmap shared.",
        "evidence_required": "ISMS mapping workbook and next independent report",
        "status": "Monitoring — accepted with conditions",
    },
    {
        "id": "CAP-007",
        "finding_id": "VR-007",
        "finding": "Vulnerability Remediation Window",
        "action": "Commit to a 15-day remediation target for High-severity findings on internet-facing CloudFlow CRM assets, with documented exceptions.",
        "recommended_control": "Differentiated SLA: Critical 7 days; internet-facing High 15 days; other High 30 days with exception register",
        "owner": "Morgan Ellis, Director of Security, CloudFlow Technologies",
        "priority": "Moderate",
        "due_date": "2026-06-30",
        "success_criteria": "Updated vulnerability policy and two months of ticket metrics demonstrating the 15-day internet-facing High target.",
        "evidence_required": "Updated policy and vulnerability SLA metrics",
        "status": "Monitoring — accepted with conditions",
    },
    {
        "id": "CAP-008",
        "finding_id": "VR-008",
        "finding": "Legacy MFA Gap",
        "action": "Enforce MFA or a documented compensating control (hardware token or identity-aware proxy) on remaining legacy administrative utilities, or retire the systems.",
        "recommended_control": "MFA for all administrative access paths, including legacy tools",
        "owner": "Morgan Ellis, Director of Security, CloudFlow Technologies",
        "priority": "High",
        "due_date": "2026-05-15",
        "success_criteria": "Inventory of legacy admin tools showing MFA enabled or systems decommissioned, with access-review evidence.",
        "evidence_required": "Updated access control evidence and SSO/MFA coverage report",
        "status": "Open",
    },
]
