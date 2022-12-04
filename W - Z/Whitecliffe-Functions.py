# Whitecliffe-Functions.py
#
# @ author: A. N. Other
# date: September 2016

def showHello():
    print("Hello there, this is my very first function!!!\n\n")

print("Testing my first user defined function...\n\n")
showHello()

showHello()

def f():
    pass

f()

def ping():
    return "Ping!"

print(ping())

# not sure why this doesnot return Ping!. It does in IDLE
# added print to function call Eg: print(ping())

x = ping()
print(x)

# does print Ping!


# Function2.py
#
# @ author: A. N. Other
# date: September 2016

def triangleArea(b, h):
    return 0.5 * b * h

print(triangleArea(3, 6))

def showHello(param):
    print("Hello there, the number of times this "
          "function is called is {0}!!!\n\n".format(param))

counter = 0

print("Testing my second user defined function...\n\n")

counter += 1
print(showHello(counter))

counter += 1
print(showHello(counter))

# Function3.py
#
# @ author: A. N. Other
# date: September 2016

firstNumber = 6
secondNumber = 4

def showDifference(number1, number2):
    print("The first number is {0}.\n"
          "The second number is {1}.\n"
          "The difference between them is {2}!!!\n"
          .format(number1, number2, number1 - number2))

print("Welcome to my difference calculator...\n\n")

showDifference(firstNumber, secondNumber)

# test case assertion:
'''
print("Test case assertion: if first number is 13 and second number is 2 "
    "then the difference should be 11!!")
    
showDifference(13, 2)
'''

# Brocode Functions with parameters

def simpleAddition(num1, num2):
    answer = num1 + num2
    print("num1 is", num1)
    print(answer)

simpleAddition(5, 3)

# test assertion: num1 is 5. sum is 8

























