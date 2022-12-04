# 3Passwords.py
#
# author: A. N. Other
# date: September 2016

# Program to prompt user for password with 3 attempts and an exit.

password = input("Please enter a password\n")
storedPassword = "Welcome1234"
counter = 0
correctFlag = False

while counter < 2 and correctFlag == False:
    if password == storedPassword:
        print("Correct Password\n")
        correctFlag = True
    elif password == "Exit":
        print("Programme terminated\n")
        correctFlag = True
    else:
        print("Incorrect password\n")
        password = input("Please enter a password\n")
        counter += 1


# Test assertions:
