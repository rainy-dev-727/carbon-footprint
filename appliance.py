from display import error, info

def _next_id(data):
    ids = [a["id"] for a in data["appliances"]]
    return max(ids, default=0) + 1

def _read_positive_int(prompt):
    while True:
        try:
            value = int(input(prompt))
            if value > 0:
                return value
            error("Enter a value greater than 0.")
        except ValueError:
            error("Please enter a whole number.")

def _read_positive_float(prompt):
    while True:
        try:
            value = float(input(prompt))
            if value > 0:
                return value
            error("Enter a value greater than 0.")
        except ValueError:
            error("Please enter a valid number.")

def add_appliance(data):
    name = input("Enter appliance name: ").strip()
    if not name:
        error("Appliance name cannot be empty.")
        return False

    if any(a["name"].lower() == name.lower()
           for a in data["appliances"]):
        error("An appliance with this name already exists.")
        return False

    quantity = _read_positive_int("Enter number of units: ")
    wattage = _read_positive_float("Enter wattage per unit (W): ")

    data["appliances"].append({
        "id": _next_id(data),
        "name": name,
        "quantity": quantity,
        "wattage": wattage,
        "is_on": False,
        "turned_on_at": None
    })
    return True

def remove_appliance(data):
    if not data["appliances"]:
        info("No appliances registered.")
        return False

    try:
        appliance_id = int(input("Enter appliance ID to remove: "))
    except ValueError:
        error("Invalid appliance ID.")
        return False

    appliance = next(
        (a for a in data["appliances"] if a["id"] == appliance_id), None
    )
    if appliance is None:
        error("Appliance not found.")
        return False

    if appliance["is_on"]:
        error("Turn off the appliance before removing it.")
        return False

    data["appliances"].remove(appliance)
    print(f"Removed: {appliance['name']}")
    return True

def update_appliance(data):
    if not data["appliances"]:
        info("No appliances registered.")
        return False

    try:
        appliance_id = int(input("Enter appliance ID to update: "))
    except ValueError:
        error("Invalid appliance ID.")
        return False

    appliance = next(
        (a for a in data["appliances"] if a["id"] == appliance_id), None
    )
    if appliance is None:
        error("Appliance not found.")
        return False

    if appliance["is_on"]:
        error("Turn off the appliance before updating it.")
        return False

    print(f"Current wattage: {appliance['wattage']} W")
    appliance["wattage"] = _read_positive_float(
        "Enter new wattage per unit (W): "
    )
    print(f"Current quantity: {appliance['quantity']}")
    appliance["quantity"] = _read_positive_int(
        "Enter new number of units: "
    )
    return True
