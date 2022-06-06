import random

num = random.randint(1,10)
guess = None

while guess != num:
    guess = int(input("Guess a Number Between 1 to 10: "))
    guess = int(guess)

    if guess == num:
        print("Congratulations! You Won!")
        break
    else:
        print("Oops, You Lose! Try Again!")