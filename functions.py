from Players import Players

computer_points = 0
user_points = 0


def show_scores():
    print("================")
    print("Current Score is: ")
    print("You: ", user_points)
    print("CPU: ", computer_points)


def who_won(user_choice, computer_choice):
    cpu_won_txt = "Computer wins!"
    player_won_txt = "You win!"

    def choice_output():
        print("Your input is ", user_choice)
        print("Computer input is ", computer_choice)

    def announce(winner):
        global computer_points, user_points
        choice_output()
        if winner == Players.USER:
            print(player_won_txt)
            user_points += 1
        else:
            print(cpu_won_txt)
            computer_points += 1

    if user_choice != "scissors" and user_choice != "rock" and user_choice != "paper":
        print("You must pick rock, paper or scissors")
    if user_choice == computer_choice:
        choice_output()
        print("it is a tie!")

    if user_choice == "rock":
        if computer_choice == "paper":
            announce(Players.CPU)
        elif computer_choice == "scissors":
            announce(Players.USER)
    elif user_choice == "paper":
        if computer_choice == "rock":
            announce(Players.USER)
        elif computer_choice == "scissors":
            announce(Players.CPU)
    elif user_choice == "scissors":
        if computer_choice == "rock":
            announce(Players.CPU)
        if computer_choice == "paper":
            announce(Players.USER)
    show_scores()
