from html import escape


def safe(value):
    return escape(str(value))


def generate_html_report(report, output_file):
    timeline_html = ""

    for item in report["timeline"]:
        timeline_html += (
            "<li>"
            "<strong>"
            + safe(item["timestamp"])
            + "</strong> - "
            + safe(item["event"])
            + "</li>"
        )

    detection_html = ""

    for item in report["detection_evidence"]:
        detection_html += (
            "<div class='card'>"
            "<strong>"
            + safe(item["detection"])
            + "</strong>"
            "<p>"
            + safe(item["evidence"])
            + "</p>"
            "</div>"
        )

    threat_html = ""

    for item in report["threat_intelligence"]:
        threat_html += (
            "<div class='card'>"
            "<strong>"
            + safe(item["provider"])
            + "</strong>"
            "<p>"
            + safe(item["finding"])
            + "</p>"
            "</div>"
        )

    confidence_reasons = ""

    for reason in report["confidence_details"]["reasons"]:
        confidence_reasons += (
            "<li>"
            + safe(reason)
            + "</li>"
        )

    recommended_actions = ""

    for action in report["recommended_actions"]["recommendations"]:
        recommended_actions += (
            "<li>"
            + safe(action)
            + "</li>"
        )

    actions_taken = ""

    for action in report["actions_taken"]:
        actions_taken += (
            "<div class='card'>"
            "<strong>"
            + safe(action["action"])
            + "</strong>"
            "<p>Target: "
            + safe(action["target"])
            + "</p>"
            "<p>Approved: "
            + safe(action["approved"])
            + "</p>"
            "<p>Executed: "
            + safe(action["executed"])
            + "</p>"
            "<p>Dry Run: "
            + safe(action["dry_run"])
            + "</p>"
            "<p>Status: "
            + safe(action["status"])
            + "</p>"
            "</div>"
        )

    unverified_html = ""

    for item in report["could_not_verify"]:
        unverified_html += (
            "<li>"
            "<strong>"
            + safe(item["item"])
            + ":</strong> "
            + safe(item["reason"])
            + "</li>"
        )

    mitre_html = ""

    for technique in report["mitre_attack"]:
        mitre_html += (
            "<div class='card'>"
            "<strong>"
            + safe(technique["technique_id"])
            + " - "
            + safe(technique["technique"])
            + "</strong>"
            "<p>"
            + safe(technique["evidence"])
            + "</p>"
            "</div>"
        )

    appendix = report["technical_appendix"]

    event_ids = ""

    for event_id in appendix["event_ids"]:
        event_ids += "<li>" + safe(event_id) + "</li>"

    log_sources = ""

    for source in appendix["log_sources"]:
        log_sources += "<li>" + safe(source) + "</li>"

    enrichment_sources = ""

    for source in appendix["enrichment_sources"]:
        enrichment_sources += "<li>" + safe(source) + "</li>"

    account = report["identity"]["account"]
    source = report["identity"]["source"]
    risk = report["risk_breakdown"]
    confidence = report["confidence_details"]
    response = report["recommended_actions"]

    html = """
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">

    <meta
        name="viewport"
        content="width=device-width, initial-scale=1.0"
    >

    <title>Security Incident Report</title>

    <style>
        body {
            font-family: Arial, sans-serif;
            background: #f4f6f8;
            margin: 0;
            padding: 0;
            color: #1f2937;
        }

        .container {
            width: 90%;
            max-width: 1100px;
            margin: 30px auto;
        }

        header {
            background: #111827;
            color: white;
            padding: 30px;
            border-radius: 10px;
            margin-bottom: 20px;
        }

        header h1 {
            margin-top: 0;
        }

        .severity {
            display: inline-block;
            background: #991b1b;
            color: white;
            padding: 8px 14px;
            border-radius: 6px;
            font-weight: bold;
        }

        section {
            background: white;
            padding: 25px;
            margin-bottom: 20px;
            border-radius: 10px;
            box-shadow: 0 2px 5px rgba(0, 0, 0, 0.08);
        }

        h2 {
            border-bottom: 2px solid #e5e7eb;
            padding-bottom: 10px;
        }

        .grid {
            display: grid;
            grid-template-columns: repeat(
                auto-fit,
                minmax(200px, 1fr)
            );
            gap: 15px;
        }

        .metric {
            background: #f9fafb;
            padding: 15px;
            border-radius: 8px;
        }

        .metric strong {
            display: block;
            margin-bottom: 6px;
        }

        .card {
            background: #f9fafb;
            border-left: 4px solid #374151;
            padding: 15px;
            margin-bottom: 12px;
            border-radius: 5px;
        }

        .warning {
            border-left-color: #b45309;
        }

        .critical {
            border-left-color: #991b1b;
        }

        ul {
            line-height: 1.7;
        }

        footer {
            text-align: center;
            padding: 20px;
            color: #6b7280;
        }
    </style>
</head>

<body>

<div class="container">

<header>
    <h1>Security Incident Report</h1>

    <p>
        Automated Security Analysis and Response Pipeline
    </p>

    <span class="severity">
        """ + safe(report["severity"]) + """
    </span>
</header>


<section>
    <h2>Executive Summary</h2>

    <p>
        """ + safe(report["executive_summary"]) + """
    </p>
</section>


<section>
    <h2>Incident Overview</h2>

    <div class="grid">

        <div class="metric">
            <strong>User</strong>
            """ + safe(report["user"]) + """
        </div>

        <div class="metric">
            <strong>Source IP</strong>
            """ + safe(report["source_ip"]) + """
        </div>

        <div class="metric">
            <strong>Risk Score</strong>
            """ + safe(report["risk_score"]) + """/90
        </div>

        <div class="metric">
            <strong>Confidence</strong>
            """ + safe(report["confidence"]) + """/10
        </div>

    </div>
</section>


<section>
    <h2>Incident Timeline</h2>

    <ul>
        """ + timeline_html + """
    </ul>
</section>


<section>
    <h2>Account Details</h2>

    <div class="grid">

        <div class="metric">
            <strong>Username</strong>
            """ + safe(account["username"]) + """
        </div>

        <div class="metric">
            <strong>Account Type</strong>
            """ + safe(account["account_type"]) + """
        </div>

        <div class="metric">
            <strong>Department</strong>
            """ + safe(account["department"]) + """
        </div>

        <div class="metric">
            <strong>Status</strong>
            """ + safe(account["status"]) + """
        </div>

    </div>
</section>


<section>
    <h2>Source Details</h2>

    <div class="grid">

        <div class="metric">
            <strong>IP Address</strong>
            """ + safe(source["ip"]) + """
        </div>

        <div class="metric">
            <strong>Country</strong>
            """ + safe(source["country"]) + """
        </div>

        <div class="metric">
            <strong>City</strong>
            """ + safe(source["city"]) + """
        </div>

        <div class="metric">
            <strong>ASN</strong>
            """ + safe(source["asn"]) + """
        </div>

        <div class="metric">
            <strong>Tor Exit Node</strong>
            """ + safe(source["tor_exit"]) + """
        </div>

    </div>
</section>


<section>
    <h2>Detection Evidence</h2>

    """ + detection_html + """
</section>


<section>
    <h2>Threat Intelligence</h2>

    """ + threat_html + """
</section>


<section>
    <h2>Risk Score Breakdown</h2>

    <div class="grid">

        <div class="metric">
            <strong>Threat Intelligence</strong>
            """ + safe(risk["threat_intelligence"]["score"]) + """/30
        </div>

        <div class="metric">
            <strong>Behavior</strong>
            """ + safe(risk["behavior"]["score"]) + """/30
        </div>

        <div class="metric">
            <strong>Impact</strong>
            """ + safe(risk["impact"]["score"]) + """/20
        </div>

        <div class="metric">
            <strong>Correlation</strong>
            """ + safe(risk["correlation"]["score"]) + """/10
        </div>

        <div class="metric">
            <strong>Final Risk</strong>
            """ + safe(risk["total"]) + """/90
        </div>

    </div>
</section>


<section>
    <h2>Confidence Analysis</h2>

    <p>
        <strong>Confidence Score:</strong>
        """ + safe(confidence["score"]) + """/10
    </p>

    <ul>
        """ + confidence_reasons + """
    </ul>
</section>


<section>
    <h2>Recommended Response</h2>

    <p>
        <strong>Response Action:</strong>
        """ + safe(response["response_action"]) + """
    </p>

    <p>
        <strong>Requires Approval:</strong>
        """ + safe(response["requires_approval"]) + """
    </p>

    <p>
        <strong>Automatic:</strong>
        """ + safe(response["automatic"]) + """
    </p>

    <ul>
        """ + recommended_actions + """
    </ul>
</section>


<section>
    <h2>Actions Taken</h2>

    """ + actions_taken + """
</section>


<section>
    <h2>Could Not Verify</h2>

    <ul>
        """ + unverified_html + """
    </ul>
</section>


<section>
    <h2>MITRE ATT&CK Mapping</h2>

    """ + mitre_html + """
</section>


<section>
    <h2>Technical Appendix</h2>

    <p>
        <strong>Pipeline Version:</strong>
        """ + safe(appendix["pipeline_version"]) + """
    </p>

    <p>
        <strong>Environment:</strong>
        """ + safe(appendix["environment"]) + """
    </p>

    <p>
        <strong>Dry Run:</strong>
        """ + safe(appendix["dry_run"]) + """
    </p>

    <h3>Event IDs</h3>

    <ul>
        """ + event_ids + """
    </ul>

    <h3>Log Sources</h3>

    <ul>
        """ + log_sources + """
    </ul>

    <h3>Enrichment Sources</h3>

    <ul>
        """ + enrichment_sources + """
    </ul>
</section>


<footer>
    Generated by Security Automation Pipeline
</footer>

</div>

</body>
</html>
"""

    with open(output_file, "w") as file:
        file.write(html)

    return html
