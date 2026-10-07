def calculate_correlation_score(signals):
    score = 0
    reasons = []

    if signals.get("success_after_failure") and signals.get("new_country"):
        score += 2
        reasons.append("+2 Success after failures + new country")

    if signals.get("impossible_travel") and signals.get("tor_exit_node"):
        score += 2
        reasons.append("+2 Impossible travel + Tor exit node")

    if signals.get("mfa_fatigue") and signals.get("success_after_failure"):
        score += 2
        reasons.append("+2 MFA fatigue + successful login after failures")

    if signals.get("suspicious_post_login") and signals.get("new_device"):
        score += 2
        reasons.append("+2 Suspicious post-login activity + new device")

    if signals.get("password_spray") and signals.get("credential_stuffing"):
        score += 2
        reasons.append("+2 Password spray + credential stuffing")

    if score > 10:
        score = 10

    return {
        "score": score,
        "max_score": 10,
        "reasons": reasons
    }
