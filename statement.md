# Project Statement

## Title
Household Carbon Footprint Tracker

## Problem Statement
Electricity is consumed by many appliances in a household every day. Without recording appliance usage, it is difficult to estimate how much electricity is being consumed and how much carbon dioxide is associated with that consumption.

The Household Carbon Footprint Tracker is a command-line application developed in pure Python. It allows users to register household appliances by entering their quantity and wattage. The user can simulate switching appliances ON and OFF, while the program records the operating time.

Using the appliance power rating and operating duration, the program calculates estimated electricity consumption in kilowatt-hours (kWh). It then estimates associated carbon emissions using a configurable emission factor expressed in kilograms of CO2 per kWh.

## Objectives
1. Register household appliances and their power ratings.
2. Track appliance ON/OFF sessions.
3. Calculate electricity consumption.
4. Estimate carbon emissions.
5. Store data permanently using JSON.
6. Generate a simple household energy report.
7. Demonstrate modular programming and file handling in Python.

## Scope
The project is designed as a software simulation. It does not directly communicate with physical switches, smart meters, IoT devices, or electricity providers.

## Formula Used

### Electricity consumption

Energy (kWh) = Power (W) × Quantity × Time (hours) / 1000

### Carbon emissions

Carbon (kg CO2) = Energy (kWh) × Emission factor (kg CO2/kWh)

The emission factor is configurable in `data/household.json`. The default value in this educational project is `0.7 kg CO2/kWh` and should be treated as an example assumption, not a universal grid value.

## Expected Outcome
The application provides a simple way to understand how appliance power ratings and usage duration affect electricity consumption and estimated household carbon emissions.
