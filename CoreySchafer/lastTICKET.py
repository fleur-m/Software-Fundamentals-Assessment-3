# Prints Menu options and collects user selection
def menuList():
    print("\nIT5016 HELP DESK TICKET SYSTEM:\n"
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

    option = int(input())

    if option == 0:
        print("Exit program:")

    elif option == 1:
        print("DEBUG - Submit ticket")
        submitTicket()

    elif option == 2:
        print("Show all tickets:")
        showTickets()

    elif option == 3:
        print("In-house respond to ticket")
        response()

    elif option == 4:
        print("In-house re-open resolved ticket")
        reopen()

    elif option == 5:
        print("Ticket Stats:")
        showStats()

    else:
        print("Invalid choice. Please enter 0 - 5")
        menuList()


class Ticket:
    """
    Sets up blueprint attributes for user input of tickets.
    Also has a password change method
    """
    counter = 2000

    def __init__(self, name, staffID, email, problem, status = 'Open', response = 'Not yet provided'):
        self.name = name
        self.staffID = staffID
        self.email = email
        self.problem = problem
        self.status = status
        self.response = response
        self.ticketNo = Ticket.counter
        Ticket.counter += 1

    def passwordChange(self):
        if self.problem == 'Password change':
            print(' Your new password is:', self.name[0:2] + self.staffID[0:3])
            self.status = 'Closed'

ticketList = []
def submitTicket():
    user = Ticket(input('Please enter your name:'), input('And staff ID:'), input('And email address'),
                  input('What seems to be the problem?'))
    #print(user.__dict__)
    ticketList.append(user)
    print(' Ticket Creator:', user.name, '\n', 'Staff ID:', user.staffID,
          '\n', 'Email Address:', user.email, '\n', 'Problem Description:', user.problem, '\n',
          'Ticket Status:', user.status, '\n', 'Technician Response:', user.response, '\n', 'Ticket Number:', user.ticketNo)
    user.passwordChange()
    ticketOption = input(" Do you have another problem to submit? (Y/N)\n")
    if ticketOption == 'Y':
        submitTicket()
    elif ticketOption == 'N':
        menuList()


def showTickets():

    #for i in ticketList:
    #    print(i)             ### prints <__main__.Ticket object at 0x100dc23d0>


    for i in range(len(ticketList)):
        print('Name:', ticketList[i].name, '\n', 'Staff ID:', ticketList[i].staffID, '\n',
              'Email Address:', ticketList[i].email, '\n', 'Problem Description:', ticketList[i].problem, '\n',
              'Ticket Status:', ticketList[i].status, '\n', 'Technician Response:', ticketList[i].response, '\n',
              'Ticket Number:', ticketList[i].ticketNo)

    menuList()


def showStats():
    for i in range(len(ticketList)):
        print('Number of Open Tickets:', ticketList[i].status.count('Open'))
        print('Number of Closed Tickets:', ticketList[i].status.count('Closed'))
        print('calculate:') # How do I calculate total number of open and total number of closed?
        print('Total number of Tickets:', len(ticketList))

    menuList()


def reopen():
    for i in range(len(ticketList)):
        print(
        'here you ask user to give number of required ticket and then find that ticket in list and change status variable value from close to open')
        int(input('Please enter the number of the ticket you would like to reopen:'))

        ### find that ticket in list
        print(ticketList[i].ticketNo)
    # change status variable to 'open'.
        Ticket.status = 'Open'
        print('Ticket Status:', Ticket.status)

    menuList()


def response():
    print(
        'here you ask user to give number of required ticket and then find that ticket in list and change response variable value by taking input from user.')
    int(input('Please enter the number of the ticket you would like to reopen:'))
    # find ticket in List
    print(Ticket.response(2001))

    menuList()


menuList()
# MAIN FILE FOR TICKETING SYSTEM