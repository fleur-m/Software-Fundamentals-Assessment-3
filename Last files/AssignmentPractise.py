# object method:
class Person:

    def __init__(self, age, gender):

        self.age = age

        self.gender = gender



    def myIntro(self):

        print("Hello my gender is " +self.gender)

        print('Hello my age is', self.age)  # , is used when we need to show int or float values.

harry = Person(36, "male")

sarrah = Person(34, "female")

harry.myIntro()

sarrah.myIntro()











# menu
'''
menu = ["Exit", "Submit helpdesk tickets",
        "Show all tickets", "Respond to ticket number",
        "Re-open resolved ticket", "Display ticket stats"]
option = [0, 1, 2, 3, 4, 5]

myorderMenu = []
myorderOption = []

print("Welcome to Ticket System") # add menu options here



nextOrder = True

while nextOrder == True:
    menuOption = input("Please select option from menu")
    if menuOption == "Exit":
        myorderMenu.append(menu[0])
        myorderOption.append(option[0])

    elif menuOption == "Submit helpdesk tickets":
        myorderMenu.append(menu[1])
        myorderOption.append(option[1])

    elif menuOption == "Show all tickets":
        myorderMenu.append(menu[2])
        myorderOption.append(option[2])

    elif menuOption == "Respond to ticket number":
        myorderMenu.append(menu[3])
        myorderOption.append(option[3])

    elif menuOption == "Re-open resolved ticket":
        myorderMenu.append(menu[4])
        myorderOption.append(option[4])

    elif menuOption == "Display ticket stats":
        myorderMenu.append(menu[5])
        myorderOption.append(option[5])

    else:
        print("Not on menu")
    finished = input("Have you finished Y/N?")
    if finished == "N":
        nextOrder = True
    else:
        nextOrder = False

print(myorderMenu)
print(myorderOption)
'''