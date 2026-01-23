math_grade = float(input("Enter your math grade: "))
physics_grade = float(input("Enter your physics grade: "))
computer_grade = float(input("Enter your computer grade: "))
english_grade = float(input("Enter your english grade: "))

semester_grade = (math_grade + physics_grade + computer_grade + english_grade) / 4
print(f"Your current average for semester 1 is {semester_grade:.2f}")
if semester_grade >= 85:
    print("Keep it up! Your above the Uvic and Ucalgary average.")
elif semester_grade >= 81:
    print(
        "Your doing well, but you need to bump up those averages to 85 and above for calgary"
    )
else:
    print("You need to work harder to improve your grades.")
