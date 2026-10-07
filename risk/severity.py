def classify_severity(risk_score):
    if risk_score >= 81:
        return "CRITICAL"

    elif risk_score >= 63:
        return "HIGH"

    elif risk_score >= 36:
        return "MEDIUM"

    return "LOW"
