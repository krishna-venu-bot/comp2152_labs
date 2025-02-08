while True:
    hero_input = input("Enter your Hero's name (in two words): ").strip()

    if len(hero_input.split()) == 2 and all(word.isalpha() for word in hero_input.split()):
        words = hero_input.split()
        short_name = words[0][:2] + words[1][0]
        print("Hero's short name:", short_name)
        break
    else:
        print("Invalid input. Please enter exactly two words using only letters.")

stars_display = f"*** {short_name} ***"
print(stars_display)

# Assuming functions_lab05.py is available
from functions_lab05 import collect_loot, use_loot

belt = collect_loot(["Health Potion", "Poison Potion", "Leather Boots", "Gold Coin"])
print("Loot collected:", belt)

health_points = use_loot(belt, 10)  # Starting health points
print("Updated health points:", health_points)

import random

if random.randint(1, 2) == 1:
    print("Hero attacks first!")
    print("Hero attacks the monster!")
    print("Monster counter-attacks!")
else:
    print("Monster attacks first!")
    print("Monster attacks the hero!")
    print("Hero counter-attacks!")


def inception_dream():
    answer = input("Do you want to dive deeper into the dream? (yes/no): ").strip().lower()
    if answer == "yes":
        return 1 + inception_dream()
    else:
        return 2


crazy_level = inception_dream()

health_points -= 1
hero_combat_strength = 5 + crazy_level
print("After the dream:")
print("Health Points:", health_points)
print("Hero Combat Strength:", hero_combat_strength)
