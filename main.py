from appliance import add_appliance, remove_appliance, update_appliance
from tracker import turn_on, turn_off, running_appliances, usage_records
from calculations import household_summary
from display import (
    banner, menu, print_appliances, print_running, print_summary,
    print_records, pause, success, error, info
)
from data import load_data, save_data
from display import add_appliance_rows

def main():
    data = load_data()
    while True:
        banner()
        menu()
        choice = input("Enter your choice: ").strip()

        if choice == "1":
            print_appliances(data)
            pause()
        elif choice == "2":
            if add_appliance(data):
                save_data(data)
                success("Appliance added successfully.")
            pause()
        elif choice == "3":
            if remove_appliance(data):
                save_data(data)
            pause()
        elif choice == "4":
            if turn_on(data):
                save_data(data)
            pause()
        elif choice == "5":
            if turn_off(data):
                save_data(data)
            pause()
        elif choice == "6":
            print_running(data)
            pause()
        elif choice == "7":
            print_summary(add_appliance_rows(household_summary(data), data))
            pause()
        elif choice == "8":
            print_records(usage_records(data))
            pause()
        elif choice == "9":
            print_summary(add_appliance_rows(household_summary(data), data))
            print()
            print_appliances(data)
            print()
            print_running(data)
            pause()
        elif choice == "10":
            save_data(data)
            print("\nThank you for using Household Carbon Footprint Tracker.")
            break
        elif choice == "11":
            if update_appliance(data):
                save_data(data)
            pause()
        else:
            error("Invalid choice. Please enter a number from 1 to 11.")

if __name__ == "__main__":
    main()
