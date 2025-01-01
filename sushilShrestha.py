# class Fuel:
    
#     def __init__(self,status): #Fuel class
#           self.status =status
    
#     def check_fuel(self): #Check fuel Status
#         pass
    
#     def refuel(self): #Fuel refuel
#         pass
    

# class Repair:
#     def __init__(self): #use any tool is required
#         pass
    
#     def energy_source(): # available energy source
#         pass
    
#     def use_energy(): # to use available energy source
#         pass
class Fuel:
    def __init__(self, capacity, current_level):  # Initialize the Fuel class
        self.capacity = capacity  # Total fuel capacity
        self.current_level = current_level  # Current fuel level
    
    def check_fuel(self):  # Check fuel status
        if self.current_level <= 0:
            return "Fuel empty. Refuel immediately!"
        elif self.current_level < self.capacity * 0.2:
            return f"Fuel low: {self.current_level}L remaining."
        else:
            return f"Fuel sufficient: {self.current_level}L available."
    
    def refuel(self, amount):  # Refuel the tank
        if amount + self.current_level > self.capacity:
            return f"Cannot refuel beyond capacity. Maximum you can add is {self.capacity - self.current_level}L."
        self.current_level += amount
        return f"Refueled {amount}L. Current fuel level: {self.current_level}L."
    
    def use_fuel(self, amount):  # Use fuel and reduce percentage
        if amount > self.current_level:
            return "Not enough fuel to use the specified amount."
        self.current_level -= amount
        return f"Used {amount}L of fuel. Remaining fuel: {self.current_level}L."


# Example usage
fuel_system = Fuel(capacity=100, current_level=50)

# Check current fuel status
print(fuel_system.check_fuel())

# Refuel the tank
print(fuel_system.refuel(30))

# Use some fuel
print(fuel_system.use_fuel(20))

# Check status again
print(fuel_system.check_fuel())
