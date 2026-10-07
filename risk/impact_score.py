def calculate_impact_score(context):
    score = 0
    reasons = []

    account_type = context.get("account_type", "normal")
    asset_criticality = context.get("asset_criticality", "low")
    sensitive_system = context.get("sensitive_system", False)

    if account_type == "privileged":
        score += 8
        reasons.append("+8 Privileged/admin account")

    elif account_type == "executive":
        score += 6
        reasons.append("+6 Executive/VIP account")

    elif account_type == "service":
        score += 5
        reasons.append("+5 Service account")

    else:
        score += 2
        reasons.append("+2 Normal user account")

    if asset_criticality == "critical":
        score += 8
        reasons.append("+8 Critical asset")

    elif asset_criticality == "high":
        score += 6
        reasons.append("+6 High-value asset")

    elif asset_criticality == "medium":
        score += 3
        reasons.append("+3 Medium-value asset")

    if sensitive_system:
        score += 4
        reasons.append("+4 Sensitive system")

    if score > 20:
        score = 20

    return {
        "score": score,
        "max_score": 20,
        "reasons": reasons
    }
