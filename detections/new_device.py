def detect_new_device(event, known_devices):
    device_id = event["device_id"]

    if device_id not in known_devices:
        return True, device_id

    return False, device_id
