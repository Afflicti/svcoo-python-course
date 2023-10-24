print("\n\nCODE MADE BY JAKUB KOPCANSKY - GUESS NUMBER\n\n\n")

import random


print("I am thinking a number from 0 to 9.")

answer = random.randint(0, 9)

while True:
    print("What is your guess?")
    guess = int(input())

    if (answer < guess):
        print("Try lower number :)")

    elif (answer > guess):
        print("Try higher number :)")
    
    else:
        print(answer, " was correct. YOU WON!")
        break
        

# improvements:
# 1. expand guessing range
# 2. check if number ( not character ) was entered
# 3. after first game ask, if you want to palay again. Yes -> play again, No -> exit the game

