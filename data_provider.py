import random

def get_inside_temperature():
    return 22.5

def get_inside_humidity():
    return 55.0

def get_fuel_level():
    return 90

def get_oxygen_level():
    return 95

def get_energy_level():
    return 85

def get_machinery_status():
    return "operational"

def get_outside_temperature():
    return 15.5

def get_gravity():
    return 0.9

def get_aerodynamics():
    return "Stable"

def get_velocity():
    return 12000

def _check_solar_flare():
    return random.choices([True, False], weights=[1, 3])[0]


