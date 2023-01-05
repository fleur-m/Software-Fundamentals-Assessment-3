class Ticket: # blueprint for creating instances

    numTickets = 2000
    increaseBy = 100
    raiseAmount = 10

    def __init__(self, name, staffID, email, problem): # method to set-up data attributes automatically for each instance.
        self.name = name
        self.staffID = staffID              # instance (self) variables: structure data for each instance, so different data, same structure.
        self.email = email                  # class variables: set the same structure and data for all instances of the class
        self.problem = problem

        Ticket.numTickets += 1
# note: when we create methods within a class they recieve the instance as the first argument automatically (self).
    def registration(self):
        return '{} {} {} {}'.format(self.name, self.staffID, self.email, self.problem) # see manual version outside of class too
    def increaseID(self):
        self.staffID = int(self.staffID * self.increaseBy) # or Ticket.increaseBy

    @classmethod
    def setRaiseAmount(cls, amount): # working with class instead of instance
        cls.raiseAmount = amount

    @classmethod
    def fromString(cls, newTicket):
        name, staffID, email, problem = newTicket.split('-')
        return cls(name, staffID, email, problem)

    @staticmethod
    def isWorkDay(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True

###########################

# creates each employee as an instance of this class
ticket1 = Ticket('Corey Schafer', 9238, 'fof@fit.com', 'problem one')
ticket2 = Ticket('Test User1', 9087, 'fow@got.com', 'problem two')
ticket3 = Ticket('Test User2', 748356, 'dod@got.com', 'problem three')
ticket4 = Ticket('Test User3', 8970, 'mot@got.com', 'problem four')
#ticket5 = Ticket(input('Please enter:'), input('Staff ID:'), input('Email:'), input('Problem:'))

#Ticket.setRaiseAmount(50) # can change class method amount

ticket6 = 'John-70000-fit@fam.com-problem three'
ticket7 = 'Steve-30000-fot@dot.com-problem four'
ticket8 = 'Jane-90000-fed@fot.com-problem five'

import datetime
myDate = datetime.date(2016, 7, 10)

print(Ticket.isWorkDay(myDate))
#name, staffID, email, problem = ticket3.split('-')
newTicket5 = Ticket.fromString(ticket7)
newTicket6 = Ticket.fromString(ticket6)
newTicket7 = Ticket.fromString(ticket8)
newTicket8 = ticket3

print(newTicket5)
print(newTicket5.name)
print(newTicket5.staffID)
print(newTicket5.email)
print(newTicket5.problem)
print(Ticket.numTickets) # 2002
#print(Ticket.raiseAmount)
#print(ticket1.raiseAmount)
#print(ticket2.raiseAmount)

