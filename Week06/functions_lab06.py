import random


# Will the line below print when you import function.py into main.py?
# print("Inside function.py")


# Lab 4: Question 4
def use_loot(belt, health_points):
    good_loot_options = ["Health Potion", "Leather Boots"]
    bad_loot_options = ["Poison Potion"]

    print("    |    !!You see a monster in the distance! So you quickly use your first item:")
    first_item = belt.pop(0)
    if first_item in good_loot_options:
        health_points = min(20, (health_points + 2))
        print("    |    You used " + first_item + " to up your health to " + str(health_points))
    elif first_item in bad_loot_options:
        health_points = max(0, (health_points - 2))
        print("    |    You used " + first_item + " to hurt your health to " + str(health_points))
    else:
        print("    |    You used " + first_item + " but it's not helpful")
    return belt, health_points


# Lab 4: Question 3
def collect_loot(loot_options, belt):
    ascii_image3 = """
                      @@@ @@                
             *# ,        @              
           @           @                
                @@@@@@@@                
               @   @ @% @*              
            @     @   ,    &@           
          @                   @         
         @                     @        
        @                       @       
        @                       @       
        @*                     @        
          @                  @@         
              @@@@@@@@@@@@          
              """
    print(ascii_image3)
    loot_roll = random.choice(range(1, len(loot_options) + 1))
    loot = loot_options.pop(loot_roll - 1)
    belt.append(loot)
    print("    |    Your belt: ", belt)
    return loot_options, belt


# Hero's Attack Function
def hero_attacks(combat_strength, m_health_points):
    ascii_image = """
                                @@   @@ 
                                @    @  
                                @   @   
               @@@@@@          @@  @    
            @@       @@        @ @@     
           @%         @     @@@ @       
            @        @@     @@@@@     
               @@@@@        @@       
               @    @@@@                
          @@@ @@                        
       @@     @                         
   @@*       @                          
   @        @@                          
           @@                                                    
         @   @@@@@@@                    
        @            @                  
      @              @                  

  """
    print(ascii_image)
    print("    |    Player's weapon (" + str(combat_strength) + ") ---> Monster (" + str(m_health_points) + ")")
    if combat_strength >= m_health_points:
        # Player was strong enough to kill monster in one blow
        m_health_points = 0
        print("    |    You have killed the monster")
    else:
        # Player only damaged the monster
        m_health_points -= combat_strength

        print("    |    You have reduced the monster's health to: " + str(m_health_points))
    return m_health_points


# Monster's Attack Function
def monster_attacks(m_combat_strength, health_points):
    ascii_image2 = """                                                                 
           @@@@ @                           
      (     @*&@  ,                         
    @               %                       
     &#(@(@%@@@@@*   /                      
      @@@@@.                                
               @       /                    
                %         @                 
            ,(@(*/           %              
               @ (  .@#                 @   
                          @           .@@. @
                   @         ,              
                      @       @ .@          
                             @              
                          *(*  *      
             """
    print(ascii_image2)
    print("    |    Monster's Claw (" + str(m_combat_strength) + ") ---> Player (" + str(health_points) + ")")
    if m_combat_strength >= health_points:
        # Monster was strong enough to kill player in one blow
        health_points = 0
        print("    |    Player is dead")
    else:
        # Monster only damaged the player
        health_points -= m_combat_strength
        print("    |    The monster has reduced Player's health to: " + str(health_points))
    return health_points


# Lab 5: Question 7
# Recursion
# You can choose to go crazy, but it will reduce your health points by 5
def inception_dream(num_dream_lvls):
    num_dream_lvls = int(num_dream_lvls)
    # Base Case
    if num_dream_lvls == 1:
        print("    |    You are in the deepest dream level now")
        print("    |", end="    ")
        input("Start to go back to real life? (Press Enter)")
        print("    |    You start to regress back through your dreams to real life.")
        return 2

    # Recursive Case
    else:
        # inception_dream(5)
        # 1 + inception_dream(4)
        # 1 + 1 + inception_dream(3)
        # 1 + 1 + 1 + inception_dream(2)
        # 1 + 1 + 1 + 1 + inception_dream(1)
        # 1 + 1 + 1 + 1 + 2
        return 1 + int(inception_dream(num_dream_lvls - 1))


# Function to handle saving the game
def save_game(winner, short_name=None, num_stars=None):
    if winner == "Hero":
        with open("save.txt", "a") as f:
            f.write(f"Hero {short_name} has killed a monster and gained {num_stars} stars.\n")
    elif winner == "Monster":
        with open("save.txt", "a") as f:
            f.write("Monster has killed the hero previously.\n")


# Function to load the game
def load_game():
    try:
        with open("save.txt", "r") as f:
            lines = f.readlines()
            last_line = lines[-1].strip()
            print(last_line)

            # Based on the last line, adjust the combat strengths
            if "Hero" in last_line and "stars" in last_line:
                num_stars = int(last_line.split("gained")[1].split("stars")[0].strip())
                if num_stars > 3:
                    return "increase_monster", num_stars
            elif "Monster" in last_line:
                return "increase_hero", None
            return "no_change", None
    except FileNotFoundError:
        print("No saved game found.")
        return "no_change", None


# Function for user input to ensure valid number of dream levels (0-3)
def get_dream_level_input():
    while True:
        try:
            num_levels = int(input("How many dream levels do you want to go down? (Enter a number 0-3): "))
            if 0 <= num_levels <= 3:
                return num_levels
            else:
                print("    |    Please enter a number between 0 and 3.")
        except ValueError:
            print("    |    Invalid input. Please enter a number between 0 and 3.")


# Example gameplay to test the new functionality
if __name__ == "__main__":
    # Load the saved game (if any) and adjust combat strength accordingly
    combat_adjustment, stars = load_game()
    hero_combat_strength = 5
    monster_combat_strength = 4

    if combat_adjustment == "increase_monster":
        monster_combat_strength += 1
        print("Monster's combat strength increased by 1.")
    elif combat_adjustment == "increase_hero":
        hero_combat_strength += 1
        print("Hero's combat strength increased by 1.")

    # Now, ask for dream levels input with validation
    dream_levels = get_dream_level_input()

    # Simulate a hero vs monster fight for example purposes
    health_points = 10
    monster_health = 10
    belt = ["Health Potion", "Poison Potion", "Leather Boots"]

    # Hero attacks
    monster_health = hero_attacks(hero_combat_strength, monster_health)
    if monster_health == 0:
        save_game("Hero", short_name="Alice", num_stars=4)

    # Monster attacks
    health_points = monster_attacks(monster_combat_strength, health_points)
    if health_points == 0:
        save_game("Monster")
