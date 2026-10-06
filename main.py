import json

from detections.post_login_activity import detect_post_login_activity


try:
    with open("sample_logs/post_login_activity.json", "r") as file:
        events = json.load(file)

    detected, suspicious_actions = detect_post_login_activity(events)

    print("Suspicious Post-Login Activity Detection")
    print("----------------------------------------")
    print("User:", events[0]["user"])
    print("Source IP:", events[0]["source_ip"])

    if detected:
        print("ALERT: Suspicious post-login activity detected")

        for action in suspicious_actions:
            print("-", action)

    else:
        print("No suspicious post-login activity detected.")

except FileNotFoundError:
    print("ERROR: Security log file was not found.")

except json.JSONDecodeError:
    print("ERROR: Security log contains invalid JSON.")
