from risk.behavior_score import calculate_behavior_score


signals = {
    "impossible_travel": True,
    "success_after_failure": True,
    "brute_force": False,
    "password_spray": False,
    "credential_stuffing": False,
    "mfa_fatigue": True,
    "suspicious_post_login": True,
    "new_country": True,
    "new_device": True,
    "new_user_agent": False,
    "abnormal_login_time": True
}


result = calculate_behavior_score(signals)


print("Behavioral Evidence Risk Score")
print("==============================")

for reason in result["reasons"]:
    print(reason)

print()

print(
    "Behavioral Evidence Score:",
    str(result["score"]) + "/" + str(result["max_score"])
)
