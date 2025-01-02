import time
from data_provider import (
    get_inside_temperature,
    get_inside_humidity,
    get_fuel_level,
    get_oxygen_level,
    get_energy_level,
    get_machinery_status,
    get_outside_temperature,
    get_gravity,
    get_aerodynamics,
    get_velocity,
    _check_solar_flare,
)

class Utilities:
    def __init__(self):
        self.resources_data = {}
        self.inside_conditions = {}
        self.outside_conditions = {}
        print("Utilities Initialized.")

    def generate_conditions(self, time_passed=None):
        if time_passed is None:
            return {
                "inside": self._initialize_inside_conditions(),
                "outside": self._initialize_outside_conditions(),
            }
        else:
            return {
                "inside": self.update_inside_conditions(time_passed),
                "outside": self.update_outside_conditions(time_passed),
            }

    def _initialize_inside_conditions(self):
        self.inside_conditions = {
            "temperature": get_inside_temperature(),
            "humidity": get_inside_humidity(),
            "fuel": get_fuel_level(),
            "oxygen": get_oxygen_level(),
            "energy": get_energy_level(),
            "machinery_status": get_machinery_status(),
        }
        return self.inside_conditions


    def _initialize_outside_conditions(self):
        self.outside_conditions = {
            "temperature": get_outside_temperature(),
            "gravity": get_gravity(),
            "aerodynamics": get_aerodynamics(),
            "velocity": get_velocity(),
        }
        return self.outside_conditions

    def update_inside_conditions(self, time_passed):
        decrement_rate = 0.03 * time_passed
        for key in ["fuel", "oxygen", "energy"]:
            self.inside_conditions[key] = max(
                0, self.inside_conditions[key] - decrement_rate
            )
        self.inside_conditions["temperature"] = self._adjust_temperature(
            self.inside_conditions["temperature"], time_passed
        )
        self.inside_conditions["humidity"] = self._adjust_humidity(
            self.inside_conditions["humidity"], time_passed
        )
        self._check_inside_alerts()
        return self.inside_conditions

    def update_outside_conditions(self, time_passed):
        self.outside_conditions["velocity"] = min(
            15000, self.outside_conditions["velocity"] + time_passed * 100
        )
        self.outside_conditions["gravity"] = max(
            0, self.outside_conditions["gravity"] - 0.01 * time_passed
        )
        self.outside_conditions["aerodynamics"] = self._adjust_aerodynamics()
        self.outside_conditions["temperature"] = self._handle_temperature_change(
            self.outside_conditions["temperature"], time_passed
        )
        if _check_solar_flare():
            self.handle_solar_flare()
        return self.outside_conditions

    def _adjust_temperature(self, temperature, time_passed):
        return max(15, temperature - 0.1 * time_passed)

    def _adjust_humidity(self, humidity, time_passed):
        return max(20, humidity - 0.05 * time_passed)

    def _adjust_aerodynamics(self):
        if self.outside_conditions["velocity"] > 12000:
            return "Turbulent"
        return "Stable"

    def _handle_temperature_change(self, temperature, time_passed):
        return max(-100, temperature - 0.5 * time_passed)

    def handle_solar_flare(self):
        self.inside_conditions["energy"] = max(
            0, self.inside_conditions["energy"] - 5
        )
        print("Warning: Solar flare detected!")

    def _check_inside_alerts(self):
        if self.inside_conditions["fuel"] < 20:
            print("ALERT: Fuel is critically low!")
        if self.inside_conditions["oxygen"] < 30:
            print("ALERT: Oxygen is critically low!")
        if self.inside_conditions["energy"] < 10:
            print("ALERT: Energy is critically low!")

# Create an instance of Utilities
utilities = Utilities()

# Step 1: Initialize conditions
initial_conditions = utilities.generate_conditions()
print("\nInitial Conditions:")
print("Inside:", initial_conditions["inside"])
print("Outside:", initial_conditions["outside"])

# Step 2: Simulate updates over time
time_intervals = [1, 2, 3]  # Simulated time intervals in seconds
for interval in time_intervals:
    print(f"\nUpdating conditions after {interval} seconds:")
    updated_conditions = utilities.generate_conditions(time_passed=interval)
    print("Inside:", updated_conditions["inside"])
    print("Outside:", updated_conditions["outside"])
    time.sleep(1)  # Simulate waiting time for more realistic output
