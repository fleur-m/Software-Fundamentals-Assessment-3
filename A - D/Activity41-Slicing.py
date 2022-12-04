# Activity41-Slicing.py
#
# author: F. MacRae
# date: November 2022

list = [ 34, 123, 5, 77, 59, 2, 4 ]
print(list[2:5]) # [5, 77, 59]

# return the first half of any list with an even number of elements
list = [2, 4, 30, 20, 12, 44]
length = len(list)
half = (int(length / 2))
print(list[0:half]) # [2, 4, 30]

# return last quarter of elements whose total number of elements is a multiple of four.
list = [ 34, 123, 5, 77, 59, 2, 4, 42, 1, 2, 19, 108]
length = len(list)
if length % 4 == 0:
    quarter = (int(length / 4))
    threeQuarters = quarter * 3
    print(list[threeQuarters:length])


