# ChineseZodiac.py
#
# author: F. MacRae
# date: November 2022

# program that assigns chinese zodiac animals to a year.

userYear = int(input("Please enter your birth-year. Eg: 2001\n"))
print("Your birth-year is", userYear)

if userYear % 12 == 0:
    print(userYear, "is the year of the Monkey\n")
elif userYear % 12 == 1:
    print(userYear, "is the year of the Rooster\n")
elif userYear % 12 == 2:
    print(userYear, "is the year of the Dog\n")
elif userYear % 12 == 3:
    print(userYear, "is the year of the Pig\n")
elif userYear % 12 == 4:
    print(userYear, "is the year of the Rat\n")
elif userYear % 12 == 5:
    print(userYear, "is the year of the Ox\n")
elif userYear % 12 == 6:
    print(userYear, "is the year of the Tiger\n")
elif userYear % 12 == 7:
    print(userYear, "is the year of the Hare\n")
elif userYear % 12 == 8:
    print(userYear, "is the year of the Dragon\n")
elif userYear % 12 == 9:
    print(userYear, "is the year of the Snake\n")
elif userYear % 12 == 10:
    print(userYear, "is the year of the Horse\n")
elif userYear % 12 == 11:
    print(userYear, "is the year of the Sheep\n")
else:
    print("You have entered an incorrect year")

'''
Test case assertion 1:
userYear = 2000
output = dragon

Test case assertion 2:
userYear = 1998
output = tiger
'''