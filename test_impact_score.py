from risk.impact_score import calculate_impact_score


context = {
    "account_type": "privileged",
    "asset_criticality": "critical",
    "sensitive_system": True
}


result = calculate_impact_score(context)


print("User / Asset Impact Score")
print("=========================")

for reason in result["reasons"]:
    print(reason)

print()
