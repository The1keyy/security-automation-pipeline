def detect_brute_force(events):
    failed_attempts = 0
    user = None

    for event in events:
        if event["auth_result"] == "failure":
            failed_attempts += 1
            user = event["user"]

    if failed_attempts >= 5:
        return True, failed_attempts, user

    return False, failed_attempts, user
