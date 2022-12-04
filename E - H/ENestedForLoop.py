# ENestedForLoop.py
# E = Example
# author: A. N. Other
# date: November 2022

# Program:

userInput = int(input("Please enter a number for the size of the shape you wish to create."))

for i in range(userInput):
    for j in range(i):
        print("*", end="")
    print("")

for i in range(userInput, 0, -1):
    for j in range(i):
        print("*", end="")
    print("")


# Test assertion 1:
'''
userInput = 3
*
**
'''
# Test assertion 2:
'''
userInput = 3
*
**
***
**
*
'''
