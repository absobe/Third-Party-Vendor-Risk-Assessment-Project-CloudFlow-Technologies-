"""Generate all Excel workbooks for the fictional CloudFlow assessment."""

from __future__ import annotations

import sys
from pathlib import Path

from openpyxl import Workbook
from openpyxl.chart import BarChart, Reference
from openpyxl.styles import Alignment, Border, Font, PatternFill, Side
from openpyxl.utils import get_column_letter

sys.path.insert(0, str(Path(__file__).resolve().parent))
from project_data import (  # noqa: E402
    ASSESSMENT,
    DISCLAIMER,
    OVERALL_SCORE,
    REMEDIATION,
    RISKS,
    SCORECARD_DOMAINS,
    ROOT,
    rating,
)

NAVY = "1B365D"
GOLD = "C4A35A"
RED = "8B1E3F"
GREEN = "2E5A3C"
WHITE = "FFFFFF"
LIGHT = "F4F1EA"
GRAY = "E8EEF2"

thin = Border(
    left=Side(style="thin", color="B0B7C3"),
    right=Side(style="thin", color="B0B7C3"),
    top=Side(style="thin", color="B0B7C3"),
    bottom=Side(style="thin", color="B0B7C3"),
)
header_font = Font(name="Calibri", bold=True, color=WHITE, size=11)
title_font = Font(name="Calibri", bold=True, color=NAVY, size=16)
body_font = Font(name="Calibri", size=10)
wrap = Alignment(wrap_text=True, vertical="center")
header_fill = PatternFill("solid", fgColor=NAVY)
gold_fill = PatternFill("solid", fgColor=GOLD)
light_fill = PatternFill("solid", fgColor=LIGHT)
alt_fill = PatternFill("solid", fgColor="F7F8FA")
green_fill = PatternFill("solid", fgColor="C8E6C9")
yellow_fill = PatternFill("solid", fgColor="FFF3B0")
orange_fill = PatternFill("solid", fgColor="FFCC80")
red_fill = PatternFill("solid", fgColor="EF9A9A")


def style_header(ws, row, cols):
    for col in range(1, cols + 1):
        cell = ws.cell(row, col)
        cell.font = header_font
        cell.fill = header_fill
        cell.alignment = Alignment(wrap_text=True, vertical="center", horizontal="center")
        cell.border = thin
    ws.row_dimensions[row].height = 32
    ws.auto_filter.ref = f"A{row}:{get_column_letter(cols)}{ws.max_row}"
    ws.freeze_panes = f"A{row + 1}"


def banner(ws, title, subtitle=None, cols=8):
    ws.merge_cells(start_row=1, start_column=1, end_row=1, end_column=cols)
    ws["A1"] = title
    ws["A1"].font = title_font
    ws.merge_cells(start_row=2, start_column=1, end_row=2, end_column=cols)
    ws["A2"] = (
        f"{ASSESSMENT['customer']}  |  Vendor: {ASSESSMENT['vendor']}  |  "
        f"Product: {ASSESSMENT['product']}  |  {ASSESSMENT['assessment_id']}  |  "
        f"Report date: {ASSESSMENT['report_date']}"
    )
    ws["A2"].font = Font(name="Calibri", italic=True, size=10, color="445566")
    ws.merge_cells(start_row=3, start_column=1, end_row=3, end_column=cols)
    ws["A3"] = DISCLAIMER
    ws["A3"].font = Font(name="Calibri", italic=True, size=9, color=RED)
    if subtitle:
        ws.merge_cells(start_row=4, start_column=1, end_row=4, end_column=cols)
        ws["A4"] = subtitle
        ws["A4"].font = Font(name="Calibri", size=10)


def autosize(ws, widths):
    for i, w in enumerate(widths, 1):
        ws.column_dimensions[get_column_letter(i)].width = w


def paint_rows(ws, start, cols):
    for r in range(start, ws.max_row + 1):
        for c in range(1, cols + 1):
            cell = ws.cell(r, c)
            cell.font = body_font
            cell.alignment = wrap
            cell.border = thin
            if r % 2 == 0:
                if cell.fill.fgColor is None or cell.fill.fgColor.rgb in ("00000000", "000000"):
                    cell.fill = alt_fill


