"""Generate fictional evidence PDFs for CloudFlow Technologies."""

from __future__ import annotations

import sys
from pathlib import Path

from reportlab.lib.colors import HexColor, white
from reportlab.lib.enums import TA_CENTER, TA_JUSTIFY, TA_LEFT
from reportlab.lib.pagesizes import LETTER
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import inch
from reportlab.platypus import (
    ListFlowable,
    ListItem,
    PageBreak,
    Paragraph,
    SimpleDocTemplate,
    Spacer,
    Table,
    TableStyle,
)

sys.path.insert(0, str(Path(__file__).resolve().parent))
from project_data import DISCLAIMER, ROOT  # noqa: E402

NAVY = HexColor("#1B365D")
GOLD = HexColor("#C4A35A")
RED = HexColor("#8B1E3F")
INK = HexColor("#1F2933")
RULE = HexColor("#C5CDD6")

OUT = ROOT / "03_Vendor_Evidence"


def styles():
    s = getSampleStyleSheet()
    s.add(ParagraphStyle("Banner", parent=s["Title"], fontName="Times-Bold", fontSize=18, textColor=NAVY, leading=22, alignment=TA_LEFT, spaceAfter=6))
    s.add(ParagraphStyle("Sub", parent=s["Normal"], fontName="Times-Italic", fontSize=10, textColor=RED, leading=13, spaceAfter=10))
    s.add(ParagraphStyle("H", parent=s["Heading1"], fontName="Times-Bold", fontSize=13, textColor=NAVY, spaceBefore=12, spaceAfter=6, leading=16))
    s.add(ParagraphStyle("H2", parent=s["Heading2"], fontName="Times-Bold", fontSize=11, textColor=NAVY, spaceBefore=8, spaceAfter=4, leading=14))
    s.add(ParagraphStyle("Body", parent=s["Normal"], fontName="Times-Roman", fontSize=10, textColor=INK, leading=14, alignment=TA_JUSTIFY, spaceAfter=6))
    s.add(ParagraphStyle("Meta", parent=s["Normal"], fontName="Times-Roman", fontSize=9, leading=12, textColor=INK))
    s.add(ParagraphStyle("Footer", parent=s["Normal"], fontName="Times-Italic", fontSize=8, textColor=HexColor("#52606D"), alignment=TA_CENTER))
    s.add(ParagraphStyle("BulletBody", parent=s["Normal"], fontName="Times-Roman", fontSize=10, leading=13, textColor=INK))
    return s


def header_footer(canvas, doc):
    canvas.saveState()
    canvas.setFillColor(NAVY)
    canvas.rect(0, 10.7 * inch, 8.5 * inch, 0.55 * inch, fill=1, stroke=0)
    canvas.setFillColor(GOLD)
    canvas.rect(0, 10.7 * inch, 0.12 * inch, 0.55 * inch, fill=1, stroke=0)
    canvas.setFillColor(white)
    canvas.setFont("Times-Bold", 9)
    canvas.drawString(0.75 * inch, 10.9 * inch, "CLOUDFLOW TECHNOLOGIES  |  SIMULATED / FICTIONAL EVIDENCE — FOR EDUCATIONAL USE ONLY")
    canvas.setFillColor(RULE)
    canvas.rect(0.75 * inch, 0.55 * inch, 7 * inch, 0.4, fill=1, stroke=0)
    canvas.setFillColor(HexColor("#52606D"))
    canvas.setFont("Times-Italic", 8)
    canvas.drawCentredString(4.25 * inch, 0.35 * inch, f"{DISCLAIMER}  |  Page {doc.page}")
    canvas.restoreState()


