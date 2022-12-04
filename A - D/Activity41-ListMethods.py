# Activity41-ListMethods.py
#
# author: F. MacRae
# date: November 2022
'''
# Challenge 1 - program to prompt user 3 times for an integer and append to list
numberOfTimes = 3
counter = 0
list = []

while counter < 3:
    userNumber = int(input("Please enter a number: "))
    list.append(userNumber)
    counter += 1

print(list)

# Challenge 2 - insert words to list from the user
numberOfTimes = 2
counter = 0
proverbPartList = [ "As a man disappears ", " the ", "land remains." ]

print("As a man disappears .......  ......., the land remains.")

while counter < 2:
    userInput = input("Please enter a word to add to this phrase.")
    proverbPartList.append(userInput)
    counter += 1

print(proverbPartList) ####### how to append elements to chosen index location?

# Challenge 3 - create random number list with 5 integers

import random

list = []
counter = 0
numberOfTimes = 5

for counter in range(5):
    numbers = random.randint(1, 10)
    list.append(numbers)
    counter += 0

print(list)
'''

# Challenge 4 - reverse user input word.

list = []

word = input("Please enter a word:")
list.append(word) ##### how to append each letter of the word?
list.reverse()
print (list)