def session_energy_kwh(appliance, duration_hours):
    return (appliance["wattage"] * appliance["quantity"]
            * duration_hours) / 1000

def completed_energy_by_appliance(data):
    result = {a["id"]: 0.0 for a in data["appliances"]}

    for session in data["usage_sessions"]:
        appliance = next(
            (a for a in data["appliances"]
             if a["id"] == session["appliance_id"]),
            None
        )
        if appliance:
            result[appliance["id"]] += session_energy_kwh(
                appliance, session["duration_hours"]
            )
    return result

def current_energy_estimate(data):
    from datetime import datetime
    result = {a["id"]: 0.0 for a in data["appliances"]}
    now = datetime.now()

    for appliance in data["appliances"]:
        if appliance["is_on"] and appliance["turned_on_at"]:
            start = datetime.fromisoformat(appliance["turned_on_at"])
            hours = max((now - start).total_seconds() / 3600, 0)
            result[appliance["id"]] = session_energy_kwh(appliance, hours)
    return result

def household_summary(data):
    completed = completed_energy_by_appliance(data)
    current = current_energy_estimate(data)
    total_energy = sum(completed.values()) + sum(current.values())
    factor = data["emission_factor_kg_per_kwh"]
    total_carbon = total_energy * factor

    return {
        "total_energy": total_energy,
        "total_carbon": total_carbon,
        "emission_factor": factor,
        "completed_energy": completed,
        "current_energy": current
    }

def appliance_summary(data):
    summary = household_summary(data)
    rows = []

    for appliance in data["appliances"]:
        energy = (summary["completed_energy"].get(appliance["id"], 0)
                  + summary["current_energy"].get(appliance["id"], 0))
        rows.append({
            "name": appliance["name"],
            "energy": energy,
            "carbon": energy * summary["emission_factor"]
        })
    return rows
