class Ticket: # blueprint for creating instances

    numTickets = 2000
    increaseBy = 100

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
###########################

# creates each employee as an instance of this class
ticket1 = Ticket('Corey Schafer', 9238, 'fof@fit.com', 'problem one')
ticket2 = Ticket('Test User', 9087, 'dod@got.com', 'problem two')
#ticket3 = Ticket(input('Please enter:'), input('Staff ID:'), input('Email:'), input('Problem:'))

print(Ticket.numTickets) # 2002

'''
ticket1.increaseBy = 200

print(Ticket.increaseBy)
print(ticket1.increaseBy)
print(ticket2.increaseBy)
'''
#ticket1.increaseID()
#print(ticket1.staffID)

#print(ticket1.registration())
#print(ticket3.registration())
#print(Ticket.registration(ticket1))
#print(Ticket.registration(ticket3))


#def newPassword(self):
#    if self.problem == 'Password change':
#        return "Your new password is:", staffID[0:2] + name[0:3]
