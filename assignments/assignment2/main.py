import random
import os
import platform

# Define Dice
small_dice_options = list(range(1, 7))  # For combat and weapon rolls
big_dice_options = list(range(1, 21))  # For health points

# Define Weapons and Loot
weapons = ["Fist", "Knife", "Club", "Gun", "Bomb", "Nuclear Bomb"]
loot_options = ["Health Potion", "Poison Potion", "Secret Note", "Leather Boots", "Flimsy Gloves"]
belt = []

# Define Monster Powers
monster_powers = {
    "Fire Magic": 2,
    "Freeze Time": 4,
    "Super Hearing": 6
}

# Define the number of stars the player will get
num_stars = 0

# Define functions

def adjust_combat_strength(combat_strength, m_combat_strength):
    """Adjust combat strength based on the hero's and monster's stats."""
    print(f"Combat strength adjusted: Hero's combat strength: {combat_strength}, Monster's combat strength: {m_combat_strength}")

def collect_loot(loot_options, belt):
    loot_roll = random.choice(range(1, len(loot_options) + 1))  # Picking a random loot option
    loot = loot_options.pop(loot_roll - 1)  # Remove the loot from the options list
    belt.append(loot)  # Add the loot to the player's belt
    print(f"    |    You find a {loot}")
    return loot_options, belt  # Returning updated loot options and belt


def use_loot(belt, health_points):
    """Use loot from the belt."""
    print(f"Your belt: {belt}")
    if "Health Potion" in belt:
        health_points += 5  # Using health potion increases health by 5
        print("You used a Health Potion! Your health is now: " + str(health_points))
        belt.remove("Health Potion")  # Health potion used
    return belt, health_points

def inception_dream(num_dream_lvls):
    """Inception dream sequence that adjusts combat strength based on dream levels."""
    crazy_level = num_dream_lvls * 2  # Increase combat strength per dream level
    print(f"Dream level {num_dream_lvls} gives {crazy_level} extra combat strength.")
    return crazy_level

def hero_attacks(combat_strength, m_health_points):
    """Hero's attack on the monster."""
    attack_damage = random.randint(1, combat_strength)
    print(f"Hero attacks with damage: {attack_damage}")
    m_health_points -= attack_damage
    return m_health_points

def monster_attacks(m_combat_strength, health_points):
    """Monster's attack on the hero."""
    attack_damage = random.randint(1, m_combat_strength)
    print(f"Monster attacks with damage: {attack_damage}")
    health_points -= attack_damage
    return health_points

