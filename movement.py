import random
import time
from kshitish import Utilities  # Assuming you have this module
import sys

# Define the log function
def log(message):
    with open("output_log.txt", "a") as log_file:  # Open the file in append mode
        log_file.write(message + "\n") 

class Movement:
    def __init__(self, utilities):
        self.utilities = utilities
        self.angle = 0  # 0 degrees is 12 o'clock, 90 degrees is 3 o'clock, etc.
        self.velocity = self.utilities.outside_conditions["velocity"]
        self.acceleration_rate = 50  # tweak this as needed
        self.deceleration_rate = 10  
        self.position = {"x": 0, "y": 0}  # Initialize position

    def accelerate(self, time_passed, angle):
        if self.utilities.inside_conditions["fuel"] <= 0:
            print("WARNING: Insufficient fuel to accelerate!")
            return

        # Set the direction to the desired angle (clock direction)
        self.angle = angle
        print(f"Accelerating towards {self.angle}°...")

        # Increase velocity based on acceleration
        new_velocity = self.velocity + self.acceleration_rate * time_passed
        self.velocity = min(new_velocity, 15000)  # Maximum velocity cap

        # Update position: using polar coordinates conversion for direction
        delta_velocity = self.velocity * time_passed
        self.utilities.inside_conditions["fuel"] -= 0.05 * time_passed  # Fuel consumption
        self.utilities.inside_conditions["energy"] -= 0.01 * time_passed  # Energy consumption

        print(f"New velocity: {self.velocity} m/s")
        print(f"Current fuel: {self.utilities.inside_conditions['fuel']}")

    def decelerate(self, time_passed):
        if self.velocity <= 0:
            print("WARNING: No velocity to decelerate!")
            return

        # Decrease velocity based on deceleration rate
        new_velocity = self.velocity - self.deceleration_rate * time_passed
        self.velocity = max(new_velocity, 0)  # Can't go below 0 velocity

        self.utilities.inside_conditions["energy"] -= 0.005 * time_passed  # Energy consumption during deceleration

        print(f"Decelerating... New velocity: {self.velocity} m/s")
        print(f"Current energy: {self.utilities.inside_conditions['energy']}")

    def cruise(self, time_passed):
        if self.velocity <= 0:
            print("WARNING: No velocity to cruise!")
            return

        # Moving steadily in the current direction (cruise mode)
        print(f"Cruising steadily at {self.velocity} m/s in direction {self.angle}°")

        # Energy consumption during cruising
        self.utilities.inside_conditions["fuel"] -= 0.02 * time_passed
        self.utilities.inside_conditions["energy"] -= 0.01 * time_passed

        print(f"Fuel after cruising: {self.utilities.inside_conditions['fuel']}")
        print(f"Energy after cruising: {self.utilities.inside_conditions['energy']}")

    def idle(self, time_passed):
        self.utilities.inside_conditions["energy"] -= 0.005 * time_passed  # Minimal energy usage when idle
        print("Idling... Minimal energy consumption.")
        print(f"Energy remaining: {self.utilities.inside_conditions['energy']}")

    def random_obstacle_avoidance(self):
        # Randomly generate obstacles in space
        random_obstacle = random.choice(["asteroid", "space debris", "solar radiation"])
        print(f"Radar warning: {random_obstacle} detected!")

        # Move to avoid the obstacle
        if random_obstacle == "asteroid":
            print("Avoiding asteroid... Changing direction.")
            self.angle = (self.angle + 90) % 360  # Turn 90 degrees to avoid the asteroid
        elif random_obstacle == "space debris":
            print("Avoiding space debris... Changing direction.")
            self.angle = (self.angle + 45) % 360  # Turn 45 degrees to avoid debris
        else:  # Solar radiation
            print("Avoiding solar radiation... Changing direction.")
            self.angle = (self.angle + 180) % 360  # Turn 180 degrees to avoid radiation

        print(f"New direction: {self.angle}°")

    def move_cardinal(self, direction, time_passed):
        if direction == "north":
            # Moving north means accelerating
            print("Moving north... Accelerating!")
            self.accelerate(time_passed, angle=0)  # Accelerating towards 12 o'clock (north)
        elif direction == "south":
            # Moving south means decelerating
            print("Moving south... Decelerating!")
            self.decelerate(time_passed)
        elif direction == "east":
            # Moving east doesn't change speed, but may adjust position
            print("Moving east... Maintaining current speed!")
            self._move(1, 0, time_passed)  # Move east (positive x direction)
        elif direction == "west":
            # Moving west doesn't change speed, but may adjust position
            print("Moving west... Maintaining current speed!")
            self._move(-1, 0, time_passed)  # Move west (negative x direction)
        else:
            print("Invalid direction! Use 'north', 'south', 'east', or 'west'.")

    def _move(self, dx, dy, time_passed):
        self.position["x"] += dx
        self.position["y"] += dy

        # Increase energy and fuel consumption
        self.utilities.inside_conditions["fuel"] = max(
            0, self.utilities.inside_conditions["fuel"] - 0.1 * time_passed
        )
        self.utilities.inside_conditions["energy"] = max(
            0, self.utilities.inside_conditions["energy"] - 0.2 * time_passed
        )

        print(f"Moved to position: {self.position}")
        print(f"Remaining fuel: {self.utilities.inside_conditions['fuel']}")
        print(f"Remaining energy: {self.utilities.inside_conditions['energy']}")

        if self.utilities.inside_conditions["fuel"] <= 0:
            print("WARNING: Fuel exhausted!")
        if self.utilities.inside_conditions["energy"] <= 0:
            print("WARNING: Energy depleted!")


