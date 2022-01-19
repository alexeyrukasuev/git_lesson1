import random


player = input()
n = ["rock", "paper", "scissors"]

comp = random.choice(n)
if player == comp:
    print("tie")
elif player == "rock":
    if comp == "scissors":
        print("you win")
    else:
        print("you loose")
elif player == "paper":
    if comp == "rock":
        print("you win")
    else:
        print("you loose")
elif player == "scissors":
    if comp == "paper":
        print("you win")
    else:
        print("you loose")
