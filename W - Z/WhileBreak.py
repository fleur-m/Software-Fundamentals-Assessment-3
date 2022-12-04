# FileName.py
#
# author: A. N. Other
# date: September 2016

numberOfTries = 3

while True:
    answer = input("What is the meaning of life?...\n")
    if answer == "42":
        print("Correct!\n")
        # correct answer, so exit loop using break
        break
    else:
        print("Sorry that is the wrong answer...\n"
              "Try again")
        numberOfTries -= 1

    # check number of tries and break if none left
    if numberOfTries == 0:
        print("You have run out of goes. Sorry.")
        break

    x = input("Press any key to exit.")

    '''
    Test case assertion 1:
    answer = 42 results
    output = Correct!
    
    Test case assertion 2:
    answer 1, 2 then 3 results
    output = You have run out of goes. Sorry.
    '''



# Test assertions:
