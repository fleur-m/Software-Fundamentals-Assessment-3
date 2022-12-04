# DoorStaff.py
#
# @ author: F. MacRae
# date: 31 October 2022

# This program is to help Bar door staff vet patrons

print("Welcome to the Bar\n")
userDate = int(input("Please enter birth-year: \n"))
print("You birth-year is: ", userDate, "\n")

userName = input("Please enter full name: \n")
print("Your name is: ", userName, "\n")

# Test case assertion 1: result should be True
print("Entry is subject to you being over 21 years old and not being on the banned list.",
      userDate < 2001
      and userName != 'Suzanne May'
      and userName != 'Wiremu Rangi')



