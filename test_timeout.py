result = {
    "success": False,
    "timeout": True,
    "error": "API request timed out"
}

print("Timeout Handling Test")
print("---------------------")

if result.get("timeout"):
    print("TIMEOUT HANDLED")
    print("Message:", result["error"])
