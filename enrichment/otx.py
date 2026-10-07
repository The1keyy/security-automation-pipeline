import os
import requests

from dotenv import load_dotenv


load_dotenv()


def check_ip_otx(ip_address):
    api_key = os.getenv("OTX_API_KEY")

    if not api_key:
        return {
            "success": False,
            "error": "OTX_API_KEY is missing"
        }

    url = (
        "https://otx.alienvault.com/api/v1/"
        f"indicators/IPv4/{ip_address}/general"
    )

    headers = {
        "X-OTX-API-KEY": api_key
    }

    try:
        response = requests.get(
            url,
            headers=headers,
            timeout=30
        )

        response.raise_for_status()

        data = response.json()

        pulse_info = data.get("pulse_info", {})

        return {
            "success": True,
            "ip": ip_address,
            "pulse_count": pulse_info.get("count", 0),
            "country": data.get("country_name"),
            "city": data.get("city"),
            "asn": data.get("asn"),
            "reputation": data.get("reputation")
        }

    except requests.RequestException as error:
        return {
            "success": False,
            "error": str(error)
        }
