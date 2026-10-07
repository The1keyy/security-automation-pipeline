from risk.threat_score import calculate_threat_intelligence_score


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


result = calculate_threat_intelligence_score(enrichment)


print("Threat Intelligence Risk Score")
print("==============================")

for reason in result["reasons"]:
    print(reason)

print()

print(
    "Threat Intelligence Score:",
    str(result["score"]) + "/" + str(result["max_score"])
)
