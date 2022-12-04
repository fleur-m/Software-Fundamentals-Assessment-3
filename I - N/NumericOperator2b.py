import math


radius = int(input("Please enter the radius of the circle c: \n"))

circle_area = int(math.pi * radius * radius)
print("The circle's radial area is", circle_area)

# Test case 1 assertion:
# radius = 3
# output = 28.27
# int output = 28

# minus a quarter of the circle
shape = int(circle_area / 4 * 3)
print("The area of the shape is", shape)

# Test case 2 assertion:
# shape = 21