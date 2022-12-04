# Nick Walter
'''
for number in range(5):
    print("Hello")
    print("Hi there")
    print(number)

favMovies = ["Sandlot", "The Lego Movie", "Dune"]

for movie in favMovies:
    print(movie)

for number in range(0, 40, 2):
    print(number)

for number in range(1,11):
    print(number)

nameList = ["Josh", "Betty", "Andrew", "Sam"]
print(nameList)
# test assertion: ["Josh", "Betty", "Andrew", "Sam"]

for names in nameList:
    print(names)
# test assertion:
# Josh
# Betty
# Andrew
# Sam
'''

isRunning = True

while isRunning:
    userNumber = int(input("Please enter a number:"))
    print(userNumber)
    if userNumber <= 0:
        print("Do not accept a negative number")
isRunning = False



