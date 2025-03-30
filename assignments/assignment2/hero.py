import random
from character import Character

class Hero(Character):
    def __init__(self):
        super().__init__()
        self.combat_strength = random.randint(15, 30)
        self.health_points = random.randint(60, 120)
        print(f"Hero created with {self.combat_strength} combat strength and {self.health_points} health points.")

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, new_name):
        self._name = new_name

    def hero_attacks(self, monster_health_points):
        damage = random.randint(5, self.combat_strength)
        print(f"Hero attacks with {damage} damage!")
        return damage

    def __del__(self):
        print("The Hero object is being destroyed by the garbage collector")