# ---------------------------------------------------------------------------
# Questionnaire (55 questions)
# ---------------------------------------------------------------------------
QUESTIONS = [
    ("Q-A-001", "A. Governance", "ISMS / accountability", "Does CloudFlow maintain a documented information security program with a named executive owner?", "Yes. Jordan Hale (CISO) owns the ISMS. The Information Security Policy (POL-IS-001 v3.2) is approved by the executive committee.", "Information Security Policy", "Received — POL-IS-001", "Complete", "Named CISO and policy exist. No ISO 27001 certification.", "Moderate — governance present without accredited ISMS certification"),
    ("Q-A-002", "A. Governance", "Roles and responsibilities", "Are information security roles and responsibilities formally assigned (CISO, security operations, engineering, legal)?", "Yes. RACI is included in POL-IS-001. Security operations reports to the Director of Security.", "Information Security Policy", "Received", "Complete", "RACI is documented at policy level.", "Low"),
    ("Q-A-003", "A. Governance", "Policy review", "How frequently are security policies reviewed and what evidence of the last review is available?", "Policies are reviewed annually. Last review 15 January 2026. Some supporting standards show incomplete review sign-off packets.", "Information Security Policy; review log excerpt", "Partial — policy dated, complete sign-off packet not provided for all standards", "Gap", "Annual cycle exists; evidence completeness is uneven. Contributes to residual governance risk.", "Moderate"),
    ("Q-B-004", "B. Security Policies", "Policy suite", "Does the vendor maintain approved policies covering access control, data protection, incident response, vulnerability management, and acceptable use?", "Yes. Core policies exist and are listed in POL-IS-001 Appendix A.", "Policy suite", "Received for sampled policies", "Complete", "Suite exists; depth varies.", "Low"),
    ("Q-B-005", "B. Security Policies", "Exception management", "Is there a documented security exception / risk-acceptance process with time-bound approvals?", "Yes, CISO-approved exceptions with 12-month maximum duration. Register not provided in full.", "Exception procedure excerpt", "Partial", "Gap", "Process claimed; full exception register not in evidence pack.", "Moderate"),
    ("Q-C-006", "C. Identity and Access Management", "RBAC", "Is access to CloudFlow CRM and supporting systems granted using role-based access control?", "Yes. RBAC is used for the product and AWS IAM permission sets.", "Access Control Policy", "Received — POL-AC-002", "Complete", "RBAC design is documented.", "Low"),
    ("Q-C-007", "C. Identity and Access Management", "Joiner-mover-leaver", "Is there a documented joiner/mover/leaver process with access revocation SLAs?", "Yes. Leavers revoked within 24 hours of HR notification. Movers reviewed within 5 business days.", "Access Control Policy", "Received", "Complete", "JML process is defined.", "Low"),
    ("Q-C-008", "C. Identity and Access Management", "MFA — privileged", "Is multi-factor authentication required for all privileged users, including cloud consoles?", "Yes for AWS, production CRM admin, and corporate SSO. Hardware and TOTP MFA are used.", "Access Control Policy", "Received", "Complete", "Privileged MFA is a strength.", "Low"),
    ("Q-C-009", "C. Identity and Access Management", "MFA coverage gaps", "Are there any systems in the production or administrative support path that do not support MFA?", "Yes. A small set of legacy internal administrative utilities do not support MFA and rely on password plus VPN.", "Access Control Policy §6.4", "Received — gap disclosed", "Finding", "Maps to VR-008. Production CRM UI and AWS privileged access do require MFA.", "High"),
    ("Q-C-010", "C. Identity and Access Management", "Access reviews", "Are user and privileged access reviews performed at least quarterly?", "Yes. Quarterly privileged reviews; semi-annual standard user reviews.", "Access Control Policy; sample review minutes Feb 2026", "Received sample", "Complete", "Reviews exist.", "Low"),
    ("Q-C-011", "C. Identity and Access Management", "Privileged access", "Is privileged access provisioned via just-in-time or jump-host controls rather than standing admin on laptops?", "AWS privileged access uses a jump host and time-bound IAM roles. Legacy tools still allow standing VPN accounts.", "Access Control Policy", "Received", "Partial", "Partial effectiveness due to legacy standing access.", "Moderate"),
    ("Q-D-012", "D. Data Protection", "Data classification", "Does CloudFlow classify customer data and apply handling rules for Confidential information?", "Yes. Nexus CRM data would be classified Confidential. Handling rules in STD-DP-004.", "Data Protection Standard", "Received", "Complete", "Classification model is adequate for this use case.", "Low"),
    ("Q-D-013", "D. Data Protection", "Data minimization", "Does the CRM collect only data required to provide the service, and will payment card or bank credentials be processed?", "CloudFlow CRM will not process payment cards, bank credentials, authentication secrets, or highly restricted financial records for Nexus.", "Data Protection Standard; architecture brief", "Received", "Complete", "Scope exclusion is explicit and material to inherent risk.", "Low"),
    ("Q-D-014", "D. Data Protection", "Tenant isolation", "How is tenant isolation enforced in the multi-tenant SaaS architecture?", "Logical isolation via tenant_id, row-level security, and IAM-scoped application roles. Shared RDS and S3 with tenant prefixes.", "Vendor Architecture; Data Protection Standard", "Received (narrative)", "Complete", "Logical isolation is standard; no dedicated-tenancy option quoted.", "Moderate"),
    ("Q-E-015", "E. Encryption", "In transit", "Is TLS 1.2+ enforced for all external connections, and are weak ciphers disabled?", "Yes. TLS 1.2+ only; TLS 1.0/1.1 disabled. Internal service mesh uses mTLS.", "Data Protection Standard", "Received", "Complete", "Encryption in transit is a strength.", "Low"),
    ("Q-E-016", "E. Encryption", "At rest", "Is customer data encrypted at rest, and who manages encryption keys?", "Yes. AES-256 via AWS KMS. CloudFlow manages keys; customer-managed keys are on the enterprise roadmap, not currently offered.", "Data Protection Standard", "Received", "Complete", "KMS-managed keys acceptable for Confidential CRM data with contractual restrictions.", "Low"),
    ("Q-F-017", "F. Vulnerability Management", "Scanning cadence", "How frequently are vulnerability scans performed, and are they authenticated?", "Monthly authenticated scanning of production and staging. Weekly unauthenticated external scans.", "Vulnerability Management Policy", "Received — POL-VM-005", "Complete", "Cadence is a strength.", "Low"),
    ("Q-F-018", "F. Vulnerability Management", "Remediation SLAs", "What are the remediation timeframes for Critical and High vulnerabilities?", "Critical: 7 days. High: 30 days. Medium: 90 days. Exceptions require CISO approval.", "Vulnerability Management Policy", "Received", "Finding", "30-day High window maps to VR-007.", "High"),
    ("Q-F-019", "F. Vulnerability Management", "Exception tracking", "Are overdue vulnerabilities tracked in a register with compensating controls?", "Yes. Overdue items require documented compensating controls. Last quarter: 3 High exceptions, all internet-internal.", "Vulnerability Management Policy", "Partial metrics", "Partial", "Process exists; limited metrics in pack.", "Moderate"),
    ("Q-G-020", "G. Penetration Testing", "Annual testing", "Is an independent penetration test performed at least annually against the SaaS production environment?", "Yes. Last test 12–23 October 2025 by Northbridge Labs (fictional). Report summary provided.", "Penetration Test Summary", "Received — redacted summary", "Complete", "Annual PT is a strength. Two High findings were remediated; one Medium open with exception.", "Moderate"),
    ("Q-G-021", "G. Penetration Testing", "Remediation of PT findings", "Were all High or Critical penetration-test findings closed, and is evidence available?", "Two High findings closed in November 2025. No Critical. One Medium (verbose error handling) open with 90-day exception.", "Penetration Test Summary", "Received", "Partial", "High items closed; Medium residual accepted by vendor CISO.", "Moderate"),
    ("Q-H-022", "H. Secure Development", "SDLC", "Is there a documented secure SDLC including threat modeling, code review, and security testing before release?", "Yes. Pull-request review required. SAST on all builds. DAST on staging before major releases.", "Information Security Policy §8; SDLC excerpt", "Partial — excerpt only", "Partial", "SDLC exists; full procedure not in pack.", "Moderate"),
    ("Q-H-023", "H. Secure Development", "Dependency management", "Are open-source and third-party libraries scanned for known vulnerabilities?", "Yes. Dependabot-equivalent plus weekly SCA. High library CVEs follow the 30-day High SLA.", "Vulnerability Management Policy", "Received (policy-level)", "Complete", "Linked to VR-007 SLA.", "Moderate"),
    ("Q-I-024", "I. Logging and Monitoring", "Central logging", "Are security-relevant logs centralized, retained, and monitored?", "Yes. Central SIEM. 12-month hot retention for auth and admin logs; 18-month cold. 24x7 alerting for privileged anomalies.", "Information Security Policy; IR plan", "Received (narrative)", "Complete", "Logging is a strength.", "Low"),
    ("Q-I-025", "I. Logging and Monitoring", "Customer audit logs", "Can Nexus obtain audit logs of access to its tenant data?", "Yes. Tenant admin audit log retained 12 months and exportable.", "Data Protection Standard", "Received", "Complete", "Supports Nexus investigation needs.", "Low"),
    ("Q-J-026", "J. Incident Response", "IR plan", "Does CloudFlow maintain a tested incident response plan covering detection, containment, eradication, recovery, and lessons learned?", "Yes. IRP-001 v2.4, last tabletop 2025-08-19.", "Incident Response Plan", "Received", "Complete", "Plan exists and is tested annually.", "Low"),
    ("Q-J-027", "J. Incident Response", "Severity model", "Are incidents classified by severity with defined internal escalation clocks?", "Yes. Sev1 internal executive escalation within 24 hours of confirmation.", "Incident Response Plan", "Received", "Complete", "Internal clocks exist; customer clock is weak.", "Moderate"),
    ("Q-J-028", "J. Incident Response", "Customer notification", "What is the contractual or documented timeframe to notify affected customers of a material cybersecurity incident?", "Notice is 'without undue delay' and as required by applicable law. No hour-based customer SLA is documented.", "Incident Response Plan §7", "Received — gap disclosed", "Finding", "Maps to VR-004. Primary High finding.", "High"),
    ("Q-J-029", "J. Incident Response", "Notification content", "Does the IR plan define the minimum content of customer incident notices (what, when, data types, mitigation)?", "Partially. Legal/comms templates exist internally but are not in the customer-facing plan excerpt.", "Incident Response Plan", "Partial", "Gap", "Templates claimed; not evidenced to Nexus.", "Moderate"),
    ("Q-K-030", "K. Business Continuity", "BCP", "Does CloudFlow maintain a business continuity plan covering CloudFlow CRM as a critical service?", "Yes. BCP-001 v1.9 identifies CRM as a Tier-1 service.", "Business Continuity Plan", "Received", "Complete", "BCP exists.", "Low"),
    ("Q-K-031", "K. Business Continuity", "RTO", "Is a Recovery Time Objective defined and approved for CloudFlow CRM?", "Yes. RTO of 8 hours for the production CRM application tier is stated in the BCP.", "Business Continuity Plan", "Received", "Complete", "RTO stated; evidence of meeting RTO is limited (annual restore only).", "Moderate"),
    ("Q-K-032", "K. Business Continuity", "Exercises", "How often is the BCP exercised?", "Annual tabletop plus annual technical restore. No full failover exercise in the last 12 months.", "Business Continuity Plan", "Received", "Partial", "Exercise cadence is thin for a Tier-1 SaaS.", "High"),
    ("Q-L-033", "L. Disaster Recovery", "RPO", "Is a Recovery Point Objective formally documented and approved for CloudFlow CRM?", "No formal RPO is documented. Daily backups imply a de facto RPO of approximately 24 hours.", "Business Continuity Plan; Backup and Recovery Summary", "Received — gap disclosed", "Finding", "Maps to VR-003.", "High"),
    ("Q-L-034", "L. Disaster Recovery", "DR site / multi-AZ", "Is the production environment deployed across multiple availability zones with a defined DR strategy?", "Yes. Multi-AZ in AWS us-east-1. DR runbook exists for regional impairment; last regional failover test was not performed in 2025.", "Vendor Architecture; BCP", "Received", "Partial", "Architecture is resilient; DR testing incomplete.", "Moderate"),
    ("Q-M-035", "M. Backup Management", "Backup cadence", "Are backups of customer data performed at least daily, encrypted, and stored off the primary account or region?", "Yes. Daily encrypted snapshots. Copies replicated to a separate AWS account in us-east-2. Retention 30 days operational, 12 months archive.", "Backup and Recovery Summary", "Received", "Complete", "Backup design is a strength.", "Low"),
    ("Q-M-036", "M. Backup Management", "Encryption of backups", "Are backups encrypted in transit and at rest with access restricted to named backup administrators?", "Yes. KMS-encrypted. Access limited to the backup administrator role, reviewed quarterly.", "Backup and Recovery Summary", "Received", "Complete", "Access control on backups is adequate.", "Low"),
    ("Q-M-037", "M. Backup Management", "Restoration testing", "How frequently are backup restorations tested, and is recovery timing recorded?", "Annually. Last restoration test 12 November 2025 on a non-production snapshot. Timing recorded as 6 hours 40 minutes.", "Backup and Recovery Summary", "Received — gap disclosed", "Finding", "Maps to VR-002. Annual only is insufficient for Confidential CRM.", "High"),
    ("Q-N-038", "N. Privacy", "Privacy program", "Does CloudFlow maintain a privacy program, DPA capability, and records of processing for customer personal data?", "Yes. DPA template available. Records of processing maintained by the DPO (Avery Chen).", "Data Protection Standard", "Received", "Complete", "Privacy posture adequate for contact/CRM data.", "Low"),
    ("Q-N-039", "N. Privacy", "Subprocessor privacy", "Are subprocessors that process personal data disclosed to customers, with a change-notification mechanism?", "Yes, a public subprocessor list is maintained. Customers are notified of material additions with 14 days' notice where practicable.", "Subprocessor Management Summary", "Received", "Partial", "Disclosure exists; security scoring of those parties is weak (VR-001).", "Moderate"),
    ("Q-O-040", "O. Compliance", "Regulatory mapping", "Has CloudFlow mapped controls to SOC 2 TSC and ISO/IEC 27001 concepts?", "Yes, internal mapping workbook. Used as methodological alignment, not certification.", "SOC2 Type I Summary; Information Security Policy", "Received (summary)", "Complete", "Mapping is useful; not a certification.", "Low"),
    ("Q-O-041", "O. Compliance", "SOC 2", "What is the most recent SOC 2 report type, period, and opinion?", "SOC 2 Type I, Security and Availability, as of 30 September 2025. Unqualified design opinion. Type II in progress for 2026.", "SOC2 Type I Summary", "Received", "Finding", "Maps to VR-005.", "Moderate"),
    ("Q-O-042", "O. Compliance", "ISO 27001", "Does CloudFlow hold ISO/IEC 27001 certification?", "No. Certification is on a 2027 roadmap. Internal ISMS is operated without accredited certification.", "Information Security Policy; questionnaire", "Received — gap disclosed", "Finding", "Maps to VR-006. Accepted with conditions.", "Moderate"),
    ("Q-P-043", "P. Physical Security", "Data center physical", "Are production systems hosted in physically secured facilities with independent assurance?", "Yes. AWS data centers. Physical security inherited from AWS. CloudFlow offices are badge-controlled; no production servers on premises.", "Vendor Architecture; SOC2 Type I Summary", "Received", "Complete / inherited", "Physical risk is largely inherited and acceptable.", "Low"),
    ("Q-Q-044", "Q. Human Resources Security", "Screening", "Are employees and contractors subject to background screening appropriate to their access?", "Yes for employees in the United States and United Kingdom. Screening depth varies by jurisdiction.", "Information Security Policy §5", "Received (policy)", "Partial", "Policy-level only; no sample screening evidence.", "Moderate"),
    ("Q-Q-045", "Q. Human Resources Security", "Awareness training", "Is security awareness training required, and is it annual or continuous?", "Annual mandatory training plus phishing simulation twice per year. Not a continuous micro-learning program.", "Information Security Policy", "Received", "Partial", "Annual training is a weakness relative to continuous programs, but not a High finding on its own.", "Moderate"),
    ("Q-Q-046", "Q. Human Resources Security", "Acceptable use / sanctions", "Are acceptable use and disciplinary processes documented for security violations?", "Yes, in the employee handbook and POL-IS-001.", "Information Security Policy", "Received", "Complete", "Standard HR security control.", "Low"),
    ("Q-R-047", "R. Cloud Security", "AWS security baseline", "Is a documented cloud security baseline applied (security groups, least privilege IAM, GuardDuty/equivalent, encryption, logging)?", "Yes. CIS Benchmark-inspired AWS baseline. GuardDuty, CloudTrail org trail, Security Hub enabled.", "Vendor Architecture; Information Security Policy", "Received (narrative)", "Complete", "Cloud security is a strength.", "Low"),
    ("Q-R-048", "R. Cloud Security", "Shared responsibility", "Is the AWS shared responsibility model documented and operationalized for CloudFlow CRM?", "Yes. CloudFlow is responsible for the application, IAM, tenant isolation, and customer data. AWS for infrastructure physical and hypervisor.", "Vendor Architecture", "Received", "Complete", "Model is understood.", "Low"),
    ("Q-S-049", "S. Third-Party / Subprocessor Management", "Inventory", "Does CloudFlow maintain a current inventory of subprocessors with data types and locations?", "Yes. Inventory includes AWS, email delivery, and analytics utilities. Reviewed annually.", "Subprocessor Management Summary", "Received", "Complete", "Inventory exists.", "Low"),
    ("Q-S-050", "S. Third-Party / Subprocessor Management", "Formal risk scoring", "Does CloudFlow apply a documented, scored security risk assessment to subprocessors before onboarding and on a defined cadence?", "Subprocessors are reviewed, but there is no fully standardized formal risk scoring process. Reviews are informal for several utility providers.", "Subprocessor Management Summary", "Received — gap disclosed", "Finding", "Maps to VR-001. Highest-priority TPRM finding.", "High"),
    ("Q-S-051", "S. Third-Party / Subprocessor Management", "Flow-down", "Are security, privacy, and incident-notice obligations flowed down contractually to subprocessors?", "Yes for AWS and two primary SaaS utilities. Not uniformly evidenced for all utility subprocessors.", "Subprocessor Management Summary", "Partial", "Partial", "Uneven flow-down.", "High"),
    ("Q-T-052", "T. Risk Management", "ERM / IS risk", "Does CloudFlow operate an information security risk management process with a risk register?", "Yes. Internal risk register reviewed quarterly by the security steering committee.", "Information Security Policy", "Partial — register not shared", "Partial", "Process claimed; contents not independently reviewed.", "Moderate"),
    ("Q-T-053", "T. Risk Management", "Customer risk communication", "Does CloudFlow notify customers of material residual risks or significant control changes?", "Material product security changes are in release notes. No structured customer residual-risk briefing process.", "Questionnaire response", "Narrative only", "Partial", "Would benefit Nexus continuous monitoring.", "Moderate"),
    ("Q-T-054", "T. Risk Management", "Insurance", "Does CloudFlow maintain cyber liability insurance appropriate to a SaaS CRM provider?", "Yes. USD 5 million cyber liability policy (fictional), certificate available on request under NDA.", "Questionnaire response", "Not provided in pack (available under NDA)", "Evidence not provided", "Insurance claimed; treat as unverified until certificate received.", "Moderate"),
    ("Q-I-055", "I. Logging and Monitoring", "Time sync / integrity", "Are system clocks synchronized and are logs protected against unauthorized alteration?", "Yes. NTP via AWS. SIEM write-once storage for 90 days; WORM archive thereafter.", "Information Security Policy", "Narrative", "Complete", "Supports forensic integrity.", "Low"),
]


