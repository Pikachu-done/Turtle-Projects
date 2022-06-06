import string
import random
print("Welcome to the Password Picker..")

adjectives = ['sleepy', 'slow', 'smelly', 'wet', 'fat', 'red', 'orange', 'yellow', 'green', 'blue','purple', 'fluffy', 'white', 'proud', 'brave']
nouns = ['apple', 'dinosaur', 'ball', 'toaster', 'goat', 'dragon', 'hammer', 'duck', 'panda']

while True:
    adjectives = random.choice(adjectives)
    nouns = random.choice(nouns)
    
    special_char = random.choice(string.punctuation)

    password = adjectives + nouns + special_char
    print("Your Password is: %s"% password)

    response = input("Would You Like to change your Password..? Type Y For Yes And N for No: ")
    if response == "n" or response == "N":
        break