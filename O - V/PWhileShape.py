# PWhileShape.py
#
# author: F. MacRae
# date: November 2022

# Program:

print("Welcome to the shape calculator.\n")
userShape = input("Which would you like to calculate? Area or Volume (or Exit)?\n")
use = True

while use == True:
    if userShape == "Exit":
        print("Press any key to exit.")
        break
    elif userShape == "Area":
        height = int(input("Enter the height(cm) of the shape: \n"))
        length = int(input("Now enter the length(cm) of the shape: \n"))
        area = height * length
        print("The area of this shape is", area, ":-)\n")
        userShape = input("Would you like to calculate Volume or Exit?\n")
    elif userShape == "Volume":
        height = int(input("Enter the height(cm) of the shape: \n"))
        width = int(input("Now enter the width(cm) of the shape: \n"))
        depth = int(input("Now enter the depth(cm) of the shape: \n"))
        volume = height * width * depth
        print("The volume of this shape is", volume, ":-)")
        userShape = input("Would you like to calculate Area or Exit?\n")
    else:
        error = input("Error")


  #  else:
  #      print("Incorrect. Exit program")


# Test assertions:
