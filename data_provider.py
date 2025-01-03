# data_provider.py
import random

def get_inside_temperature():
    return 22.5  # Replace with actual logic to fetch data

def get_inside_humidity():
    return 55.0  # Replace with actual logic to fetch data

def get_fuel_level():
    return 90  # Replace with actual logic to fetch data

def get_oxygen_level():
    return 95  # Replace with actual logic to fetch data

def get_energy_level():
    return 85  # Replace with actual logic to fetch data

def get_machinery_status():
    return "operational"  # Replace with actual logic to fetch data

def get_outside_temperature():
    return 15.5  # Replace with actual logic to fetch data

def get_gravity():
    return 0.9  # Replace with actual logic to fetch data

def get_aerodynamics():
    return "Stable"  # Replace with actual logic to fetch data

def get_velocity():
    return 12000  # Replace with actual logic to fetch data

def _check_solar_flare():
    return random.choices([True, False], weights=[1, 3])[0]