# NumericOperator2a.py
#
# author: F. MacRae
# date: November 2022

# nevermind. You ar an idiot. It is simply a rectangle, because the shape that is extended is also taken out of the rectangle.

import math

side_x = int(input("Please enter the height of the rectangle\n"))
side_y = int(input("Please enter the base length of the rectangle\n"))

rectangle = side_x * side_y
print("The area of the rectangle is", rectangle)

# Test case assertion 1:
# side_x = 4
# side_y = 6
# output = 20

circle_radius = side_x / 2
print("The circle radius is", circle_radius)

# Test case assertion 2:
# side_x = 4
# output = 2

circle_area = circle_radius ** circle_radius
print("The circle area is", circle_area)

# Test case assertion 3:
# area of circle with radius 2
# output = 4

circle = int(math.pi * circle_area)
print("The total area of the circle is", circle)

# Test case assertion 4:
# Actual area of circle with radius 2
# output = 12

# remove half of circle and add to