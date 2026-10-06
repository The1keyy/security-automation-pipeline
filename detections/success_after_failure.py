def detect_success_after_failure(events):
    failures = 0

    for event in events:
        if event["auth_result"] == "failure":
            failures += 1

        elif event["auth_result"] == "success":
            if failures >= 3:
                return True, failures

    return False, failures	
