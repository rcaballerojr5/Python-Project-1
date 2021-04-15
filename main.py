from random import randint

# player moves
moves = ["rock", "raper", "scissors"]

while True:
    computer = moves[randint(0, 2)]
    player = input("rock, paper, or scissors? (or end game)").lower()
    if player == "end the game":
        print("The game has ended.")
        break
    # Even match
    elif player == computer:
        print("Tie")
    # rock < paper
    elif player == "rock":
        if computer == "paper":
            print("You Suck", computer, "beats", player)
        else:
            print("Good Job", player, "beats", computer)
    # paper < scissors
    elif player == "paper":
        if computer == "scissors":
            print("You Suck", computer, "beats", player)
        else:
            print("Good Job", player, "beats", computer)
    # scissors < rock
    elif player == "scissors":
        if computer == "rock":
            print("You Suck", computer, "beats", player)
        else:
            print("Good Job", player, "beats", computer)
    # for mistakes
    else:
        print("Spell it right dummy.")
