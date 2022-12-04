# Function5.py
#
# @ author: A. N. Other
# date: September 2016

score = 4

def getNewScore(paramScore):
    paramScore += 1
    print("You got another point...\n"
          "Your score is now {0}.\n"
          .format(paramScore))
    return paramScore

x = input("Your score is {0} points...\n\n"
          "Hit any key to get another point. "
          .format(score))

score = getNewScore(score)

# Brocode - return statement

def multiply(num1, num2):
    result = num1 * num2
    return result

# or return num1 * num2 less code same output

print(multiply(6, 8))

# or can store in a variable: x = multiply(6, 8)
# print(x)








