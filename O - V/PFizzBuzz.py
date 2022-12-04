# PFizzBuzz.py
# P = Practice
# author: F. MacRae
# date: November 2022

# Program: iterate integers from 1-50.
# Multiples of 3 = "Fizz"
# Multiples of 5 = "Buzz"
# Multiples of both = "FizzBuzz"

'''list = []

for index in range(1,50):
    if index % 3 == 0:
        list.remove(str(index))
        print("Fizz".join(list))
'''
# Example:

for fizzbuzz in range(51):
    if fizzbuzz % 3 == 0 and fizzbuzz % 5 == 0:
        print("fizzbuzz")
        continue
    elif fizzbuzz % 3 == 0:
        print("fizz")
        continue
    elif fizzbuzz % 5 == 0:
        print("buzz")
        continue
    print(fizzbuzz)
