# EGuessName.py
# E = Example
# author: A. N. Other
# date: September 2016

# Program:

guess = int(input("Guess a number\n"))
lastGuess = int
secretNumber = 42
counter = 0
found = False

while found != True:
    if guess > secretNumber:
        print("Guess Lower")
        if lastGuess != guess:
            counter += 1
        lastGuess = guess
        guess = int(input("Guess a number"))
    elif guess < secretNumber:
        print("Guess Higher")
        if lastGuess != guess:
            counter += 1
        lastGuess = guess
        guess = int(input("Guess a number"))
# Test assertions:
