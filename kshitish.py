#This is my code i copied from utilities.py

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
                # "solar_flare": random.choice(["Present", "Absent"]) #This will be updated later (Possibly)
            }

            print("Initial Conditions Generated.")
            print("Inside Conditions:", self.inside_conditions)
            print("Outside Conditions:", self.outside_conditions)

        else:
            # Update existing conditions dynamically based on time_passed (in seconds)
            # Fuel, oxygen, energy should decrease slightly with each update
            self.inside_conditions["fuel"] -= random.uniform(0.03, 0.05)  # Random decrement per second
            self.inside_conditions["oxygen"] -= random.uniform(0.03, 0.05)
            self.inside_conditions["energy"] -= random.uniform(0.03, 0.05)

            # Ensure values don't go below 0
            self.inside_conditions["fuel"] = max(self.inside_conditions["fuel"], 0)
            self.inside_conditions["oxygen"] = max(self.inside_conditions["oxygen"], 0)
            self.inside_conditions["energy"] = max(self.inside_conditions["energy"], 0)

            # Increase velocity as long as it does not exceed the gravity threshold
            gravity_threshold = 1  # The threshold where gravity will no longer be able to pull down the velocity (1G for Earth)
            
            # Increase velocity if it's below threshold
            if self.outside_conditions["velocity"] < gravity_threshold * 1000:  # Assuming 1000 km/h is threshold (just an example)
                self.outside_conditions["velocity"] += random.uniform(50, 150)  # Increase velocity gradually
            else:
                self.outside_conditions["velocity"] = gravity_threshold * 1000  # Set constant velocity once the threshold is crossed

            # Update the outside temperature based on time passed (assuming time passed is in seconds)
            self.outside_conditions["temperature"] -= random.uniform(0.5, 2.0) * time_passed / 60  # Simulating gradual cooling with height/time
            self.outside_conditions["gravity"] = max(0, self.outside_conditions["gravity"] - random.uniform(0.01, 0.03) * time_passed / 60) #
            self.outside_conditions["aerodynamics"] = random.choice(["Stable", "Unstable", "Turbulent"])

            # Print updated conditions after each update
            print("\nUpdated Conditions:")
            print(f"Fuel: {round(self.inside_conditions['fuel'], 2)}%")
            print(f"Oxygen: {round(self.inside_conditions['oxygen'], 2)}%")
            print(f"Energy: {round(self.inside_conditions['energy'], 2)}%")
            print(f"Inside Temperature: {round(self.inside_conditions['temperature'], 2)}C")
            print(f"Inside Humidity: {round(self.inside_conditions['humidity'], 2)}%")
            print(f"Outside Temperature: {round(self.outside_conditions['temperature'], 2)}C")
            print(f"Gravity: {round(self.outside_conditions['gravity'], 3)} G")
            print(f"Aerodynamics: {self.outside_conditions['aerodynamics']}")
            print(f"Velocity: {round(self.outside_conditions['velocity'], 2)} km/h")


    

