import math

def calculate_acceleration(velocity, acceleration_rate, time_passed, max_velocity):
    return min(max_velocity, velocity + acceleration_rate * time_passed)

def calculate_deceleration(velocity, deceleration_rate, time_passed):
    return max(0, velocity - deceleration_rate * time_passed)

def calculate_position_change(velocity, time_passed, angle):
    rad_angle = math.radians(angle)
    delta_x = velocity * math.cos(rad_angle) * time_passed
    delta_y = velocity * math.sin(rad_angle) * time_passed
    return delta_x, delta_y

def calculate_energy_consumption(energy, base_consumption, activity_consumption, time_passed):
    total_consumption = base_consumption * time_passed + activity_consumption * time_passed
    return max(0, energy - total_consumption)

def calculate_fuel_consumption(fuel, consumption_rate, time_passed):
    return max(0, fuel - consumption_rate * time_passed)
