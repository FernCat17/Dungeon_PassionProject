import random

dead = 0

if dead == 1:
    exit()

Name = input("Young lad whats your name?: ")
print("Well", Name, ",You have been trapped in this dungeon and now you must escape!")

input("Press a key to continue: ")

mana = 0  
while mana < 1 or mana > 6:
    try:
        mana = int(input("Well choose your mana number 1-6 but remember the more mana you have the weaker your physical strength: "))
        if mana < 1 or mana > 6:
            print("Invalid choice! Pick a number between 1 and 6.")
    except ValueError:
        print("That’s not a number! Please enter 1, 2, 3, 4, 5, or 6.")
        mana = 0  

strength = 7 - mana
print("This is your strength number", strength)

input("Press a key to continue: ")

path_1 = 0
while path_1 != 1 and path_1 != 2:
    try:
        path_1 = int(input("You see two paths... Input 1 to go left, Input 2 to go right: "))
        if path_1 != 1 and path_1 != 2:
            print("Invalid choice! Please input 1 or 2.")
    except ValueError:
        print("That’s not a number! Please input 1 or 2.")

if path_1 == 1:
    print("You stumble into a pack of hungry lions! You feel their eyes staring at you with laser focus")
    input("Press a key to continue: ")
elif path_1 == 2:
    print("You run into a gang of goblins! You sense an ominous aura coming from them")
    input("Press a key to continue: ")

lion_strength = random.randint(3, 6) 

if path_1 == 1:
    lion_pseudo_mana = lion_strength - 1
    print("The lions leap at you with strength", lion_strength, "!")
    if strength >= lion_strength or mana >= lion_pseudo_mana:
        print("You fight bravely and defeat the lions!")
    else:
        print("The lions overpower you...")
        exit()

elif path_1 == 2:
    goblin_magic = random.randint(1, 6)  
    goblin_pseudo_strength = goblin_magic - 1
    print("The goblins attack with magic power", goblin_magic, "!")
    if mana >= goblin_magic or strength >= goblin_pseudo_strength:
        print("You barely defeat the goblins and continue moving...")
    else:
        print("The goblins swarm you and rip off your head...")
        exit()

input("Press a key to continue: ")

print("You find a blackish-red sword on the floor")
input("Press a key to continue: ")

sword_choice = int(input("Input 1 to pick up the sword Input 2 to leave it: "))
if sword_choice == 1:
    print("You pick up the sword and feel your strength increase by 2 but your mana decrease by 3")
    mana -= 3
    strength += 2
    input("Press a key to continue: ")
    print("This is your new mana number", mana)
    print("This is your new strength number", strength)
else:
    print("You leave the sword and keep moving")

print("You walk into a room there is a riddle on the wall:")
input("Press a key to continue: ")
print("I can devour kingdoms, swallow the sun, yet live in shadows feared, by everyone. Who am I? Guess wrong and you will take your final step")
riddle_answer = input("Input your answer: ")
if riddle_answer.lower() == "darkness":
    print("You live to take another step")
else:
    print("Spikes impale you to death...")
    exit()
    input("Press a key to continue: ")

print("You Continue walking... you find a room with two people, one a knight, the other a wizard")
input("Press a key to continue: ")
print("The wizard promises to help you fight and provide you with +2 mana but the knight says he will help you fight providing plus 2 strength.")
party_member = int(input("Which party member to choose Input 1 for wizard . Input 2 for Knight: "))

if party_member == 1:
    mana += 2
    print("You team with the wizard and continue moving forward")
    input("Press a key to continue: ")
    print("Your current stats are")
    print("Your current mana number is", mana)
    print("Your current strength number is", strength)
    input("Press a key to continue: ")
else:
    strength += 2
    print("You team with the knight and continue moving forward")
    input("Press a key to continue: ")
    print("Your current stats are")
    input("Press a key to continue: ")
    print("Your current mana number is", mana)
    print("Your current strength number is", strength)

print("You continue walking with them...")
input("Press a key to continue: ")
print("You continue walking and find a group of corrupted mages")
corrupted_mage_mana = random.randint(4, 6)
corrupted_mage_pseudostrength = corrupted_mage_mana + 2

if mana >= corrupted_mage_mana or strength >= corrupted_mage_pseudostrength:
    print("With a final, desperate strike, you vanquish the mages, yet they leave you weakened, stealing 1 mana!")
    mana -= 1
    print("Your current stats are")
    print("Your current mana number is", mana)
    print("Your current strength number is", strength)
    input("Press a key to continue: ")
else:
    print("The mages drain your life force and you die")
    input("Press a key to continue: ")
    exit()

print("You walk into a dimly lit chamber. The floor is covered in glowing runes that pulse ominously.")
input("Press a key to continue: ")

print("A magical trap activates! Spikes shoot from the floor and fire shoots from the walls!")
input("Press a key to continue: ")

print("You notice a lever on the wall that might disable the trap...")
input("Press a key to continue: ")

if strength >= 5 or mana >= 4:
    if strength >= 5 and mana >= 4:
        print("Using your combined strength and magic, you easily disable the trap!")
    elif strength >= 5:
        print("You yank the lever down with sheer force, halting the trap just in time!")
    else:
        print("You cast a precise spell to neutralize the trap, barely avoiding the spikes!")
else:
    print("You fail to reach the lever or cast a spell in time...")
    print("The trap hits you, and you die instantly...")
    exit()

input("Press a key to continue: ")

print("You enter a room filled with three chests. One of them holds a powerful treasure, the others are empty or trapped.")
input("Press a key to continue: ")


good_chest = random.randint(1, 3)

chest_choice = 0
while chest_choice not in [1, 2, 3]:
    try:
        chest_choice = int(input("Choose a chest to open (1, 2, or 3): "))
        if chest_choice not in [1, 2, 3]:
            print("Invalid choice! Pick 1, 2, or 3.")
    except ValueError:
        print("That’s not a number! Pick 1, 2, or 3.")

if chest_choice == good_chest:
    print("You open the chest and find a glowing relic! Your strength and mana increase by 2!")
    strength += 2
    mana += 2
    print("Your current stats are:")
    print("Strength:", strength)
    print("Mana:", mana)
else:
    print("The chest is empty! You find nothing useful, You continue walking disappointed.")

input("Press a key to continue: ")

print("You enter a room with a giant, enchanted mirror that shows two possible futures of yourself.")
input("Press a key to continue: ")

print("One reflection is powerful in strength, the other in mana.")
input("Press a key to continue: ")

mirror_choice = 0
while mirror_choice != 1 and mirror_choice != 2:
    try:
        mirror_choice = int(input("Which reflection do you follow? Input 1 for Strength, Input 2 for Mana: "))
        if mirror_choice != 1 and mirror_choice != 2:
            print("Invalid choice! Please input 1 or 2.")
    except ValueError:
        print("That's not a number! Please input 1 or 2.")

if mirror_choice == 1:
    strength += 3
    mana -= 1
    print("You follow the strength reflection. Your strength increases by 3 but your mana decreases by 1.")
elif mirror_choice == 2:
    mana += 3
    strength -= 1
    print("You follow the mana reflection. Your mana increases by 3 but your strength decreases by 1.")

input("Press a key to continue: ")
print("Your current stats are:")
print("Mana:", mana)
print("Strength:", strength)

input("Press a button to end the game: ")
