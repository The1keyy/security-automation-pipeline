# Security Automation Pipeline

An explainable security workflow for identity sign-in activity:

**Detection → enrichment → research-informed risk scoring → human-controlled response → audit and evidence → MITRE ATT&CK mapping → analyst report → automated validation.**

The project is a portfolio and learning lab, not a production SOAR platform. Incident data is synthetic. Containment is simulated. Dry-run mode stays on, so the pipeline does not disable accounts, revoke sessions, or change firewall rules.

## Pipeline

1. **Detect.** Validate a sign-in event and check it for account-takeover patterns.
2. **Enrich.** Look up the source IP across threat-intelligence providers.
3. **Score.** Combine threat intelligence, behavior, impact, and correlation into a risk score, with confidence scored separately.
4. **Respond.** Turn severity into a recommendation, then apply allowlists, approval, playbooks, rate limits, and dry-run controls.
5. **Report.** Write a text and HTML incident report an analyst can review.
6. **Validate.** Run the detectors against labeled synthetic scenarios with pytest.

## Run

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python3 main.py
```

`main.py` enriches `185.220.101.45`. Provider keys are read from the environment: `ABUSEIPDB_API_KEY`, `VIRUSTOTAL_API_KEY`, `GREYNOISE_API_KEY`, and `OTX_API_KEY`.

```bash
python3 test_final_risk_score.py
python3 test_response_decision.py
python3 test_text_report.py
python3 test_html_report.py
python3 test_end_to_end_report.py
python3 -m pytest tests -q
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
| `tests/` | Pytest suite for detections, severity, and response decisions |
| `ss/` | Full screenshot set from the runs |

The README below features the screenshots that show the safety model and the finished report. Every other run is linked from [`ss`](ss).

## Research-informed design

Scoring and prioritization are informed by security operations and risk-assessment research. Alert priority is not treated as one arbitrary severity value. The implementation is research-inspired and does not reproduce the algorithms from the cited papers.

