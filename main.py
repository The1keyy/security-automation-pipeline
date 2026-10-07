from enrichment.pipeline import enrich_ip


ip_address = "185.220.101.45"

results = enrich_ip(ip_address)

print("Security Threat Intelligence Pipeline")
print("=====================================")
print("Target IP:", ip_address)
print()

successful_providers = 0
failed_providers = 0


for provider, result in results.items():

    print(provider)
    print("-" * len(provider))

    if result.get("success"):
        successful_providers += 1

        if provider == "AbuseIPDB":
            print("Abuse Score:", result.get("abuse_score"))
            print("Reports:", result.get("total_reports"))
            print("ISP:", result.get("isp"))
            print("Cache:", result.get("cache"))

        elif provider == "VirusTotal":
            print("Malicious:", result.get("malicious"))
            print("Suspicious:", result.get("suspicious"))
            print("Reputation:", result.get("reputation"))

        elif provider == "GreyNoise":
            print("Internet Scanner:", result.get("noise"))
            print("Classification:", result.get("classification"))
            print("Name:", result.get("name"))

        elif provider == "OTX":
            print("Pulse Count:", result.get("pulse_count"))
            print("Reputation:", result.get("reputation"))

        elif provider == "Tor":
            print("Tor Exit Node:", result.get("is_tor_exit"))

        elif provider == "GeoIP":
            print("Country:", result.get("country"))
            print("City:", result.get("city"))
            print("Timezone:", result.get("timezone"))

        elif provider == "ASN":
            print("ASN:", result.get("asn"))
            print("Organization:", result.get("organization"))

        elif provider == "Blocklist":
            print("Blocklisted:", result.get("blocklisted"))

        print("Status: OK")

    else:
        failed_providers += 1
        print("Status: FAILED")
        print("Reason:", result.get("error", "Unknown error"))

    print()


print("Pipeline Summary")
print("----------------")
print("Successful providers:", successful_providers)
print("Failed providers:", failed_providers)

if successful_providers > 0:
    print("STATUS: Enrichment pipeline completed")
else:
    print("STATUS: No threat intelligence available")
