from response.evidence import build_action_evidence


detections = [
    "Impossible travel",
    "MFA fatigue",
    "Success after repeated failures"
]


threat_intel = [
    "AbuseIPDB score: 100",
    "VirusTotal malicious detections: 8",
    "Tor exit node: True"
]


evidence = build_action_evidence(
    risk_score=86,
    severity="CRITICAL",
    confidence=10,
    detections=detections,
    threat_intel=threat_intel,
    recommended_action="REVOKE_ACTIVE_SESSIONS"
)


print("Response Action Evidence")
print("========================")

print("Risk Score:", evidence["risk_score"])
print("Severity:", evidence["severity"])
print("Confidence:", evidence["confidence"])

print()
print("Detections:")

for detection in evidence["detections"]:
    print("-", detection)

print()
print("Threat Intelligence:")

for item in evidence["threat_intelligence"]:
    print("-", item)

print()
print("Recommended Action:", evidence["recommended_action"])
