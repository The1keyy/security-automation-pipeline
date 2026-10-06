# security-automation-pipeline

Python detections for identity sign-in logs. Each check reads a sample log under `sample_logs/` and prints whether the event is valid or whether an alert fired.

```bash
python3 main.py
```

`main.py` currently runs suspicious post-login activity against `sample_logs/post_login_activity.json`. The other detectors live in `detections/` with matching sample logs.

## Detections

- Event validation (`models/event.py`)
- Success after failure
- Brute force
- Password spray
- Credential stuffing
- Impossible travel, including a VPN false-positive filter
- New country, new device, and new user agent
- Abnormal login time
- Tor exit-node authentication
- Hosting-provider sign-in
- Legacy authentication
- MFA fatigue
- Suspicious post-login activity

## Screenshots

Screenshots from the runs so far are in the [`ss`](ss) folder.

### Valid security event

![Valid security event](ss/valid-security-event.jpg)

### Invalid security event

![Invalid security event missing the user field](ss/invalid-security-event.jpg)

### Missing log file

![Missing security log file](ss/missing-log-file.jpg)

### Success after failure

![Success-after-failure detection](ss/success-after-failure.jpg)

### Brute force

![Brute force detection](ss/brute-force.jpg)

### Password spray

![Password spray detection](ss/password-spray.jpg)

### Impossible travel

![Impossible travel detection](ss/impossible-travel.jpg)

### Impossible travel filtered as VPN

![Impossible travel false-positive test](ss/impossible-travel-vpn-filter.jpg)

### Tor authentication

![Tor authentication detection](ss/tor-authentication.jpg)

### MFA fatigue

![MFA fatigue detection](ss/mfa-fatigue.jpg)

### Suspicious post-login activity

![Suspicious post-login activity detection](ss/post-login-activity.jpg)
