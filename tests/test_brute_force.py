from detections.brute_force import detect_brute_force


def was_detected(result):
    if isinstance(result, tuple):
        return result[0]

    return result


def test_brute_force_detection():
    events = [
        {
            "timestamp": "2026-10-08T14:00:00Z",
            "user": "jsmith@company.com",
            "source_ip": "198.51.100.25",
            "auth_result": "failure"
        },
        {
            "timestamp": "2026-10-08T14:00:20Z",
            "user": "jsmith@company.com",
            "source_ip": "198.51.100.25",
            "auth_result": "failure"
        },
        {
            "timestamp": "2026-10-08T14:00:40Z",
            "user": "jsmith@company.com",
            "source_ip": "198.51.100.25",
            "auth_result": "failure"
        },
        {
            "timestamp": "2026-10-08T14:01:00Z",
            "user": "jsmith@company.com",
            "source_ip": "198.51.100.25",
            "auth_result": "failure"
        },
        {
            "timestamp": "2026-10-08T14:01:20Z",
            "user": "jsmith@company.com",
            "source_ip": "198.51.100.25",
            "auth_result": "failure"
        }
    ]

    result = detect_brute_force(events)

    assert was_detected(result) is True
