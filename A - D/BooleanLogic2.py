# BooleanLogic2.py
#
# @ author: F. MacRae
# date: 30 October 2022

# Program to determine whether a shopper can purchase

registered = True
oneItem = True


# Test case assertion 1: result should be True
print("The shopper can purchase: \n")
print(registered
      and oneItem)

guestLogIn = True
giftCard = True


# Test case assertion 2: result should be True
print("The shopper can purchase: \n")
print(guestLogIn
      or giftCard)

