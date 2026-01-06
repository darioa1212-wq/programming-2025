# Notes - Introduction
# 16 September
# Tim Ubial

# Create an algorithm to solve a problem
# Problem: Create our own chatbot
#          MeGPT

# 1. Greet the user with a predetermined statement
greeting = "Hello! I am a chatbot."

# 1a. Print the greeting
print(greeting)

# 2. Introduce the bot
print("My name is MeGPT.")
print("I'm not like the other guys.")
print("I'm completely deterministic.")

# 3. Wow the user with some maths
print("I bet you don't know what 8*8 is.")
print("I can do it.")
print(f"8*8 is actually {8*8}.")

print("What is pi squared?")
print("I'm smart, I can do it too.")
print(f"It is {3.14159265359 ** 2}.")

# 4. Make the bot crash out a little bit.
print("The quick brown fox jumps over the lazy dog." * 10)

# 5. Get the name of the user, store it, and use it
user_name = input("What's your name? ")
print(f"It's nice to meet you, {user_name}!")

# ...

# 8. See IF the user is someone specific.
# 8a. If they're someone specific, tell them a secret
if user_name == "Mr. Ubial":
    print("I know that you like to eat burgers.")
    print("But I won't tell anyone. Shhhhh. 🤐")

    favourite_book = input("What's your favourite book?")

    if favourite_book == "Harry Potter":
        print("I like Harry Potter, too!")
elif user_name == "Spongebob":
	print("🎶 Who lives in a pineapple under the sea? 🎶")

	print("🎶 Spongebob Squarepants. 🎶")
elif user_name == "Abraham Lincoln":
	print("Abe Lincoln? I heard you're a good wrestler.")
else:
	print("I don't have any secrets for you.")
