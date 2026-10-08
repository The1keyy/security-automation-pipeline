# Contributing

This is a synthetic security lab. Changes should stay explainable, and tests should keep passing.

## Fork and run

1. Fork the repository, or use **Use this template** on GitHub.
2. Create a virtual environment, install dependencies, and run the suite:

```bash
python3 -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
pytest
```

`pytest` runs only `tests/`. The `test_*.py` files at the repo root are demos.

## Add a detector

1. Add a function in `detections/`.
2. Add a synthetic log under `sample_logs/` if the demo needs one.
3. Add a pytest file in `tests/` that checks both a hit and a quiet case.
4. If the function returns a tuple, read the flag from the first item. Several existing tests use a `was_detected()` helper for that.

## Open a pull request

Describe what changed, which test you ran, and whether the case is synthetic. Do not commit `.env` or API keys.
