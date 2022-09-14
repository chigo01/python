from quiz.components import menu
from quiz.components import start
from quiz.listofqu import comp_quest
from quiz.listofqu import throne_quest


# from quiz.listofqu import throne_quest


def category_of_game():  # sub operator for category
    categories = input("Please choose a Category: ")

    if categories == "1":
        comp_quest.play_comp_tree()

    elif categories == "2":
        print('')  # memetree()

    elif categories == "3":
        print('dd')  # bleachtree()

    elif categories == "4":
        throne_quest.play_throne_quest()

    elif categories == "5":
        menu.menu_game()

    else:
        print("Invalid Input, Please try again")
        start.start()
