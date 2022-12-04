# NumericOperator2c.py
#
# author: F. MacRae
# date: November 2022

# calculate the area of irregular shape

import math

# shape 1 = triangle
side_g = int(input("Please enter the height of the triangle:\n"))
side_f = int(input("Please enter the length of the base of the triangle:\n"))

triangle = side_g * side_f / 2
print("The area of the triangle is", triangle, "\n")

# Test case 1 assertion:
# side_g = 4
# side_f = 4
# output = 8

# shape 2 = rectangle
side_e = int(input("Please enter the base length of the rectangle:\n"))

rectangle = side_e * side_g
print("The area of the rectangle is", rectangle)

# Test case 2 assertion:
# side_e = 2
# side_g = 4
# output = 8

# shape 3 = semi-circle
radius = side_g /2
print(radius)

# Test case 3 assertion:
# side_g = 4
# radius = 2

semi_circle = int(math.pi * radius * radius / 2)
print("The area of the semi-circle is", semi_circle)

# Test case 4 assertion:
# semi_circle = 6

# assemble the irregular shape
shape = triangle + rectangle + semi_circle
print("The area of the shape is:", shape)

# Test case 4 asssertion:
# output = 22