def meta_table(rows, st):
    data = [[Paragraph(f"<b>{k}</b>", st["Meta"]), Paragraph(v, st["Meta"])] for k, v in rows]
    t = Table(data, colWidths=[2.1 * inch, 5.0 * inch])
    t.setStyle(
        TableStyle(
            [
                ("BACKGROUND", (0, 0), (0, -1), HexColor("#E8EEF2")),
                ("BOX", (0, 0), (-1, -1), 0.4, RULE),
                ("INNERGRID", (0, 0), (-1, -1), 0.3, RULE),
                ("VALIGN", (0, 0), (-1, -1), "TOP"),
                ("LEFTPADDING", (0, 0), (-1, -1), 6),
                ("RIGHTPADDING", (0, 0), (-1, -1), 6),
                ("TOPPADDING", (0, 0), (-1, -1), 4),
                ("BOTTOMPADDING", (0, 0), (-1, -1), 4),
            ]
        )
    )
    return t


def bullets(items, st):
    return ListFlowable(
        [ListItem(Paragraph(i, st["BulletBody"]), leftIndent=12) for i in items],
        bulletType="bullet",
        start="•",
    )


def build(path, title, doc_id, story_builder):
    st = styles()
    doc = SimpleDocTemplate(
        str(path),
        pagesize=LETTER,
        leftMargin=0.75 * inch,
        rightMargin=0.75 * inch,
        topMargin=1.15 * inch,
        bottomMargin=0.8 * inch,
        title=title,
        author="CloudFlow Technologies (fictional)",
    )
    story = story_builder(st, title, doc_id)
    doc.build(story, onFirstPage=header_footer, onLaterPages=header_footer)
    print(f"Wrote {path.relative_to(ROOT)}")


COMMON_META = [
    ("Organization", "CloudFlow Technologies (fictional SaaS vendor)"),
    ("Product in scope", "CloudFlow CRM"),
    ("Classification", "Confidential — Internal Use / Simulated Evidence"),
    ("Approval status", "Approved for simulation (not a live corporate record)"),
    ("Document owner", "Jordan Hale, Chief Information Security Officer"),
]


def isp(st, title, doc_id):
    s = [
        Paragraph(title, st["Banner"]),
        Paragraph("SIMULATED / FICTIONAL EVIDENCE — FOR EDUCATIONAL USE ONLY", st["Sub"]),
        meta_table(
            COMMON_META
            + [
                ("Document ID", doc_id),
                ("Version", "3.2"),
                ("Effective date", "15 January 2025"),
                ("Last review date", "15 January 2026"),
                ("Next review", "15 January 2027"),
            ],
            st,
        ),
        Paragraph("1. Purpose", st["H"]),
        Paragraph(
            "This policy establishes CloudFlow Technologies’ information security governance for the CloudFlow CRM "
            "SaaS platform and supporting AWS environment. It assigns accountability for protecting customer and "
            "employee information classified as Confidential. This document is simulated for an educational third-party "
            "risk assessment case study and does not describe a real company.",
            st["Body"],
        ),
        Paragraph("2. Security governance", st["H"]),
        Paragraph(
            "The Chief Information Security Officer (CISO) is accountable for the information security management system "
            "(ISMS). A Security Steering Committee, chaired by the CISO, meets quarterly. Engineering, Infrastructure, "
            "Legal, and Customer Success hold defined RACI responsibilities. CloudFlow maps selected controls to NIST "
            "Cybersecurity Framework functions, ISO/IEC 27001 control concepts, and SOC 2 Trust Services Criteria as "
            "methodological guidance. CloudFlow does not claim ISO/IEC 27001 certification.",
            st["Body"],
        ),
        Paragraph("3. Roles and responsibilities", st["H"]),
        bullets(
            [
                "CISO: policy ownership, risk acceptance above defined thresholds, customer security communications.",
                "Director of Security: operations, vulnerability management, incident command, awareness training.",
                "Director of Infrastructure: AWS baseline, backups, recovery design, capacity.",
                "Engineering leads: secure SDLC, code review, application tenant isolation.",
                "All personnel: acceptable use, reporting of suspected incidents within 2 hours of awareness.",
            ],
            st,
        ),
        Paragraph("4. Policy suite and review", st["H"]),
        Paragraph(
            "Core policies include access control, data protection, incident response, vulnerability management, acceptable "
            "use, and business continuity. Policies are reviewed at least annually or after material change. The 15 January "
            "2026 review confirmed POL-IS-001, POL-AC-002, IRP-001, BCP-001, POL-VM-005, and STD-DP-004. Supporting "
            "work instructions for two secondary standards did not include complete sign-off packets at the time of this "
            "simulated evidence pack, which an assessor may treat as a documentation completeness gap rather than an "
            "absent program.",
            st["Body"],
        ),
        Paragraph("5. Human resources security", st["H"]),
        Paragraph(
            "Employees complete mandatory security awareness training at hire and annually thereafter, with two phishing "
            "simulations per year. CloudFlow does not currently operate a continuous micro-learning program. Background "
            "screening is performed for employees in the United States and United Kingdom consistent with local law. "
            "Violations of this policy may result in disciplinary action up to termination.",
            st["Body"],
        ),
        Paragraph("6. Related documents", st["H"]),
        Paragraph(
            "POL-AC-002 Access Control Policy; IRP-001 Incident Response Plan; BCP-001 Business Continuity Plan; "
            "POL-VM-005 Vulnerability Management Policy; STD-DP-004 Data Protection Standard.",
            st["Body"],
        ),
    ]
    return s


