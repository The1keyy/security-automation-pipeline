def calculate_behavior_score(signals):
    score = 0
    reasons = []

    if signals.get("impossible_travel"):
        score += 6
        reasons.append("+6 Impossible travel")

    if signals.get("success_after_failure"):
        score += 4
        reasons.append("+4 Success after repeated failures")

    if signals.get("brute_force"):
        score += 4
        reasons.append("+4 Brute force activity")

    if signals.get("password_spray"):
        score += 5
        reasons.append("+5 Password spray activity")

    if signals.get("credential_stuffing"):
        score += 5
        reasons.append("+5 Credential stuffing activity")

    if signals.get("mfa_fatigue"):
        score += 6
        reasons.append("+6 MFA fatigue activity")

    if signals.get("suspicious_post_login"):
        score += 8
        reasons.append("+8 Suspicious post-login activity")

    if signals.get("new_country"):
        score += 2
        reasons.append("+2 New country")

    if signals.get("new_device"):
        score += 2
        reasons.append("+2 New device")

    if signals.get("new_user_agent"):
        score += 1
        reasons.append("+1 New user agent")

    if signals.get("abnormal_login_time"):
        score += 1
        reasons.append("+1 Abnormal login time")

    if score > 30:
        score = 30

    return {
        "score": score,
        "max_score": 30,
        "reasons": reasons
    }
