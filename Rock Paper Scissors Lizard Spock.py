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

def RPCLS():
    choices = ["Rock","Paper","Scissors","Lizard","Spock"]

    computer = random.choice(choices)
    player = None

    print ("Let's play!")

    while player not in choices:
        player = input("Rock, Paper, Scissors, Lizard or Spock? ").capitalize()
    
    if player == computer:
        print ("Computer: ", computer)
        print ("Player: ", player)
        print ("Tie!!")

    elif player == "Rock":

        if computer == "Paper":
            print ("Computer: ", computer)
            print ("Player: ", player)
            print ("Paper covers rock. You lose!!")

        if computer == "Scissors": 
            print ("Computer: ", computer)
            print ("Player: ", player)
            print ("Rock crushes scissors. You win!!!")

        if computer == "Lizard": 
            print ("Computer: ", computer)
            print ("Player: ", player)
            print ("Rock crushes lizard. You win!!!")

        if computer == "Spock": 
            print ("Computer: ", computer)
            print ("Player: ", player)
            print ("Spock vaporizes rock. You lose!!!")

    elif player == "Paper": 
        
        if computer == "Rock":
            print ("Computer: ", computer)
            print ("Player: ", player)
            print ("Paper covers rock. You win!!!")

        if computer == "Scissors":
            print ("Computer: ", computer)
            print ("Player: ", player)
            print ("Scissors cuts paper. You lose!!")

        if computer == "Lizard": 
            print ("Computer: ", computer)
            print ("Player: ", player)
            print ("Lizard eats paper. You lose!!!")

        if computer == "Spock": 
            print ("Computer: ", computer)
            print ("Player: ", player)
            print ("Paper disproves Spock. You win!!!")

    elif player == "Scissors":

        if computer == "Rock":
            print ("Computer: ", computer)
            print ("Player: ", player)
            print ("Rock crushes scissors. You lose!!")

        if computer == "Paper":
            print ("Computer: ", computer)
            print ("Player: ", player)
            print ("Scissors cuts paper. You win!!!")

        if computer == "Lizard": 
            print ("Computer: ", computer)
            print ("Player: ", player)
            print ("Scissors decapitates lizard. You win!!!")

        if computer == "Spock": 
            print ("Computer: ", computer)
            print ("Player: ", player)
            print ("Spock smashes scissors. You lose!!!")
    
    elif player == "Lizard":

        if computer == "Rock":
            print ("Computer: ", computer)
            print ("Player: ", player)
            print ("Rock crushes lizard. You lose!!")

        if computer == "Paper": 
            print ("Computer: ", computer)
            print ("Player: ", player)
            print ("Lizard eats paper. You win!!!")
        
        if computer == "Scissors": 
            print ("Computer: ", computer)
            print ("Player: ", player)
            print ("Scissors decapitates Lizard. You lose!!!")

        if computer == "Spock": 
            print ("Computer: ", computer)
            print ("Player: ", player)
            print ("Lizard poisons Spock. You win!!!")

    elif player == "Spock":

        if computer == "Rock": 
            print ("Computer: ", computer)
            print ("Player: ", player)
            print ("Spock vaporizes rock. You win!!!")

        if computer == "Paper":
            print ("Computer: ", computer)
            print ("Player: ", player)
            print ("Paper disproves Spock. You lose!!")

        if computer == "Scissors": 
            print ("Computer: ", computer)
            print ("Player: ", player)
            print ("Spock smashes scissors. You win!!!")

        if computer == "Lizard": 
            print ("Computer: ", computer)
            print ("Player: ", player)
            print ("Lizard poisons Spock. You lose!!!")

while True:
    RPCLS()
    replay = input ("Do you wish to play again? Y/N\n").upper()
    if replay == "N":
        break
    else:
        print()
        continue