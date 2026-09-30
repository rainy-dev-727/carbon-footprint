# Household Carbon Footprint Tracker

A pure-Python command-line application for tracking household electricity usage and estimating associated carbon emissions.

## Overview

The Household Carbon Footprint Tracker allows a user to register electrical appliances, specify their quantity and wattage, simulate turning appliances ON and OFF, and calculate estimated electricity consumption and CO2 emissions.

The project is designed as a simple educational application demonstrating Python fundamentals, modular programming, file handling, JSON storage, date/time calculations, and input validation.

## Features

- Add household appliances
- Store appliance quantity and wattage
- Update appliance details
- Remove appliances
- Turn appliances ON and OFF
- Record appliance usage sessions
- Calculate electricity consumption in kWh
- Estimate carbon emissions in kg CO2
- View currently running appliances
- View usage history
- Generate a household report
- Save all data automatically in JSON
- No external Python packages required

## Project Structure

```text
household-carbon-footprint-tracker/
│
├── main.py
├── appliance.py
├── tracker.py
├── calculations.py
├── display.py
├── data.py
│
├── data/
│   └── household.json
│
├── README.md
├── statement.md
├── sample_output.txt
├── flowchart.md
├── requirements.txt
└── .gitignore
```

## Requirements

- Python 3.9 or newer
- No external packages

## Installation

Clone the repository:

```bash
git clone <your-repository-url>
cd household-carbon-footprint-tracker
```

Run the program:

```bash
python3 main.py
```

On Windows:

```bash
python main.py
```

## How It Works

First register an appliance:

```text
Appliance: Ceiling Fan
Quantity: 3
Wattage: 75 W
```

When the appliance is turned ON, the program records the start time.

When it is turned OFF, the program records the end time and calculates the duration.

The electricity calculation is:

```text
Energy = Power × Quantity × Time / 1000
```

The carbon estimate is:

```text
Carbon = Energy × Emission Factor
```

## Emission Factor

The default value is:

```text
0.7 kg CO2/kWh
```

This value is only an example assumption for the educational project. It can be changed in:

```text
data/household.json
```

For example:

```json
"emission_factor_kg_per_kwh": 0.7
```

## Important Limitation

This project records simulated appliance usage through the command line. It does not read real-time electrical measurements from a smart meter or physical switch.

## Example

For a 75 W fan used for 4 hours:

```text
Energy = 75 × 1 × 4 / 1000
       = 0.300 kWh
```

With an emission factor of 0.7 kg CO2/kWh:

```text
Carbon = 0.300 × 0.7
       = 0.210 kg CO2
```

## Educational Concepts Used

- Variables and data types
- Conditional statements
- Loops
- Functions
- Lists and dictionaries
- Modules
- File handling
- JSON
- Exception handling
- Date and time
- Mathematical calculations
- Input validation

## Future Improvements

- Daily and monthly graphs
- Electricity cost calculation
- CSV report export
- User accounts
- Real smart-meter integration
- SQLite database
- Web or GUI interface
- Appliance usage recommendations

## License

This project is intended for educational use.
