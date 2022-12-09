# TicketingProgram-v3.py
#
# Developer: Fleur MacRae
# Date: December 2022
# Program: Ticketing system for help-desk services for internal staff
# Process - It is like knowing part of the recipe, many of the instructions,
# but missing some understanding about what and when to use them and how
# to use them together.

class Menu(object):
    """
      Menu list, option selection and password change
    """

    def __init__():
        pass

    def menuList():
        # list of menu and logic to take input from user

        print("\nIT5016 Help Desk Ticket System:\n"
              "_______________________________________\n\n"
              "Select from the following choices:\n"
              "0: Exit\n"
              "1: Submit helpdesk ticket\n"
              "2: Show all tickets\n"
              "3: Respond to ticket number\n"
              "4: Re-open resolved ticket\n"
              "5: Display ticket stats\n"
              "_______________________________________\n")
        menuSelection = int(input("Enter menu selection 0 - 5:"))
        return menuSelection

    #def passwordChange():
        # logic to create new password
        # problem =
        #if problem == "Password change":
          #  newPassword = (staffID[0:2] + name[0:3])
          # print("Your new password is:", newPassword)

allTickets = []

class Ticket:
    """
    Collects user input of ticket, counts tickets and defines ticket stats
    Attributes:
        name(str)
        staffID(int)
        email(str)
        problem(str)
    """

    #@staticmethod #Static field?
    #def ticketCounter():
    counter = 2000
    counter += 1

    def __init__(self, name, staffID, email, problem):
        self.name = name
        self.staffID = staffID
        self.email = email
        self.problem = problem

    def showAllTicket(self):
        return self.name + ' ' + self.staffID + ' ' + self.email + ' ' + self.problem

    @classmethod
    def userInput(self):
       # allTickets = []  # how get store ticket info in here?
        name = input("Please enter name:")
        staffID = input("Enter staff ID:")
        email = input("And email address:")
        problem = input("What seems to be the problem?\n"
                        "Please give a brief description:")

        if problem == "Password change":
            print("Your new password is:", staffID[0:2] + name[0:3])

        allTickets.append(name)
        allTickets.append(staffID)
        allTickets.append(email)
        allTickets.append(problem)
        print(allTickets)

        anotherTicket()
       # userInfo = self(name, staffID, email, problem)
       # print(userInfo)
       # return userInfo





# creating a person object and returning their ticket details
#person1 = Ticket.userInput()
#print(person1.showAllTicket())



    # tracks ticket count stats
    def statsSubmitted():
        totalTickets = (Ticket.counter - 2000)
        print("Tickets submitted:", totalTickets)

    def statsOpen():
        open = (Ticket.counter - 5) # minus the value of Ticket.statsResolved
        print("Tickets open:", open)

'''
    def statsResolved():
        if ___ == "Resolved"
        return "Resolved Tickets:", number of Resolved tickets)
    print(statsResolved)
'''

# Function that allows ticket response from backend.
#def ticketResponse():
    # Add feedback - not user though
        
       

# another ticket function - Do you have another problem?
def anotherTicket():
    ticketOption = input("Do you have another problem to submit? (Y/N)\n")

    if ticketOption == "Y":
        Ticket.userInput()
        anotherTicket()
    elif ticketOption == "N":
        print("Thank you. Ticket", Ticket.counter, "has been submitted")
    else:
        print("Invalid entry. Print Y or N")



# MAIN FILE FOR TICKETING SYSTEM


#allTickets = [] # use a list to keep track of tickets - see submit ticket method
#instance1 = Ticket.userInput() # how do I append this info to allTickets?
#print(instance1.showAllTicket())


option=Menu.menuList()

if option == 0:
    print("exit program")

elif option == 1:
    print("submit ticket")
    Ticket.userInput()

elif option == 2:
    print("show all tickets")

elif option == 3:

    print("in-house respond to ticket")

elif option == 4:
    print("in-house re-open resolved ticket")

elif option == 5:
    print("ticket stats")
    Ticket.statsSubmitted()
    Ticket.statsOpen()

else:
    print("Invalid choice. Please enter 0 - 5")
    Menu.menuList()











# References:
# Marsh, C. (n.d.). Python Class Attributes: An Overly Thorough Guide. www.toptal.com. Retrieved December 6, 2022, from https://www.toptal.com/python/python-class-attributes-an-overly-thorough-guide
# ArjanCodes. (n.d.). If you’re not using Python DATA CLASSES yet, you should. www.youtube.com. Retrieved December 6, 2022, from https://www.youtube.com/watch?v=vRVVyl9uaZc
# Caoili, E. (2020, January 16). Python Basics: Everything is an object. www.medium.com. https://medium.com/analytics-vidhya/python-basics-everything-is-an-object-6833a7ab3285
# Bell, A. (n.d.). Introduction To Computer Science And Programming In Python. Lecture 9: Python Classes and Inheritance. Retrieved December 6, 2022, from https://ocw.mit.edu/courses/6-0001-introduction-to-computer-science-and-programming-in-python-fall-2016/resources/lecture-9-python-classes-and-inheritance

