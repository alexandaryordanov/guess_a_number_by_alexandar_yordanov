import random
# User input
computer_number = random.randint(1, 100)
# Logic
while True:
    player_input = input("Guess the number (1-100): ")
    if not player_input.isdigit():
        print("Invaid input. Try again ...")
        continue
    player_input = int(player_input)
    if player_input == computer_number:
        print("You guess it!")
        break
    elif player_input > computer_number:
        print("Too High!")
    else:
        print("Too Low!")
# Output