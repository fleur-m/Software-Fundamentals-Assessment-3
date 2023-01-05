from itresponse import itResponse


class ticket:
    counter = 2000

    def __init__(self, creatorName, staffID, email, issueDescription):
        self.creatorName = creatorName
        self.staffID = staffID
        self.email = email
        self.issueDescription = issueDescription
        ticket.counter += 1
        self.ticket_inst = ticket.counter

    def displayTicket(self):
        ticket_info = []
        ticket_info.append(self.creatorName)
        ticket_info.append(self.staffID)
        ticket_info.append(self.email)
        ticket_info.append(self.issueDescription)

        if self.creatorName == "":
            print("Ticket Creator: Not Specified")
        else:
            print("Ticket Creator: " + str(ticket_info[0]))
        if self.staffID == "":
            print("--STAFF ID REQUIRED TO SUBMIT TICKET--")
            return
        else:
            print("Staff ID: " + str(ticket_info[1]))
        if self.email == "":
            print("Email Address: Not Specified")
        else:
            print("Email Address: " + str(ticket_info[2]))
        if self.issueDescription == "":
            print("--DESCRIPTION OF YOUR ISSUE IS REQUIRED TO SUBMIT TICKET--")
            return
        else:
            print("Description: " + str(ticket_info[3]))

    def autoAssign(self):
        if self.staffID == "" or self.issueDescription == "":
            print("TICKET NOT CREATED\nTicket Number: N/A")
            return
        else:
            print("Ticket Number: " + str(self.ticket_inst))

    respond = itResponse.respond
    resolve = itResponse.resolve
    reopen = itResponse.reopenStatus


###
class itResponse:

    def __init__(self, ticketResponse):
        self.ticketResponse = ticketResponse

    def respond(self):
        if self.ticketResponse == "":
            print("Response: Not Yet Provided")
        elif "password change" in self.ticketResponse:
            print("New password generated: " + str(generatePassword.newPassword()))
        else:
            print("Response: " + self.ticketResponse)

    def resolve(self):
        if self.ticketResponse == "":
            print("Ticket Status: Open")
        else:
            print("Ticket Status: Closed")

    def reopenStatus(self):
        print("Ticket Status: Reopened")

###
from ticketClass import ticket


class ticketStats:
    tickets = ticket.displayTicket()

    def countTickets():
        ticketsCreated = []
        ticketsCreated.append(tickets)
        print(len(ticketsCreated))


# Testing:

t1 = ticket("Inna", "INNAM", "inna@whitecliffe.co.nz", "My monitor stopped working")
t1R = itResponse("sucks")
t2 = ticket("", "MARIAH", "", "Request for video camera to conduct webinars")
t2R = itResponse("")
t3 = ticket("Joel", "JOELS", "", "change password")
t3R = itResponse("ye")

print("\nPrinting Tickets:\n")

t1.autoAssign()
t1.displayTicket()
t1R.respond()
t1R.resolve()
print()

t2.autoAssign()
t2.displayTicket()
t2R.respond()
t2R.resolve()
print()

t3.autoAssign()
t3.displayTicket()
t3R.respond()
t3R.resolve()

Printing Tickets:

Ticket Number: 2001
Ticket Creator: Inna
Staff ID: INNAM
Email Address: inna@whitecliffe.co.nz
Description: My monitor stopped working
Response: sucks
Ticket Status: Closed

Ticket Number: 2002
Ticket Creator: Not Specified
Staff ID: MARIAH
Email Address: Not Specified
Description: Request for video camera to conduct webinars
Response: Not Yet Provided
Ticket Status: Open

Ticket Number: 2003
Ticket Creator: Joel
Staff ID: JOELS
Email Address: Not Specified
Description: change password
Response: ye
Ticket Status: Closed