from detections.credential_stuffing import detect_credential_stuffing


def was_detected(result):
    if isinstance(result, tuple):
        return result[0]

    return result


def test_credential_stuffing_detection():
    events = [
        {
            "timestamp": "2026-10-08T14:00:00Z",
            "user": "alice@company.com",
            "source_ip": "198.51.100.75",
            "auth_result": "failure"
        },
        {
            "timestamp": "2026-10-08T14:00:15Z",
            "user": "bob@company.com",
            "source_ip": "198.51.100.75",
            "auth_result": "failure"
        },
        {
            "timestamp": "2026-10-08T14:00:30Z",
            "user": "carol@company.com",
            "source_ip": "198.51.100.75",
            "auth_result": "failure"
        },
        {
            "timestamp": "2026-10-08T14:00:45Z",
            "user": "dave@company.com",
            "source_ip": "198.51.100.75",
            "auth_result": "failure"
        },
        {
            "timestamp": "2026-10-08T14:01:00Z",
            "user": "erin@company.com",
            "source_ip": "198.51.100.75",
            "auth_result": "success"
        }
    ]

    result = detect_credential_stuffing(events)

    assert was_detected(result) is True
    assert result[1] == 5
    assert result[2] == 4
    assert result[3] == 1
    assert result[4] == "198.51.100.75"
    assert result[5] == "erin@company.com"