def acp(st, title, doc_id):
    return [
        Paragraph(title, st["Banner"]),
        Paragraph("SIMULATED / FICTIONAL EVIDENCE — FOR EDUCATIONAL USE ONLY", st["Sub"]),
        meta_table(
            COMMON_META
            + [
                ("Document ID", doc_id),
                ("Version", "2.1"),
                ("Effective date", "01 March 2025"),
                ("Last review date", "15 January 2026"),
                ("Next review", "15 January 2027"),
            ],
            st,
        ),
        Paragraph("1. Purpose", st["H"]),
        Paragraph(
            "This policy defines identity and access management for CloudFlow CRM, corporate identity, and AWS. "
            "The objective is least privilege, unique identification, and protection of privileged access.",
            st["Body"],
        ),
        Paragraph("2. Role-based access control", st["H"]),
        Paragraph(
            "Access is granted by role, not individual standing entitlements, wherever the platform supports it. "
            "Application roles include Tenant Admin, Sales User, Support Agent, and CloudFlow Operator. AWS access "
            "uses permission sets. Production data access by CloudFlow personnel requires a documented support ticket "
            "except for automated platform operations.",
            st["Body"],
        ),
        Paragraph("3. Multi-factor authentication", st["H"]),
        Paragraph(
            "MFA is mandatory for: (a) corporate SSO; (b) CloudFlow CRM privileged (operator) access; (c) AWS IAM "
            "privileged roles. Hardware keys are preferred for administrators; TOTP is permitted. Customer tenant users "
            "may enable MFA; Nexus should require MFA for its own users via tenant policy.",
            st["Body"],
        ),
        Paragraph("4. Privileged access", st["H"]),
        Paragraph(
            "AWS privileged sessions are conducted through a jump host with time-bound roles. Standing administrator "
            "rights on laptops are prohibited for production cloud administration.",
            st["Body"],
        ),
        Paragraph("5. Joiner / mover / leaver", st["H"]),
        bullets(
            [
                "Joiners: access provisioned from HR-approved role templates after identity proofing.",
                "Movers: access recertified within five business days of role change.",
                "Leavers: all access revoked within 24 hours of HR notification; privileged access revoked immediately where feasible.",
            ],
            st,
        ),
        Paragraph("6. Periodic access reviews", st["H"]),
        Paragraph(
            "Privileged access is reviewed quarterly. Standard user access is reviewed semi-annually. Reviews are "
            "recorded and exceptions tracked.",
            st["Body"],
        ),
        Paragraph("6.4 Legacy systems exception (disclosed)", st["H"]),
        Paragraph(
            "A small set of legacy internal administrative utilities used for historical reporting do not support MFA. "
            "Access to those utilities requires corporate VPN and password authentication. This exception is recorded "
            "and is scheduled for retirement or identity-proxy enforcement. Production CloudFlow CRM and AWS privileged "
            "paths are not in this exception set. An assessor should treat this as a partial MFA coverage gap.",
            st["Body"],
        ),
    ]


