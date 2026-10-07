from datetime import datetime, timezone


def apply_score_decay(base_score, event_timestamp):
    event_time = datetime.fromisoformat(
        event_timestamp.replace("Z", "+00:00")
    )

    current_time = datetime.now(timezone.utc)

    age_hours = (
        current_time - event_time
    ).total_seconds() / 3600

    if age_hours <= 1:
        multiplier = 1.0

    elif age_hours <= 6:
        multiplier = 0.9

    elif age_hours <= 24:
        multiplier = 0.75

    elif age_hours <= 72:
        multiplier = 0.5

    else:
        multiplier = 0.25

    decayed_score = base_score * multiplier

    return {
        "original_score": base_score,
        "age_hours": round(age_hours, 2),
        "multiplier": multiplier,
        "decayed_score": round(decayed_score, 2)
    }
