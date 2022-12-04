# MultiplesOfP.py
#
# author: A. N. Other
# date: September 2016

# Program to print multiples of user-p from 10 until q(inclusive).

p = int(input("Please enter an increment:\n"))
q = int(input("Please enter an ending number:\n"))

counter = 10
number = 10

startingNumber = (10 % p) + 10

while counter < q:
    print(startingNumber, end=", ")
    startingNumber = startingNumber + p
    counter += p

# Test assertions:
'''
p = 4, q = 25 output = 12, 16, 20, 24
p = 3, q = 17 output = 12, 15
'''