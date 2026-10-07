import json


CONFIG_FILE = "config/risk_weights.json"


def load_risk_weights():
    try:
        with open(CONFIG_FILE, "r") as file:
            return json.load(file)

    except FileNotFoundError:
        print("ERROR: Risk weight configuration file not found.")
        return None

    except json.JSONDecodeError:
        print("ERROR: Risk weight configuration contains invalid JSON.")
        return None
