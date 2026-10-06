from math import radians, sin, cos, sqrt, atan2
from datetime import datetime


def calculate_distance(lat1, lon1, lat2, lon2):
    earth_radius_km = 6371

    lat1 = radians(lat1)
    lon1 = radians(lon1)
    lat2 = radians(lat2)
    lon2 = radians(lon2)

    delta_lat = lat2 - lat1
    delta_lon = lon2 - lon1

    a = sin(delta_lat / 2) ** 2 + \
        cos(lat1) * cos(lat2) * sin(delta_lon / 2) ** 2

    c = 2 * atan2(sqrt(a), sqrt(1 - a))

    return earth_radius_km * c


def detect_impossible_travel(events):
    if len(events) < 2:
        return False, 0, 0, "Not enough events"

    first = events[0]
    second = events[1]

    distance = calculate_distance(
        first["latitude"],
        first["longitude"],
        second["latitude"],
        second["longitude"]
    )

    time1 = datetime.fromisoformat(
        first["timestamp"].replace("Z", "+00:00")
    )

    time2 = datetime.fromisoformat(
        second["timestamp"].replace("Z", "+00:00")
    )

    hours = (time2 - time1).total_seconds() / 3600

    if hours <= 0:
        return False, distance, 0, "Invalid time difference"

    speed = distance / hours

    # False-positive check: VPN
    if first.get("vpn", False) or second.get("vpn", False):
        return False, distance, speed, "VPN activity detected"

    # False-positive check: same ASN/network
    if first.get("asn") == second.get("asn"):
        return False, distance, speed, "Same ASN detected"

    if speed > 900:
        return True, distance, speed, "Travel speed is physically unrealistic"

    return False, distance, speed, "Travel is possible"
