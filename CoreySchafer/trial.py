class Ticket:

    """
    Collects user input of ticket and generates new password
    Attributes:
        name(str)
        staffID(int)
        email(str)
        problem(str)
    """

    def __init__(self, name, staffID, email, problem):
        self.name = name
        self.staffID = staffID
        self.email = email
        self.problem = problem

    ticketList = []
    # ticket info input and print out
    @classmethod
    def ticketInfo(self):

        name = input("Please enter name:")
        staffID = input("Enter staff ID:")
        email = input("And email address:")
        problem = input("What seems to be the problem?\n"
                        "Please give a brief description:")

        return name, staffID, email, problem

        if problem == "Password change":
            print("Your new password is:", staffID[0:2] + name[0:3])

        Ticket.ticketList.append(name)
        Ticket.ticketList.append(staffID)
        Ticket.ticketList.append(email)
        Ticket.ticketList.append(problem)

print(Ticket.ticketInfo())