def irp(st, title, doc_id):
    return [
        Paragraph(title, st["Banner"]),
        Paragraph("SIMULATED / FICTIONAL EVIDENCE — FOR EDUCATIONAL USE ONLY", st["Sub"]),
        meta_table(
            COMMON_META
            + [
                ("Document ID", doc_id),
                ("Version", "2.4"),
                ("Effective date", "01 June 2024"),
                ("Last review date", "15 January 2026"),
                ("Last tabletop exercise", "19 August 2025"),
            ],
            st,
        ),
        Paragraph("1. Purpose", st["H"]),
        Paragraph(
            "This plan describes how CloudFlow Technologies detects, classifies, contains, eradicates, and recovers "
            "from cybersecurity incidents affecting CloudFlow CRM and supporting systems.",
            st["Body"],
        ),
        Paragraph("2. Incident classification", st["H"]),
        bullets(
            [
                "Severity 1: confirmed material impact to confidentiality, integrity, or availability of customer production data or a widespread service outage.",
                "Severity 2: confirmed security event with limited blast radius or degraded service.",
                "Severity 3: suspected event or policy violation without confirmed customer impact.",
            ],
            st,
        ),
        Paragraph("3. Detection", st["H"]),
        Paragraph(
            "Detection sources include SIEM alerts, GuardDuty, WAF events, employee reports, customer reports, and "
            "vulnerability intelligence. Security operations triages alerts 24x7 for privileged anomalies.",
            st["Body"],
        ),
        Paragraph("4. Containment, eradication, recovery", st["H"]),
        Paragraph(
            "Incident Command is the Director of Security or delegate. Containment may include credential revocation, "
            "security-group changes, tenant isolation actions, and traffic blocking. Eradication removes the cause. "
            "Recovery restores service from known-good configuration and backups. A lessons-learned review is required "
            "for Severity 1 and 2 within 15 business days.",
            st["Body"],
        ),
        Paragraph("5. Internal escalation", st["H"]),
        Paragraph(
            "Severity 1 incidents are escalated to the CISO and executive leadership within 24 hours of confirmation.",
            st["Body"],
        ),
        Paragraph("6. Notification (customer) — current language", st["H"]),
        Paragraph(
            "CloudFlow will notify affected customers of a material cybersecurity incident without undue delay and as "
            "required by applicable law. Named customer security contacts are used where provided. This plan does not "
            "currently specify an hour-based customer notification SLA (for example, 24 or 72 hours). Legal and "
            "communications maintain internal notice templates; those templates are not appended to this customer-facing "
            "excerpt. An assessor should treat the absence of a clock as a contractual and operational gap.",
            st["Body"],
        ),
        Paragraph("7. Evidence handling", st["H"]),
        Paragraph(
            "Logs and forensic images are preserved in write-once storage. Chain-of-custody is recorded for Severity 1.",
            st["Body"],
        ),
    ]


