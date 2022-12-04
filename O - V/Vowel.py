# Vowel.py
#
# @ author: F. MacRae
# date: November 2022

# Program to determine if a user enters a vowel or not.

userLetter = input("Please enter a consonant or a vowel.")

if userLetter == "a":
    print("a is a vowel")
elif userLetter == "e":
    print("e is a vowel")
elif userLetter == "i":
    print("i is a vowel")
elif userLetter == "o":
    print("o is a vowel")
elif userLetter == "u":
    print("u is a vowel")
elif userLetter == "y":
    print("sometimes y is a vowel, and sometimes y is a consonant.")
else:
    print("You have entered a consonant")

'''
Test case assertion 1:
userLetter = i
output = vowel

Test case assertion 2:
userLetter = y
output = sometimes vowel

Test case assertion 3:
userLetter = c
output = consonant
'''
