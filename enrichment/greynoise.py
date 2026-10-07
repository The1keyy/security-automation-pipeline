import os
import requests

from dotenv import load_dotenv


load_dotenv()


def check_ip_greynoise(ip_address):
    api_key = os.getenv("GREYNOISE_API_KEY")

    url = f"https://api.greynoise.io/v3/community/{ip_address}"

    headers = {
        "Accept": "application/json"
    }

    if api_key:
        headers["Key"] = api_key

    try:
        response = requests.get(
            url,
            headers=headers,
            timeout=10
        )

        if response.status_code == 404:
            return {
                "success": True,
                "ip": ip_address,
                "noise": False,
                "riot": False,
                "classification": "not found",
                "name": None,
                "last_seen": None
            }

        response.raise_for_status()

        data = response.json()

        return {
            "success": True,
            "ip": data.get("ip"),
            "noise": data.get("noise"),
            "riot": data.get("riot"),
            "classification": data.get("classification"),
            "name": data.get("name"),
            "last_seen": data.get("last_seen")
        }

    except requests.RequestException as error:
        return {
            "success": False,
            "error": str(error)
        }