def main():
    print(f"Operating System: {os.name}")
    print(f"Python Version: {platform.python_version()}")

    # Loop to get valid input for Hero and Monster's Combat Strength
    input_invalid = True
    i = 0
    while input_invalid and i < 5:
        print("    ------------------------------------------------------------------")
        combat_strength = input("Enter your combat Strength (1-6): ")
        m_combat_strength = input("Enter the monster's combat Strength (1-6): ")

        # Validate input: Check if the string inputted is numeric
        if (not combat_strength.isnumeric()) or (not m_combat_strength.isnumeric()):
            print("    |    One or more invalid inputs. Player needs to enter integer numbers for Combat Strength")
            i += 1
            continue

        # Validate input range
        if (int(combat_strength) not in range(1, 7)) or (int(m_combat_strength) not in range(1, 7)):
            print("    |    Enter a valid integer between 1 and 6 only")
            i += 1
            continue

        else:
            input_invalid = False
            combat_strength = int(combat_strength)
            m_combat_strength = int(m_combat_strength)

            break

    if not input_invalid:
        # Roll for weapon
        print("    |", end="    ")
        input("Roll the dice for your weapon (Press enter)")
        weapon_roll = random.choice(small_dice_options)
        combat_strength = min(6, (combat_strength + weapon_roll))
        print(f"    |    The hero's weapon is {weapons[weapon_roll - 1]}")

        # Adjust combat strength based on the weapon roll and previous combat strength
        adjust_combat_strength(combat_strength, m_combat_strength)

        # Weapon Roll Analysis
        print("    ------------------------------------------------------------------")
        print("    |", end="    ")
        input("Analyze the Weapon roll (Press enter)")
        if weapon_roll <= 2:
            print("--- You rolled a weak weapon, friend")
        elif weapon_roll <= 4:
            print("--- Your weapon is meh")
        else:
            print("--- Nice weapon, friend!")

        if weapons[weapon_roll - 1] != "Fist":
            print("    |    --- Thank goodness you didn't roll the Fist...")

        # Roll for player health points
        print("    |", end="    ")
        input("Roll the dice for your health points (Press enter)")
        health_points = random.choice(big_dice_options)
        print(f"    |    Player rolled {health_points} health points")

        # Roll for monster health points
        print("    |", end="    ")
        input("Roll the dice for the monster's health points (Press enter)")
        m_health_points = random.choice(big_dice_options)
        print(f"    |    Player rolled {m_health_points} health points for the monster")

        # Collect Loot
        print("    ------------------------------------------------------------------")
        print("    |    !!You find a loot bag!! You look inside to find 2 items:")

        # Collect Loot First time
        print("    |", end="    ")
        input("Roll for first item (enter)")
        loot_options, belt = collect_loot(loot_options, belt)

        # Collect Loot Second time
        print("    |", end="    ")
        input("Roll for second item (Press enter)")
        loot_options, belt = collect_loot(loot_options, belt)

        print("    |    You're super neat, so you organize your belt alphabetically:")
        belt.sort()
        print(f"    |    Your belt: {belt}")

        # Use Loot
        belt, health_points = use_loot(belt, health_points)

        # Roll for the monster's magic power
        print("    ------------------------------------------------------------------")
        print("    |", end="    ")
        input("Roll for Monster's Magic Power (Press enter)")
        power_roll = random.choice(list(monster_powers.keys()))
        m_combat_strength += min(6, m_combat_strength + monster_powers[power_roll])
        print(f"    |    The monster's combat strength is now {m_combat_strength} using the {power_roll} magic power")

        # Ask for dream levels
        print("    ------------------------------------------------------------------")
        num_dream_lvls = -1  # Initialize the number of dream levels
        while (num_dream_lvls < 0 or num_dream_lvls > 3):
            print("    |", end="    ")
            num_dream_lvls = input("How many dream levels do you want to go down? (Enter a number 0-3)")

            if ((num_dream_lvls == "")):
                num_dream_lvls = -1
                print("Number entered must be a whole number between 0-3 inclusive, try again")

            else:
                num_dream_lvls = int(num_dream_lvls)

                if ((num_dream_lvls < 0) or (num_dream_lvls > 3)):
                    num_dream_lvls = -1
                    print("Number entered must be a whole number between 0-3 inclusive, try again")
                elif (num_dream_lvls != 0):
                    health_points -= 1
                    crazy_level = inception_dream(num_dream_lvls)
                    combat_strength += crazy_level
                    print(f"combat strength: {combat_strength}")
                    print(f"health points: {health_points}")
            print(f"num_dream_lvls: {num_dream_lvls}")

        # Fight Sequence
        print("    ------------------------------------------------------------------")
        print("    |    You meet the monster. FIGHT!!")
        while m_health_points > 0 and health_points > 0:
            print("    |", end="    ")

            input("Roll to see who strikes first (Press Enter)")
            attack_roll = random.choice(small_dice_options)
            if attack_roll % 2 != 0:
                print("    |", end="    ")
                input("You strike (Press enter)")
                m_health_points = hero_attacks(combat_strength, m_health_points)
                if m_health_points == 0:
                    num_stars = 3
                else:
                    print("    |", end="    ")
                    print("------------------------------------------------------------------")
                    input("    |    The monster strikes (Press enter)!!!")
                    health_points = monster_attacks(m_combat_strength, health_points)
                    if health_points == 0:
                        num_stars = 1
                    else:
                        num_stars = 2
            else:
                print("    |", end="    ")
                input("The Monster strikes (Press enter)")
                health_points = monster_attacks(m_combat_strength, health_points)
                if health_points == 0:
                    num_stars = 1
                else:
                    print("    |", end="    ")
                    print("------------------------------------------------------------------")
                    input("The hero strikes!! (Press enter)")
                    m_health_points = hero_attacks(combat_strength, m_health_points)
                    if m_health_points == 0:
                        num_stars = 3
                    else:
                        num_stars = 2

        if m_health_points <= 0:
            winner = "Hero"
        else:
            winner = "Monster"

        # Final Score Display
        tries = 0
        input_invalid = True
        while input_invalid and tries < 5:
            print("    |", end="    ")

            hero_name = input("Enter your Hero's name (in two words): ")
            name = hero_name.split()
            if len(name) != 2:
                print("    |    Please enter a name with two parts (separated by a space)")
                tries += 1
            else:
                if not name[0].isalpha() or not name[1].isalpha():
                    print("    |    Please enter an alphabetical name")
                    tries += 1
                else:
                    short_name = name[0][0:2] + name[1][0:1]
                    print(f"    |    I'm going to call you {short_name} for short")
                    input_invalid = False

        if not input_invalid:
            stars_display = "*" * num_stars
            print(f"    |    Hero {short_name} gets <{stars_display}> stars")

            # Save game result
            with open('game_save.txt', 'w') as f:
                f.write(f"{winner} wins! Hero: {short_name}, Stars: {num_stars}")

if __name__ == "__main__":
    main()
