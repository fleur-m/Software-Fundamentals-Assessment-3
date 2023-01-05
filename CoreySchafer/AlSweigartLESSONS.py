'''
print('Hellow World')
print('What is your name?')
myName = input()
print('It is good to meet you, ' + myName)
print('The length of your name is:')
print(len(myName))
print('What is your age?')
myAge = input()
print('You will be ' + str(int(myAge) + 1) + ' in a year.')


name = 'Bob'
age = 22

if name == 'Alice':
    print('Hi Alice')
elif name == 'Bron':
    print('Hi Bron')
elif age <= 15: # 1-15 age
    print('Not Alice or Bron')
else:
    print('Nope') # name = 'Bob'


spam = 0
while spam < 5: # runs 5 times
    print('Hello World')
    spam = spam + 1

name = ''
while True:
    print('Please type your name')
    name = input()
    if name == 'your name':
        break
    print('Thankyou!')

spam = 0
while spam < 5:
    spam = spam + 1
    if spam == 3:
        continue
    print('spam is ' + str(spam))


#print('My name is')
#for i in range(5):
#    print('Ham five times ' + str(i))

i = 0
while i < 5:
    print('Ham five times ' + str(i))
    i = i + 1

total = 0
for num in range(101):
    total = total + num
print(total)

import random
print(random.randint(1, 10))

import sys
print('hello')
sys.exit()
print('goodsbye')

def hello():
    print('Howdy')
    print('Howwdy doo dee')
    print('Hello there')

hello()
hello()
hello()

def hello2(name):
    print('Hello ' + name)

hello2('Alice')
hello2('Bob')

def plusOne(number):
    return number + 1

newNumber = plusOne(5)
print(newNumber)

# local variables cannot be accessed outside of immediate code block.

def spam():
    eggs = 99
    #bacon()
    print(eggs)

def bacon():
    ham = 101
    eggs = 0
    print(ham)

spam()
bacon()

# global variables can be accessed by local variable.

def spam():
    eggs = 'Hello' # local variable
    print(eggs)

eggs = 42 # global variable
spam()
print(eggs)

# Hello
# 42



# Exceptions

def div42by(divideBy):
    try:
        return 42 / divideBy
    except ZeroDivisionError:
        print('Error: You tried to divide by zero.')

print(div42by(2))
print(div42by(12))
print(div42by(0))
print(div42by(1))

print('How many cats do you have?')
numCats = input()
try:
    if int(numCats) >= 4:
        print('That is a lot of cats.')
    else:
        print('That is not that many cats.')
except ValueError:
    print('You did not enter a number.')


# pg 74-76 Lesson 12
# Automate the boring stuff
# Guess the number game

import random

print('Hello. What is your name?')
name = input()
print('Well, ' + name + ', I am thinking of a number between 1 - 20.')

secretNumber = random.randint(1, 20)

for guessesTaken in range(1, 7):
    print('Take a guess.')
    guess = int(input())

    if guess < secretNumber:
        print('Your guess is too low.')
    elif guess > secretNumber:
        print('Your guess is too high.')
    else:
        break # This condition is for the correct guess

if guess == secretNumber:
    print('Good job, ' + name + 'You guessed my number in ' + str(guessesTaken) + 'guesses.')
else:
    print('Nope. The number I was thinking of was ' + str(secretNumber))


# pg 79-87 Lesson 13
# Automate the boring stuff
# Lists

spam = ['cat', 'bat', 'rat', 'elephant'][1]
print(spam)
print(spam[2])

#bat
#t

spam = [['cat', 'bat'], [20,30,40,50]]
print(spam[0]) # ['cat', 'bat']
print(spam[0][1]) # bat

spam = 'Hello'
spam = [10,20,30]
spam[1] = 'Hello'
print(spam) #[10, 'Hello', 30]
spam[1:2] = ['CAT', 'DOG']
print(spam) #[10, 'CAT', 'DOG', 30]


# pg 86-88 Lesson 14
# Automate the boring stuff

for i in range(4):
    print(i) # 0 1 2 3

supplies = ['pens', 'staplers', 'flame-throwers', 'bins']
for i in range(len(supplies)):
    print('Index ' + str(i) + ' in supplies is: ' + supplies[i])


tickets = ['fleur', 9876, 'fit@fam.com', 'problem one']#, 'ralph', 3456, 'fof@dot.com', 'problem two']
#for i in range(len(tickets)):
#    print('Index is:', str(i)  + ' and data is: ' + str(tickets[i]))

name, staffID, email, problem = tickets
print(name)

spam = 42
spam = spam + 1
spam += 1
print(spam)
'''
# 89-92 lesson 15
# methods

spam = ['hello', 'hi', 'howdy', 'heya']
print(spam.index('howdy'))
spam.insert(1, 'chicken')
print(spam) # ['hello', 'chicken', 'hi', 'howdy', 'heya']
