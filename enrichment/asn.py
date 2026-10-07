from enrichment.geoip import lookup_geoip


def lookup_asn(ip_address):
    geo_result = lookup_geoip(ip_address)

    if not geo_result["success"]:
        return geo_result

    org = geo_result.get("org")

    if not org:
        return {
            "success": True,
            "ip": ip_address,
            "asn": None,
            "organization": None
        }

    parts = org.split(" ", 1)

    asn = parts[0]

    organization = None

    if len(parts) > 1:
        organization = parts[1]

    return {
        "success": True,
        "ip": ip_address,
        "asn": asn,
        "organization": organization
    }
