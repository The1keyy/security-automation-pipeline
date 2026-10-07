import os

from reports.report_generator import generate_basic_report
from reports.text_report import generate_text_report
from reports.html_report import generate_html_report


detections = [
    "Impossible travel",
    "MFA fatigue",
    "Success after repeated failures",
    "Suspicious post-login activity"
]


timeline_events = [
    {
        "timestamp": "2026-10-07T14:00:00Z",
        "event": "Multiple failed login attempts detected"
    },
    {
        "timestamp": "2026-10-07T14:05:00Z",
        "event": "Successful login from suspicious IP"
    },
    {
        "timestamp": "2026-10-07T14:08:00Z",
        "event": "New MFA method added"
    },
    {
        "timestamp": "2026-10-07T14:10:00Z",
        "event": "Mailbox forwarding rule created"
    }
]


account_details = {
    "username": "jsmith@company.com",
    "account_type": "privileged",
    "department": "IT",
    "status": "active",
    "normal_country": "US"
}


source_details = {
    "ip": "185.220.101.45",
    "country": "DE",
    "city": "Berlin",
    "asn": "AS60729",
    "tor_exit": True
}


detection_evidence = [
    {
        "detection": "Impossible travel",
        "evidence": "Successful logins occurred from US and DE within an unrealistic travel window."
    },
    {
        "detection": "MFA fatigue",
        "evidence": "Multiple MFA prompts were generated before successful authentication."
    },
    {
        "detection": "Success after repeated failures",
        "evidence": "Several failed authentication attempts were followed by a successful login."
    },
    {
        "detection": "Suspicious post-login activity",
        "evidence": "A new MFA method and mailbox forwarding rule were created after login."
    }
]


threat_intelligence = [
    {
        "provider": "AbuseIPDB",
        "finding": "Abuse confidence score: 100"
    },
    {
        "provider": "VirusTotal",
        "finding": "8 security vendors flagged the IP as malicious"
    },
    {
        "provider": "Tor Exit List",
        "finding": "IP is an active Tor exit node"
    },
    {
        "provider": "OTX",
        "finding": "IP appears in 12 threat intelligence pulses"
    }
]


action_records = [
    {
        "action": "REVOKE_ACTIVE_SESSIONS",
        "target": "jsmith@company.com",
        "approved": True,
        "executed": False,
        "dry_run": True,
        "status": "Approved by analyst but simulated only"
    },
    {
        "action": "BLOCK_IP",
        "target": "185.220.101.45",
        "approved": True,
        "executed": False,
        "dry_run": True,
        "status": "Approved by analyst but simulated only"
    }
]


unverified_items = [
    {
        "item": "Endpoint compromise",
        "reason": "No endpoint telemetry was available."
    },
    {
        "item": "User intent",
        "reason": "The user was not contacted during this simulated incident."
    },
    {
        "item": "Mailbox rule impact",
        "reason": "No production mailbox data was accessed."
    }
]


report = generate_basic_report(
    user="jsmith@company.com",
    source_ip="185.220.101.45",
    severity="CRITICAL",
    risk_score=86,
    confidence=10,
    detections=detections,
    timeline_events=timeline_events,
    account_details=account_details,
    source_details=source_details,
    detection_evidence=detection_evidence,
    threat_intelligence=threat_intelligence,
    threat_score=30,
    behavior_score=28,
    impact_score=20,
    correlation_score=8,
    successful_sources=4,
    failed_sources=0,
    strong_behavior_signals=4,
    missing_fields=0,
    action_records=action_records,
    unverified_items=unverified_items,
    event_ids=[
        "evt-1001",
        "evt-1002",
        "evt-1003",
        "evt-1004"
    ],
    log_sources=[
        "Identity authentication logs",
        "MFA logs",
        "Cloud audit logs"
    ],
    enrichment_sources=[
        "AbuseIPDB",
        "VirusTotal",
        "OTX",
        "Tor Exit List"
    ],
    pipeline_version="1.0",
    dry_run=True,
    environment="Synthetic portfolio lab"
)


text_file = "reports/incident_report.txt"
html_file = "reports/incident_report.html"


generate_text_report(
    report,
    text_file
)


generate_html_report(
    report,
    html_file
)


checks = []


checks.append(
    (
        "Severity is CRITICAL",
        report["severity"] == "CRITICAL"
    )
)


checks.append(
    (
        "Risk score is 86/90",
        report["risk_score"] == 86
    )
)


checks.append(
    (
        "Confidence is 10/10",
        report["confidence"] == 10
    )
)


checks.append(
    (
        "Four detections are present",
        len(report["detection_evidence"]) == 4
    )
)


checks.append(
    (
        "MITRE ATT&CK mappings are present",
        len(report["mitre_attack"]) > 0
    )
)


checks.append(
    (
        "Response requires analyst approval",
        report["recommended_actions"]["requires_approval"] is True
    )
)


checks.append(
    (
        "Text report exists",
        os.path.exists(text_file)
    )
)


checks.append(
    (
        "HTML report exists",
        os.path.exists(html_file)
    )
)


print("Final End-to-End Report Test")
print("============================")

all_passed = True


for name, passed in checks:
    if passed:
        print("[PASS]", name)
    else:
        print("[FAIL]", name)
        all_passed = False


print()


if all_passed:
    print("FINAL STATUS: ALL REPORTING TESTS PASSED")
else:
    print("FINAL STATUS: ONE OR MORE TESTS FAILED")
