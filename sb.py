import random

class Shield:
    def __init__(self, health):
        self.health = health

    def absorb_hit(self, damage):
        self.health -= damage
        if self.health <= 0:
            print("Shield is down! Repair needed!")
            self.health = 0

class Comet:
    def __init__(self, velocity, size, destruction, position_x, position_y):
        self.velocity = velocity
        self.size = size
        self.destruction = destruction
        self.position_x = position_x
        self.position_y = position_y

    def generate_random():
        return Comet(
            velocity=random.randint(22000, 45000),
            size=random.randint(20, 62),
            destruction=random.randint(50, 200),
            position_x=random.randint(0, 800),
            position_y=random.randint(0, 600),
        )

class Weapon:
    def __init__(self, damage):
        self.damage = damage

    def fire(self, target):
        print(f"Firing at target with destruction value {target.destruction}")
        if target.destruction <= self.damage:
            print("Target destroyed!")
            return True
        else:
            print("Target is too strong!")
            return False

# Example Game Logic
shield = Shield(health=100)
weapon = Weapon(damage=75)

# Generate a random comet
comet = Comet.generate_random()
print(f"A comet is approaching! Destruction: {comet.destruction}")

# Decide to use weapon or shield
if comet.destruction <= weapon.damage:
    if weapon.fire(comet):
        print("Threat neutralized with weapons!")
else:
    print("Using shield to absorb the hit.")
    shield.absorb_hit(comet.destruction)
    print(f"Shield health remaining: {shield.health}")
