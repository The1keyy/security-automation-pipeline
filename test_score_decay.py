from datetime import datetime, timezone, timedelta

from risk.score_decay import apply_score_decay


current_time = datetime.now(timezone.utc)

test_events = [
    {
        "name": "Recent event",
        "timestamp": (
            current_time - timedelta(minutes=30)
        ).isoformat()
    },

    {
        "name": "6-hour event",
        "timestamp": (
            current_time - timedelta(hours=6)
        ).isoformat()
    },

    {
        "name": "1-day event",
        "timestamp": (
            current_time - timedelta(hours=24)
        ).isoformat()
    },

    {
        "name": "3-day event",
        "timestamp": (
            current_time - timedelta(hours=72)
        ).isoformat()
    },

    {
        "name": "Old event",
        "timestamp": (
            current_time - timedelta(days=7)
        ).isoformat()
    }
]


print("Risk Score Decay Test")
print("=====================")

for event in test_events:
    result = apply_score_decay(
        20,
        event["timestamp"]
    )

    print()
    print(event["name"])
    print("Original:", result["original_score"])
    print("Age:", result["age_hours"], "hours")
    print("Multiplier:", result["multiplier"])
    print("Decayed Score:", result["decayed_score"])
