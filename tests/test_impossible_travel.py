from detections.impossible_travel import detect_impossible_travel


def was_detected(result):
    if isinstance(result, tuple):
        return result[0]

    return result


def test_impossible_travel_detection():
    events = [
        {
            "timestamp": "2026-10-08T14:00:00Z",
            "user": "jsmith@company.com",
            "source_ip": "203.0.113.10",
            "auth_result": "success",
            "country": "US",
            "latitude": 42.3601,
            "longitude": -71.0589,
            "asn": "AS10001",
            "vpn": False
        },
        {
            "timestamp": "2026-10-08T14:30:00Z",
            "user": "jsmith@company.com",
            "source_ip": "198.51.100.10",
            "auth_result": "success",
            "country": "DE",
            "latitude": 52.5200,
            "longitude": 13.4050,
            "asn": "AS20002",
            "vpn": False
        }
    ]

    result = detect_impossible_travel(events)

    assert was_detected(result) is True
    assert result[1] > 5000
    assert result[2] > 900
    assert result[3] == "Travel speed is physically unrealistic"
