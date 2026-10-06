from datetime import datetime


def detect_mfa_fatigue(events):
    denied_prompts = []

    for event in events:
        if event["mfa_result"] == "denied":
            denied_prompts.append(event)

    if len(denied_prompts) < 3:
        return False, len(denied_prompts), 0

    first_time = datetime.fromisoformat(
        denied_prompts[0]["timestamp"].replace("Z", "+00:00")
    )

    last_time = datetime.fromisoformat(
        denied_prompts[-1]["timestamp"].replace("Z", "+00:00")
    )

    minutes = (last_time - first_time).total_seconds() / 60

    if len(denied_prompts) >= 3 and minutes <= 10:
        return True, len(denied_prompts), minutes

    return False, len(denied_prompts), minutes
