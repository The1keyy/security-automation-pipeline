from datetime import datetime


def detect_abnormal_login_time(event, normal_start_hour, normal_end_hour):
    timestamp = event["timestamp"]

    login_time = datetime.fromisoformat(
        timestamp.replace("Z", "+00:00")
    )

    login_hour = login_time.hour

    if login_hour < normal_start_hour or login_hour >= normal_end_hour:
        return True, login_hour

    return False, login_hour
