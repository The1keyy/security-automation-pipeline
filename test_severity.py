from risk.severity import classify_severity


test_scores = [
    20,
    50,
    70,
    87
]


print("Risk Severity Classification")
print("============================")

for score in test_scores:
    severity = classify_severity(score)

    print(
        str(score) + "/90",
        "->",
        severity
    )
