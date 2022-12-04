# BooleanLogic1.py
#
# author: F. MacRae
# date: November 2022

# program to determine whether a student can enrol

distance = int(input("How many kms do you live from the school?\n"))
print("You live", distance, "from the school?\n")
age = int(input("What is your age?\n"))
print("You are", age, "years of age?\n")
residency = input("Do you have the right to live in NZ? Y or N\n")
print("You have the right to live in NZ?", residency)
payFees = input("If you donot have residency in NZ and you are under 18 years of age. Do you select to pay international fees? Y or N\n")


if (distance < 4
   and age <= 18
   and residency == "Y"):
   print("Student can enrol")
elif (distance < 4
   and age < 18
   and payFees == "Y"):
   print("Student can enrol")
else:
   print("Student cannot enrol")

# Test case 1 assertion:
# distance = 3
# age = 17
# residency = "Y"
# output = "Student can enrol"

# Test case 2 assertion:
# distance = 3
# age = 19
# residency = "Y"
# output = "Student cannot enrol"

# Test case 3 assertion:
# distance = 3
# age = 18
# residency = "N"
# payFees = "Y"
