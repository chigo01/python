# file__path = 'C:/Users/favou/OneDrive/Desktop\python/quiz/FILES/highscores.txt'
import os

from quiz.utils.file_path import FilePath


def display_score():
    os.system("cls")

    print("          .-=========-.    ")
    print("          \*-=======-*/    ")
    print("          _|  ..=..  |_    ")
    print("         ((|  {{O}}  |))   ")
    print("          \|   /|\   |/    ")
    print("           \__ '`' __/     ")
    print("             _`) (`__      ")
    print("           _/_______\_     ")
    print("          /___________\    ")
    print()

    print("These are the Highscores.")
    print()
    emp_list = []
    with open(FilePath.file__path('highscores'), "r") as file_score:
        # print(file_score.read())
        for file in file_score:
            score = file.split("-")
            emp_list.append(score)

    for i in range(len(emp_list) - 1):
        print('Name: ', emp_list[i][0])
        print('Score:', emp_list[i][1])
        print('Category: ', emp_list[i][2])





