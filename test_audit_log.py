import json

from response.audit_log import write_audit_log


entry = write_audit_log(
    action="BLOCK_IP",
    target="185.220.101.45",
    severity="HIGH",
    approved=True,
    executed=False,
    reason="Analyst approved action, but system is still in dry-run mode"
)


print("Audit Logging Test")
print("==================")

print("Timestamp:", entry["timestamp"])
print("Action:", entry["action"])
print("Target:", entry["target"])
print("Severity:", entry["severity"])
print("Approved:", entry["approved"])
print("Executed:", entry["executed"])
print("Reason:", entry["reason"])

print()
print("Audit record written successfully.")