**AlertPro.** [Wang et al., *Computers & Security* (2024)](https://doi.org/10.1016/j.cose.2023.103583) influenced the idea that an alert should be prioritized with additional context, not only the original detection severity. This project does not implement AlertPro's reinforcement-learning framework.

**Intelligent priority awareness.** [Guo et al., *Journal of King Saud University Computer and Information Sciences* (2026)](https://doi.org/10.1007/s44443-026-01172-w) supports evaluating SOC alerts across multiple dimensions rather than treating each alert independently. This project does not implement that paper's knowledge-graph, semantic-integrity, or AHP scoring system.

**NIST SP 800-30 Rev. 1.** [NIST's risk-assessment guidance](https://doi.org/10.6028/NIST.SP.800-30r1) influenced the separation of threat evidence, likelihood and context, and potential impact.

**MITRE ATT&CK.** [ATT&CK](https://attack.mitre.org/) connects observed behavior to known adversary techniques.

**CVSS v4.0.** [CVSS v4.0](https://www.first.org/cvss/v4.0/) was reviewed as an example of a transparent, component-based scoring system. This project does not calculate CVSS scores for security alerts. CVSS is inspiration only for understandable components and severity boundaries.

The portfolio risk model uses five factors:

- Threat intelligence
- Behavioral evidence
- User / asset impact
- Correlation
- Confidence

## Safety and honesty

- Incident data is synthetic.
- Containment actions are simulated.
- Dry-run mode is enabled.
- No production accounts are disabled.
- No production sessions are revoked.
- No production firewall rules are changed.
- Threat-intelligence results depend on external providers.
- Missing evidence is reported. It is not filled in.
- Detection metrics come from a small synthetic dataset. They are not production accuracy.

## Earlier stages

Sign-in detections live in `detections/` with matching files in `sample_logs/`. They cover validation, brute force, password spray, credential stuffing, impossible travel with a VPN false-positive filter, new country, device, and user agent, abnormal login time, Tor authentication, hosting-provider sign-in, legacy authentication, MFA fatigue, and suspicious post-login activity.

Enrichment in `enrichment/` looks up AbuseIPDB (with a local cache), VirusTotal, GreyNoise, AlienVault OTX, the Tor exit list, GeoIP, ASN, and a local blocklist. A failed provider does not stop the others.

Phase 4, in `risk/`, scores those results separately and then classifies severity. Full runs for these stages are in [`ss`](ss), including [the enrichment pipeline](ss/enrichment-pipeline.jpg) and [the risk scenarios](ss/risk-scenarios.jpg).

## Phase 5 — Safe response automation

Phase 5 adds a controlled response layer. The goal is not to automate destructive actions. The pipeline uses severity, analyst approval, allowlists, rate limits, pre-approved playbooks, audit logging, evidence, and rollback support before a response is allowed.

Detection and scoring can be automated. Potentially disruptive containment requires additional safeguards.

```text
Risk score
→ Severity
→ Response decision
→ Safety checks
→ Analyst approval
→ Pre-approved playbook
→ Dry run / execution decision
→ Audit log
→ Rollback information
```

### 5.1 Response decision engine

The response engine converts incident severity into a recommendation. It does not treat every alert the same way.

| Severity | Response |
| --- | --- |
| LOW | Log and continue monitoring |
| MEDIUM | Recommend analyst investigation |
| HIGH | Require human approval before containment |
| CRITICAL | Allow only pre-approved response playbooks |

[Response decision run](ss/response-decision.jpg)

### 5.2 Dry-run mode

Every response action can run in dry-run mode. Dry-run simulates containment. It does not disable accounts, block IP addresses, revoke sessions, or change production systems.

```text
Action: BLOCK_IP
Target: 185.220.101.45
Dry Run: True
Executed: False
```

[Dry-run test](ss/response-dry-run.jpg)

### 5.3 IP allowlist

Trusted IP addresses are protected from automated containment. The pipeline checks the trusted allowlist before an IP-based response.

```text
10.0.0.10
Response Allowed: False
Reason: IP is on the trusted allowlist

185.220.101.45
Response Allowed: True
Reason: IP is not on the trusted allowlist
```

[IP allowlist test](ss/ip-allowlist.jpg)

### 5.4 Protected account allowlist

Sensitive accounts are protected from automatic containment. That includes security administrator accounts, executive accounts, and emergency or break-glass accounts, so automation does not disable a critical account by mistake.

[User allowlist test](ss/user-allowlist.jpg)

### 5.5 Action rate limiting

The lab configuration allows at most 3 response actions in a 60-second window. The fourth attempt is rejected. This limits the damage from runaway automation or a logic error.

[Action rate-limit test](ss/action-rate-limit.jpg)

### 5.6 Human approval

HIGH-risk response actions require an analyst decision before containment.

```text
Proposed action
→ Analyst review
→ Approve or deny
→ Continue safety checks
```

Approval is recorded. Approval does not mean the action was executed.

![Analyst approval and denial of a proposed block](ss/human-approval.jpg)

### 5.7 Pre-approved playbooks

CRITICAL incidents can use only explicitly approved playbooks:

- `BLOCK_MALICIOUS_IP`
- `DISABLE_COMPROMISED_ACCOUNT`
- `REVOKE_ACTIVE_SESSIONS`

An action such as `DELETE_USER_ACCOUNT` is rejected because it is not an approved playbook.

[Playbook test](ss/response-playbook.jpg)

### 5.8 Audit logging

Response decisions are written to an audit trail: timestamp, action, target, severity, approval status, execution status, and reason.

```text
Action: BLOCK_IP
Target: 185.220.101.45
Severity: HIGH
Approved: True
Executed: False
Reason: Analyst approved action, but system is still in dry-run mode
```

[Audit log test](ss/audit-log.jpg)

### 5.9 Evidence attached to the action

A recommendation includes the evidence behind it: risk score, severity, confidence, detections, threat intelligence, and the recommended response. The action is not a black-box decision.

![Evidence attached to a recommended response](ss/response-evidence.jpg)

### 5.10 Rollback

The pipeline records whether a response can be reversed.

| Action | Rollback |
| --- | --- |
| `BLOCK_IP` | `UNBLOCK_IP` |
| `DISABLE_ACCOUNT` | `ENABLE_ACCOUNT` |
| `ADD_IP_TO_DENYLIST` | `REMOVE_IP_FROM_DENYLIST` |
| `REVOKE_ACTIVE_SESSIONS` | No automatic rollback |

Actions with no mapping, such as `DELETE_USER_ACCOUNT`, are marked as not reversible.

![Rollback support for containment actions](ss/response-rollback.jpg)

## Phase 6 — Automated incident reporting

Phase 6 turns detection, enrichment, scoring, and response data into an analyst-readable incident report. The same case is written as plain text (`reports/incident_report.txt`) and HTML (`reports/incident_report.html`).

```text
Detection results
→ Threat intelligence
→ Risk score
→ Confidence
→ Response decision
→ Evidence
→ MITRE ATT&CK mapping
→ Incident report
```

### 6.1 Executive summary

The summary names the affected user, source IP, severity, risk score, confidence, and how many suspicious indicators fired. In the sample case, `jsmith@company.com` from `185.220.101.45` is scored CRITICAL at 86/90 with confidence 10/10.

[Executive summary run](ss/incident-executive-summary.jpg)

### 6.2 Incident timeline

Events are sorted into chronological order so an analyst can reconstruct the sequence: failed logins, a successful login from the suspicious IP, a new MFA method, and a mailbox forwarding rule.

[Incident timeline](ss/incident-timeline.jpg)

### 6.3 Account and source context

The report describes both the identity and the source.

Account context includes username, account type, department, account status, and normal country. Source context includes IP address, country, city, ASN, and Tor exit-node status.

### 6.4 Detection evidence

Each detection is paired with the reason it fired: impossible travel between the US and Germany, MFA fatigue before a successful login, success after repeated failures, and post-login changes to MFA and mailbox forwarding.

[Detection evidence](ss/detection-evidence.jpg)

### 6.5 Threat-intelligence findings

Enrichment results are included in the report from AbuseIPDB, VirusTotal, AlienVault OTX, the Tor exit list, GreyNoise when it is available, GeoIP and ASN, and the local blocklist.

[Threat-intelligence findings](ss/threat-intelligence-findings.jpg)

### 6.6 Explainable risk breakdown

The report shows how the final score was built. The sample case is threat intelligence 30/30, behavior 28/30, impact 20/20, and correlation 8/10, for a final score of 86/90 and severity CRITICAL.

![Risk score breakdown inside the incident report](ss/risk-score-breakdown.jpg)

### 6.7 Confidence

Risk and confidence are separate. Risk asks how dangerous the incident appears. Confidence asks how strongly the available evidence supports that assessment. Confidence uses successful enrichment sources, failed providers, strong behavioral signals, and missing data.

[Confidence analysis](ss/confidence-analysis.jpg)

### 6.8 Recommended response

The report uses the Phase 5 engine. A CRITICAL case recommends immediate escalation, a pre-approved containment playbook, session revocation, account disablement only after approval, and evidence preservation. The sample recommendation is `PREAPPROVED_PLAYBOOK_ONLY`, with approval required and automatic execution off.

[Recommended response](ss/recommended-response.jpg)

### 6.9 Actions taken

The report separates recommended, approved, executed, and simulated. In the sample, `REVOKE_ACTIVE_SESSIONS` and `BLOCK_IP` are approved and still marked executed false because dry-run is on. The report does not claim that containment happened.

[Actions taken](ss/actions-taken.jpg)

### 6.10 Could not verify

The report lists investigation gaps instead of guessing. The sample cannot verify endpoint compromise, user intent, or mailbox-rule impact, because endpoint telemetry, user contact, and production mailbox data were not available.

[Could not verify](ss/could-not-verify.jpg)

### 6.11 MITRE ATT&CK mapping

Observed activity in the simulated incident is mapped to:

| Technique | Name |
| --- | --- |
| T1078 | Valid Accounts |
| T1621 | Multi-Factor Authentication Request Generation |
| T1098 | Account Manipulation |
| T1114.003 | Email Forwarding Rule |

![MITRE ATT&CK mapping for the simulated incident](ss/mitre-attack-mapping.jpg)

### 6.12 Technical appendix

The appendix records event IDs, log sources, enrichment sources, pipeline version, dry-run status, and environment. The sample environment is pipeline version 1.0, a synthetic portfolio lab, with dry-run enabled.

### 6.13 Text report

`reports/incident_report.txt` contains the full investigation: summary, timeline, identity, source, detections, threat intelligence, risk, confidence, recommendations, actions taken, unverified findings, ATT&CK, and the technical appendix.

[Text report generation](ss/text-report.jpg)

### 6.14 HTML report

`reports/incident_report.html` renders the same data for review. Dynamic report content is escaped before it is written, so report data is not interpreted as HTML or JavaScript.

![HTML security incident report](ss/html-incident-report.jpg)

### 6.15 End-to-end reporting check

`python3 test_end_to_end_report.py` checks the finished report:

- Severity is CRITICAL
- Risk score is 86/90
- Confidence is 10/10
- Four detections are present
- MITRE ATT&CK mappings are present
- Response requires analyst approval
- The text report file exists
- The HTML report file exists

A passing run prints `FINAL STATUS: ALL REPORTING TESTS PASSED`.

## Phase 7 — Automated testing and detection validation

Phase 7 moves detection checks from one-off scripts into a repeatable pytest suite in `tests/`. Pytest is listed in `requirements.txt`.

```text
Detection logic
→ Synthetic test scenarios
→ Automated pytest validation
→ Benign versus malicious comparison
→ False-positive handling
→ Detection quality metrics
```

The suite checks that selected detectors fire on malicious scenarios, stay quiet on benign logins, and apply false-positive suppression. It does not cover every attack or edge case.

```bash
python3 -m pytest tests -q
```

### 7.1 Smoke tests

`tests/test_smoke.py` checks severity bands and the critical response decision.

| Score | Severity |
| --- | --- |
| 2 | LOW |
| 39 | MEDIUM |
| 64 | HIGH |
| 86 | CRITICAL |

A CRITICAL decision must return `PREAPPROVED_PLAYBOOK_ONLY`, require approval, and stay non-automatic.

### 7.2 Normal login

`tests/test_normal_login.py` uses a successful login from a known country, device, and user agent, during a normal hour, from a non-Tor IP. It expects no alert from success-after-failure, brute force, password spray, credential stuffing, new country, new device, new user agent, abnormal login time, or Tor authentication.

Several detectors return a tuple such as `(False, 0)` rather than a Boolean. The tests use a small helper, `was_detected()`, so pytest reads the detection flag from either shape. The new-device detector expects `device_id`, not `device`.

![Normal login stays quiet](ss/pytest-normal-login.jpg)

### 7.3 Brute force

`tests/test_brute_force.py` repeats failed authentication for the same user from the same source IP and expects `detect_brute_force()` to fire.

[Brute-force test](ss/pytest-brute-force.jpg)

### 7.4 Password spray

`tests/test_password_spray.py` uses one source IP against multiple users and expects the password-spray detector to fire.

[Password-spray test](ss/pytest-password-spray.jpg)

### 7.5 Credential stuffing

`tests/test_credential_stuffing.py` matches the detector's actual rule: at least 5 unique users, at least 4 failures, and at least 1 success from the same source IP. The test checks the flag, the user count, the failure count, the success count, the source IP, and the successful user. It does not stop at "the detector fired."

![Credential-stuffing test checks the full result](ss/pytest-credential-stuffing.jpg)

### 7.6 Success after failure

`tests/test_success_after_failure.py` places several failures before a successful login for the same account and expects that detector to fire.

[Success-after-failure test](ss/pytest-success-after-failure.jpg)

### 7.7 Impossible travel

`tests/test_impossible_travel.py` moves a login from Boston to Berlin in about 30 minutes, with coordinates, VPN off, and two different ASNs (`AS10001` and `AS20002`). The test expects a detection, distance over 5,000 km, speed over 900 km/h, and the reason `Travel speed is physically unrealistic`.

Writing this test found an edge case. If both events omit ASN, both values are `None`, and `None == None` takes the same-ASN suppression path. Missing ASN values should not be treated as a match. The current test supplies different ASNs. Treating a missing ASN as unknown is a future hardening change.

![Impossible-travel test](ss/pytest-impossible-travel.jpg)

### 7.8 Benign VPN

`tests/test_benign_vpn.py` uses the same Boston-to-Berlin pair with `vpn` set on one login. Detection must be false, with the reason `VPN activity detected`. Geographic distance alone does not raise the alert.

![VPN false-positive suppression](ss/pytest-benign-vpn.jpg)

### 7.9 Tor authentication

`tests/test_tor_login.py` signs in from `185.220.101.45` with that address on the Tor exit list and expects the Tor detector to fire.

[Tor login test](ss/pytest-tor-login.jpg)

### 7.10 New device

`tests/test_new_device.py` uses `device_id` `unknown-laptop-99` against known devices `laptop-01`, `phone-01`, and `desktop-01`, and expects the new-device detector to fire.

[New-device test](ss/pytest-new-device.jpg)

### 7.11 Malicious versus benign

`tests/test_malicious_vs_benign.py` compares one normal successful login with a burst of failures from one IP followed by a success. The benign case must not fire success-after-failure, brute force, or password spray. The malicious case must fire success-after-failure and brute force.

![Benign activity stays quiet and the malicious pattern fires](ss/pytest-malicious-vs-benign.jpg)

### 7.12 Detection quality metrics

`tests/test_detection_metrics.py` labels a small synthetic set. Two benign cases are a normal success and a single failure. Three malicious cases are brute force, success after repeated failures, and password spray. Each case is classified with those three detectors.

On the bundled synthetic validation scenarios, the tested detection subset achieved 1.00 precision, 1.00 recall, and a 0.00 false-positive rate: 3 true positives, 2 true negatives, 0 false positives, and 0 false negatives. These results are limited to the included synthetic dataset and are not presented as production detection performance.

![Synthetic detection-quality metrics](ss/pytest-detection-metrics.jpg)

## License

Released under the [MIT License](LICENSE).
