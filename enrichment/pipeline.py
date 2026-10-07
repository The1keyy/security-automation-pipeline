from enrichment.abuseipdb import check_ip_abuseipdb
from enrichment.virustotal import check_ip_virustotal
from enrichment.greynoise import check_ip_greynoise
from enrichment.otx import check_ip_otx
from enrichment.tor_exit import check_tor_exit
from enrichment.geoip import lookup_geoip
from enrichment.asn import lookup_asn
from enrichment.blocklist import check_blocklist


def enrich_ip(ip_address):
    results = {}

    # AbuseIPDB
    try:
        results["AbuseIPDB"] = check_ip_abuseipdb(ip_address)
    except Exception as error:
        results["AbuseIPDB"] = {
            "success": False,
            "error": str(error)
        }

    # VirusTotal
    try:
        results["VirusTotal"] = check_ip_virustotal(ip_address)
    except Exception as error:
        results["VirusTotal"] = {
            "success": False,
            "error": str(error)
        }

    # GreyNoise
    try:
        results["GreyNoise"] = check_ip_greynoise(ip_address)
    except Exception as error:
        results["GreyNoise"] = {
            "success": False,
            "error": str(error)
        }

    # AlienVault OTX
    try:
        results["OTX"] = check_ip_otx(ip_address)
    except Exception as error:
        results["OTX"] = {
            "success": False,
            "error": str(error)
        }

    # Tor
    try:
        results["Tor"] = check_tor_exit(ip_address)
    except Exception as error:
        results["Tor"] = {
            "success": False,
            "error": str(error)
        }

    # GeoIP
    try:
        results["GeoIP"] = lookup_geoip(ip_address)
    except Exception as error:
        results["GeoIP"] = {
            "success": False,
            "error": str(error)
        }

    # ASN
    try:
        results["ASN"] = lookup_asn(ip_address)
    except Exception as error:
        results["ASN"] = {
            "success": False,
            "error": str(error)
        }

    # Local blocklist
    blocklisted_ips = [
        "185.220.101.45",
        "91.198.40.22",
        "45.83.64.10"
    ]

    try:
        results["Blocklist"] = check_blocklist(
            ip_address,
            blocklisted_ips
        )
    except Exception as error:
        results["Blocklist"] = {
            "success": False,
            "error": str(error)
        }

    return results
