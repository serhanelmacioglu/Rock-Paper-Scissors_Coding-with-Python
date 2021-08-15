import random

while True:

    user_action = input("Rock, paper, scissors? ")
    possible_actions = ["rock", "paper", "scissors"]
    computer_action = random.choice(possible_actions)

    if user_action == computer_action:
        print(f'Both players selected {user_action}. Tie!')
    elif user_action.lower() == "rock":
        if computer_action.lower() == "scissors":
            print("Rock smashes scissors! You win!")
        else:
            print("Paper covers rock! You lose.")
    elif user_action.lower() == "paper":
        if computer_action.lower() == "rock":
            print("Paper covers rock! You win!")
        else:
            print("Scissors cuts paper! You lose.")
    elif user_action.lower() == "scissors":
        if computer_action.lower() == "paper":
            print("Scissors cuts paper! You win!")
        else:
            print("Rock smashes scissors! You lose.")
