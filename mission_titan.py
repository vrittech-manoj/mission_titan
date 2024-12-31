import time
from missile import *
from utilities import *
from utilities import Utilities  # Import the Utilities class

if __name__ == "__main__":
    # Testing the Utilities class( ~ Utilities Group Member)
    mission = Utilities()  # No arguments needed now
    mission.generate_conditions()

    #Run this for 3 minutes(for now) and later on update it so that it runs until it reaches its destination by accessing values from other models such as radar and missile. 
    #Hope every collaborators could understand it 
    for minute in range(1, 4):  # Simulate for 3 updates
        print(f"\nTime Passed: {minute} minute(s)")
        mission.generate_conditions(time_passed=60)