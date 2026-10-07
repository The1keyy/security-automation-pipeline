import time


ACTION_HISTORY = []
MAX_ACTIONS = 3
WINDOW_SECONDS = 60


def cleanup_history():
    current_time = time.time()

    active_actions = []

    for timestamp in ACTION_HISTORY:
        if current_time - timestamp <= WINDOW_SECONDS:
            active_actions.append(timestamp)

    ACTION_HISTORY.clear()
    ACTION_HISTORY.extend(active_actions)


def can_execute_action():
    cleanup_history()

    if len(ACTION_HISTORY) >= MAX_ACTIONS:
        return {
            "allowed": False,
            "reason": "Action rate limit reached",
            "actions_in_window": len(ACTION_HISTORY),
            "max_actions": MAX_ACTIONS
        }

    return {
        "allowed": True,
        "reason": "Action is within the allowed rate limit",
        "actions_in_window": len(ACTION_HISTORY),
        "max_actions": MAX_ACTIONS
    }


def record_action():
    ACTION_HISTORY.append(time.time())
