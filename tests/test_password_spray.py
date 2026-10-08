from detections.password_spray import detect_password_spray


def was_detected(result):
    if isinstance(result, tuple):
        return result[0]

    return result


def test_password_spray_detection():
    events = [
        {
            "timestamp": "2026-10-08T14:00:00Z",
            "user": "alice@company.com",
            "source_ip": "198.51.100.50",
            "auth_result": "failure"
        },
        {
            "timestamp": "2026-10-08T14:00:15Z",
            "user": "bob@company.com",
            "source_ip": "198.51.100.50",
            "auth_result": "failure"
        },
        {
            "timestamp": "2026-10-08T14:00:30Z",
            "user": "carol@company.com",
            "source_ip": "198.51.100.50",
            "auth_result": "failure"
        },
        {
            "timestamp": "2026-10-08T14:00:45Z",
            "user": "dave@company.com",
            "source_ip": "198.51.100.50",
            "auth_result": "failure"
        },
        {
            "timestamp": "2026-10-08T14:01:00Z",
            "user": "erin@company.com",
            "source_ip": "198.51.100.50",
            "auth_result": "failure"
        }
    ]

    result = detect_password_spray(events)

    assert was_detected(result) is True
