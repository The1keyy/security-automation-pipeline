TRUSTED_IPS = [
    "10.0.0.10",
    "10.0.0.20",
    "192.168.1.100"
]


def is_ip_allowed(ip_address):
    if ip_address in TRUSTED_IPS:
        return True

    return False


def check_ip_response_safety(ip_address):
    if is_ip_allowed(ip_address):
        return {
            "allowed": False,
            "reason": "IP is on the trusted allowlist"
        }

    return {
        "allowed": True,
        "reason": "IP is not on the trusted allowlist"
    }
