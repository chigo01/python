from datetime import datetime

from quiz.utils.file_path import FilePath

now = datetime.now()
time_now = now.strftime("%m/%d/%Y, %H:%M:%S")


def write_highest_score(score, game_name):
    name = input("Please Enter Your Glorious Name: ")
    print(name, "your score will be put in the highscore records.")
    with open(FilePath.file__path('highscores'), 'a') as f:
        f.write(name + "-" + str(score) + "-" + game_name + "-" + time_now)

# f.write(name + "-" + str(score) + "-" + game_name + "\n")
