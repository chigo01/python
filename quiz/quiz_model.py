import random

from quiz.components.menu import menu
from quiz.listofqu import comp_quest


def operator():
    pass


def write_highest_score(score, game_name):
    name = input("Please Enter Your Glorious Name: ")
    print(name, "your score will be put in the highscore records.")
    with open('highscores.txt', 'a') as f:
        f.write(name + "-" + str(score) + "-" + game_name + "\n")


class Qa:
    def __init__(self, question, answer):
        self.question = question
        self.answer = answer

    @staticmethod
    def open_file(filename):
        file_question = open(filename, "r")
        file_out = None
        question_sheet = []

        for line1 in file_question:
            rand_quest = line1.split("-")
            question_sheet.append(rand_quest)

            file_out = question_sheet[: 28]
        file_question.close()
        return file_out

    @staticmethod
    # menu will be added
    def display_question(list_of_questions, low_points, high_points, game_name):
        count = 0
        score = 0
        ran_list = random.sample(list_of_questions, len(list_of_questions))
        while count < 20:
            for line in ran_list:
                print(f'[{count + 1}], {line.question}')

                answer = input('enter number ').lower()
                print()
                if answer == line.answer:
                    score += 2
                    print('correct answer')
                    print()
                elif answer == 'quit':
                    pass
                # menu()
                else:
                    print("The answer is obviously wrong.")
                    print()

                print()
                print("Your score is: ", score, )
                print()

                count += 1
        if score > 12:
            high_points()
            write_highest_score(score, game_name)
        else:
            low_points()
            print()
            print()
            # after the game ends the player will be redirected to the main menu
            print("You will now be redirected to the Main Menu.")
            # where they can view their highscore
            print("Thank you for playing the Game.")
            menu()


if __name__ == "__main__":
    comp_quest.play_comp_tree()

