from config.load_config import load_risk_weights


def calculate_threat_intelligence_score(enrichment):
    config = load_risk_weights()

    if config is None:
        return {
            "score": 0,
            "max_score": 30,
            "reasons": []
        }

    weights = config["threat_intelligence"]

    score = 0
    reasons = []

    abuseipdb = enrichment.get("AbuseIPDB", {})
    virustotal = enrichment.get("VirusTotal", {})
    greynoise = enrichment.get("GreyNoise", {})
    otx = enrichment.get("OTX", {})
    tor = enrichment.get("Tor", {})
    blocklist = enrichment.get("Blocklist", {})

    if abuseipdb.get("success"):
        abuse_score = abuseipdb.get("abuse_score", 0)

        if abuse_score >= 90:
            points = weights["abuseipdb_90"]
            score += points
            reasons.append(
                "+" + str(points) + " AbuseIPDB score >= 90"
            )

        elif abuse_score >= 50:
            points = weights["abuseipdb_50"]
            score += points
            reasons.append(
                "+" + str(points) + " AbuseIPDB score >= 50"
            )

    if virustotal.get("success"):
        malicious = virustotal.get("malicious", 0)

        if malicious >= 5:
            points = weights["virustotal_5"]
            score += points
            reasons.append(
                "+" + str(points) +
                " VirusTotal: 5+ malicious detections"
            )

        elif malicious >= 1:
            points = weights["virustotal_1"]
            score += points
            reasons.append(
                "+" + str(points) +
                " VirusTotal: malicious detections present"
            )

    if greynoise.get("success"):
        if greynoise.get("classification") == "malicious":
            points = weights["greynoise_malicious"]
            score += points
            reasons.append(
                "+" + str(points) +
                " GreyNoise classified IP as malicious"
            )

    if otx.get("success"):
        pulse_count = otx.get("pulse_count", 0)

        if pulse_count >= 10:
            points = weights["otx_10"]
            score += points
            reasons.append(
                "+" + str(points) + " OTX: 10+ threat pulses"
            )

        elif pulse_count > 0:
            points = weights["otx_1"]
            score += points
            reasons.append(
                "+" + str(points) + " OTX: threat pulse activity"
            )

    if tor.get("success") and tor.get("is_tor_exit"):
        points = weights["tor_exit_node"]
        score += points
        reasons.append(
            "+" + str(points) + " Current Tor exit node"
        )

    if blocklist.get("success") and blocklist.get("blocklisted"):
        points = weights["blocklist"]
        score += points
        reasons.append(
            "+" + str(points) + " IP appears on blocklist"
        )

    if score > 30:
        score = 30

    return {
        "score": score,
        "max_score": 30,
        "reasons": reasons
    }
