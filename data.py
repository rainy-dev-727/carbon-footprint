import json
import os
from datetime import datetime

DATA_FILE = os.path.join(os.path.dirname(__file__), "data", "household.json")

DEFAULT_DATA = {
    "emission_factor_kg_per_kwh": 0.7,
    "appliances": [],
    "usage_sessions": []
}

def load_data():
    os.makedirs(os.path.dirname(DATA_FILE), exist_ok=True)
    if not os.path.exists(DATA_FILE):
        save_data(DEFAULT_DATA.copy())
        return DEFAULT_DATA.copy()

    try:
        with open(DATA_FILE, "r", encoding="utf-8") as file:
            data = json.load(file)
    except (json.JSONDecodeError, OSError):
        data = DEFAULT_DATA.copy()

    data.setdefault("emission_factor_kg_per_kwh", 0.7)
    data.setdefault("appliances", [])
    data.setdefault("usage_sessions", [])
    return data

def save_data(data):
    with open(DATA_FILE, "w", encoding="utf-8") as file:
        json.dump(data, file, indent=4)

def timestamp():
    return datetime.now().isoformat(timespec="seconds")
