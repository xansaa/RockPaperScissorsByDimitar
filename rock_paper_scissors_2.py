import random
user_win = 0
computer_win = 0

while user_win < 3 and computer_win < 3:
    user_input = input("Choose [r]ock, [p]aper, [s]cissors: ").lower()
    computer_input = random.choice(["r", "p", "s"])

    if (user_input == "r" and computer_input == "s") or \
        (user_input == "p" and computer_input == "r") or \
        (user_input == "s" and computer_input == "p"):
        print("Congratulations!!! You Won This Round!!!")
        user_win += 1
    elif user_input == computer_input:
        print("Draw!")
    else:
        print("You Lose!!! Computer Won This Round")
        computer_win += 1

print(f"Final Result: {user_win}:{computer_win}")

if user_win > computer_win:
    print("Congratulations!!! You Won This Game!!!")
else:
    print("You Lose!!! Computer Won This Game")

