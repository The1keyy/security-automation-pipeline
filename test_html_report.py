from test_text_report import report
from reports.html_report import generate_html_report


output_file = "reports/incident_report.html"


generate_html_report(
    report,
    output_file
)


print()
print("HTML Report Generation Test")
print("===========================")
print("STATUS: HTML report generated successfully")
print("File:", output_file)
print("Severity:", report["severity"])
print("Risk Score:", str(report["risk_score"]) + "/90")
print("Confidence:", str(report["confidence"]) + "/10")
