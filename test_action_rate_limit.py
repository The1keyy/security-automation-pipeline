from response.action_rate_limit import can_execute_action, record_action


print("Action Rate-Limit Test")
print("======================")

for attempt in range(1, 5):
    result = can_execute_action()

    print()
    print("Attempt:", attempt)
    print("Allowed:", result["allowed"])
    print("Actions in window:", result["actions_in_window"])
    print("Maximum actions:", result["max_actions"])
    print("Reason:", result["reason"])

    if result["allowed"]:
        record_action()
