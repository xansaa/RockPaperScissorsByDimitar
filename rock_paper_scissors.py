import random

rock = "Rock"
paper = "Paper"
scissors = "Scissors"

player_move = input("Choose [r]ock, [p]aper, [s]cissors: ")

if player_move == "r":
    player_move = rock
elif player_move == "p":
    player_move = paper
elif player_move == "s":
    player_move = scissors
else:
    raise SystemExit("Invalid Input. Try again...")

computer_random_name = random.randint(1, 3)
computer_move = ""

if computer_random_name == 1:
    computer_move = rock
elif computer_random_name == 2:
    computer_move = paper
elif computer_random_name == 3:
    computer_move = scissors

print(f"The computer chose {computer_move}.")

if (player_move == "r" and computer_move == "s") or \
        (player_move == "p" and computer_move == "r") or \
        (player_move == "s" and computer_move == "p"):
    print("Congratulations You Won This Game!!!")

elif player_move == computer_move:
    print("Draw!")
else:
    print("You Lose This Game")
