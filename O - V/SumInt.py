# SumInt.py
#
# author: A. N. Other
# date: September 2016

# Program with while loop to output the sum of 'the first n positive' integers.

number = int(input("Please enter a number\n\n"))
counter = 0
total = 0

while counter <= number:
    total = total + counter
    counter += 1
    print("counter =", counter)
    print("total =",total)

print("\nn =", number, " sum= ", total, "\n\n")


# Test assertions:
'''
number = 5 output = 15
number = 19 output = 190
'''
