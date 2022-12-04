# P3Passwords.py
#
# author: F. MacRae
# date: November 2022

# Program to prompt user to enter password with 3 attempts. Exit, terminates.

password = input("Please enter password:\n")
answer = "beef10"
counter = 0

while counter <= 2:
    if password == answer:
        print("correct.")
    elif password == "exit":
        print("End")
    else:
        print("Incorrect password")
        password = input("Please enter password again:\n")
        counter += 1


# Test assertions:
'''
answer = beef10 output = correct
answer = exit output = end
answer = cheese50 output = incorrect password. please enter password again
'''