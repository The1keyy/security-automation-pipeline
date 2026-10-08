from detections.new_device import detect_new_device


def was_detected(result):
    if isinstance(result, tuple):
        return result[0]

    return result


def test_new_device_detection():
    event = {
        "timestamp": "2026-10-08T14:00:00Z",
        "user": "jsmith@company.com",
        "source_ip": "203.0.113.25",
        "country": "US",
        "auth_result": "success",
        "device_id": "unknown-laptop-99"
    }

    known_devices = [
        "laptop-01",
        "phone-01",
        "desktop-01"
    ]

    result = detect_new_device(
        event,
        known_devices
    )

    assert was_detected(result) is True