class Radar:
    def __init__(self, log_func):
        self.detected_objects = []
        self.log_func = log_func

    def scan_space(self):
        # Simulate random detection of objects
        space_objects = ["No Threat", "Asteroid", "Debris", "Alien Ship", "Comet", "Space Dust"]
        weight = [4, 1, 1, 1, 1, 1]
        detected = random.choices(space_objects, weights=weight, k=1)[0]
        self.detected_objects.append(detected)
        self.log_func(f"Radar detected: {detected}")
        return detected

    def avoid_object(self, movement, object_detected):
        self.log_func(f"Taking evasive action to avoid: {object_detected}")
        # Randomly choose an avoidance direction
        avoidance_directions = ["north", "south", "east", "west"]
        chosen_direction = random.choice(avoidance_directions)
        movement.move_cardinal(chosen_direction, time_passed=2)
        self.log_func(f"Evasion completed by moving {chosen_direction}.")


# Main Execution
if __name__ == "__main__":
    # Assuming Utilities class is already defined
    utilities = Utilities()
    utilities.generate_conditions()  # Initialize conditions

    # Create instances of Movement and Radar, passing the log function
    movement = Movement(utilities=utilities)
    radar = Radar(log_func=log)  # Pass the log function to Radar

    # Simulate operations
    for _ in range(5):  # Simulate 5 cycles
        time.sleep(1)  # Wait 1 second between operations
        radar_object = radar.scan_space()
        radar.avoid_object(movement, radar_object)

        # Randomly move the ship forward
        movement.move_cardinal(random.choice(["north", "east", "south", "west"]), time_passed=1)

        # Check fuel and energy levels
        if utilities.inside_conditions["fuel"] <= 0 or utilities.inside_conditions["energy"] <= 0:
            print("The ship is out of resources and cannot continue!")
            break

    # Test the Movement Class
    movement.accelerate(time_passed=2, angle=30)  # Accelerate towards 1 o'clock
    time.sleep(1)
    movement.cruise(time_passed=2)
    time.sleep(1)
    movement.decelerate(time_passed=2)
    time.sleep(1)
    movement.idle(time_passed=2)

    # Simulate random obstacle avoidance
    movement.random_obstacle_avoidance()
