# While[1-n].py
#
# author:
# date: November 2022

# Program with while loop that prints Eg: n = 3 [1][2][3]

import random

number = random.randint(1,9)
counter = 0

while counter < number:
    print("[", counter + 1, "] ", end="")
    counter += 1

# Testing assertions:
'''
number = 6 output = [1] [2] [3] [4] [5] [6]
number = 3 output = [1] [2] [3]
'''
