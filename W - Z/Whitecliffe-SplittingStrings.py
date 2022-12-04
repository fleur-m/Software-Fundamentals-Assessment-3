# String5.py
#
# @ author: A. N. Other
# date: September 2016

string1 = "It's only after we've lost everything "\
          "that we're free to do anything"

# split string
print("Splitting the string...\n{0}"
      .format(string1.split()),
      "\n")
# ["It's", 'only', 'after', "we've", 'lost', 'everything',
# 'that', "we're", 'free', 'to', 'do', 'anything']

# split string on letter e
print("Splitting the string on the letter e...\n{0}"
      .format(string1.split("e")),
      "\n")
# ["It's only aft", 'r w', "'v", ' lost ', 'v', 'rything
# that w', "'r", ' fr', '', ' to do anything']

# ImprovedCalculator.py
#
# @ author: A. N. Other
# date: September 2016
'''
# function
def doCalculation(userInput):
    # variable to store result
    calculatedAnswer = int

    # split the input
    splitInput = userInput.split()

    # get parameters form splitInput
    inputParams = splitInput[1].split(",")

    # do if elif
    if splitInput[0] == "add":
        calculatedAnswer = int(inputParams[0]) + int(inputParams[1])
    elif splitInput[0] == "subtract":
        calculatedAnswer = int(inputParams[0]) - int(inputParams[1])
    else:
        return "Unknown command entered!"
    return calculatedAnswer

# program run:
# get input
userInput = input("Please enter an operation and 2 parameters...\n")

# do calculation and display
print("The answer is: {0}".format(doCalculation(userInput)),
      "\n")


# Test assertion: 6 add 12 should be 18...\n")
print("The answer is: {0}".format(doCalculation("add 6,12")),
      "\n")

# Test assertion: 626 subtract 100 should be 526...\n")
print("The answer is: {0}".format(doCalculation("subtract 626,100")),
      "\n")

# Test assertion: 54 plus 8 should be Unknown command entered!...\n")
print(doCalculation("plus 54,8"),
      "\n")
'''

# clever programming
# split() and join()
problems = "broke, pale, short, nerdy"
print(problems)

list = problems.split(", ")
print(list)
# ['broke', 'pale', 'short', 'nerdy']

joined = " and ".join(list)
print(joined)
# broke and pale and short and nerdy

csv = ",".join(list)
print(csv)
# broke,pale,short,nerdy

# LinkedIn learning
# Chapter 11

print("Hello World.{0}".format(42 * 7))
# Hello World.294

x = 42
print("The number is {}".format(x))

x = 42
y = 73
print("The number is {} {}".format(x, y))
# print("The number is {xx} {bb}".format(xx = x, bb = y))
# print("The number is {0} {1}".format(x, y))

x = 42 * 747
print("The number is {}".format(x))
# print("The number is {} {}".format(x, y))
print("The number is {:,}".format(x))
# The number is 31,374
print("The number is {:.3f}".format(x))
# three decimal places - The number is 31374.000

# shortcut formatting method
x = 42
print(f"The number is {x:.3f}")

s = "This is a long string with a bunch of words in it."
print(s.split())
# ['This', 'is', 'a', 'long', 'string', 'with', 'a', 'bunch', 'of', 'words', 'in', 'it.']
list = s.split("a")
print(list)
# ['This is ', ' long string with ', ' bunch of words in it.']

s2 = ":".join(list)
print(s2)
# This is : long string with : bunch of words in it.

