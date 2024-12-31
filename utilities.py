class Utilities:
    def __init__(self):
        # Initialize the spaceship utilities
        # Initialize resources and conditions as empty or default values
        self.resources_data = {}  # Stores spaceship resources
        self.conditions_data = {}  # Stores environmental conditions
        print("Utilities Initialized.")

    def resources(self):
        #Randomly generate resources for the spaceship
        #Assign values for:
        #Tools, Materials, Equipment
        #Oxygen, Fuel, Energy levels
        #Machinery conditions (status such as operational, minor fault, etc.)
        #Store generated resources for further monitoring
        print("Generating Resources...")
        pass

    def generate_conditions(self):
        #Randomly generate environmental conditions
        #Generate:
        #Inside conditions: Temperature, Humidity
        #Outside conditions: Temperature, Gravity, Aerodynamics, Solar Flare activity, Radiation levels
        #Store conditions for later checks
        print("Generating Conditions...")
        pass

    def assess_conditions(self):
        # Assess current conditions
        #Evaluate if:
        #Inside temperature and pressure are suitable
        #Outside environment permits takeoff or landing
        #Current resources match the demands of conditions
        #Return assessment as "Suitable" or "Not Suitable"
        print("Assessing Conditions...")
        pass

    def degrade_conditions(self):
        #Simulate the natural degradation of conditions
        #Randomly decrease conditions and resource levels by a value within a range (5-10)
        #Ensure values do not go below 0
        #Adjust changes dynamically based on user input
        print("Degrading Conditions...")
        pass

    def user_input_for_further_actions(self):
        #Gather user input for actions during simulation
        #Ask user to:
        #Check radar for outside dangers (like debris, asteroids)
        #Trigger repairs for equipment or resources
        #Guide course of action (e.g., adjust altitude, repair machinery)
        #Execute corresponding actions based on user input
        print("Gathering User Input for Further Actions...")
        pass
