import random
import time

from quiz.components import menu
# from quiz.listofqu import throne_quest

from quiz.utils.higest_input import write_highest_score


class Qa:
    def __init__(self, question, answer):
        self.question = question
        self.answer = answer

    @staticmethod
    def open_file(filename):
        file_question = open(filename, "r")  # open the question text file
        file_out = None
        question_sheet = []  # this will store the questions line by line

        for line1 in file_question:  # gets the question from text file and transfers it to the questionsheet list
            rand_quest = line1.split("-")
            question_sheet.append(rand_quest)

            file_out = question_sheet[: 28]  # slice the list to output from 0 index to 28 index
        file_question.close()  # if you open something then make sure to close it
        return file_out

    @staticmethod
    def display_question(list_of_questions, low_points, high_points, game_name):
        count = 0
        score = 0
        # Picks a random question from the text file and displays it along with the choices
        ran_list = random.sample(list_of_questions, len(list_of_questions))
        while count < 20:
            for line in ran_list:
                print(f'[{count + 1}], {line.question}')

                answer = input('enter number ').lower()
                print()
                # in the answer if equal to the answer in the question class detail then it is correct, otherwise wrong
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
        if score >= 25:  # if the score is equal to or greater than half their scores are qualified to be recorded

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
        time.sleep(3)
        menu.menu_game()
