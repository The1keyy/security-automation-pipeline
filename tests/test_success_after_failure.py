from detections.success_after_failure import detect_success_after_failure


def was_detected(result):
    if isinstance(result, tuple):
        return result[0]

    return result


def test_success_after_failure_detection():
    events = [
        {
            "timestamp": "2026-10-08T14:00:00Z",
            "user": "jsmith@company.com",
            "source_ip": "198.51.100.90",
            "auth_result": "failure"
        },
        {
            "timestamp": "2026-10-08T14:00:20Z",
            "user": "jsmith@company.com",
            "source_ip": "198.51.100.90",
            "auth_result": "failure"
        },
        {
            "timestamp": "2026-10-08T14:00:40Z",
            "user": "jsmith@company.com",
            "source_ip": "198.51.100.90",
            "auth_result": "failure"
        },
        {
            "timestamp": "2026-10-08T14:01:00Z",
            "user": "jsmith@company.com",
            "source_ip": "198.51.100.90",
            "auth_result": "success"
        }
    ]

    result = detect_success_after_failure(events)

    assert was_detected(result) is True
