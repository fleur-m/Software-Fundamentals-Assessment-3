# Whitecliffe-Exceptions.py

# Exception0
#
# @ author: A. N. Other
# date: September 2016

# LBYL exceptions
'''
def divideNumbers(number1, number2):
    if number2 == 0:
        return "Cannot divide by zero."
    return number1 / number2

print(divideNumbers(3,0))
'''
# EAFP exceptions
# Exception1
#
# @ author: A. N. Other
# date: September 2016
'''
def divideNumbers(number1, number2):
    try:
        return number1 / number2
    except ZeroDivisionError:
        return "Error, cannot divide by zero!"

print(divideNumbers(3,0))
'''
# Exception2
#
# @ author: A. N. Other
# date: September 2016
'''
def divideNumbers(number1, number2):
    try:
        return number1 / number2
    except (ZeroDivisionError, TypeError):
        return "Error, check your parameters!"

print(divideNumbers(3,0))
'''
######### Best practice ##############
# Exception3
#
# @ author: A. N. Other
# date: September 2016

def divideNumbers(number1, number2):
    try:
        return number1 / number2
    except ZeroDivisionError:
        return "Error, cannot divide zero."
    except TypeError as e:
        message = "Error, an operand is the wrong type...\n" \
                "Or as Python would say...\n{0}".format(e)
        return message

print(divideNumbers(3,"Four"))
