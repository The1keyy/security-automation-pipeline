from response.user_allowlist import check_user_response_safety


test_users = [
    "ceo@company.com",
    "jsmith@company.com"
]


print("User Allowlist Safety Test")
print("==========================")

for username in test_users:
    result = check_user_response_safety(username)

    print()
    print("User:", username)
    print("Response Allowed:", result["allowed"])
    print("Reason:", result["reason"])
