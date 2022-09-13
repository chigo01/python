file__path = 'C:/Users/favou/OneDrive/Desktop\python/quiz/FILES/highscores.txt'


def display_score():
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
    with open(file__path, "r") as file_score:
        # print(file_score.read())
        for file in file_score:
            score = file.split("-")
            emp_list.append(score)

    for i in range(len(emp_list) - 1):
        print('Name: ', emp_list[i][0])
        print('Score:', emp_list[i][1])
        print('Category: ', emp_list[i][2])


display_score()
