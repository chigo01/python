from quiz.components import category


def start():  # sub menu for choosing the quiz category
    # os.system("cls")
    print("Please Select a category:")
    print()
    print("[1] Computers (no computation needed) - Easy")
    print("[2] Memes (mims not meh-mehs) - Medium")
    print("[3] Bleach (not used in laundry) - Hard")
    print("[4] Game of Thrones (not really a game) - Very Hard")
    print("[5] Back to Menu")
    print()
    category.category_of_game()
