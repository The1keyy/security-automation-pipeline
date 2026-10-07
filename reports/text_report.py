def generate_text_report(report, output_file):
    lines = []

    lines.append("SECURITY INCIDENT REPORT")
    lines.append("=" * 24)
    lines.append("")

    lines.append("Executive Summary")
    lines.append("-----------------")
    lines.append(report["executive_summary"])
    lines.append("")

    lines.append("Incident Details")
    lines.append("----------------")
    lines.append("User: " + report["user"])
    lines.append("Source IP: " + report["source_ip"])
    lines.append("Severity: " + report["severity"])
    lines.append(
        "Risk Score: "
        + str(report["risk_score"])
        + "/90"
    )
    lines.append(
        "Confidence: "
        + str(report["confidence"])
        + "/10"
    )
    lines.append("")

    lines.append("Incident Timeline")
    lines.append("-----------------")

    for item in report["timeline"]:
        lines.append(
            item["timestamp"]
            + " - "
            + item["event"]
        )

    lines.append("")

    lines.append("Account Details")
    lines.append("---------------")

    account = report["identity"]["account"]

    lines.append("Username: " + account["username"])
    lines.append("Account Type: " + account["account_type"])
    lines.append("Department: " + account["department"])
    lines.append("Status: " + account["status"])
    lines.append("Normal Country: " + account["normal_country"])
    lines.append("")

    lines.append("Source Details")
    lines.append("--------------")

    source = report["identity"]["source"]

    lines.append("IP: " + source["ip"])
    lines.append("Country: " + source["country"])
    lines.append("City: " + source["city"])
    lines.append("ASN: " + source["asn"])
    lines.append("Tor Exit Node: " + str(source["tor_exit"]))
    lines.append("")

    lines.append("Detection Evidence")
    lines.append("------------------")

    for item in report["detection_evidence"]:
        lines.append(
            "- "
            + item["detection"]
            + ": "
            + item["evidence"]
        )

    lines.append("")

    lines.append("Threat Intelligence")
    lines.append("-------------------")

    for item in report["threat_intelligence"]:
        lines.append(
            "- "
            + item["provider"]
            + ": "
            + item["finding"]
        )

    lines.append("")

    lines.append("Risk Score Breakdown")
    lines.append("--------------------")

    risk = report["risk_breakdown"]

    lines.append(
        "Threat Intelligence: "
        + str(risk["threat_intelligence"]["score"])
        + "/30"
    )

    lines.append(
        "Behavior: "
        + str(risk["behavior"]["score"])
        + "/30"
    )

    lines.append(
        "Impact: "
        + str(risk["impact"]["score"])
        + "/20"
    )

    lines.append(
        "Correlation: "
        + str(risk["correlation"]["score"])
        + "/10"
    )

    lines.append(
        "Final Risk Score: "
        + str(risk["total"])
        + "/90"
    )

    lines.append("")

    lines.append("Confidence Analysis")
    lines.append("-------------------")

    confidence = report["confidence_details"]

    lines.append(
        "Confidence Score: "
        + str(confidence["score"])
        + "/10"
    )

    for reason in confidence["reasons"]:
        lines.append("- " + reason)

    lines.append("")

    lines.append("Recommended Actions")
    lines.append("-------------------")

    response = report["recommended_actions"]

    lines.append(
        "Response Action: "
        + response["response_action"]
    )

    lines.append(
        "Requires Approval: "
        + str(response["requires_approval"])
    )

    lines.append(
        "Automatic: "
        + str(response["automatic"])
    )

    for action in response["recommendations"]:
        lines.append("- " + action)

    lines.append("")

    lines.append("Actions Taken")
    lines.append("-------------")

    for action in report["actions_taken"]:
        lines.append(
            "- "
            + action["action"]
            + " | Target: "
            + action["target"]
            + " | Approved: "
            + str(action["approved"])
            + " | Executed: "
            + str(action["executed"])
            + " | Dry Run: "
            + str(action["dry_run"])
        )

        lines.append(
            "  Status: "
            + action["status"]
        )

    lines.append("")

    lines.append("Could Not Verify")
    lines.append("----------------")

    for item in report["could_not_verify"]:
        lines.append(
            "- "
            + item["item"]
            + ": "
            + item["reason"]
        )

    lines.append("")

    lines.append("MITRE ATT&CK Mapping")
    lines.append("--------------------")

    for technique in report["mitre_attack"]:
        lines.append(
            "- "
            + technique["technique_id"]
            + " - "
            + technique["technique"]
        )

        lines.append(
            "  Evidence: "
            + technique["evidence"]
        )

    lines.append("")

    lines.append("Technical Appendix")
    lines.append("------------------")

    appendix = report["technical_appendix"]

    lines.append(
        "Pipeline Version: "
        + appendix["pipeline_version"]
    )

    lines.append(
        "Environment: "
        + appendix["environment"]
    )

    lines.append(
        "Dry Run: "
        + str(appendix["dry_run"])
    )

    lines.append("")

    lines.append("Event IDs")

    for event_id in appendix["event_ids"]:
        lines.append("- " + event_id)

    lines.append("")

    lines.append("Log Sources")

    for source_name in appendix["log_sources"]:
        lines.append("- " + source_name)

    lines.append("")

    lines.append("Enrichment Sources")

    for source_name in appendix["enrichment_sources"]:
        lines.append("- " + source_name)

    report_text = "\n".join(lines)

    with open(output_file, "w") as file:
        file.write(report_text)

    return report_text
