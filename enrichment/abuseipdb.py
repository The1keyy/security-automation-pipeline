import os
import requests

from dotenv import load_dotenv
from enrichment.cache import get_cached_result, save_cached_result


load_dotenv()


def check_ip_abuseipdb(ip_address):
    cache_key = f"abuseipdb:{ip_address}"

    cached = get_cached_result(cache_key)

    if cached:
        cached["cache"] = "HIT"
        return cached

    api_key = os.getenv("ABUSEIPDB_API_KEY")

    if not api_key:
        return {
            "success": False,
            "error": "ABUSEIPDB_API_KEY is missing"
        }

    url = "https://api.abuseipdb.com/api/v2/check"

    headers = {
        "Accept": "application/json",
        "Key": api_key
    }

    params = {
        "ipAddress": ip_address,
        "maxAgeInDays": 90
    }

    try:
        response = requests.get(
            url,
            headers=headers,
            params=params,
            timeout=10
        )

        if response.status_code == 429:
            retry_after = response.headers.get("Retry-After")

            return {
                "success": False,
                "rate_limited": True,
                "error": "API rate limit reached",
                "retry_after": retry_after
            }

        response.raise_for_status()

        data = response.json()["data"]

        result = {
            "success": True,
            "ip": data.get("ipAddress"),
            "abuse_score": data.get("abuseConfidenceScore"),
            "country": data.get("countryCode"),
            "usage_type": data.get("usageType"),
            "isp": data.get("isp"),
            "domain": data.get("domain"),
            "total_reports": data.get("totalReports"),
            "cache": "MISS"
        }

        save_cached_result(cache_key, result)

        return result

    except requests.Timeout:
        return {
            "success": False,
            "timeout": True,
            "error": "API request timed out"
        }

    except requests.RequestException as error:
        return {
            "success": False,
            "error": str(error)
        }
