def check_blocklist(ip_address, blocklisted_ips):
    if ip_address in blocklisted_ips:
        return {
            "success": True,
            "ip": ip_address,
            "blocklisted": True
        }

    return {
        "success": True,
        "ip": ip_address,
        "blocklisted": False
    }
