import mathquiz
import physicsquiz
import sciencequiz

print("!!!!!!............Welcome to Our Daily Quizzes........ !!!!!!!!!")
print("!!!......______________________________________________!!!!!!!!!")
print("!!!.....Choose your Quiz Category from the Following.. !!!!!!!!!")
print("!!!......______________________________________________!!!!!!!!!")
print("!!!......______________________________________________!!!!!!!!!")
print("________________Press 'A' for Math Quiz_________________________")
print("________________Press 'B' for Science Quiz______________________")
print("________________Press 'C' for Physics Quiz______________________")
print("!!!......______________________________________________!!!!!!!!!")
print("!!!......______________________________________________!!!!!!!!!")
print("!!!......______________________PRESS 'Q' to quit_______!!!!!!!!!")


user_choice = input("Choose your Option:")
if user_choice == "Q":
    exit()
elif user_choice == "A":
    mathquiz.math_quiz()
elif user_choice == "B":
    physicsquiz.physics_quiz()
elif user_choice == "C":
    sciencequiz.science_quiz()
else:
    print("Choose a Valid Option")

