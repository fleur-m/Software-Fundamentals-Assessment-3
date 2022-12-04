# PGuessGame.py
# P = Practise
# author: F. MacRae
# date: November 2022

# Program: user to guess a stored number with prompts - higher or lower.
# print number of tries.

userGuess = int(input("Please enter a number:"))
lastGuess = int
storedNumber = 56
counter = 0
numberOfTries = 0

while userGuess != 56:
    if userGuess < 56:
        if lastGuess != userGuess:
            counter += 1
        lastGuess = userGuess
        userGuess = int(input("Guess a higher number"))
    elif userGuess > 56:
        if lastGuess != userGuess:
            counter += 1
            lastGuess = userGuess
            userGuess = int(input("Guess a lower number"))
    else:
        print("and Nope")




# Test assertions:
