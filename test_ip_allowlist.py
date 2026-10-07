from response.ip_allowlist import check_ip_response_safety


test_ips = [
    "10.0.0.10",
    "185.220.101.45"
]


print("IP Allowlist Safety Test")
print("========================")

for ip_address in test_ips:
    result = check_ip_response_safety(ip_address)

    print()
    print("IP:", ip_address)
    print("Response Allowed:", result["allowed"])
    print("Reason:", result["reason"])
