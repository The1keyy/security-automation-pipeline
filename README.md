# Security Automation Pipeline

An explainable security pipeline for identity sign-in activity. It validates events, detects suspicious behavior, enriches the source IP, scores the case, recommends a safe response, and writes an incident report.

The response path is deliberately constrained. Containment actions are simulated, rate-limited, and blocked for trusted IPs and protected accounts. High and critical actions require analyst approval.

## Pipeline

1. **Detect.** Validate a sign-in event and check it for account-takeover patterns.
2. **Enrich.** Look up the source IP across threat-intelligence providers.
3. **Score.** Combine threat intelligence, behavior, impact, and correlation into a risk score, with a separate confidence score.
4. **Respond.** Choose a severity-based action, then apply allowlists, approval, playbooks, and dry-run controls.
5. **Report.** Produce a text and HTML incident report with evidence, ATT&CK mapping, and items that could not be verified.

## Run

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python3 main.py
```

`main.py` enriches `185.220.101.45`. Provider keys are read from the environment:

- `ABUSEIPDB_API_KEY`
- `VIRUSTOTAL_API_KEY`
- `GREYNOISE_API_KEY`
- `OTX_API_KEY`

Sample checks for the later stages:

```bash
python3 test_final_risk_score.py
python3 test_response_decision.py
python3 test_text_report.py
python3 test_html_report.py
```

## Project layout

| Path | Purpose |
| --- | --- |
| `detections/` | Sign-in detections |
| `sample_logs/` | Sample events for those detections |
| `enrichment/` | IP threat-intelligence lookups and cache |
| `risk/` | Explainable risk and confidence scoring |
| `config/` | Risk weights and severity thresholds |
| `response/` | Decision, approval, allowlist, playbook, audit, and rollback controls |
| `reports/` | Text and HTML incident reports |
| `ss/` | Screenshots from the runs below |

## Research basis

The Phase 4 risk engine is research-inspired. It draws on SOC alert-prioritization research and established risk standards, then applies them as a simplified, explainable portfolio model. This project does not reproduce those academic models, and it does not implement CVSS as a scoring method for SOC alerts.

Each case is scored from five factors:

- Threat intelligence
- Behavioral evidence
- User / asset impact
- Correlation
- Confidence

The sources below are design references only.

- [Wang et al., AlertPro (Computers & Security, 2024)](https://doi.org/10.1016/j.cose.2023.103583) contributes context-aware SOC alert prioritization: ranking alerts with the surrounding investigation context rather than treating each alert in isolation. The project does not implement AlertPro's reinforcement-learning framework.
- [Guo et al., "Intelligent priority awareness method for alert data in SOC threat response" (Journal of King Saud University Computer and Information Sciences, 2026)](https://doi.org/10.1007/s44443-026-01172-w) contributes multi-dimensional, dynamic SOC risk scoring and prioritization. The project does not implement that paper's knowledge-graph, semantic-integrity, or AHP scoring system.
- [NIST SP 800-30 Rev. 1](https://doi.org/10.6028/NIST.SP.800-30r1) contributes the risk concepts of likelihood, context, and impact.
- [MITRE ATT&CK](https://attack.mitre.org/) is the reference for mapping observed activity to adversary behavior and techniques.
- [CVSS v4.0](https://www.first.org/cvss/v4.0/) is inspiration only for a transparent scoring structure and severity bands. Scores produced by this project are not CVSS scores.

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

## Enrichment

- AbuseIPDB, with a local response cache
- VirusTotal
- GreyNoise
- AlienVault OTX
- Tor exit-node list
- GeoIP and ASN
- Local blocklist
- Handling for rate limits, timeouts, missing fields, and a provider that fails while the rest continue

## Example output

Screenshots are stored in [`ss`](ss).

### Sign-in detections

#### Valid security event

![Valid security event](ss/valid-security-event.jpg)

#### Invalid security event

![Invalid security event missing the user field](ss/invalid-security-event.jpg)

#### Missing log file

![Missing security log file](ss/missing-log-file.jpg)

#### Success after failure

![Success-after-failure detection](ss/success-after-failure.jpg)

#### Brute force

![Brute force detection](ss/brute-force.jpg)

#### Password spray

![Password spray detection](ss/password-spray.jpg)

#### Impossible travel

![Impossible travel detection](ss/impossible-travel.jpg)

#### Impossible travel filtered as VPN

![Impossible travel false-positive test](ss/impossible-travel-vpn-filter.jpg)

#### Tor authentication

![Tor authentication detection](ss/tor-authentication.jpg)

#### MFA fatigue

![MFA fatigue detection](ss/mfa-fatigue.jpg)

#### Suspicious post-login activity

![Suspicious post-login activity detection](ss/post-login-activity.jpg)

### Threat intelligence

#### AbuseIPDB

![AbuseIPDB threat intelligence](ss/abuseipdb.jpg)

#### VirusTotal

![VirusTotal threat intelligence](ss/virustotal.jpg)

#### GreyNoise

![GreyNoise threat intelligence](ss/greynoise.jpg)

#### AlienVault OTX

![AlienVault OTX threat intelligence](ss/otx.jpg)

#### Tor exit node

![Tor exit-node intelligence](ss/tor-exit-node.jpg)

#### AbuseIPDB cache hit

![AbuseIPDB cache test](ss/abuseipdb-cache.jpg)

#### Rate limit

![Rate-limit handling test](ss/rate-limit.jpg)

#### Timeout

![Timeout handling test](ss/timeout.jpg)

#### Missing data

![Missing-data handling test](ss/missing-data.jpg)

#### Graceful degradation

![Graceful degradation test](ss/graceful-degradation.jpg)

#### Full enrichment pipeline

![Security threat intelligence pipeline](ss/enrichment-pipeline.jpg)

### Phase 4: Risk score

The explainable risk model scores threat intelligence, behavioral evidence, user and asset impact, correlation, and confidence separately, then classifies the total.

#### Threat intelligence score

![Threat intelligence risk score](ss/threat-intelligence-score.jpg)

#### Behavioral evidence score

![Behavioral evidence risk score](ss/behavior-score.jpg)

#### User and asset impact score

![User and asset impact score](ss/impact-score.jpg)

#### Correlation score

![Signal correlation score](ss/correlation-score.jpg)

#### Confidence score

![Confidence score](ss/confidence-score.jpg)

#### Final risk score

![Final security risk assessment](ss/final-risk-score.jpg)

#### Severity bands

![Risk severity classification](ss/severity.jpg)

#### Risk scenarios

![Low, medium, high, and critical risk scenarios](ss/risk-scenarios.jpg)

### Phase 5: Safe response

Response controls cover severity decisions, dry-run, IP and user allowlists, action rate limits, human approval, playbooks, audit logging, evidence, and rollback.

#### Response decision

![Safe response decision engine](ss/response-decision.jpg)

#### Dry run

![Safe response dry-run test](ss/response-dry-run.jpg)

#### IP allowlist

![IP allowlist safety test](ss/ip-allowlist.jpg)

#### User allowlist

![User allowlist safety test](ss/user-allowlist.jpg)

#### Action rate limit

![Action rate-limit test](ss/action-rate-limit.jpg)

#### Human approval

![Human approval required](ss/human-approval.jpg)

#### Playbooks

![Critical response playbook test](ss/response-playbook.jpg)

#### Audit log

![Audit logging test](ss/audit-log.jpg)

#### Response evidence

![Response action evidence](ss/response-evidence.jpg)

#### Rollback

![Response rollback test](ss/response-rollback.jpg)

### Phase 6: Incident report

The report includes an executive summary, timeline, detection evidence, threat intelligence, risk breakdown, confidence, recommended response, simulated actions, gaps, ATT&CK mapping, and both text and HTML output.

#### Executive summary

![Security incident executive summary](ss/incident-executive-summary.jpg)

#### Incident timeline

![Incident timeline](ss/incident-timeline.jpg)

#### Detection evidence

![Detection evidence](ss/detection-evidence.jpg)

#### Threat intelligence findings

![Threat intelligence findings](ss/threat-intelligence-findings.jpg)

#### Risk score breakdown

![Risk score breakdown](ss/risk-score-breakdown.jpg)

#### Confidence analysis

![Confidence analysis](ss/confidence-analysis.jpg)

#### Recommended response

![Recommended response](ss/recommended-response.jpg)

#### Actions taken

![Simulated response actions](ss/actions-taken.jpg)

#### Could not verify

![Items the report could not verify](ss/could-not-verify.jpg)

#### MITRE ATT&CK mapping

![MITRE ATT&CK mapping](ss/mitre-attack-mapping.jpg)

#### Text report

![Text report generation](ss/text-report.jpg)

#### HTML report

![HTML security incident report](ss/html-incident-report.jpg)

## License

Released under the [MIT License](LICENSE).
