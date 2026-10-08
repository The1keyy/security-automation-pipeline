from response.decision_engine import choose_response
from risk.severity import classify_severity


def test_severity_classification():
    assert classify_severity(2) == "LOW"
    assert classify_severity(39) == "MEDIUM"
    assert classify_severity(64) == "HIGH"
    assert classify_severity(86) == "CRITICAL"


def test_response_decision():
    result = choose_response("CRITICAL")

    assert result["action"] == "PREAPPROVED_PLAYBOOK_ONLY"
    assert result["requires_approval"] is True
    assert result["automatic"] is False
