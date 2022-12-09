class Ticket:
    """
    Registration information of a ticket
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

    def showAllTicket(self):
        return self.name + ' ' + self.staffID + ' ' + self.email + ' ' + self.problem

    @classmethod
    def get_user_input(self):
        name = input("Please enter your name:")
        staffID = input("Enter staff ID:")
        email = input("And email address:")
        problem = input("What seems to be the problem?\n"
                        "Please give a brief description:")
        return self(name, staffID, email, problem)



# creating a person object and returning their full name
person1 = Ticket.get_user_input()
print(person1.showAllTicket())