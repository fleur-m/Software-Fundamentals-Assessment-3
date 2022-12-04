# TicketingProgram-Assessment2.py
#
# Developer: Fleur MacRae
# Date: November 2022
# Program: Ticketing system for help-desk services for internal staff

# class Ticket for user input
class Ticket:

    # to create ticket number
    @staticmethod
    def ticketCounter(number):
        counter = 2000
        counter += 1
        print(number)

    # stores the Ticket data from user: How does it track ticket count?
    def __init__(self, number, name, staffID, email, problem):
        self.number = number
        self.name = name
        self.staffID = staffID
        self.email = email
        self.problem = problem

    #def stats(selfany list you have used to maintain objects of ticket):
    #return resolved, opened and closed ticketStaffID
    # 3 methods here. resolved, open and closed.

    # object methods
    def ticketName(self):
        input("Please enter name:")

    def ticketStaffID(self):
        input("and staff ID:")

    def ticketEmail(self):
        input("Your email address:")

    def ticketDescription(self):
        input("If you require a new password type: Password change\n"
              "Enter a short description of the request:")

    ticket2001 = Ticket(optionsMenu.ticketname)
    print(ticket2001)


'''
    @classmethod
    def fromString(cls, ticketString):
        number, name, staffID, email, problem, status, response = ticketString.split(",")
        cls(number, name, email, problem, status, response)  # this line creates new ticket
        return cls(number, name, email, problem, status, response)

    @classmethod
    def passwordChange(cls, newPassword):
        name, staffID = newPassword.split(" ")
        cls(name, staffID)
        return cls(name[0:2] + staffID[0:3])

newTicket = Ticket.passwordChange("ticket2001")

print(newTicket)

'''
class optionsMenu:

# function - option menu:
    def menu():
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

# calls function and requests user-menu selection:
    menu()
    menuSelection = int(input("Enter menu selection 0 - 5:"))

    if menuSelection == 0:
        print("Program exited")

    elif menuSelection == 1:
        # make a ticket
        # increment and print ticket number
        # counter += 1
        #ticketNumber = ("Ticket Number:", counter)
        ticketName = input("Please enter name:")
        ticketStaffID = input("and staff ID:")
        ticketEmail = input("Your email address:")
        ticketDescription = input("If you require a new password type: Password change\n"
                              "Enter a short description of the request:")
        # user submit ticket and generate ticket number and status and response

        # Ticket.ticketCounter("number")
        # Ticket.ticketName("self")
        # Ticket.ticketStaffID("self")
        # Ticket.ticketEmail("self")
        # Ticket.ticketDescription("self")

        if ticketDescription == "Password change":
            print("Your new password is:", (ticketStaffID[0:2] + ticketName[0:3]))
            # Test assertion: if ticketName is fleur, and ticketDescription is
            # password change and ticketStaffID is 9872135 output = 98fle
            # Test assertion: if ticketName is Jerry, and ticketDescription is
            # password change, and ticketStaffID is 87654, output = 87Jer

        # another ticket
            anotherTicket = input("Do you have another problem to submit? (Y/N)\n")

            if anotherTicket == "Y":
                while anotherTicket == "Y":
                    # next ticket
                    #counter += 1
                    #print("Ticket Number:", counter)
                    print("Name:", ticketName, "\nStaff ID:", ticketStaffID, "\nEmail:", ticketEmail)
                    ticketDescription = input("Enter a short description of the request:")
                    anotherTicket = input("Do you have another problem to submit? (Y/N)\n")
            else:
                print(Ticket.name()) # How to call Ticket class
                print("Thank you. Ticket submitted") # but how and where is this info stored and retrieved. In what variables? What kind of method and where to submit

        # next ticket
        #counter += 1
        #print("Ticket Number:", counter)
        #print("Name:", ticketName, "\nStaff ID:", ticketStaffID, "\nEmail:", ticketEmail)
        #ticketDescription = input("Enter a short description of the request:")
        #anotherTicket = input("Do you have another problem to submit? (Y/N)\n")

    else:
        print("\nTicket has been submitted.") # Method to call?

    elif menuSelection == 2:
        # show all tickets
        # list<Ticket>
        print("option 2")

    elif menuSelection == 3:
        # ticket response
        print("option 3")

    elif menuSelection == 4:
        # open or closed ticket - re-open resolved ticket?
        print("option 4")

    elif menuSelection == 5:
        # display ticket stats
        print("option 5")

else:
    print("Invalid Option")
























'''
                    
# use list<Ticketclass>
# method to store menuSelection variables?
# instructions for selections:

if menuSelection == 0:
     # exit program
    print("Program exited") # test assertion: menuSelection = 6, "Invalid option". Correct
                            # test assertion: menuSelection = 0, "Exited program". Correct

elif menuSelection == 1:
    # make a ticket
    # increment and print ticket number
    counter += 1
    ticketNumber = ("Ticket Number:", counter)
    ticketName = input("Please enter name:")
    ticketStaffID = input("and staff ID:")
    ticketEmail = input("Your email address:")
    ticketDescription = input("If you require a new password type: Password change\n"
                              "Enter a short description of the request:")

    if ticketDescription == "Password change":
        print("Your new password is:", (ticketStaffID[0:2] + ticketName[0:3]))
        # Test assertion: if ticketName is fleur, and ticketDescription is
        # password change and ticketStaffID is 9872135 output = 98fle
        # Test assertion: if ticketName is Jerry, and ticketDescription is
        # password change, and ticketStaffID is 87654, output = 87Jer

      

elif menuSelection == 2: # show all tickets
    ticketDict = {"Ticket number:": ticketNumber, "\nName": ticketName,
                  "\nStaff ID:": ticketStaffID, "\nEmail:": ticketEmail,
                  "\nDescription of problem:": ticketDescription}
    # "\nTicket status:": ticketStatus, "\nResponse:": ticketResponse}
    #   print(ticketDict)
    print(ticketDict)






# References:
# Pozo Ramos, L. (2022, February 16). Providing Multiple Constructors in Your Python Classes. www.realpython.com. https://realpython.com/python-multiple-constructors
# Godbold, C. (2020, September 7). Simple Ordering System, Video 1 - 3. www.youtube.com. https://www.youtube.com/watch?v=Z47CSq85zGE
# Python Classes and Objects. (n.d.). www.programiz.com. Retrieved November 26, 2022, from https://www.programiz.com/python-programming/class
# Schaefer, C. (2016, June 21). Python OOP Tutorial 1: Classes and Instances. www.youtube.com. https://www.youtube.com/watch?v=ZDa-Z5JzLYM
# Python Method – Classes, Objects and Functions in Python. (n.d.). www.data-flair.training. Retrieved November 29, 2022, from https://data-flair.training/blogs/python-method

'''