CONTROLS = [
    ("CTRL-GOV-001", "Documented ISMS with named CISO", "Governance", "Information_Security_Policy.pdf", "Q-A-001", "Effective", "Named CISO and policy. Not ISO certified.", "VR-006"),
    ("CTRL-GOV-002", "Annual policy review with complete evidence", "Governance", "Information_Security_Policy.pdf", "Q-A-003", "Partially Effective", "Review date present; sign-off packets incomplete for some standards.", ""),
    ("CTRL-AC-001", "MFA for privileged users (AWS and CRM admin)", "Access Control", "Access_Control_Policy.pdf", "Q-C-008", "Effective", "Privileged MFA enforced on production and AWS.", "VR-008"),
    ("CTRL-AC-002", "RBAC and joiner-mover-leaver", "Access Control", "Access_Control_Policy.pdf", "Q-C-006, Q-C-007", "Effective", "RBAC and 24-hour leaver revocation.", ""),
    ("CTRL-AC-003", "Periodic access reviews", "Access Control", "Access_Control_Policy.pdf", "Q-C-010", "Effective", "Quarterly privileged reviews evidenced by sample.", ""),
    ("CTRL-AC-004", "MFA on all administrative paths including legacy tools", "Access Control", "Access_Control_Policy.pdf", "Q-C-009", "Partially Effective", "Legacy utilities without MFA. Maps to VR-008.", "VR-008"),
    ("CTRL-DP-001", "Data classification and Confidential handling", "Data Protection", "Data_Protection_Standard.pdf", "Q-D-012", "Effective", "Classification model covers Nexus CRM data.", ""),
    ("CTRL-DP-002", "Encryption in transit TLS 1.2+", "Encryption", "Data_Protection_Standard.pdf", "Q-E-015", "Effective", "TLS 1.2+ enforced.", ""),
    ("CTRL-DP-003", "Encryption at rest AES-256 / KMS", "Encryption", "Data_Protection_Standard.pdf", "Q-E-016", "Effective", "AWS KMS AES-256.", ""),
    ("CTRL-DP-004", "Tenant isolation in multi-tenant SaaS", "Data Protection", "Vendor_Architecture.md; Data_Protection_Standard.pdf", "Q-D-014", "Effective", "Logical isolation documented. No dedicated tenancy.", ""),
    ("CTRL-VM-001", "Monthly authenticated vulnerability scanning", "Vulnerability Management", "Vulnerability_Management_Policy.pdf", "Q-F-017", "Effective", "Monthly authenticated + weekly external.", ""),
    ("CTRL-VM-002", "Risk-based vulnerability remediation SLAs", "Vulnerability Management", "Vulnerability_Management_Policy.pdf", "Q-F-018", "Partially Effective", "30-day High window. Maps to VR-007.", "VR-007"),
    ("CTRL-VM-003", "Annual independent penetration testing", "Vulnerability Management", "Penetration_Test_Summary.pdf", "Q-G-020", "Effective", "Oct 2025 test; High findings closed.", "VR-007"),
    ("CTRL-IR-001", "Documented and tabletop-tested IR plan", "Incident Response", "Incident_Response_Plan.pdf", "Q-J-026", "Effective", "IRP v2.4; tabletop Aug 2025.", ""),
    ("CTRL-IR-002", "Customer material-incident notification SLA", "Incident Response", "Incident_Response_Plan.pdf", "Q-J-028", "Partially Effective", "'Without undue delay' only. Maps to VR-004.", "VR-004"),
    ("CTRL-IR-003", "Incident severity classification and internal escalation", "Incident Response", "Incident_Response_Plan.pdf", "Q-J-027", "Effective", "Sev1 internal 24-hour executive escalation.", ""),
    ("CTRL-IR-004", "Customer notification content standards", "Incident Response", "Incident_Response_Plan.pdf", "Q-J-029", "Partially Effective", "Templates claimed, not fully evidenced.", "VR-004"),
    ("CTRL-BC-001", "Documented RTO for CloudFlow CRM", "Business Continuity", "Business_Continuity_Plan.pdf", "Q-K-031", "Effective", "RTO 8 hours stated.", "VR-003"),
    ("CTRL-BC-002", "Documented RPO for CloudFlow CRM", "Business Continuity", "Business_Continuity_Plan.pdf", "Q-L-033", "Ineffective", "No formal RPO. Maps to VR-003.", "VR-003"),
    ("CTRL-BC-003", "BCP / DR exercises at a frequency matching criticality", "Business Continuity", "Business_Continuity_Plan.pdf", "Q-K-032", "Partially Effective", "Annual tabletop only; no 2025 regional failover test.", "VR-002"),
    ("CTRL-DR-001", "Formally approved recovery objectives (RTO and RPO)", "Disaster Recovery", "Business_Continuity_Plan.pdf", "Q-L-033", "Partially Effective", "RTO yes, RPO no.", "VR-003"),
    ("CTRL-BU-001", "Daily encrypted backups with off-account replication", "Backup Management", "Backup_and_Recovery_Summary.pdf", "Q-M-035", "Effective", "Daily KMS-encrypted backups to us-east-2.", ""),
    ("CTRL-BU-002", "Restoration testing sufficient to evidence recoverability", "Backup Management", "Backup_and_Recovery_Summary.pdf", "Q-M-037", "Partially Effective", "Annual restore only. Maps to VR-002.", "VR-002"),
    ("CTRL-CM-001", "Independent SOC 2 assurance", "Compliance", "SOC2_TypeI_Summary.pdf", "Q-O-041", "Partially Effective", "Type I only. Maps to VR-005.", "VR-005"),
    ("CTRL-CM-002", "Operating-effectiveness evidence over a period (Type II)", "Compliance", "SOC2_TypeI_Summary.pdf", "Q-O-041", "Evidence Not Provided", "Type II not yet available.", "VR-005"),
    ("CTRL-CM-003", "ISO/IEC 27001 certification", "Compliance", "Information_Security_Policy.pdf", "Q-O-042", "Ineffective", "No certification. ISMS still operated. Maps to VR-006.", "VR-006"),
    ("CTRL-CLD-001", "AWS security baseline (logging, detection, IAM, encryption)", "Cloud Security", "Vendor_Architecture.md", "Q-R-047", "Effective", "GuardDuty, CloudTrail, Security Hub, KMS.", ""),
    ("CTRL-HR-001", "Security awareness training", "HR Security", "Information_Security_Policy.pdf", "Q-Q-045", "Partially Effective", "Annual plus two phishing simulations; not continuous.", ""),
    ("CTRL-TPRM-001", "Subprocessor inventory and customer disclosure", "Third-Party Management", "Subprocessor_Management_Summary.pdf", "Q-S-049", "Effective", "Inventory and 14-day material-change notice.", "VR-001"),
    ("CTRL-TPRM-004", "Formal scored subprocessor risk assessment", "Third-Party Management", "Subprocessor_Management_Summary.pdf", "Q-S-050", "Partially Effective", "Reviews occur; scoring not standardized. Maps to VR-001.", "VR-001"),
    ("CTRL-TPRM-005", "Contractual security flow-down to all subprocessors", "Third-Party Management", "Subprocessor_Management_Summary.pdf", "Q-S-051", "Partially Effective", "Not uniform across utility providers.", "VR-001"),
]


