def detect_password_spray(events):
    users = set()
    source_ip = None
    failed_attempts = 0

    for event in events:
        if event["auth_result"] == "failure":
            failed_attempts += 1
            users.add(event["user"])
            source_ip = event["source_ip"]

    if len(users) >= 5:
        return True, len(users), failed_attempts, source_ip

    return False, len(users), failed_attempts, source_ip
