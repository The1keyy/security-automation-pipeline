import json
from datetime import datetime, timezone


AUDIT_FILE = "response/audit_log.jsonl"


def write_audit_log(
    action,
    target,
    severity,
    approved,
    executed,
    reason
):
    entry = {
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "action": action,
        "target": target,
        "severity": severity,
        "approved": approved,
        "executed": executed,
        "reason": reason
    }

    with open(AUDIT_FILE, "a") as file:
        file.write(json.dumps(entry) + "\n")

    return entry
