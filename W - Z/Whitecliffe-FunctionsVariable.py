# Function4.py
#
# @ author: A. N. Other
# date: September 2016

# trying to use a variable that is out of scope
'''
score = 4

def showNewScore():
    score += 1
    print("You got another point...\n"
          "Your score is now {0}.\n"
          .format(score))

x = input("Your score is {0} points...\n\n"
          "Hit any key to get another point. "
          .format(score))

showNewScore()

# Brocode functions and variable scope

# local scope variable
def displayName():
    name = "Code"
    print(name)

# attempt to print variable outside of the function
print(name)
'''
# test assertion: Name Error

name = "Bro" # global variable

def displayName():
    name = "Code"
    print(name)

displayName()
print(name)
# Test assertion:
# print Code
# print Bro

