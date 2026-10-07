from risk.risk_engine import calculate_final_risk


enrichment = {
    "AbuseIPDB": {
        "success": True,
        "abuse_score": 100
    },

    "VirusTotal": {
        "success": True,
        "malicious": 8
    },

    "GreyNoise": {
        "success": True,
        "classification": "malicious"
    },

    "OTX": {
        "success": True,
        "pulse_count": 12
    },

    "Tor": {
        "success": True,
        "is_tor_exit": True
    },

    "Blocklist": {
        "success": True,
        "blocklisted": True
    }
}


behavior_signals = {
    "impossible_travel": True,
    "success_after_failure": True,
    "brute_force": False,
    "password_spray": False,
    "credential_stuffing": False,
    "mfa_fatigue": True,
    "suspicious_post_login": True,
    "new_country": True,
    "new_device": True,
    "new_user_agent": False,
    "abnormal_login_time": True,
    "tor_exit_node": True
}


context = {
    "account_type": "privileged",
    "asset_criticality": "critical",
    "sensitive_system": True
}


confidence_evidence = {
    "successful_sources": 6,
    "failed_sources": 0,
    "strong_behavior_signals": 4,
    "missing_fields": 0
}


result = calculate_final_risk(
    enrichment,
    behavior_signals,
    context,
    confidence_evidence
)


print("Final Security Risk Assessment")
print("==============================")

print(
    "Threat Intelligence:",
    str(result["threat"]["score"]) + "/30"
)

print(
    "Behavioral Evidence:",
    str(result["behavior"]["score"]) + "/30"
)

print(
    "User / Asset Impact:",
    str(result["impact"]["score"]) + "/20"
)

print(
    "Correlation:",
    str(result["correlation"]["score"]) + "/10"
)

print("------------------------------")

print(
    "Final Risk Score:",
    str(result["risk_score"]) + "/90"
)

print(
    "Confidence:",
    str(result["confidence_score"]) + "/10"
)
