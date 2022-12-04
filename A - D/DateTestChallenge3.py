# DateTestChallenge3.py
#
# author: F. MacRae
# date: November 2022

# input two birthdates and output age difference.

from datetime import datetime
from datetime import timedelta

date_one = input("Please enter a birthdate in format DD/MM/YYYY: \n")
date_two = input("Please enter another birthdate in same format: \n")

# cast to datetime object
object_one = datetime.strptime(date_one, '%d/%m/%Y')
object_two = datetime.strptime(date_two, '%d/%m/%Y')

# output years
year_one = object_one.year
print(year_one)
year_two = object_two.year
print(year_two)

# calculate and output the age difference
age_difference = year_two - year_one
print("The age difference in years, between the two is ", age_difference)