def bcp(st, title, doc_id):
    return [
        Paragraph(title, st["Banner"]),
        Paragraph("SIMULATED / FICTIONAL EVIDENCE — FOR EDUCATIONAL USE ONLY", st["Sub"]),
        meta_table(
            COMMON_META
            + [
                ("Document ID", doc_id),
                ("Version", "1.9"),
                ("Effective date", "01 September 2024"),
                ("Last review date", "15 January 2026"),
                ("Last tabletop", "04 December 2025"),
            ],
            st,
        ),
        Paragraph("1. Critical services", st["H"]),
        Paragraph(
            "CloudFlow CRM production application, primary PostgreSQL-compatible data store, authentication service, "
            "and customer notification email pipeline are Tier-1. Analytics pipelines are Tier-2.",
            st["Body"],
        ),
        Paragraph("2. Recovery objectives", st["H"]),
        Paragraph(
            "The approved Recovery Time Objective (RTO) for the production CRM application tier is eight (8) hours. "
            "A Recovery Point Objective (RPO) is not formally documented or approved in this plan. Daily backups currently "
            "provide a de facto recovery point of approximately 24 hours. Technology and business owners have not signed "
            "an RPO statement. This is an intentional disclosure for the simulated assessment.",
            st["Body"],
        ),
        Paragraph("3. Business continuity", st["H"]),
        Paragraph(
            "Workforce continuity uses corporate SaaS productivity tools and a documented crisis communications roster. "
            "Customer Success maintains a status page process for availability events.",
            st["Body"],
        ),
        Paragraph("4. Disaster recovery", st["H"]),
        Paragraph(
            "Production is deployed multi-AZ in AWS us-east-1. Backups replicate to a separate AWS account in us-east-2. "
            "A regional impairment runbook exists. A full regional failover exercise was not completed in calendar year 2025. "
            "The BCP is exercised via annual tabletop and annual technical restore.",
            st["Body"],
        ),
        Paragraph("5. Dependencies", st["H"]),
        Paragraph(
            "Critical subprocessors include Amazon Web Services. Email delivery and selected analytics utilities are listed "
            "in the subprocessor inventory. Continuity of those parties is addressed contractually but not through a fully "
            "scored residual-risk process (see Subprocessor Management Summary).",
            st["Body"],
        ),
    ]


def vmp(st, title, doc_id):
    return [
        Paragraph(title, st["Banner"]),
        Paragraph("SIMULATED / FICTIONAL EVIDENCE — FOR EDUCATIONAL USE ONLY", st["Sub"]),
        meta_table(
            COMMON_META
            + [
                ("Document ID", doc_id),
                ("Version", "1.6"),
                ("Effective date", "10 February 2025"),
                ("Last review date", "15 January 2026"),
            ],
            st,
        ),
        Paragraph("1. Scanning", st["H"]),
        Paragraph(
            "Authenticated vulnerability scanning of production and staging is performed at least monthly. Unauthenticated "
            "external scanning is performed weekly. Software composition analysis runs on each build and weekly on default branches.",
            st["Body"],
        ),
        Paragraph("2. Remediation windows", st["H"]),
        bullets(
            [
                "Critical: 7 days from confirmation.",
                "High: 30 days from confirmation.",
                "Medium: 90 days from confirmation.",
                "Low: best effort, not to exceed 180 days without exception.",
            ],
            st,
        ),
        Paragraph(
            "Exceptions require CISO approval, a compensating control, and an expiry date not exceeding 90 days without re-approval. "
            "The 30-day High window applies to application and infrastructure findings, including internet-facing assets unless a "
            "shorter target is agreed with a customer in a security exhibit.",
            st["Body"],
        ),
        Paragraph("3. Penetration testing", st["H"]),
        Paragraph(
            "An independent penetration test of the SaaS environment is performed at least annually. Findings are entered into "
            "the vulnerability register and follow the SLAs above unless the tester’s severity mapping is adjusted by the CISO "
            "with written rationale.",
            st["Body"],
        ),
        Paragraph("4. Patching of cloud images", st["H"]),
        Paragraph(
            "Base images are rebuilt at least monthly. Emergency patches follow the Critical SLA.",
            st["Body"],
        ),
    ]


