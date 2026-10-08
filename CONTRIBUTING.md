# Contributing

Thanks for looking. This is a synthetic portfolio lab, and changes are welcome.

1. Fork the repo (or use it as a template).
2. Create a branch: `git checkout -b my-change`
3. Set up: `python3 -m venv .venv && source .venv/bin/activate && pip install -r requirements.txt`
4. Make your change, then run `pytest`. Everything should pass.
5. Open a pull request and say what you changed and why.

Good first changes: a new detector in `detections/`, another source in `enrichment/`, a new playbook in `response/`, or a new report format in `reports/`.
Please keep the synthetic-data rule: no real logs, credentials, or personal data.
