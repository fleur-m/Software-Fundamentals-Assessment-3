# NumericOperator1c.py
#
# author: F. MacRae
# date: November 2022

# calculate the area of this irregular shape

side_u = int(input("Please enter the height of the rectangle: \n"))
side_m = int(input("Please enter the length of the base of the rectangle: \n"))

base_triangle = side_u + side_m * 2
print("The base of the triangle is ", base_triangle)

# Test assertion 1:
# side_u = 4, side_m = 2, output = 8

side_n = int(input("Please enter the side n length of the triangle: \n"))

triangle = base_triangle * side_n / 2
print(triangle)

#Test assertion 2:
# side_n = 5, output = 20