result = {
    "success": True,
    "ip": "185.220.101.45",
    "country": "DE",
    "city": None,
    "asn": None,
    "reputation": None
}

print("Missing-Data Handling Test")
print("--------------------------")

print("IP:", result.get("ip") or "Unknown")
print("Country:", result.get("country") or "Unknown")
print("City:", result.get("city") or "Unknown")
print("ASN:", result.get("asn") or "Unknown")
print("Reputation:", result.get("reputation") or "Unknown")

missing_fields = []

for field in ["city", "asn", "reputation"]:
    if result.get(field) is None:
        missing_fields.append(field)

if missing_fields:
    print("Missing fields:", ", ".join(missing_fields))
    print("STATUS: Partial enrichment result handled safely")
else:
    print("STATUS: Complete enrichment result")
