import time

from quiz.components import menu
from quiz.components import start
from quiz.listofqu import comp_quest
from quiz.listofqu import throne_quest
from quiz.listofqu import meme_tree
from quiz.listofqu import bleach_quest

# from quiz.listofqu import throne_quest
#


timer = 3


def category_of_game():  # sub operator for category
    categories = input("Please choose a Category: ")

    if categories == "1":
        time.sleep(timer)
        comp_quest.play_comp_tree()

    elif categories == "2":
        time.sleep(timer)
        meme_tree.play_meme_tree()

    elif categories == "3":
        time.sleep(timer)
        bleach_quest.play_bleach()

    elif categories == "4":
        time.sleep(timer)
        throne_quest.play_throne_quest()

    elif categories == "5":
        time.sleep(timer)
        menu.menu_game()

    else:
        print("Invalid Input, Please try again")
        start.start()
