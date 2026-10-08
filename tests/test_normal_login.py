from detections.success_after_failure import detect_success_after_failure
from detections.brute_force import detect_brute_force
from detections.password_spray import detect_password_spray
from detections.credential_stuffing import detect_credential_stuffing
from detections.new_country import detect_new_country
from detections.new_device import detect_new_device
from detections.new_user_agent import detect_new_user_agent
from detections.abnormal_login_time import detect_abnormal_login_time
from detections.tor_authentication import detect_tor_authentication


def was_detected(result):
    if isinstance(result, tuple):
        return result[0]

    return result


def test_normal_login_is_not_suspicious():
    events = [
        {
            "timestamp": "2026-10-08T14:00:00Z",
            "user": "jsmith@company.com",
            "source_ip": "203.0.113.10",
            "country": "US",
            "auth_result": "success",
            "device_id": "laptop-01",
            "user_agent": "Chrome",
            "hour": 14
        }
    ]

    event = events[0]

    known_countries = ["US"]
    known_devices = ["laptop-01"]
    known_user_agents = ["Chrome"]
    tor_exit_nodes = []

    success_after_failure = detect_success_after_failure(events)
    brute_force = detect_brute_force(events)
    password_spray = detect_password_spray(events)
    credential_stuffing = detect_credential_stuffing(events)

    new_country = detect_new_country(
        event,
        known_countries
    )

    new_device = detect_new_device(
        event,
        known_devices
    )

    new_user_agent = detect_new_user_agent(
        event,
        known_user_agents
    )

    abnormal_time = detect_abnormal_login_time(
        event,
        8,
        18
    )

    tor_auth = detect_tor_authentication(
        event,
        tor_exit_nodes
    )

    assert was_detected(success_after_failure) is False
    assert was_detected(brute_force) is False
    assert was_detected(password_spray) is False
    assert was_detected(credential_stuffing) is False
    assert was_detected(new_country) is False
    assert was_detected(new_device) is False
    assert was_detected(new_user_agent) is False
    assert was_detected(abnormal_time) is False
    assert was_detected(tor_auth) is False


