from risk.correlation_score import calculate_correlation_score


signals = {
    "success_after_failure": True,
    "new_country": True,
    "impossible_travel": True,
    "tor_exit_node": True,
    "mfa_fatigue": True,
    "suspicious_post_login": True,
    "new_device": True,
    "password_spray": False,
    "credential_stuffing": False
}


result = calculate_correlation_score(signals)


print("Signal Correlation Score")
print("========================")

for reason in result["reasons"]:
    print(reason)

print()

print(
    "Correlation Score:",
    str(result["score"]) + "/" + str(result["max_score"])
)
