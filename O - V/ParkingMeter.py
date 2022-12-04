# ParkingMeter.py
#
# author: A. N. Other
# date: September 2016

# program to calculate cost of parking

print("Kia Ora, this is a parking meter")
parkTime = int(input("How many hours would you like to park?"))
print("parkTime time is ", parkTime, " hours.")

rate = 4
cost = 0

if parkTime > 3:
    cost = rate * 3
    # drop the rate by $2
    rate -= 2
    # get remainder of parking time
    parkTime -= 3
    # add to the current cost
    cost += rate * parkTime
    print("The cost of the parking is $", cost)

# Test case assertion 1:
'''
parkTime = 4
total cost of parking = $14
'''

# Test case assertion 2:
'''
parkTime = 6
total cost of parking = $18
'''

# Test case assertion 3:
'''
parkTime = 5
total cost of parking = $16
'''

