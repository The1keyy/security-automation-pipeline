def request_approval(action, target):
    print("Human Approval Required")
    print("=======================")
    print("Action:", action)
    print("Target:", target)
    print()

    decision = input("Approve action? (yes/no): ").strip().lower()

    if decision == "yes":
        return {
            "approved": True,
            "decision": "APPROVED",
            "message": "Analyst approved the response action."
        }

    return {
        "approved": False,
        "decision": "DENIED",
        "message": "Analyst denied the response action."
    }
