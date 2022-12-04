# Whitecliffe-ChangingLists.py

list = [2, 7, 3, 90]
list2 = ["monkey", "rabbit", "juice"]

# append - add a single element to a list
list.append(20)
list.append(30)
print(list) # [2, 7, 3, 90, 20, 30]

# extend - add another list to the end
list.extend(list2)
print(list) # [2, 7, 3, 90, 20, 30, 'monkey', 'rabbit', 'juice']

# insert - insert an element at chosen index
list.insert(2, "chicca")
print(list) # [2, 7, 'chicca', 3, 90, 20, 30, 'monkey', 'rabbit', 'juice']

# remove - remove the first instance of an element
list.remove("monkey")
print(list) # [2, 7, 'chicca', 3, 90, 20, 30, 'rabbit', 'juice']

# sort - sorts list, doesnot return
list = [90, 5, 1, 100, 10]
list.sort()
print(list) # [1, 5, 10, 90, 100]

# reverse - reverses the list, doesnot return
list.reverse()
print(list) # [100, 90, 10, 5, 1]

# pop - removes and returns an element at chosen index.
list.pop(2)
print(list) # [100, 90, 5, 1]
list.pop(0)
print(list) # [90, 5, 1]

# if value in L: - boolean check
if 90 in list:
    print(True)