def dps(st, title, doc_id):
    return [
        Paragraph(title, st["Banner"]),
        Paragraph("SIMULATED / FICTIONAL EVIDENCE — FOR EDUCATIONAL USE ONLY", st["Sub"]),
        meta_table(
            COMMON_META
            + [
                ("Document ID", doc_id),
                ("Version", "2.0"),
                ("Effective date", "01 April 2025"),
                ("Last review date", "15 January 2026"),
            ],
            st,
        ),
        Paragraph("1. Data in scope for typical CRM tenants", st["H"]),
        Paragraph(
            "CloudFlow CRM stores customer names, email addresses, telephone numbers, business contact information, "
            "employee contact information, customer support information, sales records, and other internal business "
            "information classified Confidential. CloudFlow CRM is not designed to store credit card primary account "
            "numbers, bank account credentials, authentication secrets belonging to the customer’s other systems, or "
            "highly restricted financial records.",
            st["Body"],
        ),
        Paragraph("2. Classification", st["H"]),
        Paragraph(
            "Public, Internal, Confidential, and Restricted. Tenant CRM data is Confidential. Restricted is reserved for "
            "secrets and would be out of product scope.",
            st["Body"],
        ),
        Paragraph("3. Encryption", st["H"]),
        Paragraph(
            "Data in transit uses TLS 1.2 or higher; TLS 1.0 and 1.1 are disabled. Internal service-to-service traffic uses "
            "mTLS. Data at rest is encrypted with AES-256 using AWS KMS. Backup copies are encrypted with KMS. "
            "Customer-managed keys are on the enterprise roadmap and are not currently generally available.",
            st["Body"],
        ),
        Paragraph("4. Tenant isolation", st["H"]),
        Paragraph(
            "The platform is multi-tenant. Isolation is logical: tenant identifiers, row-level constraints, and IAM-scoped "
            "application roles. Object storage uses tenant prefixes. Dedicated tenancy is not included in the standard offering.",
            st["Body"],
        ),
        Paragraph("5. Privacy", st["H"]),
        Paragraph(
            "A Data Protection Officer (Avery Chen, fictional) maintains records of processing. A Data Processing Addendum "
            "is available. Data subject requests received from a customer’s contacts are referred to the customer as controller "
            "unless CloudFlow is legally required to act directly.",
            st["Body"],
        ),
        Paragraph("6. Retention and deletion", st["H"]),
        Paragraph(
            "Upon contract termination, tenant data is deleted or returned within 30 days of written request, with backups "
            "expiring through the backup cycle (operational 30 days; archive 12 months) unless law requires longer retention.",
            st["Body"],
        ),
    ]


def pentest(st, title, doc_id):
    return [
        Paragraph(title, st["Banner"]),
        Paragraph("SIMULATED / FICTIONAL EVIDENCE — FOR EDUCATIONAL USE ONLY", st["Sub"]),
        meta_table(
            [
                ("Document ID", doc_id),
                ("Version", "1.0 (customer summary)"),
                ("Tester (fictional)", "Northbridge Labs"),
                ("Test window", "12–23 October 2025"),
                ("Report date", "04 November 2025"),
                ("Classification", "Confidential — Simulated"),
                ("Scope", "CloudFlow CRM production-equivalent staging and selected external attack surface"),
            ],
            st,
        ),
        Paragraph("1. Notice", st["H"]),
        Paragraph(
            "This is a simulated, redacted customer summary. It is not a real penetration test report and must not be "
            "represented as testing of a live organization.",
            st["Body"],
        ),
        Paragraph("2. Finding counts (fictional)", st["H"]),
        bullets(
            [
                "Critical: 0",
                "High: 2 (both closed 18 November 2025 — overly permissive S3 bucket policy on a non-production artifact store; missing rate limiting on a legacy export API).",
                "Medium: 3 (two closed; one open — verbose error messages on an internal admin endpoint, exception expiry 04 February 2026).",
                "Low / Informational: 7",
            ],
            st,
        ),
        Paragraph("3. Methodology (high level)", st["H"]),
        Paragraph(
            "Authenticated and unauthenticated web application testing, limited API testing, and review of selected cloud "
            "misconfiguration classes. Exploitation of customer tenant data outside the authorized staging tenants was out of scope.",
            st["Body"],
        ),
        Paragraph("4. Tester opinion (simulated)", st["H"]),
        Paragraph(
            "Northbridge Labs (fictional) concluded that the design of core tenant isolation and authentication controls was "
            "appropriate for a multi-tenant SaaS CRM, with the High findings representing configuration and API-hardening "
            "issues rather than a systemic authentication bypass. This summary does not replace a full report under NDA.",
            st["Body"],
        ),
    ]


