def calculate_confidence_score(evidence):
    score = 0
    reasons = []

    successful_sources = evidence.get("successful_sources", 0)
    failed_sources = evidence.get("failed_sources", 0)
    strong_behavior_signals = evidence.get("strong_behavior_signals", 0)
    missing_fields = evidence.get("missing_fields", 0)

    if successful_sources >= 4:
        score += 4
        reasons.append("+4 Four or more enrichment sources succeeded")

    elif successful_sources >= 2:
        score += 2
        reasons.append("+2 Multiple enrichment sources succeeded")

    elif successful_sources == 1:
        score += 1
        reasons.append("+1 Only one enrichment source succeeded")

    if strong_behavior_signals >= 3:
        score += 3
        reasons.append("+3 Multiple strong behavioral signals agree")

    elif strong_behavior_signals >= 1:
        score += 1
        reasons.append("+1 Behavioral evidence is present")

    if failed_sources == 0:
        score += 2
        reasons.append("+2 No enrichment providers failed")

    elif failed_sources >= 3:
        score -= 2
        reasons.append("-2 Several enrichment providers failed")

    if missing_fields == 0:
        score += 1
        reasons.append("+1 No important evidence fields are missing")

    elif missing_fields >= 3:
        score -= 1
        reasons.append("-1 Several evidence fields are missing")

    if score < 0:
        score = 0

    if score > 10:
        score = 10

    return {
        "score": score,
        "max_score": 10,
        "reasons": reasons
    }
