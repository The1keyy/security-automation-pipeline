result = {
    "success": False,
    "rate_limited": True,
    "error": "API rate limit reached",
    "retry_after": "60 seconds"
}

print("Rate-Limit Handling Test")
print("------------------------")

if result.get("rate_limited"):
    print("RATE LIMITED")
    print("Message:", result["error"])
    print("Retry After:", result["retry_after"])
