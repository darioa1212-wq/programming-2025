# password generator

print("Would you like to generate a strong password?")
user_input = input()
if user_input.lower() == "yes":
    import random

    password = ""
    for _ in range(12):
        password += random.choice(
            "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()_+-=[]{}|;:,.<>?"
        )
        print(password)
elif user_input.lower() == "no":
    print("No password Shall BE GENERATED")
else:
    print("invalid input")
