# Upgraded version of the basic game rock paper scissors that adds two other options, lizard and Spock

# Rock crushes scissors
# Rock crushes lizard
# Paper covers rock
# Paper disproves Spock
# Scissors cuts paper
# Scissors decapitates lizard
# Lizard poisons Spock
# Lizard eats paper
# Spock smashes scissors
# Spock vaporizes rock

import random

# Definindo escolhas
choices = {"rock": {"scissors", "lizard"},
           "paper": {"rock", "spock"},
           "scissors": {"paper", "lizard"},
           "lizard": {"paper", "spock"},
           "spock": {"rock", "scissors"}}

win_verbs = {"rock": {"scissors": "smashes", "lizard": "crushes"},
             "paper": {"rock": "covers", "spock": "disproves"},
             "scissors": {"paper": "cuts", "lizard": "decapitates"},
             "lizard": {"paper": "eats", "spock": "poisons"},
             "spock": {"rock": "vaporizes", "scissors": "smashes"}}

# Função pegar a escolha do usuario
def get_user_choice():
    while True:
        choice = input("Let's play!" + "\n" + "Rock, Paper, Scissors, Lizard or Spock?" + "  ").lower()
        if choice in choices:
            return choice
        else:
            print("Invalid input!")

# Função pegar escolha do computador
def get_computer_choice():
    return random.choice(list(choices.keys()))

# Função para determinar o vencedor
def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "Tie"
    elif computer_choice in choices[user_choice]:
        return user_choice.capitalize() + " " + win_verbs[user_choice][computer_choice] + " " + computer_choice + "." + " " + " You win!!!!"
    else:
        return computer_choice.capitalize() + " " + win_verbs[computer_choice][user_choice] + " " + user_choice.capitalize() + "." + " " + " You lose!!"

# loop
while True:
    user_choice = get_user_choice()
    computer_choice = get_computer_choice()
    print(f"You chose {user_choice} and computer chose {computer_choice}.")
    print(determine_winner(user_choice, computer_choice))
    play_again = input("Do you wish to play again? Y/N ").lower()
    if play_again != "y":
        break
