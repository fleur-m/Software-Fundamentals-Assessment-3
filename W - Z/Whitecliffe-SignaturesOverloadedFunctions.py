# Signatures1.py
#
# @ author: A. N. Other
# date: September 2016

def showYoungAge(myAge):
    print("My age 10 years ago was {0}.\n"
          .format(myAge - 10))

showYoungAge(22)

# Signatures2.py
#
# @ author: A. N. Other
# date: September 2016

def showYoungAge(myAge, myName):
    print("My age 10 years ago was {0}.\n"
          "My name is {1}."
          .format(myAge - 10, myName))

showYoungAge(22, "Tuheitia")

# overloaded functions - more than one signature. Python does not support these kinds of functions




