# SleepCalculator.py
#
# author: F. MacRae
# date: November 2022

birth_year = int(input("Welcome to Sleep Calculator.\nPlease enter your birth year:  "))

your_age = (2022 - birth_year)
print("You are ", your_age, "years old.")

hours_slept = (your_age * 356 * 7)
print("You have slept approximately:  ", hours_slept)


