# ForLoop.py
#
# @ author: A. N. Other
# date: September 2016

# Program: display user message a requested number of times.

userInput = int(input("Please enter the number of times you wish to see the message."))

for i in range(userInput):
    print("hello world...", i)

# Testing. Assertion 1:
'''
userInput = 2
hello world.... 0
hello world.... 1
'''