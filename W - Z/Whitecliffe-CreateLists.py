# Whitecliffe-CreateLists.py
#
# author: Whitecliffe
# date: November 2022

# Program: create a list.

# list display
list = [1, 2, 3]
print(list)

a = b = [10, "A", 90.9]
print(a)
print(b)

# Testing. Assertion 1:
'''
print(a) = [10, 'A', 90.9]
print(b) = [10, 'A', 90.9]
'''
'''
##### error ? #####
# built-in list
l = list(1, 2, 3)
print(l) # error ?
'''

# length of list
print(len(list))

# returns item at index [i]
#list[i]
# eg:
print(list[0])

# list[i:j] returns a new list, containing objects between i and j
list = [20, 30, 65, 77]
print(list[0:3])
print(list[1:4])

# nested indexes
list = ["mouse", [1, 3, 6]]
print(list[1][2])
# Test assertion:
output = 6 # correct

# Lists.py
#
# @ author: A. N. Other
# date: September 2016

# empty list
myList = []

# list of integers
myList = [1, 3, 6, 4]

# list with mixed data types
myList = ["mouse", 12, 33.34]

# nested list
myList = ["mouse", [12, 30, 23]]
print(myList[1][2]) # = 23
print(myList[1][0]) # = 12
print(myList[1][-1])# -1 refers to the last number and -2 the second to last number
# = 23

# selection by index
myList = ["p","r","o","b","e"]
print(myList[0]) # = p
print(myList[2]) # = o

# append to list (add to)
myList.append(17)
myList.append(19)
print(myList)

# slicing (cuts a piece out to keep)
myList = ["p","r","o","b","e"]
print(myList[1:3]) # "r", "o"

# dir(numbers)
# Eg: help(numbers.reverse) - Help on built-in function reverse.