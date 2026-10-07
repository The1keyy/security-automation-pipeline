# security-automation-pipeline

Python detections for identity sign-in logs, plus IP threat-intelligence enrichment.

```bash
pip install -r requirements.txt
python3 main.py
```

`main.py` enriches `185.220.101.45` through AbuseIPDB, VirusTotal, GreyNoise, AlienVault OTX, the Tor exit-node list, GeoIP, ASN, and a local blocklist. API keys are read from the environment (`ABUSEIPDB_API_KEY`, `VIRUSTOTAL_API_KEY`, `GREYNOISE_API_KEY`, `OTX_API_KEY`).

The sign-in detectors live in `detections/` with matching sample logs.

## Enrichment

- AbuseIPDB, with a local response cache
- VirusTotal
- GreyNoise
- AlienVault OTX
- Tor exit-node list
- GeoIP and ASN
- Local blocklist
- Handling for rate limits, timeouts, missing fields, and a provider that fails while the rest continue

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

### AbuseIPDB

![AbuseIPDB threat intelligence](ss/abuseipdb.jpg)

### VirusTotal

![VirusTotal threat intelligence](ss/virustotal.jpg)

### GreyNoise

![GreyNoise threat intelligence](ss/greynoise.jpg)

### AlienVault OTX

![AlienVault OTX threat intelligence](ss/otx.jpg)

### Tor exit node

![Tor exit-node intelligence](ss/tor-exit-node.jpg)

### AbuseIPDB cache hit

![AbuseIPDB cache test](ss/abuseipdb-cache.jpg)

### Rate limit

![Rate-limit handling test](ss/rate-limit.jpg)

### Timeout

![Timeout handling test](ss/timeout.jpg)

### Missing data

![Missing-data handling test](ss/missing-data.jpg)

### Graceful degradation

![Graceful degradation test](ss/graceful-degradation.jpg)

### Full enrichment pipeline

![Security threat intelligence pipeline](ss/enrichment-pipeline.jpg)
