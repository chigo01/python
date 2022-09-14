from quiz.components import about
from quiz.components import display_high_score
from quiz.components import menu
from quiz.components import start


def operator_of_game():  # function for choosing an operaiton in the main menu
    operand = input("Please Choose an Operation: ")
    if operand == "1":
        start.start()
    elif operand == "2":
        about.about_game()
    elif operand == "3":
        display_high_score.display_score()
    elif operand == "4":
        exit1()
    else:
        print("Invalid Input, Please Choose again.")
        menu.menu_game()


def exit1():  # exit function
    print("Have a good day.")
    quit()
