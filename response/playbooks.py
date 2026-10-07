PREAPPROVED_PLAYBOOKS = {
    "BLOCK_MALICIOUS_IP": {
        "description": "Block a confirmed malicious IP address",
        "allowed": True
    },

    "DISABLE_COMPROMISED_ACCOUNT": {
        "description": "Disable a confirmed compromised user account",
        "allowed": True
    },

    "REVOKE_ACTIVE_SESSIONS": {
        "description": "Revoke active sessions for a compromised account",
        "allowed": True
    }
}


def check_playbook(playbook_name):
    playbook = PREAPPROVED_PLAYBOOKS.get(playbook_name)

    if playbook is None:
        return {
            "approved": False,
            "playbook": playbook_name,
            "reason": "Playbook is not pre-approved"
        }

    if not playbook["allowed"]:
        return {
            "approved": False,
            "playbook": playbook_name,
            "reason": "Playbook exists but is currently disabled"
        }

    return {
        "approved": True,
        "playbook": playbook_name,
        "description": playbook["description"],
        "reason": "Playbook is pre-approved"
    }