def save(wb, rel):
    path = ROOT / rel
    path.parent.mkdir(parents=True, exist_ok=True)
    wb.save(path)
    print(f"Wrote {path.relative_to(ROOT)}")


def build_questionnaire():
    wb = Workbook()
    ws = wb.active
    ws.title = "Questionnaire"
    banner(ws, "Vendor Security Questionnaire — CloudFlow CRM", "Initial due-diligence questionnaire with fictional vendor responses.", 12)
    headers = [
        "Question ID", "Domain", "Control Area", "Question", "Vendor Response",
        "Evidence Requested", "Evidence Received", "Assessment Status",
        "Assessor Notes", "Risk Impact", "Linked Risk ID",
    ]
    start = 6
    for i, h in enumerate(headers, 1):
        ws.cell(start, i, h)
    risk_by_q = {}
    for r in RISKS:
        for qid in r["questionnaire_ids"].replace(" ", "").split(","):
            risk_by_q.setdefault(qid, []).append(r["id"])
    for i, q in enumerate(QUESTIONS):
        row = start + 1 + i
        for c, val in enumerate(q, 1):
            ws.cell(row, c, val)
        qid = q[0]
        ws.cell(row, 11, ", ".join(risk_by_q.get(qid, [])) or "—")
    style_header(ws, start, 11)
    paint_rows(ws, start + 1, 11)
    autosize(ws, [12, 28, 28, 55, 55, 32, 40, 16, 45, 22, 16])
    ws.row_dimensions[1].height = 22
    legend = wb.create_sheet("Cover")
    banner(legend, "Questionnaire Cover", cols=6)
    legend["A6"] = "Purpose"
    legend["A7"] = (
        "This workbook records the security questionnaire issued by Nexus Financial Services "
        "to CloudFlow Technologies, fictional vendor responses, evidence status, and assessor notes."
    )
    legend["A9"] = "Question count"
    legend["B9"] = len(QUESTIONS)
    legend["A10"] = "Domains"
    legend["B10"] = "A–T as specified in the project methodology"
    legend["A12"] = DISCLAIMER
    legend["A12"].font = Font(italic=True, color=RED)
    autosize(legend, [28, 80, 20, 20, 20, 20])
    # Domain summary
    sm = wb.create_sheet("Domain_Status")
    banner(sm, "Questionnaire status by domain", cols=5)
    sm["A6"] = "Domain"
    sm["B6"] = "Questions"
    sm["C6"] = "Findings / Gaps"
    sm["D6"] = "Complete"
    style_header(sm, 6, 4)
    from collections import Counter
    counts = Counter(q[1] for q in QUESTIONS)
    gaps = Counter(q[1] for q in QUESTIONS if q[7] in ("Finding", "Gap", "Partial"))
    complete = Counter(q[1] for q in QUESTIONS if q[7] == "Complete")
    r = 7
    for domain, n in counts.items():
        sm.cell(r, 1, domain)
        sm.cell(r, 2, n)
        sm.cell(r, 3, gaps.get(domain, 0))
        sm.cell(r, 4, complete.get(domain, 0))
        r += 1
    paint_rows(sm, 7, 4)
    autosize(sm, [40, 16, 18, 14, 14])
    save(wb, "02_Security_Questionnaire/Vendor_Security_Questionnaire.xlsx")


