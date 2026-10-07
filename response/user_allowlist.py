PROTECTED_USERS = [
    "ceo@company.com",
    "security-admin@company.com",
    "breakglass@company.com"
]


def is_user_protected(username):
    if username in PROTECTED_USERS:
        return True

    return False


def check_user_response_safety(username):
    if is_user_protected(username):
        return {
            "allowed": False,
            "reason": "User is on the protected account allowlist"
        }

    return {
        "allowed": True,
        "reason": "User is not on the protected account allowlist"
    }
