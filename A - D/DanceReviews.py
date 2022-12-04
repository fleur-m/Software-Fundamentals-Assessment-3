# DanceReviews.py
#
# author: F. MacRae
# date: November 2022

# program to rate employee performance

'''
rates = 0.0, 0.4, 0.6 ...
0.0 Unacceptable
0.4 Acceptable
0.6 ... Meritorious
bonus = $2400 * rating
'''

userRating = float(input("Please enter the performance rating number:"))

if userRating == 0.0:
    print("Unacceptable performance")
elif userRating == 0.4:
    print("Acceptable performance")
    print("The bonus is $", 2400. * userRating)
elif userRating >= 0.6:
    print("Meritorious performance")
    print("The bonus is $", 2400. * userRating)
else:
    print("Invalid number entered")

'''
Testing assertions:
0.4 = 960
0.6 = 1440
0.8 = 1920
'''