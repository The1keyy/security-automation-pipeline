from risk.threat_score import calculate_threat_intelligence_score
from risk.behavior_score import calculate_behavior_score
from risk.impact_score import calculate_impact_score
from risk.correlation_score import calculate_correlation_score
from risk.confidence_score import calculate_confidence_score
from risk.severity import classify_severity


def calculate_final_risk(
    enrichment,
    behavior_signals,
    context,
    confidence_evidence
):
    threat = calculate_threat_intelligence_score(enrichment)
    behavior = calculate_behavior_score(behavior_signals)
    impact = calculate_impact_score(context)
    correlation = calculate_correlation_score(behavior_signals)
    confidence = calculate_confidence_score(confidence_evidence)

    risk_score = (
        threat["score"]
        + behavior["score"]
        + impact["score"]
        + correlation["score"]
    )

    if risk_score > 90:
        risk_score = 90

    severity = classify_severity(risk_score)

    return {
        "risk_score": risk_score,
        "max_risk_score": 90,
        "severity": severity,
        "confidence_score": confidence["score"],
        "max_confidence_score": confidence["max_score"],
        "threat": threat,
        "behavior": behavior,
        "impact": impact,
        "correlation": correlation,
        "confidence": confidence
    }
