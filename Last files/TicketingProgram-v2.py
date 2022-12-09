# TicketingProgram-Assessment2.py
#
# Developer: Fleur MacRae
# Date: November 2022
# Program: Ticketing system for help-desk services for internal staff

# class Ticket for user input
class Ticket:

    def __init__(self, name, staffID, email, problem):
        self.name = ticketName
        self.staffID = staffID
        self.email = email
        self.problem = problem

    # method?
    def ticketName(self):
        ticketName = input("Please enter name:")
        print(self.name)

object = Ticket()
Ticket.ticketName(object)


    ####################################################
    # DONE? create ticket_number variable here and use it inside init() to set value of each ticket and update its value inside init()
    # to create ticket number
def ticketNumber__init__(self, number):
    self.number = number

    @staticmethod
    def ticketCounter(number):
        counter = 2000
        counter += 1
        print(number)

    # def stats(any list you have used to maintain objects of ticket):
    # return resolved, opened and closed tickets
    # 3 methods here - resolved, open and closed.

    # object methods
    # def ticketName(self):
    # input("Please enter name:")

    # def ticketStaffID(self):
    #   input("and staff ID:")

    # def ticketEmail(self):
    # input("Your email address:")


# def ticketDescription(self):
#  input("If you require a new password type: Password change\n"
#      "Enter a short description of the request:")

# ticket2001 = Ticket(optionsMenu.ticketname)
# print(ticket2001)


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
    #############################################
    allTickets = []  # DONE create a list here where you can put all the tickets and later you can use them to traverse all tickets and open close them.
    print(allTickets)

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
        def submit(ticketName, ticketStaffID, ticketEmail,
                   ticketDescription):  # here should be a method called for example submit() and define that method up so that you can call it whenever you need to
            ticketName = input("Please enter name:")
            ticketStaffID = input("and staff ID:")
            ticketEmail = input("Your email address:")
            ticketDescription = input("If you require a new password type: Password change\n"
                                      "Enter a short description of the request:")
    submit(1, 2, 3, 4)

    # make a ticket
    # increment and print ticket number
    # counter += 1
    # ticketNumber = ("Ticket Number:", counter)

    ####################################################
    # here create ticket object by calling init() method of ticket class.
    ticketobj = ticket(name, staffID, email, problem)  # number should not be in the init() method
    #  now you have create a ticket object , now you will add this object in the list for example ticket_List here .
    #####################################################

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
        # here you should put all this logic inside a function so that you can call that method in case user want to add new tickets.
        def anotherTicket():
            input("Do you have another problem to submit? (Y/N)\n")

            if anotherTicket == "Y":
                while anotherTicket == "Y":
                    # next ticket
                    # counter += 1
                    # print("Ticket Number:", counter)
                    print("Name:", ticketName, "\nStaff ID:", ticketStaffID, "\nEmail:", ticketEmail)
                    ticketDescription = input("Enter a short description of the request:")
                    anotherTicket = input("Do you have another problem to submit? (Y/N)\n")
            else:
                print(Ticket.name())  # How to call Ticket class
                print(
                    "Thank you. Ticket submitted")  # but how and where is this info stored and retrieved. In what variables? What kind of method and where to submit
    anotherTicket()
    print(anotherTicket())
    # next ticket
    # counter += 1
    # print("Ticket Number:", counter)
    # print("Name:", ticketName, "\nStaff ID:", ticketStaffID, "\nEmail:", ticketEmail)
    # ticketDescription = input("Enter a short description of the request:")
    # anotherTicket = input("Do you have another problem to submit? (Y/N)\n")

        #else:
            #print("\nTicket has been submitted.")  # Method to call?

elif menuSelection == 2:
# show all tickets
#################################################
print(allTickets)
# ??define this ?method? above the ifs and call it here
print("option 2")

elif menuSelection == 3:
# ticket response
###########################################
# response(ticket_List)
print("option 3")

elif menuSelection == 4:
# open or closed ticket - re-open resolved ticket?
#####################################################
# change_status(ticket_List)
print("option 4")

elif menuSelection == 5:
# display ticket stats
#####################################################
# stats(ticket_List)
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
# Sturtz, J. (n.d.). Defining your own Python Function. www.realpython.com. Retrieved November 29, 2022, from https://realpython.com/defining-your-own-python-function/
# Arpitkhushwaha. (2022, February 22). Using a Class with Input in Python. www.geeksforgeeks.org. https://www.geeksforgeeks.org/using-a-class-with-input-in-python/
# Dolinski, A. (2020, May 11). Making a Menu in Python. www.youtube.com. https://www.youtube.com/watch?v=63nw00JqHo0
# Adams, P. (2015, February 24). Creating a menu-based program using functions in Python. www.youtube.com. https://www.youtube.com/watch?v=f3D-w6XMTN8
'''
