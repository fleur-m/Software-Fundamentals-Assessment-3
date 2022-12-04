# Activity42-Tuples.py

## tuple creation
'''
inventory = ()

# tuple as a condition
if not inventory:
    print("You are empty-handed.")

input("Press the enter key to continue.")

# create tuple
inventory = ("sword",
             "armour",
             "shield",
             "healing potion")

print(inventory)

# print each element
for item in inventory:
    print(item)

# Hero's Inventory 2.0
# Demonstrates tuples

# create a tuple with some items and display with a 'for' loop
inventory =  ("sword",
              "armor",
              "shield",
              "healing potion")

for item in inventory:
    print(item)

# get length of tuple
print(len(inventory))

# test for membership with 'in' operator
if "healing potion" in inventory:
    print("You will live to fight another day.")

# display on item through index
index = int(input("Enter the index number for an item in inventory:"))
print(index, inventory[index])

# slicing tuples
start = int(input("Enter an index number to begin slice:"))
end = int(input("Enter the index number to end the slice:"))
print(inventory[start:end])

# concatenate tuples
chest = ("gold", "gems")
print(chest)
inventory += chest
print(inventory)
'''

# Word Jumble
# The computer picks a random word and then "jumbles" it
# The player has to guess the original word

import random

# create a sequence of words to choose from
words = ("python", "jumble", "easy", "difficult", "answer", "xylophone")
word = random.choice(words)

##### Doesn't work ######



