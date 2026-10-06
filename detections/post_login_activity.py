def detect_post_login_activity(events):
    suspicious_actions = []

    for event in events:
        action = event.get("action")

        if action == "new_mfa_method":
            suspicious_actions.append("New MFA method added")

        elif action == "mailbox_forwarding_rule":
            suspicious_actions.append("Mailbox forwarding rule created")

        elif action == "password_changed":
            suspicious_actions.append("Password changed after login")

    if suspicious_actions:
        return True, suspicious_actions

    return False, []
