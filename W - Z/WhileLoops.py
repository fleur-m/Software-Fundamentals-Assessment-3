# WhileLoops.py
#
# author: A. N. Other
# date: September 2016

isRunning = True

while isRunning:
    answer = input("What is the meaning of life?...\n")
    if answer == "42":
        print("Correct! Well done!\n")
        # correct answer, so exit loop - reset isRunning
        isRunning = False
    else:
        print("Sorry that is the wrong answer..."
              "Try again!\n")

x = input("Press any key to exit.")

'''
Test case assertion 1:
answer = love then loop executes

Test case assertion 2:
answer = 42 results in Correct! Welldone!
'''
