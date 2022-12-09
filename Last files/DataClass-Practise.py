'''
from dataclasses import dataclass

@dataclass
class Ticket:

    name: int
    staffID: int
    email: str
    problem: str

    def registration():
        name = input("Please enter your name:")
        staffID = input("Enter staff ID:")
        email = input("And email address:")
        problem = input("What seems to be the problem?\n"
                   "Please give a brief description:")
        print("Name:", name,"\n"
              "Staff ID:", staffID, "\n"
              "Email:", email, "\n"
              "Problem:", problem)

Ticket.registration()



class Coordinate(object):

    #data: what is the object:
    def __init__(self, x, y): # creates an instance
        self.x = x
        self.y = y

    # create an instance by calling init method
    c = Coordinate(3,4)
    origin = Coordinate(0,0)

    # interaction: methods. function for this object only. Ways people can interact with this object.
    def distance(self, other):
        xDiffSQ = (self.x - other.x) ** 2
        yDiffSQ = (self.y - other.y) ** 2

        c = Coordinate(3, 4)
        origin = Coordinate(0, 0)
        print(c.distance(origin)) # or print(Coordinate.distance(c, zero))

    def __str__(self):
        return "<" + str(self.x) + "," + str(self.y) + ">"
        print(c)



# use class by creating instances/object of the class
'''


