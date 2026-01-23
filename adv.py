# Choose Your Own Adventure
# Dario Androsevic
# 31 Septeber 2025

# Choose your own adventure story focusing on using variables and branching/conditionals

greeting = "Welcome to your adventure through the mountains of MoonLand"
print(greeting)

name = input("What is your name, adventurer?")
print(f"Hello {name}")

print("Do you want to go through the narrow valley or in the dark cave")

while True:
    choice = input()
    if choice == "narrow valley":
        print("You have decided to enter through the narrow valley")
        print(
            "You have become thirsty! You check your inventory and nothing appears. You look to the left and see water in the distance past a steep cliff. However, there's a chance that water is present straight at the end of the narrow valley. Will you go left or straight?"
        )

        while True:
            choice = input()
            if choice == "left":
                print("You went left and fell off the cliff. You died. Try Again.")
                break

            elif choice == "straight":
                print(
                    "You went straight and continued through the valley. You find a lake at the end of the passage. However, an alligator is lurking in the water. Above you, the dark clouds appear heavy with rain. Your thirst is overwhelming. Do you risk it and drink the lake water or sit and wait for rain. Select drink water or wait for rain."
                )

                while True:
                    choice = input()
                    if choice == "drink water":
                        print(
                            "The alligator was happy for the company and let you drink the water safely. You lived with him together forever. Congratulations - You Survived!"
                        )
                        break

                    elif choice == "wait for rain":
                        print("The rain never came and you died of thirst. Try Again.")
                        break

                    else:
                        print(
                            "That was not an option. Select by typing 'drink water' or 'wait for rain'"
                        )
            else:
                print("That was not an option. Select by typing 'left' or 'straight'")

    elif choice == "dark cave":
        print("You have entered the dark cave.")
        print(
            "You need light. With the little light coming from the entrance, you see 2 rocks with smoke wafting from them. You might be able to rub them together to create a fire. However, you risk completely burning your hand off. Do you rub the rocks or continue on?"
        )

        while True:
            choice = input()
            if choice == "rub the rocks":
                print(
                    "When the rocks were rubbed together a HUGE explosion occured. You have died. Try again."
                )
                break

            elif choice == "continue on":
                print("You have continued on without light")
                print(
                    "The path splits ahead. To the left you hear running water and to the right you smell fresh barbequed steak. You haven't eaten in so long but you're also very thirsty. Do you go left or right?"
                )

                while True:
                    choice = input()
                    if choice == "left":
                        print(
                            "You stumble into a current and fall into an underground river."
                        )
                        print(
                            "Luckily, the current pushes you out of the cave and into a vast field. You're still hungry but there is an apple tree in front of you. Do you eat the apple or stay hungry?"
                        )

                        while True:
                            choice = input()
                            if choice == "eat the apple":
                                print(
                                    "You ate the apple and lived happily ever after. Congratulations. You have survived!"
                                )
                                break
                            elif choice == "stay hungry":
                                print(
                                    "You foolishly decided not to eat the apple and died of hunger. Try again."
                                )
                                break
                            else:
                                print(
                                    "That was not an option. Select 'eat the apple' or 'stay hungry'."
                                )

                    elif choice == "right":
                        print(
                            "A tribe of Jonas Raghani's swarmed angrily at you for stealing the food and threw you into the cave dungeon forever. You have died. Try Again!"
                        )
                        break

                    else:
                        print(
                            "That was not an option. Select by typing 'left' or 'right'."
                        )
            else:
                print(
                    "That was not an option. Select by typing 'rub the rocks' or 'continue on'."
                )
    else:
        print("That was not an option. Select by typing 'narrow valley' or 'dark cave'")
