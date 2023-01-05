# show menu to user?
# or create a more controlled main method?
# ask user to make option selection?
# or ask to create ticket? First things first.

# option 0 = exit program
# tell user they have exited program

# option 1 = create a ticket
# ask user to input: name, staff ID, email, problem
# generate an automatic ticket number
# generate a new password method. if problem == 'password change'
# new password = first two characters of staff ID and first three
# characters of name.

# option 2 = show all tickets
# print out all tickets:
# ticket number,
# name,
# staff ID,
# email address,
# problem
# response from problem solver
# and ticket status.

# option 3 = re-open resolved ticket and provide feedback
# ask problem solver if they wish to re-open a ticket by number
# and provide feedback about the problem
# include default response 'not yet provided'
# generate an automatic open tickets + 1 and closed ticket - 1
# and status 're-opened'

# option 4 = # ask problem solver to update ticket status to Open or Closed.
# generate an automatic open tickets - 1 and closed ticket + 1

# option 5 = display ticket stats
# print number of tickets submitted,
# number of resolved tickets,
# and number of open tickets.

# Technical...
# Ticket class: for common ticket information
# method to submit a ticket
# method to re-open a ticket by number to open, close and give feedback.
# method to set up 'password changed' feedback
# and change ticket status to closed
# and generate new password.
# method to print all ticket objects - List<Ticket>?
# method to return ticket stats:
# number of tickets,
# number of tickets closed,
# number of tickets open.

# Main class: containing the main method
# one instance of submitting tickets
# and include one ticket with the request of password change.
# Then display ticket stats.
# close some of the tickets
# then display ticket information and ticket stats.
# re-open some of the closed tickets
# and display ticket information and ticket stats.




#Prints Menu options and collects user selection
def menuList():
    print("\nIT5016 HELP DESK TICKET SYSTEM:"
          "_______________________________________\n"
          "Select from the following choices:\n"
          "0: Exit\n"
          "1: Submit helpdesk ticket\n"
          "2: Show all tickets\n"
          "3: Respond to ticket number\n"
          "4: Re-open resolved ticket\n"
          "5: Display ticket stats\n"
          "_______________________________________\n"
          "Please enter menu selection 0 - 5:")
    menuSelection = int(input())
    return menuSelection

# Why does the option selection only work once at the beginning but not when called again
# in other places in the program.


class Ticket:
    """
    To create a Ticket.
    Attributes: Input from user (name, staff ID, email and problem description).
    Method: create new password.
    """

    def __init__(self, name, staffID, email, problem):
        self.name = name
        self.staffID = staffID
        self.email = email
        self.problem = problem

    def passwordChange(self):
        if self.problem == 'Password change':
            print(' Your new password is:', self.name[0:2] + self.staffID[0:3])

    def __repr__(self):
        description = 'Ticket Creator: {name} \n'
        'Staff ID: {staffID} \n'
        'And email address: {email} \n'
        'What seems to be the problem? \n'
        'Please give a brief description:'.format(name = self.name, staffID = self.staffID, email = self.email, problem = self.problem)
        return description


#print(user.__repr__())
# Do I create the objects in the main file under the if statements?
# how do I store all of the objects and retrieve their data?


def submitTicket():

    while option == 1:

        user = Ticket(input('Please enter your name:'), input('And staff ID:'), input('And email address'),
                  input('What seems to be the problem?'))

        print(' Ticket Creator:', user.name, '\n', 'Staff ID:', user.staffID,
              '\n', 'Email Address:', user.email, '\n', 'Problem Description:', user.problem)

        ticketList = []
        ticketList.append(user.name)
        ticketList.append(user.staffID)
        ticketList.append(user.email)
        ticketList.append(user.problem)

        print(ticketList)

        user.passwordChange()
        break
    else:
        print('Nope')

    return user.name, user.staffID, user.email, user.problem
    return ticketList


def anotherTicket():
    ticketOption = input(" Do you have another problem to submit? (Y/N)\n")

    while ticketOption == "Y":
        submitTicket()
        anotherTicket()
        continue
    if ticketOption == "N":
        ticketCount()
        print(" Thank you. Ticket", ticketCount.counter, "has been submitted")
    else:
        print(" Invalid entry. Print Y or N")


class ticketCount:
    # this is used to print the number
    # of instances of the class ticketCount
    counter = 2000

    def __init__(self):
        # increment
        ticketCount.counter += 1

def ticketStats():
    pass


# MAIN FILE FOR TICKETING SYSTEM

option = menuList()
ticketList = []

if option == 0:
    print("Exit program:")

elif option == 1:
    print("DEBUG - Submit ticket")
    test = submitTicket()
    print(test[:2])
    print(test)
    anotherTicket()

elif option == 2:
    print("Show all tickets:")

    if ticketCount.counter == 2003:
        print(ticketCount.counter)

elif option == 3:
    print("In-house respond to ticket")

elif option == 4:
    print("In-house re-open resolved ticket")

elif option == 5:
    print("Ticket Stats:")

else:
    print("Invalid choice. Please enter 0 - 5")


