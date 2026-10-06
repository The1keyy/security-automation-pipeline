REQUIRED_FIELDS = [
    "timestamp",
    "user",
    "source_ip",
    "country",
    "auth_result",
    "source"
]


def validate_event(event):
    missing_fields = []

    for field in REQUIRED_FIELDS:
        if field not in event:
            missing_fields.append(field)

    if missing_fields:
        return False, missing_fields

    return True, []
