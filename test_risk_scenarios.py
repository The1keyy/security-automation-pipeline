from risk.risk_engine import calculate_final_risk
from risk.severity import classify_severity


def run_scenario(
    name,
    enrichment,
    behavior,
    context,
    confidence
):
    result = calculate_final_risk(
        enrichment,
        behavior,
        context,
        confidence
    )

    severity = classify_severity(result["risk_score"])

    print()
    print(name)
    print("=" * len(name))

    print("Threat:", str(result["threat"]["score"]) + "/30")
    print("Behavior:", str(result["behavior"]["score"]) + "/30")
    print("Impact:", str(result["impact"]["score"]) + "/20")
    print("Correlation:", str(result["correlation"]["score"]) + "/10")
    print("Risk:", str(result["risk_score"]) + "/90")
    print("Confidence:", str(result["confidence_score"]) + "/10")
    print("Severity:", severity)


clean_enrichment = {
    "AbuseIPDB": {
        "success": True,
        "abuse_score": 0
    },
    "VirusTotal": {
        "success": True,
        "malicious": 0
    },
    "GreyNoise": {
        "success": True,
        "classification": "benign"
    },
    "OTX": {
        "success": True,
        "pulse_count": 0
    },
    "Tor": {
        "success": True,
        "is_tor_exit": False
    },
    "Blocklist": {
        "success": True,
        "blocklisted": False
    }
}


normal_behavior = {
    "impossible_travel": False,
    "success_after_failure": False,
    "brute_force": False,
    "password_spray": False,
    "credential_stuffing": False,
    "mfa_fatigue": False,
    "suspicious_post_login": False,
    "new_country": False,
    "new_device": False,
    "new_user_agent": False,
    "abnormal_login_time": False,
    "tor_exit_node": False
}


high_confidence = {
    "successful_sources": 6,
    "failed_sources": 0,
    "strong_behavior_signals": 0,
    "missing_fields": 0
}


# LOW
run_scenario(
    "LOW - Normal Login",
    clean_enrichment,
    normal_behavior,
    {
        "account_type": "normal",
        "asset_criticality": "low",
        "sensitive_system": False
    },
    high_confidence
)


# MEDIUM
medium_enrichment = {
    "AbuseIPDB": {
        "success": True,
        "abuse_score": 60
    },
    "VirusTotal": {
        "success": True,
        "malicious": 1
    },
    "GreyNoise": {
        "success": True,
        "classification": "benign"
    },
    "OTX": {
        "success": True,
        "pulse_count": 2
    },
    "Tor": {
        "success": True,
        "is_tor_exit": False
    },
    "Blocklist": {
        "success": True,
        "blocklisted": False
    }
}


medium_behavior = normal_behavior.copy()
medium_behavior["new_country"] = True
medium_behavior["new_device"] = True
medium_behavior["abnormal_login_time"] = True
medium_behavior["success_after_failure"] = True
medium_behavior["brute_force"] = True
medium_behavior["mfa_fatigue"] = True


run_scenario(
    "MEDIUM - Suspicious Login",
    medium_enrichment,
    medium_behavior,
    {
        "account_type": "normal",
        "asset_criticality": "medium",
        "sensitive_system": False
    },
    {
        "successful_sources": 6,
        "failed_sources": 0,
        "strong_behavior_signals": 2,
        "missing_fields": 0
    }
)


# HIGH
high_enrichment = {
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


high_behavior = normal_behavior.copy()
high_behavior["impossible_travel"] = True
high_behavior["mfa_fatigue"] = True
high_behavior["new_country"] = True
high_behavior["success_after_failure"] = True
high_behavior["new_device"] = True
high_behavior["tor_exit_node"] = True


run_scenario(
    "HIGH - Likely Compromise",
    high_enrichment,
    high_behavior,
    {
        "account_type": "normal",
        "asset_criticality": "high",
        "sensitive_system": False
    },
    {
        "successful_sources": 6,
        "failed_sources": 0,
        "strong_behavior_signals": 4,
        "missing_fields": 0
    }
)


# CRITICAL
critical_behavior = high_behavior.copy()
critical_behavior["suspicious_post_login"] = True


run_scenario(
    "CRITICAL - Privileged Account Compromise",
    high_enrichment,
    critical_behavior,
    {
        "account_type": "privileged",
        "asset_criticality": "critical",
        "sensitive_system": True
    },
    {
        "successful_sources": 6,
        "failed_sources": 0,
        "strong_behavior_signals": 5,
        "missing_fields": 0
    }
)
