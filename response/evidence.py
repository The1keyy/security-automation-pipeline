def build_action_evidence(
    risk_score,
    severity,
    confidence,
    detections,
    threat_intel,
    recommended_action
):
    evidence = {
        "risk_score": risk_score,
        "severity": severity,
        "confidence": confidence,
        "detections": detections,
        "threat_intelligence": threat_intel,
        "recommended_action": recommended_action
    }

    return evidence
