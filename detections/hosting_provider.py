def detect_hosting_provider(event, hosting_asns):
    asn = event["asn"]

    if asn in hosting_asns:
        return True, asn

    return False, asn