def build_response_summary():
    wb = Workbook()
    ws = wb.active
    ws.title = "Response_Summary"
    banner(ws, "Vendor Response Summary", cols=8)
    headers = ["Question ID", "Domain", "Assessment Status", "Risk Impact", "Strength or Weakness", "Linked Finding"]
    start = 6
    for i, h in enumerate(headers, 1):
        ws.cell(start, i, h)
    weakness_ids = {"Q-A-003", "Q-C-009", "Q-F-018", "Q-J-028", "Q-J-029", "Q-K-032", "Q-L-033", "Q-M-037", "Q-O-041", "Q-O-042", "Q-Q-045", "Q-S-050", "Q-S-051"}
    risk_by_q = {}
    for r in RISKS:
        for qid in r["questionnaire_ids"].replace(" ", "").split(","):
            risk_by_q.setdefault(qid, []).append(r["id"])
    for i, q in enumerate(QUESTIONS):
        row = start + 1 + i
        ws.cell(row, 1, q[0])
        ws.cell(row, 2, q[1])
        ws.cell(row, 3, q[7])
        ws.cell(row, 4, q[9])
        ws.cell(row, 5, "Weakness" if q[0] in weakness_ids or q[7] == "Finding" else "Strength or adequate")
        ws.cell(row, 6, ", ".join(risk_by_q.get(q[0], [])) or "—")
        if q[7] == "Finding":
            ws.cell(row, 3).fill = red_fill
        elif q[7] in ("Gap", "Partial"):
            ws.cell(row, 3).fill = yellow_fill
        elif q[7] == "Complete":
            ws.cell(row, 3).fill = green_fill
    style_header(ws, start, 6)
    paint_rows(ws, start + 1, 6)
    autosize(ws, [14, 36, 22, 18, 28, 18])
    k = wb.create_sheet("Key_Takeaways")
    banner(k, "Key takeaways from vendor responses", cols=4)
    k["A6"] = "Strengths"
    k["A7"] = "MFA for privileged AWS/CRM access; TLS 1.2+; AES-256 at rest; monthly authenticated scanning; annual penetration test; daily encrypted backups; formal IR plan; SIEM logging; security awareness training; named CISO."
    k["A9"] = "Weaknesses"
    k["A10"] = (
        "No ISO 27001; SOC 2 Type I only; informal subprocessor scoring; annual-only restore testing; "
        "RPO not formally documented; unclear customer incident notification SLA; incomplete policy review evidence; "
        "annual rather than continuous awareness training; legacy MFA gaps; 30-day High vulnerability window."
    )
    k["A12"] = DISCLAIMER
    autosize(k, [22, 100, 20, 20])
    save(wb, "02_Security_Questionnaire/Vendor_Response_Summary.xlsx")


def build_control_assessment():
    wb = Workbook()
    ws = wb.active
    ws.title = "Control_Assessment"
    banner(ws, "Control Assessment — CloudFlow Technologies", cols=10)
    headers = [
        "Control ID", "Control", "Domain", "Evidence", "Questionnaire IDs",
        "Result", "Assessor Rationale", "Linked Risk ID",
    ]
    start = 6
    for i, h in enumerate(headers, 1):
        ws.cell(start, i, h)
    for i, c in enumerate(CONTROLS):
        row = start + 1 + i
        for col, val in enumerate(c, 1):
            ws.cell(row, col, val)
        result = c[5]
        fills = {
            "Effective": green_fill,
            "Partially Effective": yellow_fill,
            "Ineffective": red_fill,
            "Evidence Not Provided": orange_fill,
            "Not Applicable": PatternFill("solid", fgColor="CFD8DC"),
        }
        ws.cell(row, 6).fill = fills.get(result, alt_fill)
    style_header(ws, start, 8)
    paint_rows(ws, start + 1, 8)
    autosize(ws, [16, 48, 24, 42, 22, 22, 55, 14])
    sm = wb.create_sheet("Result_Counts")
    banner(sm, "Control assessment result counts", cols=4)
    sm["A6"] = "Result"
    sm["B6"] = "Count"
    style_header(sm, 6, 2)
    from collections import Counter
    cc = Counter(c[5] for c in CONTROLS)
    r = 7
    for k, v in cc.items():
        sm.cell(r, 1, k)
        sm.cell(r, 2, v)
        r += 1
    sm.cell(r + 1, 1, "Total controls")
    sm.cell(r + 1, 2, len(CONTROLS))
    paint_rows(sm, 7, 2)
    autosize(sm, [40, 12, 20, 20])
    save(wb, "04_Control_Assessment/Control_Assessment.xlsx")


