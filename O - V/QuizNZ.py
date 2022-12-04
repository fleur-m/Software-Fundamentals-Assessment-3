# QuizNZ.py
#
# author: F. MacRae
# date: November 2022

# program of 5 quiz questions about NZ.

print("How well do you know New Zealand??")

isRunning = True
while isRunning:
    question_one = int(input("How many sheep do you think there are per person in NZ?\n"
                       " 20\n"
                       " 2\n"
                       " 7\n"))
    if question_one == 7:
        print("correct")
        isRunning = False
    else:
        print("Try again")


'''
question_two = input("Does NZ have the most bookstores per person in the world?\nYes or No")

if question_two == "yes":# options Y, YES, Yes, y
    print("It does.")
else:
    print("Actually, it does.")

question_three = input("Is NZ the newest country to be populated?\nYes or No")

if question_three == "yes":
    print("Correct. As far as we know, humans were in NZ later than any other country. Well landmass. Except the polar regions.")
else:
    print("It was.")

#question_four
#question_five
#How to make case sensitive
'''