def soc2(st, title, doc_id):
    return [
        Paragraph(title, st["Banner"]),
        Paragraph("SIMULATED / FICTIONAL EVIDENCE — FOR EDUCATIONAL USE ONLY", st["Sub"]),
        meta_table(
            [
                ("Document ID", doc_id),
                ("Version", "Customer summary 1.0"),
                ("Report type", "SOC 2 Type I (simulated)"),
                ("Trust Services Criteria", "Security and Availability"),
                ("As-of date", "30 September 2025"),
                ("Fictional firm", "Harbor & Pike LLP"),
                ("Opinion (simulated)", "Unqualified as to design of described controls as of the as-of date"),
            ],
            st,
        ),
        Paragraph("1. Important limitation", st["H"]),
        Paragraph(
            "A Type I report describes the suitability of the design of controls at a point in time. It does not provide "
            "the same assurance as a Type II report regarding whether controls operated effectively over a period. CloudFlow "
            "has engaged a Type II examination targeting issuance in calendar year 2026. This summary is fictional and is "
            "not a real SOC report.",
            st["Body"],
        ),
        Paragraph("2. System description (excerpt)", st["H"]),
        Paragraph(
            "The system is CloudFlow CRM hosted on AWS (us-east-1) with encrypted data stores, centralized logging, "
            "identity federation, and a documented incident response process. Complementary user entity controls include "
            "tenant administration, MFA for customer users, and appropriate use of API keys.",
            st["Body"],
        ),
        Paragraph("3. Notable complementary points for TPRM", st["H"]),
        bullets(
            [
                "Physical data-center security is inherited from AWS.",
                "The examination did not include subprocessors beyond AWS as carved-out or included; customer TPRM should still review CloudFlow’s subprocessor process.",
                "No qualified opinion on design was issued in this simulated Type I.",
            ],
            st,
        ),
    ]


def backup(st, title, doc_id):
    return [
        Paragraph(title, st["Banner"]),
        Paragraph("SIMULATED / FICTIONAL EVIDENCE — FOR EDUCATIONAL USE ONLY", st["Sub"]),
        meta_table(
            COMMON_META
            + [
                ("Document ID", doc_id),
                ("Version", "1.3"),
                ("Effective date", "01 July 2025"),
                ("Last restoration test", "12 November 2025"),
            ],
            st,
        ),
        Paragraph("1. Backup cadence", st["H"]),
        Paragraph(
            "Production database snapshots are taken daily. Object-storage versioning is enabled. Snapshots are encrypted "
            "with AWS KMS and replicated to a separate AWS account in us-east-2.",
            st["Body"],
        ),
        Paragraph("2. Retention", st["H"]),
        Paragraph(
            "Operational snapshots: 30 days. Archive copies: 12 months. Access is limited to the backup administrator role, "
            "reviewed quarterly.",
            st["Body"],
        ),
        Paragraph("3. Restoration testing", st["H"]),
        Paragraph(
            "Restoration testing is performed annually. The 12 November 2025 test restored a non-production snapshot to an "
            "isolated account. Recorded recovery timing was 6 hours and 40 minutes, within the 8-hour RTO, but the dataset "
            "was not a full production-scale tenant set. Timing against an RPO cannot be fully evidenced because RPO is not "
            "formally documented. Quarterly restoration testing is not currently performed.",
            st["Body"],
        ),
        Paragraph("4. Recovery limitations", st["H"]),
        bullets(
            [
                "Point-in-time recovery finer than the daily snapshot is not generally offered to customers.",
                "Regional failover is runbook-based and was not fully exercised in 2025.",
                "Customer-managed key restore scenarios are not applicable (CMK not generally available).",
            ],
            st,
        ),
    ]


