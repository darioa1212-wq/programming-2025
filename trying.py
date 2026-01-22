def question():
    print("Ask about Jonas but read the code lol")
    user_question = input("> ")

    if user_question == "Is Jonas stupid":
        print("Yes, Jonas is stupid.")
    elif user_question == "Is Jonas a good person":
        print("Absolutely not, Jonas is not a good person.")
    else:
        print("Invalid question.")

question()
