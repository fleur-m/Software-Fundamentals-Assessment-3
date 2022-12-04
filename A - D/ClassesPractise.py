# each employee = each Ticket
# class blueprint for ticket/employee

class Ticket:

    def __init__(self, number, name, staffID, email, description, status, response):
        self.number = number
        self.name = name
        self.staffID = staffID
        self.email = email
        self.description = description
        self.status = status
        self.response = response

    # create method
    def nameEmail(self):
        return '{} {}'.format(self.name, self.email)


ticket2001 = Ticket(2001, "Fleur MacRae", 2983748, "fleurm@fof.com", "Won't work",
                    "Closed", "Rebooted system")
ticket2002 = Ticket(2002, "Raff Jinks", 298758, "farr@hom.com", "Password change",
                    "Open", "Not yet provided" )

print(ticket2001)
print(ticket2002)

print(ticket2001.email, ticket2001.name)
print(ticket2002.name, ticket2002.status)

print(ticket2001.nameEmail())

print(Ticket.nameEmail(ticket2001))
