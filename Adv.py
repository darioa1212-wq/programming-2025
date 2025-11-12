# Notes - Adventure Game
# 25 September
# Osmond Fu

import time

# start with 0 gold
gold = 0

# 1. Get the player's name
name = input("What is your name? ")

# 2. Greet the player with story introduction
print(f"Hi, {name}. You are a normal high school student,")
time.sleep(2)
print("but one afternoon you hear strange whispers from the basement.")
time.sleep(2)
print("You discover a glowing portal hidden behind an old locker.")
time.sleep(2)
print("The air feels heavy, as if calling you inside.")
time.sleep(2)

# 3. First choice
choice1 = input("Do you ENTER the portal or WALK away? (enter/walk) ")

if choice1 == "walk":
    print("You step back. The portal flickers, then vanishes forever.")
    time.sleep(2)
    print("You return home, but you always wonder what adventure you missed.")
    time.sleep(2)
    print(f"Ending: Normal Life | Total Gold Collected: {gold}")

elif choice1 == "enter":
    gold += 1
    print("The portal pulls you in! You land on cold stone. (+1 gold)")
    time.sleep(2)
    print("You are inside a dark dungeon. Torches flicker on the walls.")
    time.sleep(2)
    print("A foul smell fills the air. Danger is close...")
    time.sleep(2)

    # 4. Second choice: Sword
    choice2 = input("A rusty sword lies ahead. PICK it up or LEAVE it? (pick/leave) ")

    if choice2 == "pick":
        has_sword = True
        gold += 1
        print("You grip the sword. It makes you feel braver. (+1 gold)")
        time.sleep(2)
    else:
        has_sword = False
        print("You ignore the sword and continue unarmed. Risky...")
        time.sleep(2)

    # 4b. Torch option
    choice2b = input("A torch burns on the wall. TAKE it or LEAVE it? (take/leave) ")

    if choice2b == "take":
        has_torch = True
        gold += 1
        print("You pull the torch. It lights your way. (+1 gold)")
        time.sleep(2)
    else:
        has_torch = False
        print("You leave the torch. The dungeon stays dark.")
        time.sleep(2)

    # 5. Third choice
    choice3 = input(
        "Two paths: LEFT (eery whispers) or RIGHT (glowing tunnel). (left/right) "
    )

    if choice3 == "left":
        print("You step into the tunnel. The whispers grow louder...")
        time.sleep(2)
        print("Suddenly, a monster leaps from the shadows!")
        time.sleep(2)

        if has_sword:
            print("You raise your sword as the monster charges!")
            time.sleep(2)
            print("After a fierce battle, you slay the beast. (+1 gold)")
            gold += 1
            time.sleep(2)

            # 6. New choice after monster
            choice5 = input("Deeper hallway ahead. SEARCH or EXIT? (search/exit) ")

            if choice5 == "search":
                print("You venture deeper. The dungeon trembles...")
                time.sleep(2)

                if has_torch:
                    print("With your torch, you spot traps and avoid them.")
                    time.sleep(2)
                    print("You find a chamber full of gold! (+2 gold)")
                    gold += 2
                    time.sleep(2)
                    print("You grab what you can and escape back to school.")
                    time.sleep(2)
                    print(f"Ending: Treasure Hunter | Total Gold Collected: {gold}")
                else:
                    print("It’s too dark. You fall into a hidden trap!")
                    time.sleep(2)
                    print(f"Ending: Game Over | Total Gold Collected: {gold}")

            elif choice5 == "exit":
                gold += 1
                print("You escape through a side tunnel. (+1 gold)")
                time.sleep(2)
                print("Your bravery will be remembered.")
                time.sleep(2)
                print(f"Ending: Hero’s Victory | Total Gold Collected: {gold}")
            else:
                print("You wait too long. The dungeon collapses!")
                time.sleep(2)
                print(f"Ending: Game Over | Total Gold Collected: {gold}")
        else:
            print("You try to run, but the monster is too fast.")
            time.sleep(2)
            print("With no weapon, you are defeated.")
            time.sleep(2)
            print(f"Ending: Game Over | Total Gold Collected: {gold}")

    elif choice3 == "right":
        print("You enter a glowing chamber. The air hums with magic.")
        time.sleep(2)
        print("In the middle is a large treasure chest.")
        time.sleep(2)

        choice4 = input("Do you OPEN the chest or LEAVE it? (open/leave) ")

        if choice4 == "open":
            if has_torch:
                gold += 2
                print("Torchlight reveals strange runes. It’s cursed!")
                time.sleep(2)
                print("You slam it shut just in time. (+2 gold)")
                time.sleep(2)
                print("A secret door opens, leading you outside.")
                time.sleep(2)
                print(f"Ending: Clever Survivor | Total Gold Collected: {gold}")
            else:
                print("You open the chest... it’s a trap!")
                time.sleep(2)
                print("Poison gas fills the room.")
                time.sleep(2)
                print(f"Ending: Game Over | Total Gold Collected: {gold}")

        elif choice4 == "leave":
            gold += 1
            print("You leave the chest untouched. (+1 gold)")
            time.sleep(2)
            print("Behind it, a hidden door takes you back to school.")
            time.sleep(2)
            print("You survived the dungeon’s tricks!")
            time.sleep(2)
            print(f"Ending: Cautious Victory | Total Gold Collected: {gold}")
        else:
            print("You freeze. The chamber collapses!")
            time.sleep(2)
            print(f"Ending: Game Over | Total Gold Collected: {gold}")

else:
    print("You stand frozen. The portal flickers, then disappears.")
    time.sleep(2)
    print("The adventure passes you by...")
    time.sleep(2)
    print(f"Ending: Missed Adventure | Total Gold Collected: {gold}")
