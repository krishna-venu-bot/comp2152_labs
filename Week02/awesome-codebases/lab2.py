import random

weapons = ["Fist", "Knife", "Club", "Gun", "Bomb", "Nuclear bomb"]

def roll_dice():
    try:
        user_choice = input("Enter 'r' to roll the dice or enter a custom weapon roll (1-6): ").strip().lower()

        if user_choice == 'r':
            weaponRoll = random.randint(1, 6)
        else:
            weaponRoll = int(user_choice)
            if weaponRoll < 1 or weaponRoll > 6:
                raise ValueError("Invalid number! Please enter a number between 1 and 6.")

        return weaponRoll

    except Exception as e:
        print(f"Error occurred: {e}")
        return None


def combat_strength():
    try:
        weaponRoll = roll_dice()

        if weaponRoll is None:
            return

        hero_combat_strength = 10

        hero_combat_strength += weaponRoll

        weapon = weapons[weaponRoll - 1]

        print(f"Your weapon is: {weapon}")

        if weaponRoll <= 2:
            print("You rolled a weak weapon, friend.")
        elif weaponRoll <= 4:
            print("Your weapon is meh.")
        else:
            print("Nice weapon, friend!")

        if weapon != "Fist":
            print("Thank goodness you didn't roll the Fist...")

    except ValueError as e:
        # Handle invalid input
        print(f"Error: {e}")

if __name__ == "__main__":
    combat_strength()
