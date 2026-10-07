# security-automation-pipeline

Python detections for identity sign-in logs, plus IP threat-intelligence enrichment.

```bash
pip install -r requirements.txt
python3 main.py
```

`main.py` enriches `185.220.101.45` through AbuseIPDB, VirusTotal, GreyNoise, AlienVault OTX, the Tor exit-node list, GeoIP, ASN, and a local blocklist. API keys are read from the environment (`ABUSEIPDB_API_KEY`, `VIRUSTOTAL_API_KEY`, `GREYNOISE_API_KEY`, `OTX_API_KEY`).

The sign-in detectors live in `detections/` with matching sample logs.

## Research Basis

The Phase 4 risk engine is research-inspired. It draws on SOC alert-prioritization research and established risk standards, then applies them as a simplified, explainable portfolio model. This project does not reproduce those academic models, and it does not implement CVSS as a scoring method for SOC alerts.

Each case is scored from five factors:

- Threat Intelligence
- Behavioral Evidence
- User / Asset Impact
- Correlation
- Confidence

The sources below are design references only.

- [Wang et al., AlertPro (Computers & Security, 2024)](https://doi.org/10.1016/j.cose.2023.103583) contributes context-aware SOC alert prioritization: ranking alerts with the surrounding investigation context rather than treating each alert in isolation. The project does not implement AlertPro's reinforcement-learning framework.
- [Guo et al., "Intelligent priority awareness method for alert data in SOC threat response" (Journal of King Saud University Computer and Information Sciences, 2026)](https://doi.org/10.1007/s44443-026-01172-w) contributes multi-dimensional, dynamic SOC risk scoring and prioritization. The project does not implement that paper's knowledge-graph, semantic-integrity, or AHP scoring system.
- [NIST SP 800-30 Rev. 1](https://doi.org/10.6028/NIST.SP.800-30r1) contributes the risk concepts of likelihood, context, and impact.
- [MITRE ATT&CK](https://attack.mitre.org/) is the reference for mapping observed activity to adversary behavior and techniques.
- [CVSS v4.0](https://www.first.org/cvss/v4.0/) is inspiration only for a transparent scoring structure and severity bands. Scores produced by this project are not CVSS scores.

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
