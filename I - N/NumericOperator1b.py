# NumericOperator1b.py
#
# author: A. N. Other
# date: September 2016
side_q = int(input("Please enter the length of the small rectangle\n\n"))
side_w = int(input("Please enter the width of the small rectangle\n\n"))
side_s = int(input("Please enter the length of the large rectangle\n\n"))
side_g = int(input("Please enter the width of the large rectangle\n\n"))
print("\nThe area of your shape is ", side_g * side_s - side_q * side_w,"\n\n")
# Testing
'''
print("My assertions are:"
      "\nq = 5, w = 3, s = 8, g = 4 output = 17"
      "\nq = 2, w = 1, s = 5, g = 3 output = 13")
'''