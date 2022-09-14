#
# from quiz.model import quiz_model
import os

from quiz.model.quiz_model import Qa
from quiz.utils.file_path import FilePath


class BleachQuest(Qa):

    @staticmethod
    def display_art():
        print("Hello, you have chosen the Bleach Category, this category is about the Anime Bleach by Tite Kubo.")
        print("The questions here revolves throughout the whole series,being very specific in detail.")
        print("Note: Remember to type in your answers correctly and be wary of the spaces.")
        print()
        # art hart

    @staticmethod
    def high_points():
        print("	._._._._._._._._._|_____________________________________________________________________	")
        print("	|_|_|_|_|_|_|_|_|_|____________________________________________________________________/ 	")
        print()
        print("Congratulations you have passed the quiz in Hard difficulty")
        print("The Soul King smiles upon you.")
        print()

    @staticmethod
    def low_points():
        print("Sorry but you have failed the quiz, thus you will not be able ")
        print("to qualify for the highscores. ")
        print("Such a shame.")


def play_bleach():
    BleachQuest.display_art()
    file = Qa.open_file(FilePath.file__path('bleachquest'))
    line = '<>======================================================<>'

    list_of_qa = [

        Qa(f'{file[0][0]}\n{line}\n(1) ' f'{file[0][1]}\n(2) {file[0][2]}\n(3) {file[0][3]}\n(4) {file[0][4]}\n', '2'),

        Qa(f'{file[1][0]}\n{line}\n(1) ' f'{file[1][1]}\n(2) {file[1][2]}\n(3) {file[1][3]}\n(4) {file[1][4]}\n', '4'),

        Qa(f'{file[2][0]}\n{line}\n(1) ' f'{file[2][1]}\n(2) {file[2][2]}\n(3) {file[2][3]}\n(4) {file[2][4]}\n', '1'),

        Qa(f'{file[3][0]}\n{line}\n(1) ' f'{file[3][1]}\n(2) {file[3][2]}\n(3) {file[3][3]}\n(4) {file[3][4]}\n', '2'),

        Qa(f'{file[4][0]}\n{line}\n(1) ' f'{file[4][1]}\n(2) {file[4][2]}\n(3) {file[4][3]}\n(4) {file[4][4]}\n', '3'),

        Qa(f'{file[5][0]}\n{line}\n(1) ' f'{file[5][1]}\n(2) {file[5][2]}\n(3) {file[5][3]}\n(4) {file[5][4]}\n', '2'),

        Qa(f'{file[6][0]}\n{line}\n(1) ' f'{file[6][1]}\n(2) {file[6][2]}\n(3) {file[6][3]}\n(4) {file[6][4]}\n', '2'),

        Qa(f'{file[7][0]}\n{line}\n(1) ' f'{file[7][1]}\n(2) {file[7][2]}\n(3) {file[7][3]}\n(4) {file[7][4]}\n', '1'),

        Qa(f'{file[8][0]}\n{line}\n(1) ' f'{file[8][1]}\n(2) {file[8][2]}\n(3) {file[8][3]}\n(4) {file[8][4]}\n', '2'),

        Qa(f'{file[9][0]}\n{line}\n(1) ' f'{file[9][1]}\n(2) {file[9][2]}\n(3) {file[9][3]}\n(4) {file[9][4]}\n', '1'),

        Qa(f'{file[10][0]}\n{line}\n(1) ' f'{file[10][1]}\n(2) {file[10][2]}\n(3) {file[10][3]}\n(4) {file[10][4]}\n',
           '3'),

        Qa(f'{file[11][0]}\n{line}\n(1) ' f'{file[11][1]}\n(2) {file[11][2]}\n(3) {file[11][3]}\n(4) {file[11][4]}\n',
           '3'),

        Qa(f'{file[12][0]}\n{line}\n(1) ' f'{file[12][1]}\n(2) {file[12][2]}\n(3) {file[12][3]}\n(4) {file[12][4]}\n',
           '1'),

        Qa(f'{file[13][0]}\n{line}\n(1) ' f'{file[13][1]}\n(2) {file[13][2]}\n(3) {file[13][3]}\n(4) {file[13][4]}\n',
           '2'),

        Qa(f'{file[14][0]}\n{line}\n(1) ' f'{file[14][1]}\n(2) {file[14][2]}\n(3) {file[14][3]}\n(4) {file[14][4]}\n',
           '1'),

        Qa(f'{file[15][0]}\n{line}\n(1) ' f'{file[15][1]}\n(2) {file[15][2]}\n(3) {file[15][3]}\n(4) {file[15][4]}\n',
           '3'),

        Qa(f'{file[16][0]}\n{line}\n(1) ' f'{file[16][1]}\n(2) {file[16][2]}\n(3) {file[16][3]}\n(4) {file[16][4]}\n',
           '4'),

        Qa(f'{file[17][0]}\n{line}\n(1) ' f'{file[17][1]}\n(2) {file[17][2]}\n(3) {file[17][3]}\n(4) {file[17][4]}\n',
           '4'),

        Qa(f'{file[18][0]}\n{line}\n(1) ' f'{file[18][1]}\n(2) {file[18][2]}\n(3) {file[18][3]}\n(4) {file[18][4]}\n',
           '2'),

        Qa(f'{file[19][0]}\n{line}\n(1) ' f'{file[19][1]}\n(2) {file[19][2]}\n(3) {file[19][3]}\n(4) {file[19][4]}\n',
           '3'),

    ]

    # file = Qa.open_file("thronequest.txt")
    # print(file)

    BleachQuest.display_question(list_of_qa, BleachQuest.low_points, BleachQuest.high_points, 'Bleach')
