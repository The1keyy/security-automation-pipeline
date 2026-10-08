from detections.success_after_failure import detect_success_after_failure
from detections.brute_force import detect_brute_force
from detections.password_spray import detect_password_spray


def was_detected(result):
    if isinstance(result, tuple):
        return result[0]

    return result


def test_benign_and_malicious_scenarios():
    benign_events = [
        {
            "timestamp": "2026-10-08T14:00:00Z",
            "user": "jsmith@company.com",
            "source_ip": "203.0.113.10",
            "auth_result": "success"
        }
    ]

    malicious_events = [
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
        },
        {
            "timestamp": "2026-10-08T14:01:40Z",
            "user": "jsmith@company.com",
            "source_ip": "198.51.100.25",
            "auth_result": "success"
        }
    ]

    benign_success_after_failure = was_detected(
        detect_success_after_failure(benign_events)
    )

    benign_brute_force = was_detected(
        detect_brute_force(benign_events)
    )

    benign_password_spray = was_detected(
        detect_password_spray(benign_events)
    )

    malicious_success_after_failure = was_detected(
        detect_success_after_failure(malicious_events)
    )

    malicious_brute_force = was_detected(
        detect_brute_force(malicious_events)
    )

    assert benign_success_after_failure is False
    assert benign_brute_force is False
    assert benign_password_spray is False

    assert malicious_success_after_failure is True
    assert malicious_brute_force is True