def subproc(st, title, doc_id):
    return [
        Paragraph(title, st["Banner"]),
        Paragraph("SIMULATED / FICTIONAL EVIDENCE — FOR EDUCATIONAL USE ONLY", st["Sub"]),
        meta_table(
            COMMON_META
            + [
                ("Document ID", doc_id),
                ("Version", "1.1"),
                ("Effective date", "01 August 2025"),
                ("Last inventory review", "20 January 2026"),
            ],
            st,
        ),
        Paragraph("1. Purpose", st["H"]),
        Paragraph(
            "This summary describes how CloudFlow Technologies inventories and reviews subprocessors that support CloudFlow CRM.",
            st["Body"],
        ),
        Paragraph("2. Inventory (illustrative, fictional)", st["H"]),
        bullets(
            [
                "Amazon Web Services — infrastructure hosting, United States regions.",
                "Northmail Delivery (fictional) — transactional email.",
                "PulseAnalytics Cloud (fictional) — product telemetry (no payment data).",
            ],
            st,
        ),
        Paragraph("3. Review practice — disclosed weakness", st["H"]),
        Paragraph(
            "Subprocessors are reviewed, but there is no fully standardized formal risk scoring process. AWS is treated as a "
            "strategic provider with contractual flow-down, SOC reports on request, and architecture review. Smaller utility "
            "providers may be onboarded after Legal review of DPA language and a security questionnaire that is not scored "
            "against a documented residual-risk scale. Re-reviews occur at least annually for named subprocessors, but the "
            "depth of review is not consistent. Customers receive 14 days’ notice of material subprocessor additions where practicable.",
            st["Body"],
        ),
        Paragraph("4. Intended improvement", st["H"]),
        Paragraph(
            "Security intends to introduce a scored subprocessor assessment (likelihood, impact, residual rating, and approval) "
            "for all critical subprocessors. Until that procedure is approved and executed, an assessor should rate formal "
            "subprocessor risk assessment as only partially effective.",
            st["Body"],
        ),
    ]


def main():
    OUT.mkdir(parents=True, exist_ok=True)
    jobs = [
        ("Information_Security_Policy.pdf", "Information Security Policy", "POL-IS-001", isp),
        ("Access_Control_Policy.pdf", "Access Control Policy", "POL-AC-002", acp),
        ("Incident_Response_Plan.pdf", "Incident Response Plan", "IRP-001", irp),
        ("Business_Continuity_Plan.pdf", "Business Continuity Plan", "BCP-001", bcp),
        ("Vulnerability_Management_Policy.pdf", "Vulnerability Management Policy", "POL-VM-005", vmp),
        ("Data_Protection_Standard.pdf", "Data Protection Standard", "STD-DP-004", dps),
        ("Penetration_Test_Summary.pdf", "Penetration Test Summary (Customer Extract)", "PTS-2025-10", pentest),
        ("SOC2_TypeI_Summary.pdf", "SOC 2 Type I Summary (Simulated)", "SOC2-T1-2025-09", soc2),
        ("Backup_and_Recovery_Summary.pdf", "Backup and Recovery Summary", "OPS-BU-003", backup),
        ("Subprocessor_Management_Summary.pdf", "Subprocessor Management Summary", "TPRM-SP-001", subproc),
    ]
    for name, title, doc_id, fn in jobs:
        build(OUT / name, title, doc_id, fn)


if __name__ == "__main__":
    main()
