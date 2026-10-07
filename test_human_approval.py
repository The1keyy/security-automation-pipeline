from response.approval import request_approval


action = "BLOCK_IP"
target = "185.220.101.45"


result = request_approval(
    action,
    target
)


print()
print("Approval Result")
print("===============")
print("Decision:", result["decision"])
print("Approved:", result["approved"])
print("Message:", result["message"])
