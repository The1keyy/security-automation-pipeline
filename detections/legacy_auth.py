def detect_legacy_auth(event, legacy_protocols):
    protocol = event["auth_protocol"]

    if protocol in legacy_protocols:
        return True, protocol

    return False, protocol
