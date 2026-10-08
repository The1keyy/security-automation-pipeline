from detections.tor_authentication import detect_tor_authentication


def was_detected(result):
    if isinstance(result, tuple):
        return result[0]

    return result


def test_tor_login_detection():
    event = {
        "timestamp": "2026-10-08T14:00:00Z",
        "user": "jsmith@company.com",
        "source_ip": "185.220.101.45",
        "country": "DE",
        "auth_result": "success"
    }

    tor_exit_nodes = [
        "185.220.101.45",
        "185.220.101.46"
    ]

    result = detect_tor_authentication(
        event,
        tor_exit_nodes
    )

    assert was_detected(result) is True
