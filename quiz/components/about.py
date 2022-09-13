from quiz.components import menu


def about_game():  # Displays the about page, the instructions, and the details of the Quiz Categories.

    print("This Game was made for a Project by Robie A. Carlos")
    print()
    print("Instructions: ")
    print("To start the game,type in the number 1 in the main menu then choose a category of your liking.")
    print(
        "There are 4 Categories to choose from, each consists of 12 questions and randomly drawn from a question pool.")
    print()
    print("To sumbit your answer, simply type in the number beside your answer, there are 4 choices for each question,")
    print(
        "so you will need to type in a number from 1-4, incorrect inputs such as other numbers or other characters will")
    print(
        "result in a wrong answer.To quit mid-game, simply type in 'quit' and you'll be redirected to the main menu.")
    print(" ")
    print("If you score half or more than half of the total amount of points in a given category you will be")
    print("able to qualify for a highscore record and your name will be taken to be recorded as well.")
    print(
        "To view all the highscores, simply type in the number 3 in the main menu and it will display all the highscores.")
    print("--------------------------------------------------------------------- ")
    print("The Computer Category is the easiest and requires basic knowledge of computers.")
    print("Each question in this category is worth 1 point.")
    print(" ")
    print("The Meme category has Medium difficulty and requires an intermediate understanding of memes")
    print("as well as their origins and where they are derived from.")
    print("Each question in this category is worth 2 points.")
    print(" ")
    print("The Bleach Category is placed in Hard difficulty and its questions are focused on Cloth Cleaning")
    print("products as well as some questions about detergents and fabric conditioners.")
    print("Each question in this category is worth 3 points.")
    print(" ")
    print("The Game of Thrones category is the most difficult question set in the quiz game.")
    print("The questions range from the names of places,characters, and specific objects in the TV series")
    print("Each question in this category amounts to 4 points.")
    print("---------------------------------------------------------------------- ")
    print("For suggestions and inquiries you may email me at racarlos1@up.edu.ph")
    print()
    menu.menu_game()



