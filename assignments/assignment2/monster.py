import random
from character import Character

class Monster(Character):
    def __init__(self):
        super().__init__()
        self.m_combat_strength = random.randint(10, 25)
        self.m_health_points = random.randint(40, 100)
        print(f"Monster created with {self.m_combat_strength} combat strength and {self.m_health_points} health points.")

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, new_name):
        self._name = new_name

    def monster_attacks(self, hero_health_points):
        damage = random.randint(5, self.m_combat_strength)
        print(f"Monster attacks with {damage} damage!")
        return damage

    def __del__(self):
        print("The Monster object is being destroyed by the garbage collector")
