import random

numLives = 10
mNumLives = 12

diceOptions = [1, 2, 3, 4, 5, 6]
combatStrength = int(input("Enter your combat Strength: (Number between 1-6) "))

if (combatStrength < 1 or combatStrength > 6):
    print("Input must be an integer between 1-6")
else:
    mCombatStrength = int(input("Enter the monster's combat Strength: "))

    if (mCombatStrength < 1 or mCombatStrength > 6):
        print("Input must be an integer between 1-6")
    else:
        weapons = ["Fist", "Knife", "Club", "Gun", "Bomb", "Nuclear bomb"]

        input("Roll the dice for your health points (Press enter)")
        healthPoints = random.choice(diceOptions)
        print("You rolled " + str(healthPoints) + " health points")

        input("Roll the dice for the monster's health points (Press enter)")
        mHealthPoints = random.choice(diceOptions)
        print("You rolled " + str(mHealthPoints) + " health points for the monster")

        input("Roll the dice to see if you find a healing potion (Press enter)")
        healingPotion = random.choice([0, 1])
        print("Have you found a healing potion?: " + str(bool(healingPotion)))

        weaponRoll = random.choice([0, 1, 2, 3, 4, 5])

        combatStrength += weaponRoll

        print("The name of the hero's weapon is: " + weapons[weaponRoll])

        if (weaponRoll <= 2):
            print("You rolled a weak weapon, friend")
        elif (weaponRoll <= 4):
            print("Your weapon is meh")
        else:
            print("Nice weapon, friend! ")

        if (weapons[weaponRoll] != "Fist"):
            print("Thank goodness you didn't roll the Fist...")

        input("Analyze the roll (Press enter)")

        print("--- You are matched in strength: " + str(combatStrength == mCombatStrength))

        print("--- You have a strong player: " + str((combatStrength + healthPoints) >= 15))

        print("--- Remember to take a healing potion!: " + str(healingPotion == 1 and healthPoints <= 6))

        print("--- Phew, you have a healing potion: " + str(
            not (
                    healthPoints < mCombatStrength
            )
            and
            healingPotion == 1
        ))

        print("--- Things are getting dangerous: " + str(healingPotion == 0 or healthPoints == 1))

        print("--- Is it possible to roll 0 in the dice?: " + str(0 in diceOptions))

        if healthPoints >= 5:
            print("--- Your health is ok")
        elif healingPotion == 1:
            healingPotion = 0
            healthPoints = 6
            print("--- Using your healing potion... Your Health Points is now full at " + str(healthPoints))
        else:
            print("--- Your health is low at " + str(healthPoints) + " and you have no healing potions available!")

        print("You meet the monster. FIGHT!!")
        input("You strike first (Press enter)")

        print("Your sword (" + str(combatStrength) + ") ---> Monster (" + str(mHealthPoints) + ")")
        if combatStrength >= mHealthPoints:
            mHealthPoints = 0
            print("You've killed the monster")
        else:
            mHealthPoints -= combatStrength
            print("You've reduced the monster's health to: " + str(mHealthPoints))

        print("The monster strikes!!!")
        print("Monster's Claw (" + str(mCombatStrength) + ") ---> You (" + str(healthPoints) + ")")
        if mCombatStrength >= healthPoints:
            healthPoints = 0
            print("You're dead")
        else:
            healthPoints -= mCombatStrength
            print("The monster has reduced your health to: " + str(healthPoints))

        for j in range(1, 11):
            print(f"--- Round {j} ---")

            heroRoll = random.choice(diceOptions)
            monsterRoll = random.choice(diceOptions)

            combatStrength += heroRoll
            mCombatStrength += monsterRoll

            weaponRoll = random.choice([0, 1, 2, 3, 4, 5])

            print(f"Hero rolls a {heroRoll}, Monster rolls a {monsterRoll}")
            print(f"Hero's combat strength: {combatStrength}")
            print(f"Monster's combat strength: {mCombatStrength}")
            print(f"Weapon used by Hero: {weapons[weaponRoll]}")

            if combatStrength > mCombatStrength:
                print("Hero wins this round!")
            elif combatStrength < mCombatStrength:
                print("Monster wins this round!")
            else:
                print("It's a draw!")

            if j == 10:
                print("Battle Truce! The fight ends here.")
                break
