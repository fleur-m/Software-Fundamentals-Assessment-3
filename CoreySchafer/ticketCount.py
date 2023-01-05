class ticketCount:
    # this is used to print the number
    # of instances of a class
    counter = 2000

    # constructor of geeks class
    def __init__(self):
        # increment
        ticketCount.counter += 1


# object or instance of geeks class
g1 = ticketCount()
g2 = ticketCount()
g3 = ticketCount()
print(ticketCount.counter)