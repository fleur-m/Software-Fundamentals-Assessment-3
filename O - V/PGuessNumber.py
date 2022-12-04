# PFileName.py
# P = Practice
# author: F. MacRae
# date: November 2022

# Program: guess a number between 1-9.

import random

userNumber = int(input("Enter a number between 1 and 9."))
secretNumber = random.randint(1,10)

while secretNumber != userNumber:
    if userNumber == secretNumber:
        print("You are right!")
    print("Try again")
    userNumber = int(input("Enter a number between 1 and 9."))
    secretNumber = random.randint(1, 10)



# Example:
import random
target_num, guess_num = random.randint(1, 10), 0
while target_num != guess_num:
    guess_num = int(input('Guess a number between 1 and 10 until you get it right : '))
print('Well guessed!')