def build_evidence_mapping():
    wb = Workbook()
    ws = wb.active
    ws.title = "Evidence_Mapping"
    banner(ws, "Evidence-to-Control Mapping", cols=8)
    headers = ["Evidence Artifact", "Control IDs", "Questionnaire IDs", "Related Risks", "Assessment Use"]
    start = 6
    for i, h in enumerate(headers, 1):
        ws.cell(start, i, h)
    artifacts = [
        ("Information_Security_Policy.pdf", "CTRL-GOV-001, CTRL-GOV-002, CTRL-HR-001, CTRL-CM-003", "Q-A-001, Q-A-003, Q-O-042, Q-Q-045", "VR-006", "Governance and ISMS design"),
        ("Access_Control_Policy.pdf", "CTRL-AC-001, CTRL-AC-002, CTRL-AC-003, CTRL-AC-004", "Q-C-006 to Q-C-011", "VR-008", "IAM including MFA gap"),
        ("Incident_Response_Plan.pdf", "CTRL-IR-001, CTRL-IR-002, CTRL-IR-003, CTRL-IR-004", "Q-J-026 to Q-J-029", "VR-004", "IR capability and notification SLA"),
        ("Business_Continuity_Plan.pdf", "CTRL-BC-001, CTRL-BC-002, CTRL-BC-003, CTRL-DR-001", "Q-K-030 to Q-L-034", "VR-002, VR-003", "RTO/RPO and exercises"),
        ("Vulnerability_Management_Policy.pdf", "CTRL-VM-001, CTRL-VM-002", "Q-F-017 to Q-F-019", "VR-007", "Scan cadence and SLAs"),
        ("Data_Protection_Standard.pdf", "CTRL-DP-001 to CTRL-DP-004", "Q-D-012 to Q-E-016", "", "Classification, encryption, isolation"),
        ("Penetration_Test_Summary.pdf", "CTRL-VM-003", "Q-G-020, Q-G-021", "VR-007", "Independent testing"),
        ("SOC2_TypeI_Summary.pdf", "CTRL-CM-001, CTRL-CM-002", "Q-O-041", "VR-005", "Independent assurance scope"),
        ("Backup_and_Recovery_Summary.pdf", "CTRL-BU-001, CTRL-BU-002", "Q-M-035 to Q-M-037", "VR-002, VR-003", "Backup design and restore testing"),
        ("Subprocessor_Management_Summary.pdf", "CTRL-TPRM-001, CTRL-TPRM-004, CTRL-TPRM-005", "Q-S-049 to Q-S-051", "VR-001", "TPRM / supply chain"),
    ]
    for i, a in enumerate(artifacts):
        row = start + 1 + i
        for c, val in enumerate(a, 1):
            ws.cell(row, c, val)
    style_header(ws, start, 5)
    paint_rows(ws, start + 1, 5)
    autosize(ws, [42, 55, 28, 18, 36])
    save(wb, "04_Control_Assessment/Evidence_Mapping.xlsx")


EXCEL_RATING = '=IF(I{r}<=4,"Low",IF(I{r}<=9,"Moderate",IF(I{r}<=16,"High","Critical")))'
EXCEL_RES_RATING = '=IF(M{r}<=4,"Low",IF(M{r}<=9,"Moderate",IF(M{r}<=16,"High","Critical")))'


def build_inherent():
    wb = Workbook()
    ws = wb.active
    ws.title = "Inherent_Risk"
    banner(ws, "Inherent Risk Assessment (before existing controls)", cols=10)
    headers = [
        "Risk ID", "Risk Title", "Description", "Likelihood", "Impact",
        "Inherent Score (L×I)", "Inherent Rating", "Rationale (no credit for controls)",
    ]
    start = 6
    for i, h in enumerate(headers, 1):
        ws.cell(start, i, h)
    for i, rsk in enumerate(RISKS):
        row = start + 1 + i
        ws.cell(row, 1, rsk["id"])
        ws.cell(row, 2, rsk["title"])
        ws.cell(row, 3, rsk["description"])
        ws.cell(row, 4, rsk["likelihood"])
        ws.cell(row, 5, rsk["impact"])
        ws.cell(row, 6, f"=D{row}*E{row}")
        ws.cell(row, 7, EXCEL_RATING.format(r=row).replace("I{r}", f"F{row}"))
        # fix: rating should reference column F
        ws.cell(row, 7, f'=IF(F{row}<=4,"Low",IF(F{row}<=9,"Moderate",IF(F{row}<=16,"High","Critical")))')
        ws.cell(row, 8, "Scored as if compensating/existing controls were absent or failed.")
    style_header(ws, start, 8)
    paint_rows(ws, start + 1, 8)
    autosize(ws, [12, 32, 55, 14, 12, 20, 16, 50])
    save(wb, "05_Risk_Assessment/Inherent_Risk_Assessment.xlsx")


def build_residual():
    wb = Workbook()
    ws = wb.active
    ws.title = "Residual_Risk"
    banner(
        ws,
        "Residual Risk Assessment (after existing controls)",
        "Existing controls do not automatically reduce scores. Likelihood is reduced only where controls demonstrably lower frequency or detectability.",
        12,
    )
    headers = [
        "Risk ID", "Risk Title", "Existing Controls", "Inherent Score",
        "Residual Likelihood", "Residual Impact", "Residual Score (L×I)",
        "Residual Rating", "Why residual did or did not decrease",
    ]
    start = 6
    for i, h in enumerate(headers, 1):
        ws.cell(start, i, h)
    notes = {
        "VR-001": "Inventory and some contracts exist, so likelihood reduced from 4 to 3. Impact remains 4 because a weak subprocessor can still expose Confidential data.",
        "VR-002": "Daily backups exist, so a total inability to recover is less likely (4→3). Impact remains 4 because restore evidence is still annual and RTO confidence is limited.",
        "VR-003": "Daily backup implies ~24h loss, reducing likelihood of unbounded loss (4→3). Impact stays 4 because 24h may still exceed Nexus tolerance and is not approved.",
        "VR-004": "Internal escalation exists, so complete non-notification is less likely (4→3). Impact remains 4 because Nexus regulatory clocks still depend on vendor notice.",
        "VR-005": "Type I plus internal policies reduce likelihood of a wholly undesigned control environment (3→2). Impact remains 3 (assurance gap, not a direct technical failure).",
        "VR-006": "Operated ISMS and SOC 2 Type I reduce likelihood (3→2). Impact remains 3 (missing certification is an assurance issue).",
        "VR-007": "Scanning, PT, and WAF reduce likelihood (4→3). Impact reduced to 3 because the window applies to High, not unpatched Critical, and Critical SLA is 7 days.",
        "VR-008": "MFA on production/AWS and VPN for legacy tools reduce both likelihood and impact (4×4 → 3×3). Residual remains Moderate until legacy MFA is closed.",
    }
    for i, rsk in enumerate(RISKS):
        row = start + 1 + i
        ws.cell(row, 1, rsk["id"])
        ws.cell(row, 2, rsk["title"])
        ws.cell(row, 3, rsk["existing_controls"])
        ws.cell(row, 4, rsk["inherent_risk"])
        ws.cell(row, 5, rsk["residual_likelihood"])
        ws.cell(row, 6, rsk["residual_impact"])
        ws.cell(row, 7, f"=E{row}*F{row}")
        ws.cell(row, 8, f'=IF(G{row}<=4,"Low",IF(G{row}<=9,"Moderate",IF(G{row}<=16,"High","Critical")))')
        ws.cell(row, 9, notes[rsk["id"]])
    style_header(ws, start, 9)
    paint_rows(ws, start + 1, 9)
    autosize(ws, [12, 32, 55, 16, 18, 16, 18, 16, 55])
    save(wb, "05_Risk_Assessment/Residual_Risk_Assessment.xlsx")


