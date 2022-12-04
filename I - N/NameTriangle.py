# NameTriangle.py
#
# author: F. MacRae
# date: November 2022

# program to name the type of triangle.

#length of sides =
# equilateral - all sides same
# isosceles - two sides the same
# scalene - all sides have different lengths

print("Please enter the lengths of a, b and c sides of the triangle:\n")
a = int(input("a:     \n"))
b = int(input("b:     \n"))
c = int(input("c:     \n"))



if a == b == c:
    print("This is an equilateral triangle.")
elif (a == b or a == c
    and b == a or b == c
    and c == a or c == b):
    print("This is an isosceles triangle.")
else:
    print("This is an scalene triangle.")

# Test case assertion 1:
'''
a = 10
b = 10
c = 10
"This is an equilateral triangle"
'''

# Test case assertion 2:
'''
a = 5
b = 10
c = 10
"This is an isosceles triangle"
'''

# Test case assertion 3:
'''
a = 5
b = 8
c = 10
"This is a scalene triangle"
'''