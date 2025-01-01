import time
import random

class Utilities:
    def __init__(self):
        # Initialize resources and conditions
        self.resources_data = {}  # Stores spaceship resources
        self.inside_conditions = {}
        self.outside_conditions = {}
        print("Utilities Initialized.")

    def generate_conditions(self, time_passed=None):
        if time_passed is None:
            # Initial setup for conditions
            self.inside_conditions = {
                "temperature": random.uniform(18, 25),  # In degrees Celsius
                "humidity": random.uniform(30, 70),  # In percentage
                "fuel": 100,  # In percentage
                "oxygen": 100,  # In percentage
                "energy": 100,  # In percentage
                "machinery_status": random.choice(["operational", "minor fault", "major fault"])
            }

            self.outside_conditions = {
                "temperature": random.uniform(10, 30),  # Initial temperature in space
                "gravity": random.uniform(0.8, 1),  # Near-Earth gravity, say between 0.8-1.0 G
                "aerodynamics": random.choice(["Stable", "Unstable"]),  # Initial status
                "velocity": random.randint(10000, 15000),  # Initial velocity in km/h
            }

            print("Initial Conditions Generated.")
            print("Inside Conditions:", self.inside_conditions)
            print("Outside Conditions:", self.outside_conditions)

        else:
            # Update existing conditions dynamically based on time_passed (in seconds)
            self._update_inside_conditions(time_passed)
            self._update_outside_conditions(time_passed)

            # Periodically log conditions
            self._log_conditions()

    def _update_inside_conditions(self, time_passed):
        # Gradual decrement of critical resources
        decrement_rate = 0.03 * time_passed  # Base decrement rate
        for key in ["fuel", "oxygen", "energy"]:
            self.inside_conditions[key] = max(0, self.inside_conditions[key] - random.uniform(decrement_rate, 1.5 * decrement_rate))

        # Handle temperature and humidity
        min_temp = 15  # Minimum inside temperature
        self.inside_conditions["temperature"] = max(
            min_temp, self.inside_conditions["temperature"] - random.uniform(0.1, 0.5) * time_passed / 60
        )
        self.inside_conditions["humidity"] = max(
            20, self.inside_conditions["humidity"] - random.uniform(0.1, 0.3) * time_passed / 60
        )

        # Alerts for critical levels
        if self.inside_conditions["fuel"] < 20:
            print("ALERT: Fuel is critically low!")
        if self.inside_conditions["oxygen"] < 30:
            print("ALERT: Oxygen is critically low!")
        if self.inside_conditions["energy"] < 10:
            print("ALERT: Energy levels are dangerously low!")

    def _update_outside_conditions(self, time_passed):
        # Update velocity dynamically
        gravity_threshold = 1  # 1G threshold for reference
        if self.outside_conditions["velocity"] < gravity_threshold * 1000:
            self.outside_conditions["velocity"] += random.uniform(50, 150) * time_passed / 60
        else:
            self.outside_conditions["velocity"] = gravity_threshold * 1000

        # Update gravity and aerodynamics
        self.outside_conditions["gravity"] = max(
            0, self.outside_conditions["gravity"] - random.uniform(0.01, 0.03) * time_passed / 60
        )
        if self.outside_conditions["velocity"] > 12000 and self.outside_conditions["gravity"] < 0.5:
            self.outside_conditions["aerodynamics"] = "Turbulent"
        elif self.outside_conditions["velocity"] > 15000:
            self.outside_conditions["aerodynamics"] = "Extreme Turbulence"
        else:
            self.outside_conditions["aerodynamics"] = random.choice(["Stable", "Unstable"])

        # Simulate cooling or heating effect of outer space
        self.outside_conditions["temperature"] -= random.uniform(0.5, 2.0) * time_passed / 60

        # Possible external events: Solar flare
        if random.choice([True, False]):  # 50% chance of a solar flare
            print("Warning: Solar flare detected! Energy consumption spiked.")
            self.inside_conditions["energy"] -= random.uniform(1, 5)

    def _log_conditions(self):
        with open("conditions_log.txt", "a") as log_file:
            log_file.write(
                f"Time: {time.ctime()} | Inside: {self.inside_conditions} | Outside: {self.outside_conditions}\n"
            )

    def reset_conditions(self):
        # Reset to safe default conditions
        self.inside_conditions.update({
            "fuel": 100,
            "oxygen": 100,
            "energy": 100,
            "temperature": random.uniform(18, 25),
            "humidity": random.uniform(30, 70),
        })
        print("Conditions reset to safe levels.")

# Example usage:
utilities = Utilities()
utilities.generate_conditions()
for i in range(10):  # Simulate updates over time
    time.sleep(60)  # Simulate time passing
    utilities.generate_conditions(time_passed=2)
    
    



# class DebrisTracking:
#     def __init__(self):
#         self.debris_list = []  # Track detected debris
#         print("Debris Tracking Initialized.")

#     def detect_debris(self):
#         pass

#     def clear_debris(self):
#         pass