def build_risk_register():
    wb = Workbook()
    ws = wb.active
    ws.title = "Risk_Register"
    banner(ws, "Vendor Risk Register — CloudFlow Technologies", cols=20)
    headers = [
        "Risk ID", "Risk Title", "Description", "Business Impact", "Affected Asset",
        "Control Domain", "Likelihood", "Impact", "Inherent Risk", "Existing Controls",
        "Residual Likelihood", "Residual Impact", "Residual Risk", "Risk Rating",
        "Risk Owner", "Treatment", "Due Date", "Status", "Acceptance Required", "Evidence Reference",
    ]
    start = 6
    for i, h in enumerate(headers, 1):
        ws.cell(start, i, h)
    for i, rsk in enumerate(RISKS):
        row = start + 1 + i
        ws.cell(row, 1, rsk["id"])
        ws.cell(row, 2, rsk["title"])
        ws.cell(row, 3, rsk["description"])
        ws.cell(row, 4, rsk["business_impact"])
        ws.cell(row, 5, rsk["affected_asset"])
        ws.cell(row, 6, rsk["control_domain"])
        ws.cell(row, 7, rsk["likelihood"])
        ws.cell(row, 8, rsk["impact"])
        ws.cell(row, 9, f"=G{row}*H{row}")
        ws.cell(row, 10, rsk["existing_controls"])
        ws.cell(row, 11, rsk["residual_likelihood"])
        ws.cell(row, 12, rsk["residual_impact"])
        ws.cell(row, 13, f"=K{row}*L{row}")
        ws.cell(row, 14, f'=IF(M{row}<=4,"Low",IF(M{row}<=9,"Moderate",IF(M{row}<=16,"High","Critical")))')
        ws.cell(row, 15, rsk["owner"])
        ws.cell(row, 16, rsk["treatment"])
        ws.cell(row, 17, rsk["due_date"])
        ws.cell(row, 18, rsk["status"])
        ws.cell(row, 19, rsk["acceptance_required"])
        ws.cell(row, 20, rsk["evidence"])
        fill = {"Mitigate": orange_fill, "Accept": yellow_fill}.get(rsk["treatment"], alt_fill)
        ws.cell(row, 16).fill = fill
    last = start + len(RISKS)
    style_header(ws, start, 20)
    paint_rows(ws, start + 1, 20)
    autosize(ws, [12, 28, 40, 40, 32, 28, 12, 10, 14, 40, 18, 14, 14, 14, 36, 12, 14, 40, 40, 40])

    dash = wb.create_sheet("Dashboard")
    banner(dash, "Risk register dashboard", cols=6)
    dash["A6"] = "Metric"
    dash["B6"] = "Value"
    style_header(dash, 6, 2)
    dash["A7"] = "Count of risks"
    dash["B7"] = f"=COUNTA(Risk_Register!A7:A{last})"
    dash["A8"] = "High residual (rating High)"
    dash["B8"] = f'=COUNTIF(Risk_Register!N7:N{last},"High")'
    dash["A9"] = "Moderate residual"
    dash["B9"] = f'=COUNTIF(Risk_Register!N7:N{last},"Moderate")'
    dash["A10"] = "Low residual"
    dash["B10"] = f'=COUNTIF(Risk_Register!N7:N{last},"Low")'
    dash["A11"] = "Critical residual"
    dash["B11"] = f'=COUNTIF(Risk_Register!N7:N{last},"Critical")'
    dash["A12"] = "Treatments = Mitigate"
    dash["B12"] = f'=COUNTIF(Risk_Register!P7:P{last},"Mitigate")'
    dash["A13"] = "Treatments = Accept"
    dash["B13"] = f'=COUNTIF(Risk_Register!P7:P{last},"Accept")'
    dash["A15"] = "Overall vendor residual risk rating"
    dash["B15"] = ASSESSMENT["overall_risk"]
    dash["A16"] = "Recommendation"
    dash["B16"] = ASSESSMENT["recommendation"]
    dash["A18"] = DISCLAIMER
    dash["A18"].font = Font(italic=True, color=RED)
    paint_rows(dash, 7, 2)
    autosize(dash, [40, 55, 20, 20, 20, 20])

    scale = wb.create_sheet("Scoring_Scale")
    banner(scale, "5x5 scoring scale used by formulas", cols=6)
    scale["A6"] = "Score range"
    scale["B6"] = "Rating"
    scale["A7"] = "1–4"
    scale["B7"] = "Low"
    scale["A8"] = "5–9"
    scale["B8"] = "Moderate"
    scale["A9"] = "10–16"
    scale["B9"] = "High"
    scale["A10"] = "17–25"
    scale["B10"] = "Critical"
    scale["A12"] = "Formula"
    scale["B12"] = "Risk Score = Likelihood × Impact"
    autosize(scale, [18, 40, 20, 20, 20, 20])
    save(wb, "06_Risk_Register/Vendor_Risk_Register.xlsx")


def build_remediation():
    wb = Workbook()
    ws = wb.active
    ws.title = "Remediation_Plan"
    banner(ws, "Corrective Action / Remediation Tracker", cols=12)
    headers = [
        "Finding ID", "Finding", "Required Action", "Recommended Control",
        "Responsible Owner", "Priority", "Due Date", "Success Criteria",
        "Evidence Required", "Status", "CAP ID",
    ]
    start = 6
    for i, h in enumerate(headers, 1):
        ws.cell(start, i, h)
    for i, cap in enumerate(REMEDIATION):
        row = start + 1 + i
        ws.cell(row, 1, cap["finding_id"])
        ws.cell(row, 2, cap["finding"])
        ws.cell(row, 3, cap["action"])
        ws.cell(row, 4, cap["recommended_control"])
        ws.cell(row, 5, cap["owner"])
        ws.cell(row, 6, cap["priority"])
        ws.cell(row, 7, cap["due_date"])
        ws.cell(row, 8, cap["success_criteria"])
        ws.cell(row, 9, cap["evidence_required"])
        ws.cell(row, 10, cap["status"])
        ws.cell(row, 11, cap["id"])
        if cap["priority"] == "High":
            ws.cell(row, 6).fill = red_fill
        elif cap["priority"] == "Moderate":
            ws.cell(row, 6).fill = yellow_fill
        else:
            ws.cell(row, 6).fill = green_fill
    style_header(ws, start, 11)
    paint_rows(ws, start + 1, 11)
    autosize(ws, [12, 32, 50, 40, 40, 12, 14, 50, 40, 32, 12])
    save(wb, "07_Remediation/Remediation_Plan.xlsx")


