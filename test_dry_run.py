from response.dry_run import execute_response


action = "BLOCK_IP"
target = "185.220.101.45"


result = execute_response(
    action,
    target,
    dry_run=True
)


print("Safe Response Dry-Run Test")
print("==========================")

print("Action:", result["action"])
print("Target:", result["target"])
print("Dry Run:", result["dry_run"])
print("Executed:", result["executed"])
print("Message:", result["message"])
