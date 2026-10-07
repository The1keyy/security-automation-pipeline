def choose_response(severity):
    severity = severity.upper()

    if severity == "LOW":
        return {
            "action": "LOG_ONLY",
            "requires_approval": False,
            "automatic": True,
            "message": "Log the event and continue monitoring."
        }

    if severity == "MEDIUM":
        return {
            "action": "RECOMMEND_INVESTIGATION",
            "requires_approval": False,
            "automatic": False,
            "message": "Recommend analyst investigation."
        }

    if severity == "HIGH":
        return {
            "action": "REQUEST_APPROVAL",
            "requires_approval": True,
            "automatic": False,
            "message": "Human approval is required before containment."
        }

    if severity == "CRITICAL":
        return {
            "action": "PREAPPROVED_PLAYBOOK_ONLY",
            "requires_approval": True,
            "automatic": False,
            "message": "Only a pre-approved response playbook may be executed."
        }

    return {
        "action": "NO_ACTION",
        "requires_approval": False,
        "automatic": False,
        "message": "Unknown severity. No response selected."
    }
