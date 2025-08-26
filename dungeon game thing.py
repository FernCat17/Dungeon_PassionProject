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

path_1 = int(input("You see two paths... Input 1 to go left, Input 2 to go right: "))

if path_1 == 1:
    print("You stumble into a pack of hungry lions! You feel their eyes staring at you with laser focus")
    input("Press a key to continue: ")
elif path_1 == 2:
    print("You run into a gang of goblins! You sense an ominous aura coming from them")
    input("Press a key to continue: ")
else:
    print("Invalid")
    path_1 = int(input("You see two paths... Input 1 to go left, Input 2 to go right: "))

if path_1 == 1:
    lion_strength = random.randint(3, 6)  
    print("The lions leap at you with strength", lion_strength, "!")
    if strength >= lion_strength:
        print("You fight bravely and defeat the lions!")
    else:
        print("The lions overpower you...")
        exit()

elif path_1 == 2:
    goblin_magic = random.randint(1, 6)  
    print("The goblins attack with magic power", goblin_magic, "!")
    if mana >= goblin_magic:
        print("You cast a spell and blast the goblins back!")
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
    print("You team with the wizard and continue moving foward")
    input("Press a key to continue: ")
    print("Your current stats are")
    input("Press a key to continue: ")
    print("Your current mana number is", mana)
    print("Your current strength number is", strength)
else:
    strength += 2
    print("You team with the knight and continue moving foward")
    input("Press a key to continue: ")
    print("Your current stats are")
    input("Press a key to continue: ")
    print("Your current mana number is", mana)
    print("Your current strength number is", strength)


input("Press a button to end the game: ")
