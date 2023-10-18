import random

secret = random.randint(0,10)
guess = False

while not guess:
    user = int(input("Choose a number between 0 and 10: "))
    if user == secret:
        print("YOU WON!")
        guess = True
    elif user < secret:
        print("More")
    else:
        print("Less")
        
# Made by JunLovin