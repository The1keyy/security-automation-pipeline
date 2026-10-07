providers = {
    "AbuseIPDB": {
        "success": True,
        "abuse_score": 100
    },
    "VirusTotal": {
        "success": True,
        "malicious": 6
    },
    "GreyNoise": {
        "success": False,
        "error": "API request timed out"
    },
    "OTX": {
        "success": True,
        "pulse_count": 12
    }
}

print("Graceful Degradation Test")
print("-------------------------")

successful_providers = 0
failed_providers = 0

for name, result in providers.items():
    if result["success"]:
        successful_providers += 1
        print(name + ": OK")
    else:
        failed_providers += 1
        print(name + ": FAILED")
        print("Reason:", result["error"])

print()
print("Successful providers:", successful_providers)
print("Failed providers:", failed_providers)

if successful_providers > 0:
    print("STATUS: Pipeline continued with available intelligence")
else:
    print("STATUS: No enrichment data available")
