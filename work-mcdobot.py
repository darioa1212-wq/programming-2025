# McDoBot
# Author: Ubial
# 6 October 2025

# Write a McDonald's bot that asks if you want fries with your meal.
fries = input("Would you like fries with your meal? ").strip(",.?! ").lower()

# It should accept  Yes/yes  or  No/no  as inputs, and reply
# appropriately depending on the answer.
# If the user inputs anything else, it should repeat back their answer
# and say that it does not understand.

if fries == "yes":
    print("Here's your meal with fries.")
elif fries == "no":
    print("Here's your meal without fries.")
else:
    print(f"Sorry, I don't know what \"{fries}\" means.")
