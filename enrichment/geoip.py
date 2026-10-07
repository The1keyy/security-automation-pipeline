import requests


def lookup_geoip(ip_address):
    url = f"https://ipinfo.io/{ip_address}/json"

    try:
        response = requests.get(
            url,
            timeout=10
        )

        response.raise_for_status()

        data = response.json()

        location = data.get("loc")

        latitude = None
        longitude = None

        if location:
            latitude, longitude = location.split(",")

        return {
            "success": True,
            "ip": data.get("ip"),
            "city": data.get("city"),
            "region": data.get("region"),
            "country": data.get("country"),
            "latitude": latitude,
            "longitude": longitude,
            "timezone": data.get("timezone"),
            "org": data.get("org")
        }

    except requests.RequestException as error:
        return {
            "success": False,
            "error": str(error)
        }
