class Fuel:
    def __init__(self, capacity=100, current_level=100):  # Initialize the Fuel class
        self.capacity = capacity  # Total fuel capacity
        self.current_level = current_level  # Current fuel level

    def check_fuel(self):  # Check fuel percentage
        fuel_percentage = (self.current_level / self.capacity)*100
        return fuel_percentage #Current fuel level

    def refuel(self, amount):  # Refuel the tank
        if amount + self.current_level > self.capacity:
            return "overflow"
        self.current_level += amount
        return "refueled"

    def use_fuel(self, amount):  # Use fuel
        if amount > self.current_level:
            return "insufficient"
        self.current_level -= amount
        return "successful"

# Main program just for try and easy for developer not use in our project
def main():
    print("<<<----Fuel System---->>>")
    capacity = int(input("Enter the total tank capacity: "))
    current_level = int(input("Enter the current fuel level: "))

    if current_level > capacity:
        print("Current fuel level cannot exceed tank capacity.")
        return

    fuel_system = Fuel(capacity, current_level)

    while True:
        print("\nMenu:")
        print("1. Check fuel level")
        print("2. Refuel")
        print("3. Use fuel")
        print("4. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            print(fuel_system.check_fuel())
        elif choice == "2":
            amount = int(input("Enter the amount of fuel to add: "))
            print(fuel_system.refuel(amount))
        elif choice == "3":
            amount = int(input("Enter the amount of fuel to use: "))
            print(fuel_system.use_fuel(amount))
        elif choice == "4":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

main()



