from response.rollback import get_rollback_action


test_actions = [
    "BLOCK_IP",
    "DISABLE_ACCOUNT",
    "REVOKE_ACTIVE_SESSIONS",
    "DELETE_USER_ACCOUNT"
]


print("Response Rollback Test")
print("======================")

for action in test_actions:
    result = get_rollback_action(action)

    print()
    print("Original Action:", result["action"])
    print("Rollback Supported:", result["supported"])
    print("Rollback Action:", result["rollback_action"])
    print("Reason:", result["reason"])
