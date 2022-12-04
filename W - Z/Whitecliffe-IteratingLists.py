# Whitecliffe-IteratingLists.py
#
# author: A. N. Other
# date: November 2022
'''
# iterate = to loop through a list. Use for ... in
list = [1, 4, 5, 2, 9, 12]

for item in list:
    print("An item in the list is ", item)

# if you need both index and item, use enumerate.
for index, item in enumerate(list):
    print("The element index is ", index, "and the value is ", item)

# if index only, use range and length(len).
for index in range(len(list)):
    print("The element index is ", index)

# to iterate a list, use built-in iter function.
i = iter(list)
item = i.__next__() # to fetch the first value
print("An item in the list is ", item)
item = i.__next__() # to fetch the second value
print("An item in the list is ", item)

# sum function gives you the sum of items.
list = sum(list)
print("The sum of the items in the list is....", list)

# Testing. Assertion 1:
# 1 + 4 + 5 + 2 + 9 + 12 = 33

list = [1, 4, 5, 2, 9, 12]
anotherNum = 5
total = sum(list, anotherNum)
print("The sum of the items in the list and another number is....", total)

# average = sum of the list divided by length of the list
average = float(sum(list)) / len(list)
print("The average of the items in the list is....", average)
'''
# join strings using join method
hakaList = ["Taringa","whakarongo","Kia","rite!","Kia","rite!"]
joinedList = " ".join(hakaList)
print("The joined list is....", joinedList)
