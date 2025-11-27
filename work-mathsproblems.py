# Dario Androsevic
# Nov 14, 2025

def main():
    # Question 1

    current_age = int(input("Enter your current age"))

    year_now = 2025
    year_final = 2049

    year_old = (year_final - year_now) + current_age

    print(f"You will be {year_old} years old in {year_final}")

    # Question 2

    judge1_score = float(input("Enter judge 1 score out of 10"))
    if judge1_score > 10:
        print("Invalid score")
    elif judge1_score < 0:
        print("Invalid score")
    judge2_score = float(input("Enter judge 2 score out of 10"))
    if judge2_score > 10:
        print("Invalid score")
    elif judge2_score < 0:
        print("Invalid score")
    judge3_score = float(input("Enter judge 3 score out of 10"))
    if judge3_score > 10:
        print("Invalid score")
    elif judge3_score < 0:
        print("Invalid score")
    judge4_score = float(input("Enter judge 4 score out of 10"))
    if judge4_score > 10:
        print("Invalid score")
    elif judge4_score < 0:
        print("Invalid score")
    judge5_score = float(input("Enter judge 5 score out of 10"))
    if judge5_score > 10:
        print("Invalid score")
    elif judge5_score < 0:
        print("Invalid score")

    Olympic_score = ((judge1_score + judge2_score + judge3_score + judge4_score + judge5_score) / 5)
    print(f"Your Olympic score is {Olympic_score} out of 10")

    # Question 3

    burger_price = 5
    fries_price = 3
    drink_price = 1
    tax_rate = 1.14

    burger = input("Do you want a burger for 5 dollars? (Yes/No)").strip().lower()
    fries = input("Do you want fries for 3 dollars? (Yes/No)").strip().lower()
    drink = input("Do you want a drink for 1 dollar? (Yes/No)").strip().lower()

    total_price = ((burger_price if burger == "yes" else 0) + (fries_price if fries == "yes" else 0) + (drink_price if drink == "yes" else 0)) * tax_rate
    print(f"Your total price is ${total_price} Enjoy your meal!")
if __name__ == "__main__":
    main()
