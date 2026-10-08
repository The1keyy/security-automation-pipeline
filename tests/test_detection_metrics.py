from detections.success_after_failure import detect_success_after_failure
from detections.brute_force import detect_brute_force
from detections.password_spray import detect_password_spray


def was_detected(result):
    if isinstance(result, tuple):
        return result[0]

    return result


def classify_scenario(events):
    detections = [
        was_detected(
            detect_success_after_failure(events)
        ),
        was_detected(
            detect_brute_force(events)
        ),
        was_detected(
            detect_password_spray(events)
        )
    ]

    return any(detections)


def test_detection_metrics():
    scenarios = [
        {
            "name": "Normal login",
            "expected_malicious": False,
            "events": [
                {
                    "timestamp": "2026-10-08T14:00:00Z",
                    "user": "jsmith@company.com",
                    "source_ip": "203.0.113.10",
                    "auth_result": "success"
                }
            ]
        },

        {
            "name": "Normal failed login",
            "expected_malicious": False,
            "events": [
                {
                    "timestamp": "2026-10-08T14:00:00Z",
                    "user": "alice@company.com",
                    "source_ip": "203.0.113.20",
                    "auth_result": "failure"
                }
            ]
        },

        {
            "name": "Brute force",
            "expected_malicious": True,
            "events": [
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
        },

        {
            "name": "Success after failure",
            "expected_malicious": True,
            "events": [
                {
                    "timestamp": "2026-10-08T14:00:00Z",
                    "user": "admin@company.com",
                    "source_ip": "198.51.100.90",
                    "auth_result": "failure"
                },
                {
                    "timestamp": "2026-10-08T14:00:20Z",
                    "user": "admin@company.com",
                    "source_ip": "198.51.100.90",
                    "auth_result": "failure"
                },
                {
                    "timestamp": "2026-10-08T14:00:40Z",
                    "user": "admin@company.com",
                    "source_ip": "198.51.100.90",
                    "auth_result": "failure"
                },
                {
                    "timestamp": "2026-10-08T14:01:00Z",
                    "user": "admin@company.com",
                    "source_ip": "198.51.100.90",
                    "auth_result": "success"
                }
            ]
        },

        {
            "name": "Password spray",
            "expected_malicious": True,
            "events": [
                {
                    "timestamp": "2026-10-08T14:00:00Z",
                    "user": "alice@company.com",
                    "source_ip": "198.51.100.50",
                    "auth_result": "failure"
                },
                {
                    "timestamp": "2026-10-08T14:00:10Z",
                    "user": "bob@company.com",
                    "source_ip": "198.51.100.50",
                    "auth_result": "failure"
                },
                {
                    "timestamp": "2026-10-08T14:00:20Z",
                    "user": "carol@company.com",
                    "source_ip": "198.51.100.50",
                    "auth_result": "failure"
                },
                {
                    "timestamp": "2026-10-08T14:00:30Z",
                    "user": "dave@company.com",
                    "source_ip": "198.51.100.50",
                    "auth_result": "failure"
                },
                {
                    "timestamp": "2026-10-08T14:00:40Z",
                    "user": "erin@company.com",
                    "source_ip": "198.51.100.50",
                    "auth_result": "failure"
                }
            ]
        }
    ]

    true_positive = 0
    true_negative = 0
    false_positive = 0
    false_negative = 0

    for scenario in scenarios:
        predicted_malicious = classify_scenario(
            scenario["events"]
        )

        expected_malicious = scenario[
            "expected_malicious"
        ]

        if predicted_malicious and expected_malicious:
            true_positive += 1

        elif not predicted_malicious and not expected_malicious:
            true_negative += 1

        elif predicted_malicious and not expected_malicious:
            false_positive += 1

        elif not predicted_malicious and expected_malicious:
            false_negative += 1

    precision = true_positive / (
        true_positive + false_positive
    )

    recall = true_positive / (
        true_positive + false_negative
    )

    false_positive_rate = false_positive / (
        false_positive + true_negative
    )

    print()
    print("Detection Quality Metrics")
    print("=========================")
    print("True Positives:", true_positive)
    print("True Negatives:", true_negative)
    print("False Positives:", false_positive)
    print("False Negatives:", false_negative)
    print()
    print("Precision:", round(precision, 2))
    print("Recall:", round(recall, 2))
    print(
        "False Positive Rate:",
        round(false_positive_rate, 2)
    )

    assert precision == 1.0
    assert recall == 1.0
    assert false_positive_rate == 0.0
