import random

from functions import show_scores, who_won

hasExit = False

while not hasExit:
    options = ["rock", "paper", "scissors"]
    user_input = input("Choose 1 = rock, 2 = paper, 3 = scissors or 0 = exit: ")
    computer_input = random.choice(options)
    if user_input == "exit" or user_input == "0":
        print("Game ended")
        show_scores()
        hasExit = True
    else:
        if user_input == "1" or user_input == "2" or user_input == "3":
            user_input = options[int(user_input) - 1]
        who_won(user_input, computer_input)
