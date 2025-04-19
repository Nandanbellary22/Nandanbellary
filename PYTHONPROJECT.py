import random
import time
import sys
def print_line():
    print("-" * 50)
def start_adventure():
    print("\nWelcome traveller, your journey awaits!!")
    print("You find yourself in front of a dark forest. Your goal is to find the treasure guarded by a vicious dragon!.")
    print_line()
    while True:
        time.sleep(1)
        print("\nDo you want to enter the jungle??")
        print("1. Yes")
        print("2. No")
        print('Type 1 or 2')
        print_line()
        time.sleep(1)

        choice = int(input("Enter your choice: "))

        if choice == 1:
            explore_forest()
        elif choice == 2:
            print("Thanks for playing!")
            print_line()
            break
        else:
            print("Invalid choice. Please choose again.")
            print_line()
def fight_dragon():
    print_line()
    print("You finally reach the dragon's lair!")
    print("The dragon roars and prepares to attack.")

    player_health = 100
    dragon_health = 150

    while player_health > 0 and dragon_health > 0:
        print_line()
        print(f"Your health: {player_health}")
        print(f"Dragon's health: {dragon_health}")
        action = input("Do you want to (1) attack or (2) defend? (1/2): ")
        if action == "1":
            damage = random.randint(17, 30)
            dragon_health -= damage
            print(f"You hit the dragon for {damage} damage!")
        else:
            print("You brace yourself for the dragon's attack.")

        dragon_damage = random.randint(5, 25)
        if action == "2":
            dragon_damage //= 2
            print("Your defense reduces the damage!")
        player_health -= dragon_damage
        print(f"The dragon hits you for {dragon_damage} damage!")

    if player_health > 0:
        print_line()
        print("You have defeated the dragon and claimed the treasure!")
        sys.exit(0)
    else:
        print_line()
        print("You were defeated by the dragon. Better luck next time!")
        sys.exit(0)
def dia():
    print('''
          \nYou have defeated the Bear and have venture throught the forest and see the dragons lair.
          But there is a raid that you have to cross
          ''')
def fight_bear():
    man=100
    bear=125
    print('Your Health:',man)
    print('Bear Health:',bear)
    while man>0 and bear>0:
        print_line()
        choice=int(input('Do you want to (1) attack or (2) defend? (1/2):'))
        if choice==1:
            damage=random.randint(5,10)
            man=man-damage
            print_line()
            a=input('Do you want to (1) punch or (2) kick? (1/2):')
            if a==1:
                bear=bear-20
            else:
                bear=bear-15
        if choice==2:
            beardamage=random.randint(10,15)
            bear=bear-beardamage
            print_line()
            print('Do you want to use your (1) Sheild or (2) Hands or (3) Duck? (1/2/3)')
            b=int(input())
            if b==1:
                man=man-15
            elif b==2:
                man=man-20
            else:
                man=man-10
        else:
            print('Invalid input')
        print('Your Health:',man)
        print('Bear Health:',bear)
        print_line()
    if man > 0:
        print_line()
        print("You have defeated the Bear and can continue")
    else:
        print_line()
        print("You were defeated by the Bear. Better luck next time!")

def explore_forest():
    print_line()
    print('''
          \nYou venture deeper into the forest...
          and find a clearing
          ''')
    while True:

        print_line()
        print("\nOptions")
        print("1. Enter the opening in the forest")
        print("2. Go back")
        print('Type 1 or 2')
        choice = int(input("Enter your choice: "))

        if choice == 1:
            print_line ()
            print('''
            You  enter the clearing and find yourself surrounded by wild flowers...
            HALT!! there is a black bear charging towards you ...
            Fend for yourself
              Good luck traveller....
            ''')
            fight_bear()


        elif choice == 2:
            print_line()
            print("\nYou decide to turn back.")
            print('Thank you for playing!!')
            sys.exit(0)
        else:
            print_line()
            print("\nInvalid choice. Please choose again.")

        print_line()
        print('''
            After defeating the bear you look across the  mighty river and see the dragons lair...
            BEWARE mighty taveller proceed with caution and claim your glory..
            good luck traveller....
              ''')
        print("1.Cross the river")
        print("2. Go back")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            print("\nOptions")
            print("1. Attempt to swim across")
            print("2. Build a raft")
            print("3. Go back")

            river_choice = int(input("Enter your choice: "))

            if river_choice == 1:
                print_line()
                print("\nYou decide to swim across the river\nThere are strong currents and spikey rocks sticking out!!\nAs you move forward, you catch sight of the dragon's lair on the other side.\nJust as you reach the bank, you are swept away by the current.\nYou wake up on the riverbank, safe")
                fight_dragon()
                break

            elif river_choice == 2:

                print_line()
                print("\nYou decide to build a raft")
                print("After gathering logs and vines, you successfully construct a sturdy raft.")
                print("You paddle across the river and discover a hidden cave.")
                choice = input("Enter the cave? (yes/no): ").lower()
                if choice == "yes":
                    fight_dragon()
                    break
                else:
                    print("\nYou have decided not to enter the dragon's lair.")
            elif river_choice == 3:
                dia()
                break
            else:
                print("\nInvalid choice. Please choose again.")
        elif river_choice == 2:
                print("\nYou decide to go back to the to the clearing.")
        else:
                print("\nInvalid choice. Please choose again.")


start_adventure()