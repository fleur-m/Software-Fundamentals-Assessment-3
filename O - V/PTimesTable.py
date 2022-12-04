# PFileName.py
# P = Practice
# author: F. MacRae
# date: November 2022

# Program: create a multiplication table from 1-10

n = int(input("Enter a number:"))

# use for loop to iterate 10 times
for i in range(1,11):
    print(n,"x", i,"=",n * i)


# Testing. Assertion 1:
'''
n = 2
ouput =
2 x 1 = 2
2 x 2 = 4
2 x 3 = 6
2 x 4 = 8
2 x 5 = 10
2 x 6 = 12
2 x 7 = 14
2 x 8 = 16
2 x 9 = 18
2 x 10 = 20
'''