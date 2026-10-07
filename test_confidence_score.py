from risk.confidence_score import calculate_confidence_score


evidence = {
    "successful_sources": 6,
    "failed_sources": 0,
    "strong_behavior_signals": 4,
    "missing_fields": 0
}


result = calculate_confidence_score(evidence)


print("Confidence Score")
print("================")

for reason in result["reasons"]:
    print(reason)

print()

print(
    "Confidence:",
    str(result["score"]) + "/" + str(result["max_score"])
)

