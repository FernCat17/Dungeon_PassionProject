import random

input("Press enter to start: ")

dead = 0
if dead == 1:
    exit()

Name = input("Young lad, what's your name?: ")
print("Well", Name, ",You have been trapped in this dungeon and now you must escape!")
input("Press enter to continue: ")

# OG STATS
mana = 0
while mana < 1 or mana > 6:
    try:
        mana = int(input("Well choose your mana number 1-6 but remember the more mana you have the weaker your physical strength: "))
        if mana < 1 or mana > 6:
            print("Invalid choice! Pick a number between 1 and 6.")
    except ValueError:
        print("That’s not a number! Enter 1-6.")
        mana = 0

strength = 7 - mana
print("This is your strength number", strength)
input("Press enter to continue: ")

# first path player goes
path_1 = 0
while path_1 not in [1, 2]:
    try:
        path_1 = int(input("You see two paths... Input 1 to go left, Input 2 to go right: "))
        if path_1 not in [1, 2]:
            print("Invalid choice! Please input 1 or 2.")
    except ValueError:
        print("That's not a number! Input 1 or 2.")

# enemies based on path
if path_1 == 1:
    print("You stumble into a pack of hungry lions! Their eyes lock onto you.")
    enemy_name = "Lions"
    enemy_hp = random.randint(30, 40)
else:
    print("You run into a gang of goblins! You sense an ominous aura.")
    enemy_name = "Goblins"
    enemy_hp = random.randint(30, 40)
input("Press enter to continue: ")

# Player combat stats
hp = 100
defending = False

# Combat loop
while hp > 0 and enemy_hp > 0:
    print("Your HP:", hp, "|", enemy_name, "HP:", enemy_hp)
    action = 0
    while action not in [1, 2, 3]:
        try:
            action = int(input("Choose your action: 1-Attack  2-Defend  3-Cast Spell: "))
            if action not in [1, 2, 3]:
                print("Invalid choice! Pick 1, 2, or 3.")
        except ValueError:
            print("That's not a number! Pick 1, 2, or 3.")

    # Player action choice
    if action == 1:
        attack_dmg = strength * random.randint(2, 5)
        enemy_hp -= attack_dmg
        print("You attack and deal", attack_dmg, "damage!")
    elif action == 2:
        defending = True
        print("You brace yourself to defend against the next attack!")
    elif action == 3:
        spell_dmg = mana * random.randint(3, 6)
        enemy_hp -= spell_dmg
        print("You cast a spell and deal", spell_dmg, "damage!")

    # Enemy attack
    if enemy_hp > 0:
        enemy_attack = random.randint(5, 12)
        if defending:
            enemy_attack = enemy_attack // 2
            defending = False
        hp -= enemy_attack
        print("The", enemy_name, "strike back for", enemy_attack, "damage! Your HP is now", hp)

# End combat
if hp <= 0:
    print("The", enemy_name, "have defeated you...")
    exit()
else:
    print("You have defeated the", enemy_name, "! You continue your journey.")
input("Press enter to continue: ")

# Sword room
print("You find a blackish-red sword on the floor")
input("Press enter to continue: ")

sword_choice = int(input("Input 1 to pick up the sword Input 2 to leave it: "))
if sword_choice == 1:
    print("You pick up the sword and feel your strength increase by 2 but your mana decrease by 3")
    mana -= 3
    strength += 2
    input("Press enter to continue: ")
    print("This is your new mana number", mana)
    print("This is your new strength number", strength)
else:
    print("You leave the sword and keep moving")

# Riddle room
print("You walk into a room there is a riddle on the wall:")
input("Press enter to continue: ")
print("I can devour kingdoms, swallow the sun, yet live in shadows feared, by everyone. Who am I? Guess wrong and you will take your final step")
riddle_answer = input("Input your answer: ")
if riddle_answer.lower() == "darkness":
    print("You live to take another step")
else:
    print("Spikes impale you to death...")
    exit()
input("Press enter to continue: ")

# Party member room
print("You find a wizard and a knight. One will help you boost mana, the other strength.")
party_member = 0
while party_member not in [1, 2]:
    try:
        party_member = int(input("Choose your party member: 1-Wizard 2-Knight: "))
        if party_member not in [1, 2]:
            print("Pick 1 or 2!")
    except ValueError:
        print("That's not a number! Pick 1 or 2.")

if party_member == 1:
    mana += 2
    print("You team with the wizard. Mana increased by 2.")
else:
    strength += 2
    print("You team with the knight. Strength increased by 2.")
print("Your current stats: Mana =", mana, "Strength =", strength)
input("Press enter to continue: ")

# Corrupted mage room (combat)
print("You encounter a group of corrupted mages!")
enemy_name = "Corrupted Mages"
enemy_hp = random.randint(25, 45)
hp_defending = False

while hp > 0 and enemy_hp > 0:
    print("Your HP:", hp, "|", enemy_name, "HP:", enemy_hp)
    action = 0
    while action not in [1, 2, 3]:
        try:
            action = int(input("Choose your action: 1-Attack 2-Defend 3-Cast Spell: "))
            if action not in [1, 2, 3]:
                print("Pick 1, 2, or 3!")
        except ValueError:
            print("Pick a number 1, 2, or 3!")

    if action == 1:
        attack_dmg = strength * random.randint(2, 5)
        enemy_hp -= attack_dmg
        print("You attack and deal", attack_dmg, "damage!")
    elif action == 2:
        hp_defending = True
        print("You brace yourself!")
    elif action == 3:
        spell_dmg = mana * random.randint(3, 6)
        enemy_hp -= spell_dmg
        print("You cast a spell and deal", spell_dmg, "damage!")

    # Enemy attack
    if enemy_hp > 0:
        enemy_attack = random.randint(6, 12)
        if hp_defending:
            enemy_attack = enemy_attack // 2
            hp_defending = False
        hp -= enemy_attack
        print("The", enemy_name, "attack for", enemy_attack, "damage! Your HP is now", hp)

if hp <= 0:
    print("The", enemy_name, "have defeated you...")
    exit()
else:
    print("You have defeated the", enemy_name, "!")
    input("Press enter to continue: ")

print("The adventure continues...")
input("Press enter to end the game: ")
