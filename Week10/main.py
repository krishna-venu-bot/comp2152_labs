import random
import os
import platform
from hero import Hero
from monster import Monster
import functions


def main():
    print(f"Operating System: {os.name}")
    print(f"Python Version: {platform.python_version()}")

    # Create Hero and Monster objects
    hero = Hero()
    monster = Monster()

    # Game logic can proceed here where hero and monster interact with each other
    # For example, using hero's attack function
    monster_health = monster.m_health_points
    hero_attack = hero.hero_attacks(monster_health)
    monster.m_health_points = monster_health - hero_attack

    # Continue game flow...


if __name__ == "__main__":
    main()
