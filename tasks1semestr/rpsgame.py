player_a=input("choose your hero, p1")
player_b=input("choose your hero, p2")
def Game(p1, p2):
    if p1 == p2:
        print("tie")
    elif p1 == "rock" and p2 == "sciss":
        print("p1 win")
    elif p1 == "rock" and p2 == "paper":
        print("p2 win")
    elif p1 == "бумага" and p2 == "rock":
        print("p1 win")
    elif p1 == "paper" and p2 == "sciss":
        print("p2 win")
    elif p1 == "sciss" and p2 == "rock":
        print("p2 win")
    elif p1 == "sciss" and p2 == "paper":
        print("p1 win")
Game(player_a, player_b)
playAgain = input("restart? y - n ")
while playAgain == "y":
    player_a = input("your turn p1: ")
    player_b = input("your turn p2: ")
    Game(player_a, player_b)
else:
    print("gg")
