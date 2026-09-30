def banner():
    print("\n" + "=" * 58)
    print("       HOUSEHOLD CARBON FOOTPRINT TRACKER")
    print("=" * 58)

def menu():
    print("""
1. View Appliances
2. Add Appliance
3. Remove Appliance
4. Turn Appliance ON
5. Turn Appliance OFF
6. View Running Appliances
7. View Energy & Carbon Summary
8. View Usage Records
9. Generate Household Report
10. Exit
11. Update Appliance
""")

def success(message):
    print(f"[SUCCESS] {message}")

def error(message):
    print(f"[ERROR] {message}")

def info(message):
    print(f"[INFO] {message}")

def pause():
    input("\nPress Enter to continue...")

def print_appliances(data):
    print("\nREGISTERED APPLIANCES")
    print("-" * 70)
    if not data["appliances"]:
        print("No appliances registered.")
        return

    print(f"{'ID':<5}{'Appliance':<22}{'Units':<8}"
          f"{'Wattage':<12}{'Status':<10}")
    print("-" * 70)

    for a in data["appliances"]:
        status = "ON" if a["is_on"] else "OFF"
        print(f"{a['id']:<5}{a['name']:<22}{a['quantity']:<8}"
              f"{a['wattage']:<12.1f}{status:<10}")

def print_running(data):
    print("\nCURRENTLY RUNNING")
    print("-" * 45)
    running = [a for a in data["appliances"] if a["is_on"]]

    if not running:
        print("No appliances are currently ON.")
        return

    for a in running:
        print(f"ID {a['id']}: {a['name']} "
              f"({a['quantity']} × {a['wattage']} W)")

def print_summary(summary):
    print("\nHOUSEHOLD ENERGY & CARBON SUMMARY")
    print("-" * 55)
    print(f"Total electricity used/estimated : "
          f"{summary['total_energy']:.3f} kWh")
    print(f"Emission factor                 : "
          f"{summary['emission_factor']:.3f} kg CO2/kWh")
    print(f"Estimated carbon emissions      : "
          f"{summary['total_carbon']:.3f} kg CO2")

    print("\nAPPLIANCE-WISE CONSUMPTION")
    print("-" * 55)
    for appliance in summary.get("appliance_rows", []):
        print(f"{appliance['name']:<25}"
              f"{appliance['energy']:>8.3f} kWh"
              f"  {appliance['carbon']:>8.3f} kg CO2")

def print_records(records):
    print("\nUSAGE RECORDS")
    print("-" * 90)
    if not records:
        print("No completed usage sessions.")
        return

    for i, record in enumerate(records, 1):
        print(f"{i}. {record['appliance_name']}")
        print(f"   ON : {record['start_time']}")
        print(f"   OFF: {record['end_time']}")
        print(f"   Duration: {record['duration_hours']:.2f} hours")

def add_appliance_rows(summary, data):
    rows = []
    for a in data["appliances"]:
        energy = (summary["completed_energy"].get(a["id"], 0)
                  + summary["current_energy"].get(a["id"], 0))
        rows.append({
            "name": a["name"],
            "energy": energy,
            "carbon": energy * summary["emission_factor"]
        })
    summary["appliance_rows"] = rows
    return summary
