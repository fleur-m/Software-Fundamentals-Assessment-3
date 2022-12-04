# WhileBreak.py
#
# @ author: A. N. Other
# date: September 2016

numberOfTries = 3

while True:
    answer = input("What is the meaning of life?...\n")
    if answer == "42":
        print("Correct! Well done!\n")
        # correct answer so exit loop with break
        break
    else:
        print("Sorry that is the wrong answer...."
                "Try again!\n")
        numberOfTries -= 1 # countdown number of tries

    if numberOfTries == 0:
        print("You have run out of goes. Sorry.")
        break
