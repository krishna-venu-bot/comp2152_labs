import random
import functions_lab06
# Game Flow
# Define two Dice
small_dice_options = list(range(1, 7))
big_dice_options = list(range(1, 21))

# Define the Weapons
weapons = ["Fist", "Knife", "Club", "Gun", "Bomb", "Nuclear Bomb"]

# Define the Loot
loot_options = ["Health Potion", "Poison Potion", "Secret Note", "Leather Boots", "Flimsy Gloves"]
belt = []

# Define the Monster's Powers
monster_powers = {
    "Fire Magic": 2,
    "Freeze Time": 4,
    "Super Hearing": 6
}

# Load saved game state from the file
def load_game_state():
    try:
        with open('save.txt', 'r') as file:
            last_line = file.readlines()[-1].strip()
            print(f"    |    Loaded game state: {last_line}")
            return last_line
    except FileNotFoundError:
        return None

# Save the game state to the file
def save_game_state(result, short_name=None, num_stars=None):
    with open('save.txt', 'a') as file:
        if result == "hero":
            file.write(f"Hero {short_name} has killed a monster and gained {num_stars} stars.\n")
        elif result == "monster":
            file.write("Monster has killed the hero previously.\n")

# Game state adjustment based on the last outcome
def adjust_combat_strength(last_line, combat_strength, m_combat_strength):
    if last_line:
        if "Hero" in last_line and "stars" in last_line:
            num_stars = int(last_line.split()[-2])  # Extract the number of stars from the string
            if num_stars > 3:
                m_combat_strength += 1  # Increase monster's combat strength if hero won with > 3 stars
                print("    |    Monster's combat strength increased by 1 due to previous hero victory with > 3 stars.")
        elif "Monster" in last_line:
            combat_strength += 1  # Increase hero's combat strength if monster won previously
            print("    |    Hero's combat strength increased by 1 due to previous monster victory.")
    return combat_strength, m_combat_strength

# Loop to get valid input for Hero and Monster's Combat Strength
i = 0
input_invalid = True
while input_invalid and i in range(5):
    print("    ------------------------------------------------------------------")
    print("    |", end="    ")
    combat_strength = input("Enter your combat Strength (1-6): ")
    print("    |", end="    ")
    m_combat_strength = input("Enter the monster's combat Strength (1-6): ")

    # Validate input: Check if the string inputted is numeric
    if (not combat_strength.isnumeric()) or (not m_combat_strength.isnumeric()):
        # If one of the inputs are invalid, print error message and halt
        print("    |    One or more invalid inputs. Player needs to enter integer numbers for Combat Strength    |")
        i = i + 1
        continue

    # Note: Now safe to cast combat_strength to integer
    # Validate input: Check if the string inputted
    elif (int(combat_strength) not in range(1, 7)) or (int(m_combat_strength)) not in range(1, 7):
        print("    |    Enter a valid integer between 1 and 6 only")
        i = i + 1
        continue
    else:
        input_invalid = False
        break

if not input_invalid:
    input_invalid = False
    combat_strength = int(combat_strength)
    m_combat_strength = int(m_combat_strength)

    # Load the previous game state and adjust combat strengths accordingly
    last_line = load_game_state()
    combat_strength, m_combat_strength = adjust_combat_strength(last_line, combat_strength, m_combat_strength)

    # Roll for weapon
    print("    |", end="    ")
    input("Roll the dice for your weapon (Press enter)")
    weapon_roll = random.choice(small_dice_options)

    # Limit the combat strength to 6
    combat_strength = min(6, (combat_strength + weapon_roll))
    print(f"    |    The hero's weapon is {weapons[weapon_roll - 1]}")

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
    print("    |", end="    ")
    input("Roll for first item (Press enter)")
    loot_options, belt = functions_lab06.collect_loot(loot_options, belt)
    print("    ------------------------------------------------------------------")
    print("    |", end="    ")
    input("Roll for second item (Press enter)")
    loot_options, belt = functions_lab06.collect_loot(loot_options, belt)

    print("    |    You're super neat, so you organize your belt alphabetically:")
    belt.sort()
    print(f"    |    Your belt: {belt}")

    # Use Loot
    belt, health_points = functions_lab06.use_loot(belt, health_points)

    # Compare Player vs Monster's strength
    print("    ------------------------------------------------------------------")
    print(f"    |    --- You are matched in strength: {combat_strength == m_combat_strength}")
    print(f"    |    --- You have a strong player: {(combat_strength + health_points) >= 15}")

    # Roll for the monster's power
    print("    |", end="    ")
    input("Roll for Monster's Magic Power (Press enter)")
    power_roll = random.choice(list(monster_powers.keys()))
    m_combat_strength += min(6, m_combat_strength + monster_powers[power_roll])
    print(f"    |    The monster's combat strength is now {m_combat_strength} using the {power_roll} magic power")

    # Call Recursive function
    print("    |", end="    ")
    num_dream_lvls = input("How many dream levels do you want to go down? (Enter a number 0-3)")
    if num_dream_lvls not in ['0', '1', '2', '3']:
        print("    |    Invalid input, must enter a number between 0 and 3.")
    else:
        health_points -= 1
        crazy_level = functions_lab06.inception_dream(int(num_dream_lvls))
        combat_strength += crazy_level
        print(f"combat strength: {combat_strength}")
        print(f"health points: {health_points}")

    # Fight Sequence
    print("    ------------------------------------------------------------------")
    print("    |    You meet the monster. FIGHT!!")
    while m_health_points > 0 and health_points > 0:
        # Fight Sequence
        print("    |", end="    ")

        # Lab 5: Question 5:
        input("Roll to see who strikes first (Press Enter)")
        attack_roll = random.choice(small_dice_options)
        if not (attack_roll % 2 == 0):
            print("    |", end="    ")
            input("You strike (Press enter)")
            m_health_points = functions_lab06.hero_attacks(combat_strength, m_health_points)
            if m_health_points == 0:
                save_game_state("hero", short_name, 3)
                break
            else:
                print("    |", end="    ")
                print("------------------------------------------------------------------")
                input("    |    The monster strikes (Press enter)!!!")
                health_points = functions_lab06.monster_attacks(m_combat_strength, health_points)
                if health_points == 0:
                    save_game_state("monster")
                    break
                else:
                    num_stars = 2
        else:
            print("    |", end="    ")
            input("The Monster strikes (Press enter)")
            health_points = functions_lab06.monster_attacks(m_combat_strength, health_points)
            if health_points == 0:
                save_game_state("monster")
                break
            else:
                print("    |", end="    ")
                print("------------------------------------------------------------------")
                input("The hero strikes!! (Press enter)")
                m_health_points = functions_lab06.hero_attacks(combat_strength, m_health_points)
                if m_health_points == 0:
                    save_game_state("hero", short_name, 3)
                    break
                else:
                    num_stars = 2

    # Final Score Display
    tries = 0
    input_invalid = True
    while input_invalid and tries in range(5):
        print("    |", end="    ")
        hero_name = input("Enter your Hero's name (in two words)")
        name = hero_name.split()
        if len(name) != 2:
            print("    |    Please enter a name with two parts (separated by a space)")
            tries += 1
        else:
            if not name[0].isalpha() or not name[1].isalpha():
                print("    |    Please enter an alphabetical name")
                tries += 1
            else:
                short_name = name[0][0:2:1] + name[1][0:1:1]
                print(f"    |    I'm going to call you {short_name} for short")
                input_invalid = False

    if not input_invalid:
        stars_display = "*" * num_stars
        print(f"    |    Hero {short_name} gets <{stars_display}> stars")