def build_scorecard():
    wb = Workbook()
    ws = wb.active
    ws.title = "Scorecard"
    banner(ws, "Vendor Risk Scorecard — CloudFlow Technologies", cols=8)
    headers = ["Domain", "Weight", "Domain Score (0–100)", "Weighted Score", "Scoring Notes"]
    start = 6
    for i, h in enumerate(headers, 1):
        ws.cell(start, i, h)
    notes = {
        "Security Governance": "Named CISO and policies; incomplete review evidence; no ISO 27001.",
        "Access Control": "Strong privileged MFA and RBAC; legacy MFA gap prevents a higher score.",
        "Data Protection": "Encryption, classification, and tenant isolation are strengths. Scope excludes card data.",
        "Vulnerability Management": "Good scanning and PT; 30-day High SLA reduces the score.",
        "Incident Response": "Mature IR plan; customer notification SLA is unclear.",
        "Business Continuity": "Daily backups and stated RTO; RPO missing; restore tests annual only.",
        "Compliance": "SOC 2 Type I (not Type II); no ISO 27001; mapping exists.",
        "Cloud Security": "AWS baseline, logging, detection, and encryption are strong.",
        "Third-Party Management": "Inventory exists; formal scored assessments are missing.",
    }
    first = start + 1
    for i, d in enumerate(SCORECARD_DOMAINS):
        row = start + 1 + i
        ws.cell(row, 1, d["domain"])
        ws.cell(row, 2, d["weight"])
        ws.cell(row, 2).number_format = "0%"
        ws.cell(row, 3, d["score"])
        ws.cell(row, 4, f"=B{row}*C{row}")
        ws.cell(row, 5, notes[d["domain"]])
    last = start + len(SCORECARD_DOMAINS)
    tot = last + 1
    ws.cell(tot, 1, "WEIGHTED OVERALL SCORE")
    ws.cell(tot, 2, f"=SUM(B{first}:B{last})")
    ws.cell(tot, 2).number_format = "0%"
    ws.cell(tot, 4, f"=SUM(D{first}:D{last})")
    ws.cell(tot, 4).number_format = "0.0"
    ws.cell(tot, 4).font = Font(bold=True, size=14, color=NAVY)
    ws.cell(tot + 2, 1, "Overall residual risk rating (not derived from the score alone)")
    ws.cell(tot + 2, 2, ASSESSMENT["overall_risk"])
    ws.cell(tot + 3, 1, "Recommendation")
    ws.cell(tot + 3, 2, ASSESSMENT["recommendation"])
    ws.cell(tot + 5, 1, (
        "Interpretation: a score in the 70–80 range indicates a generally capable SaaS control "
        "environment with material gaps. Domain scores are not a substitute for residual risk. "
        "Four High residual risks remain; therefore overall vendor risk is High despite a 74.4 overall score."
    ))
    style_header(ws, start, 5)
    paint_rows(ws, start + 1, 5)
    autosize(ws, [28, 12, 22, 16, 70])

    chart = BarChart()
    chart.type = "col"
    chart.title = "Domain scores (0–100)"
    chart.y_axis.title = "Score"
    data = Reference(ws, min_col=3, min_row=start, max_row=last)
    cats = Reference(ws, min_col=1, min_row=first, max_row=last)
    chart.add_data(data, titles_from_data=True)
    chart.set_categories(cats)
    chart.shape = 4
    chart.y_axis.scaling.min = 0
    chart.y_axis.scaling.max = 100
    chart.style = 10
    ws.add_chart(chart, "A22")

    heat = wb.create_sheet("Risk_vs_Score")
    banner(heat, "Why 74.4% is still High residual risk", cols=6)
    heat["A6"] = "Overall score"
    heat["B6"] = OVERALL_SCORE
    heat["A7"] = "Overall residual risk"
    heat["B7"] = "High"
    heat["A8"] = "Primary High residual risks"
    heat["B8"] = "VR-001, VR-002, VR-003, VR-004"
    heat["A10"] = DISCLAIMER
    autosize(heat, [40, 50, 20, 20, 20, 20])
    save(wb, "09_Vendor_Scorecard/Vendor_Risk_Scorecard.xlsx")


def build_traceability():
    wb = Workbook()
    ws = wb.active
    ws.title = "Traceability_Matrix"
    banner(ws, "Evidence Traceability Matrix", "Finding → Control → Question → Response → Evidence → Result → Risk → Treatment → Remediation", 12)
    headers = [
        "Finding ID", "Finding", "Control ID(s)", "Questionnaire Question ID(s)",
        "Vendor Response (summary)", "Evidence", "Assessment Result",
        "Risk ID", "Inherent", "Residual", "Treatment", "Remediation ID",
    ]
    start = 6
    for i, h in enumerate(headers, 1):
        ws.cell(start, i, h)
    responses = {
        "VR-001": "Subprocessors are reviewed, but there is no fully standardized formal risk scoring process.",
        "VR-002": "Restoration testing is annual; last test 12 November 2025 (6h 40m).",
        "VR-003": "No formal RPO; daily backups imply ~24 hours potential data loss.",
        "VR-004": "Customer notice is 'without undue delay' with no hour-based SLA.",
        "VR-005": "SOC 2 Type I as of 30 September 2025; Type II in progress.",
        "VR-006": "No ISO/IEC 27001 certification; internal ISMS operated.",
        "VR-007": "High-severity vulnerabilities targeted for 30-day remediation.",
        "VR-008": "Legacy internal admin utilities do not support MFA.",
    }
    results = {
        "VR-001": "Partially Effective (CTRL-TPRM-004)",
        "VR-002": "Partially Effective (CTRL-BU-002)",
        "VR-003": "Ineffective for RPO (CTRL-BC-002)",
        "VR-004": "Partially Effective (CTRL-IR-002)",
        "VR-005": "Partially Effective / Type II Evidence Not Provided",
        "VR-006": "Ineffective as a certification control; ISMS otherwise operated",
        "VR-007": "Partially Effective SLA (CTRL-VM-002)",
        "VR-008": "Partially Effective (CTRL-AC-004)",
    }
    for i, rsk in enumerate(RISKS):
        row = start + 1 + i
        ws.cell(row, 1, rsk["id"])
        ws.cell(row, 2, rsk["title"])
        ws.cell(row, 3, rsk["control_ids"])
        ws.cell(row, 4, rsk["questionnaire_ids"])
        ws.cell(row, 5, responses[rsk["id"]])
        ws.cell(row, 6, rsk["evidence"])
        ws.cell(row, 7, results[rsk["id"]])
        ws.cell(row, 8, rsk["id"])
        ws.cell(row, 9, rsk["inherent_risk"])
        ws.cell(row, 10, rsk["residual_risk"])
        ws.cell(row, 11, rsk["treatment"])
        ws.cell(row, 12, rsk["remediation_id"])
    style_header(ws, start, 12)
    paint_rows(ws, start + 1, 12)
    autosize(ws, [12, 32, 36, 28, 50, 45, 40, 12, 12, 12, 12, 14])
    legend = wb.create_sheet("Chain_Legend")
    banner(legend, "How to read the traceability chain", cols=4)
    legend["A6"] = "Every significant risk is traceable from finding through remediation. Validation script validate_project.py checks uniqueness, treatments, owners, and report coverage."
    legend["A8"] = DISCLAIMER
    autosize(legend, [40, 40, 20, 20])
    save(wb, "15_Final_Checks/Evidence_Traceability_Matrix.xlsx")


def main():
    build_questionnaire()
    build_response_summary()
    build_control_assessment()
    build_evidence_mapping()
    build_inherent()
    build_residual()
    build_risk_register()
    build_remediation()
    build_scorecard()
    build_traceability()
    print("All workbooks generated.")
    print(f"Overall score {OVERALL_SCORE}; overall risk {ASSESSMENT['overall_risk']}; decision {ASSESSMENT['recommendation']}")


if __name__ == "__main__":
    main()
