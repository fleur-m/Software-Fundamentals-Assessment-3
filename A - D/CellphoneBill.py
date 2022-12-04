# CellphoneBill.py
#
# @ author: F. MacRae
# date: November 2022

# program to calculate cell-phone usage

# 50 mins air-time
# 50 text messages
# $15 per month
# then air-time = .25c per min
# then text messages = .15c each
# .44c flat charge to support 111 calls
# + 5% sales tax

# number of air-time mins
airTime = int(input("Please enter air-time minutes used this month: \n"))
print("You have used", airTime, "air-time minutes this month.")

# number of text messages
textMessages = int(input("Please enter number of text messages used this month: \n"))
print("You have used", textMessages, "text messages this month.")

baseCharge = 15.00
print(baseCharge, "is your monthly plan fixed rate.")

moreMinutes = 0.25
print("Air-Time minutes over your allocated 50 mins is charged at a rate of", moreMinutes, "per minute")

moreText = 0.15
print("Text messages over your allocated 50 is charged at a rate of", moreText, "per text.")

fee111 = 0.44
print(fee111, "flat charge to support 111 calls")

# more air-time?
if airTime >= 50:
    print(airTime % 50)

totalMinutes = (airTime % 50)
costMinutes = print(totalMinutes * moreMinutes)

# Test case assertion 1:
'''
minutes = 55
remainder = 5
total minutes = 1.25
'''

# more texts?
if textMessages >= 50:
    print(textMessages % 50)

totalText = (textMessages % 50)
costText = print(totalText * moreText)

# Test case assertion 2:
'''
minutes = 55
remainder = 5
total minutes = 0.75
'''

# calculate total cost
print(airTime + textMessages + baseCharge + fee111 + costText + costMinutes)


# Test case assertion 4:
# total cost = 127.44


#print("The total cost for your cellphone this month is",
     # baseCharge + textMessages)

# Test case assertion 3:
'''
minutes = 55
texts = 55
total cost = 125.00
'''



