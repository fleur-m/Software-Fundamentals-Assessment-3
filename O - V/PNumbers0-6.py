# PNumbers0-6.py
# P = Practice
# author: F. MacRae
# date: November 2022

# Program: print numbers 0-6, except 3 and 6. Use continue instead of break.


for index in range(0,7):
    if (index == 3 or index == 6):
        continue
    print(index, end="")


# Test assertion 1:
'''
0
1
2
3
4
5
6
'''
# Test assertion 2: