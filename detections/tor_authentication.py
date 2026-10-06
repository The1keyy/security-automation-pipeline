def detect_tor_authentication(event, tor_exit_nodes):
    source_ip = event["source_ip"]

    if source_ip in tor_exit_nodes:
        return True, source_ip

    return False, source_ip
