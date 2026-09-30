from datetime import datetime
from data import timestamp
from display import error, info

def _find_appliance(data, appliance_id):
    return next(
        (a for a in data["appliances"] if a["id"] == appliance_id), None
    )

def _read_id(prompt):
    try:
        return int(input(prompt))
    except ValueError:
        error("Please enter a valid appliance ID.")
        return None

def turn_on(data):
    appliance_id = _read_id("Enter appliance ID to turn ON: ")
    if appliance_id is None:
        return False

    appliance = _find_appliance(data, appliance_id)
    if appliance is None:
        error("Appliance not found.")
        return False

    if appliance["is_on"]:
        error("This appliance is already ON.")
        return False

    appliance["is_on"] = True
    appliance["turned_on_at"] = timestamp()
    print(f"{appliance['name']} turned ON.")
    return True

def turn_off(data):
    appliance_id = _read_id("Enter appliance ID to turn OFF: ")
    if appliance_id is None:
        return False

    appliance = _find_appliance(data, appliance_id)
    if appliance is None:
        error("Appliance not found.")
        return False

    if not appliance["is_on"]:
        error("This appliance is already OFF.")
        return False

    start = datetime.fromisoformat(appliance["turned_on_at"])
    end = datetime.now()
    duration_hours = max((end - start).total_seconds() / 3600, 0)

    session = {
        "appliance_id": appliance["id"],
        "appliance_name": appliance["name"],
        "start_time": appliance["turned_on_at"],
        "end_time": end.isoformat(timespec="seconds"),
        "duration_hours": round(duration_hours, 4)
    }
    data["usage_sessions"].append(session)

    appliance["is_on"] = False
    appliance["turned_on_at"] = None

    print(f"{appliance['name']} turned OFF.")
    print(f"Session duration: {duration_hours:.2f} hours")
    return True

def running_appliances(data):
    return [a for a in data["appliances"] if a["is_on"]]

def usage_records(data):
    return data["usage_sessions"]
