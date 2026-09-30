# Flowchart

Copy the following flowchart into a diagram/flowchart tool or reproduce it using boxes and arrows for the project submission.

```text
                 ┌─────────────────────┐
                 │        START        │
                 └──────────┬──────────┘
                            ↓
                 ┌─────────────────────┐
                 │ Load JSON data      │
                 │ from household.json │
                 └──────────┬──────────┘
                            ↓
                 ┌─────────────────────┐
                 │ Display Main Menu   │
                 └──────────┬──────────┘
                            ↓
                 ┌─────────────────────┐
                 │  Read User Choice   │
                 └──────────┬──────────┘
                            ↓
              ┌─────────────┴─────────────┐
              │                           │
          Add Appliance               Turn ON/OFF
              │                           │
              ↓                           ↓
      ┌───────────────┐           ┌───────────────┐
      │ Enter name,   │           │ Record start/ │
      │ quantity and  │           │ end time      │
      │ wattage       │           └───────┬───────┘
      └───────┬───────┘                   ↓
              │                    ┌───────────────┐
              ↓                    │ Calculate     │
      ┌───────────────┐            │ duration      │
      │ Save appliance│            └───────┬───────┘
      └───────┬───────┘                   │
              │                            ↓
              │                    ┌───────────────┐
              │                    │ Calculate kWh │
              │                    └───────┬───────┘
              │                            ↓
              │                    ┌───────────────┐
              │                    │ Calculate CO2 │
              │                    └───────┬───────┘
              │                            │
              └──────────────┬─────────────┘
                             ↓
                   ┌─────────────────────┐
                   │ Save data to JSON   │
                   └──────────┬──────────┘
                              ↓
                   ┌─────────────────────┐
                   │ Display report or   │
                   │ return to main menu │
                   └──────────┬──────────┘
                              ↓
                       ┌──────────────┐
                       │ Exit chosen? │
                       └──────┬───────┘
                         No ↙     ↘ Yes
                            ↙       ↘
                   ┌──────────┐  ┌─────────┐
                   │ Main Menu│  │   END   │
                   └──────────┘  └─────────┘
```
