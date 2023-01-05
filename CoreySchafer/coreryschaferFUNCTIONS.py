def ticketInfo(*args, **kwargs):
    print(args)
    print(kwargs)

test = True
while test == True:
    data = ticketInfo(input('1:'), input('2:'), input('3:'), input('4:'))


