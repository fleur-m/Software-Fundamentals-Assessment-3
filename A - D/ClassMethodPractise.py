#@classmethod
#def fromString(cls, empString):
#   first, last, pay = empString.split('-')
#   return cls(first, last, pay)

#emp1 = Employee()
'''
x = "blue,green,red"

print(x.split(","))

a,b,c = x.split(",")


ticket2001 = "2001, Fleur MacRae, 2983748, fleurm@fof.com, Won't work, " \
             "Closed, Rebooted system"

print(ticket2001.split(","))

number,name,staffID,email,problem,status,response = ticket2001.split(",")
print(staffID[0:3], name[0:4])

newTicket = ticket2001.split(",")
print(newTicket)


ticket2001 = "2001, Fleur MacRae, 2983748, fleurm@fof.com, Won't work, " \
             "Closed, Rebooted system"

print(ticket2001.split(","))

# join
myList = ticket2001.split(",")
# ['2001', ' Fleur MacRae', ' 2983748', ' fleurm@fof.com', " Won't work", ' Closed', ' Rebooted system']

print(",".join(myList))
# 2001---  Fleur MacRae---  2983748---  fleurm@fof.com---  Won't work---  Closed---  Rebooted system
# 2001, Fleur MacRae, 2983748, fleurm@fof.com, Won't work, Closed, Rebooted system
print(",".join(myList[1:3]))

'''
message = "Hello World"
print("Hello World")
print(message)

print(len(message))
print(message[0])
print(message[0:5])

# Hello World
# Hello World
# 11
# H
# Hello

ticket2001 = "2001, Fleur MacRae, 2983748, fleurm@fof.com, Won't work, " \
             "Closed, Rebooted system"

print(ticket2001)

print(len(ticket2001))
print(ticket2001[0])
print(ticket2001[0:5])
print(ticket2001[6:9])