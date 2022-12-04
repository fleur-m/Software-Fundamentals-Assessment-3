# DatetimeChallenge4.py
#
# author: F. MacRae
# date: November 2022

from datetime import datetime
from datetime import timedelta

# input date and int: number of years = the difference
date = input("Welcome and please enter a date in the format DD/MM/YYYY: \n")
number = int(input("Now please enter a number: \n"))

# cast date to datetime object
date_object = datetime.strptime(date, '%d/%m/%Y')

# add number to date
later_date = date_object + timedelta(days = number)# timedelta doesnot accept a string


