import random

cards = ["Diamonds" ,"Clubs" , "Spades" , "Hearts"]
ranks = [2 , 3 , 4 , 5 , 6 , 7 , 8 , 9 , "Jack" , "Queen" , "King" , "Ace"]

def pick_a_card():
    card = random.choice(cards)
    rank = random.choice(ranks)
    return(f"The {rank} of {card}")

print(pick_a_card())