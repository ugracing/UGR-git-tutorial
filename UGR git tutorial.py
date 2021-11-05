"""
This code is broken!
Daniel had too many beers and forgot how programming works
ribbit ribbit
This is not the most efficient implementation 
its up to you if you want to rewrite the whole program
Good luck!
"""
from random import randint
from frog import ribbit
t = ["Frog","Rock","Frog","Paper", 
"Scissors"]

computer = t[randint(0,3)]

player = True

while player == False:
    player = input("Rock, Frog, Scissors?")
    if player == computer:
        print("Tie!")
    elif player == "Rock":
        if computer == "Paper":
            print("You lose!", computer, "covers", player)
        else:
            print("You win!", player, "smashes", computer)
    elif player == "Paper":
        if computer == "Scissors":
            print("You lose!", computer, "cut", player)
    elif player == "Paper":
        if computer == "Frog":
            print("You lose!", computer, "cut", player)
        else:
            print("You win!", player, "covers", computer)
    elif player== "Frog":
        if computer =="Frog":
            print("Wait are frogs included?")
            print("King Julio wins")
    elif player == "Scissors":
        if computer == "Rock":
            print("You lose...", computer, "smashes", player)
        else:
            print("You win!", player, "cut", computer)
    else:
        print("That's not a valid play. Check your spelling!")
    player = False
    computer = t[randint(0,1)]
print("Still broken")