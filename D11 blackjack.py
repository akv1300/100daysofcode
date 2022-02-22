#blackjack
import random
def card():
    cards = [11,2,3,4,5,6,7,8,9,10,10,10,10]
    return (random.choice(cards))
user = []
computer = []
user.append(card())
computer.append(card())
def play():
    user.append(card())
    computer.append(card())
    print(f"your cards {user}")
    print(f"computer's {computer[0]}")
    if sum(user) == 21:
        print(f"You won {user}")
    elif sum(computer) == 21:
        print("You lose")
    elif sum(user) > 21:
        if (x for x in user) == 11:
            user[0]-=10
        else:
            print("You lose")
    cont = input("Do you want to play futher y or n")
    if cont == "y":
        play()
    else:
        while sum(computer) <17:
            computer.append(card())
        if sum(computer) > 21 :
            print("You won")
        elif sum(user) > sum(computer):
            print("You won")
        elif sum(user) < sum(computer):
            print("You lose")
        else:
            print("Match draw")
play()