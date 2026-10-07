from response.decision_engine import choose_response


def generate_executive_summary(
    user,
    source_ip,
    severity,
    risk_score,
    confidence,
    detections
):
    detection_count = len(detections)

    summary = (
        f"A {severity} security incident was identified for user {user}. "
        f"The activity originated from source IP {source_ip}. "
        f"The risk engine assigned a score of {risk_score}/90 "
        f"with a confidence score of {confidence}/10. "
        f"A total of {detection_count} suspicious indicators were identified."
    )

    return summary


def build_timeline(events):
    sorted_events = sorted(
        events,
        key=lambda event: event["timestamp"]
    )

    timeline = []

    for event in sorted_events:
        timeline.append(
            {
                "timestamp": event["timestamp"],
                "event": event["event"]
            }
        )

    return timeline


def build_identity_details(account_details, source_details):
    return {
        "account": account_details,
        "source": source_details
    }


def build_detection_evidence(detection_evidence):
    evidence_list = []

    for item in detection_evidence:
        evidence_list.append(
            {
                "detection": item["detection"],
                "evidence": item["evidence"]
            }
        )

    return evidence_list


def build_threat_intelligence(threat_intelligence):
    findings = []

    for item in threat_intelligence:
        findings.append(
            {
                "provider": item["provider"],
                "finding": item["finding"]
            }
        )

    return findings


def build_risk_breakdown(
    threat_score,
    behavior_score,
    impact_score,
    correlation_score
):
    total = (
        threat_score
        + behavior_score
        + impact_score
        + correlation_score
    )

    return {
        "threat_intelligence": {
            "score": threat_score,
            "max_score": 30
        },
        "behavior": {
            "score": behavior_score,
            "max_score": 30
        },
        "impact": {
            "score": impact_score,
            "max_score": 20
        },
        "correlation": {
            "score": correlation_score,
            "max_score": 10
        },
        "total": total,
        "max_total": 90
    }


def build_confidence_details(
    confidence_score,
    successful_sources,
    failed_sources,
    strong_behavior_signals,
    missing_fields
):
    reasons = []

    if successful_sources >= 4:
        reasons.append(
            "Multiple threat intelligence sources returned usable data."
        )

    if strong_behavior_signals >= 3:
        reasons.append(
            "Multiple strong behavioral detections were observed."
        )

    if failed_sources == 0:
        reasons.append(
            "No enrichment providers failed."
        )

    if missing_fields == 0:
        reasons.append(
            "No important enrichment fields were missing."
        )

    return {
        "score": confidence_score,
        "max_score": 10,
        "successful_sources": successful_sources,
        "failed_sources": failed_sources,
        "strong_behavior_signals": strong_behavior_signals,
        "missing_fields": missing_fields,
        "reasons": reasons
    }


def build_recommended_actions(severity):
    decision = choose_response(severity)

    recommendations = []

    if severity == "LOW":
        recommendations.append(
            "Log the event and continue monitoring."
        )

    elif severity == "MEDIUM":
        recommendations.append(
            "Review authentication and account activity."
        )
        recommendations.append(
            "Validate the activity with the user if necessary."
        )

    elif severity == "HIGH":
        recommendations.append(
            "Begin analyst investigation."
        )
        recommendations.append(
            "Request approval before containment."
        )
        recommendations.append(
            "Review active sessions and recent account changes."
        )

    elif severity == "CRITICAL":
        recommendations.append(
            "Escalate immediately to a security analyst."
        )
        recommendations.append(
            "Use only a pre-approved containment playbook."
        )
        recommendations.append(
            "Consider revoking active sessions."
        )
        recommendations.append(
            "Consider disabling the account after approval."
        )
        recommendations.append(
            "Preserve evidence before additional response actions."
        )

    return {
        "response_action": decision["action"],
        "requires_approval": decision["requires_approval"],
        "automatic": decision["automatic"],
        "message": decision["message"],
        "recommendations": recommendations
    }


def build_actions_taken(action_records):
    actions = []

    for item in action_records:
        actions.append(
            {
                "action": item["action"],
                "target": item["target"],
                "approved": item["approved"],
                "executed": item["executed"],
                "dry_run": item["dry_run"],
                "status": item["status"]
            }
        )

    return actions


def build_unverified_findings(unverified_items):
    findings = []

    for item in unverified_items:
        findings.append(
            {
                "item": item["item"],
                "reason": item["reason"]
            }
        )

    return findings


def build_mitre_mapping():
    return [
        {
            "technique_id": "T1078",
            "technique": "Valid Accounts",
            "evidence": "A successful login occurred using the affected account."
        },
        {
            "technique_id": "T1621",
            "technique": "Multi-Factor Authentication Request Generation",
            "evidence": "Multiple MFA prompts were generated before successful authentication."
        },
        {
            "technique_id": "T1098",
            "technique": "Account Manipulation",
            "evidence": "A new MFA method was added after the suspicious login."
        },
        {
            "technique_id": "T1114.003",
            "technique": "Email Forwarding Rule",
            "evidence": "A mailbox forwarding rule was created after login."
        }
    ]


def build_technical_appendix(
    event_ids,
    log_sources,
    enrichment_sources,
    pipeline_version,
    dry_run,
    environment
):
    return {
        "event_ids": event_ids,
        "log_sources": log_sources,
        "enrichment_sources": enrichment_sources,
        "pipeline_version": pipeline_version,
        "dry_run": dry_run,
        "environment": environment
    }


def generate_basic_report(
    user,
    source_ip,
    severity,
    risk_score,
    confidence,
    detections,
    timeline_events,
    account_details,
    source_details,
    detection_evidence,
    threat_intelligence,
    threat_score,
    behavior_score,
    impact_score,
    correlation_score,
    successful_sources,
    failed_sources,
    strong_behavior_signals,
    missing_fields,
    action_records,
    unverified_items,
    event_ids,
    log_sources,
    enrichment_sources,
    pipeline_version,
    dry_run,
    environment
):
    summary = generate_executive_summary(
        user,
        source_ip,
        severity,
        risk_score,
        confidence,
        detections
    )

    timeline = build_timeline(timeline_events)

    identity = build_identity_details(
        account_details,
        source_details
    )

    evidence = build_detection_evidence(
        detection_evidence
    )

    threat_findings = build_threat_intelligence(
        threat_intelligence
    )

    risk_breakdown = build_risk_breakdown(
        threat_score,
        behavior_score,
        impact_score,
        correlation_score
    )

    confidence_details = build_confidence_details(
        confidence,
        successful_sources,
        failed_sources,
        strong_behavior_signals,
        missing_fields
    )

    recommended_actions = build_recommended_actions(
        severity
    )

    actions_taken = build_actions_taken(
        action_records
    )

    unverified = build_unverified_findings(
        unverified_items
    )

    mitre_mapping = build_mitre_mapping()

    technical_appendix = build_technical_appendix(
        event_ids,
        log_sources,
        enrichment_sources,
        pipeline_version,
        dry_run,
        environment
    )

    report = {
        "executive_summary": summary,
        "user": user,
        "source_ip": source_ip,
        "severity": severity,
        "risk_score": risk_score,
        "confidence": confidence,
        "detections": detections,
        "timeline": timeline,
        "identity": identity,
        "detection_evidence": evidence,
        "threat_intelligence": threat_findings,
        "risk_breakdown": risk_breakdown,
        "confidence_details": confidence_details,
        "recommended_actions": recommended_actions,
        "actions_taken": actions_taken,
        "could_not_verify": unverified,
        "mitre_attack": mitre_mapping,
        "technical_appendix": technical_appendix
    }

    return report
