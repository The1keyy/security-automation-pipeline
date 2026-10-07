from response.decision_engine import choose_response


severities = [
    "LOW",
    "MEDIUM",
    "HIGH",
    "CRITICAL"
]


print("Safe Response Decision Engine")
print("=============================")

for severity in severities:
    result = choose_response(severity)

    print()
    print("Severity:", severity)
    print("Action:", result["action"])
    print("Requires Approval:", result["requires_approval"])
    print("Automatic:", result["automatic"])
    print("Message:", result["message"])
