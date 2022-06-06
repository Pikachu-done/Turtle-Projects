import random

run = True

while run:
    user_input = input("Press Enter to Roll the Dice or Press 'x' to Stop: ")
    if user_input == "x":
        break
    else:
        roll = random.randint(1,6)
        print(f"You Rolled {roll}")

print("Thanks for Playing")