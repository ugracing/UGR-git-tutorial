"""
This code is broken!
Daniel had too many beers and forgot how programming works
ribbit ribbit
This is not the most efficient implementation
its up to you if you want to rewrite the whole program
Good luck!
"""
import random

wins = 0
looses = 0


def win_or_lose(player_input, computer_play, lost):
    global looses
    global wins

    if lost == "":
        return None

    elif player_input == computer_play:
        print("Tie! ribbit")

    elif lost == "Frog" == player_input:
        print("Wait are frogs included?")
        print("King Julio wins")

    elif lost == computer_play != "Frog":
        print("You lose!", computer_play, verbs[computer_play], player_input)
        looses += 1

    else:
        print("You win!", player_input, verbs[player_input], computer_play)
        wins += 1


def who_won(play_num, lost_num, win_num):
    print("We played", str(play_num), "time(s). You won", str(win_num), "time(s).")

    if lost_num > win_num:
        print("𓆏 This means I won!! I must say, it is rather sad for a human to loose to a virtual frog.")

    elif win_num > lost_num:
        print("You won overall... Beginners luck.")

    else:
        print("We tied. Only because you did not want to keep playing, ribbit.")


loosing_condition = {
    "Rock": "Paper",
    "Paper": "Scissors",
    "Scissors": "Rock",
    "Frog": "Frog"
}

verbs = {
    "Rock": "smashes",
    "Paper": "covers",
    "Scissors": "cut",
}


play = input("Hello there 𓆏 ribbit! Do you want to play a game of rock, paper, scissors with me? Say yes (\"Y\") if "
             "you do. ribbit\n")

counter = 0

while play.capitalize() == "Y" or play.capitalize() == "Yes":     # accepts any variation of "yes"
    computer = random.choice(list(loosing_condition.items()))

    player = input("Rock, Paper, Scissors, Frog?\n").capitalize()

    if player not in loosing_condition:
        print("That's not a valid play. Even a frog can spell better than you! 𓆏")

    else:
        counter += 1
        win_or_lose(player, computer, loosing_condition[player])

    play = input("Do you wish to keep playing? Say yes (\"Y\") if you do.\n")

who_won(counter, looses, wins)
