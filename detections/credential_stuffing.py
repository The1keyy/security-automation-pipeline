def detect_credential_stuffing(events):
    users = set()
    failures = 0
    successes = 0
    source_ip = None
    successful_user = None

    for event in events:
        users.add(event["user"])
        source_ip = event["source_ip"]

        if event["auth_result"] == "failure":
            failures += 1

        elif event["auth_result"] == "success":
            successes += 1
            successful_user = event["user"]

    if len(users) >= 5 and failures >= 4 and successes >= 1:
        return True, len(users), failures, successes, source_ip, successful_user

    return False, len(users), failures, successes, source_ip, successful_user
