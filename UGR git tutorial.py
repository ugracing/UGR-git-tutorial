"""
Edit By: Emma Neillie
This code is broken!
Daniel had too many beers and forgot how programming works
ribbit ribbit
This is not the most efficient implementation 
its up to you if you want to rewrite the whole program
Good luck!
"""
from random import randint

t = ["Rock","Paper", "Scissors"]

computer = t[randint(0,2)]

player = False

while player == False:
    playerinput = input("Rock, Paper, Scissors?")
    if playerinput == computer:
        print("Tie!")
        
    elif playerinput == "Rock":
        if computer == "Paper":
            print("You lose!", computer, "covers", playerinput)
        else:
            print("You win!", playerinput, "smashes", computer)
            player = True
            
    elif playerinput == "Paper":
        if computer == "Scissors":
            print("You lose!", computer, "cut", playerinput)
        else:
            print("You win!", playerinput, "covers", computer)
            player = True
            
    elif playerinput == "Scissors":
        if computer == "Rock":
            print("You lose...", computer, "smashes", playerinput)
        else:
            print("You win!", playerinput, "cut", computer)
            player = True
            
    else:
        print("That's not a valid play. Check your spelling!")
       
    computer = t[randint(0,2)]
