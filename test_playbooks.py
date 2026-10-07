from response.playbooks import check_playbook


test_playbooks = [
    "BLOCK_MALICIOUS_IP",
    "DELETE_USER_ACCOUNT"
]


print("Critical Response Playbook Test")
print("===============================")

for playbook_name in test_playbooks:
    result = check_playbook(playbook_name)

    print()
    print("Playbook:", playbook_name)
    print("Approved:", result["approved"])
    print("Reason:", result["reason"])

    if result["approved"]:
        print("Description:", result["description"])
