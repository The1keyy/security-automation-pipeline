ROLLBACK_ACTIONS = {
    "BLOCK_IP": "UNBLOCK_IP",
    "DISABLE_ACCOUNT": "ENABLE_ACCOUNT",
    "REVOKE_ACTIVE_SESSIONS": "NO_ROLLBACK",
    "ADD_IP_TO_DENYLIST": "REMOVE_IP_FROM_DENYLIST"
}


def get_rollback_action(action):
    rollback = ROLLBACK_ACTIONS.get(action)

    if rollback is None:
        return {
            "supported": False,
            "action": action,
            "rollback_action": None,
            "reason": "No rollback mapping exists for this action"
        }

    if rollback == "NO_ROLLBACK":
        return {
            "supported": False,
            "action": action,
            "rollback_action": None,
            "reason": "This action cannot be automatically reversed"
        }

    return {
        "supported": True,
        "action": action,
        "rollback_action": rollback,
        "reason": "Rollback action is available"
    }
