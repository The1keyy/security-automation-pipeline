import os
import requests

from dotenv import load_dotenv


load_dotenv()


def check_ip_virustotal(ip_address):
    api_key = os.getenv("VIRUSTOTAL_API_KEY")

    if not api_key:
        return {
            "success": False,
            "error": "VIRUSTOTAL_API_KEY is missing"
        }

    url = f"https://www.virustotal.com/api/v3/ip_addresses/{ip_address}"

    headers = {
        "x-apikey": api_key
    }

    try:
        response = requests.get(
            url,
            headers=headers,
            timeout=10
        )

        response.raise_for_status()

        data = response.json()["data"]["attributes"]

        stats = data.get("last_analysis_stats", {})

        return {
            "success": True,
            "ip": ip_address,
            "malicious": stats.get("malicious", 0),
            "suspicious": stats.get("suspicious", 0),
            "harmless": stats.get("harmless", 0),
            "undetected": stats.get("undetected", 0),
            "reputation": data.get("reputation"),
            "country": data.get("country"),
            "as_owner": data.get("as_owner")
        }

    except requests.RequestException as error:
        return {
            "success": False,
            "error": str(error)
        }
