# make a menu

# function job is to print this information:
def menu():
    print("\nIT5016 Help Desk Ticket System:\n"
          "_______________________________________\n\n"
          "Select from the following choices:\n"
          "0: Exit\n"
          "1: Submit helpdesk ticket\n"
          "2: Show all tickets\n"
          "3: Respond to ticket number\n"
          "4: Re-open resolved ticket\n"
          "5: Display ticket stats\n"
          "_______________________________________\n")

menu()
menuSelection = int(input("Enter menu selection 0 - 5:"))

while menuSelection <= 6:
    if menuSelection == 0:
        # do option 0 stuff
        print("Selected option 0")
    elif menuSelection == 1:
        # do option 1 stuff
        print("Selected option 1")
    elif menuSelection == 2:
        # do option 2 stuff
        print("Selected option 2")
    elif menuSelection == 3:
        # do option 3 stuff
        print("Selected option 3")
    elif menuSelection == 4:
        # do option 4 stuff
        print("Selected option 4")
    elif menuSelection == 5:
        # do option 5 stuff
        print("Selected option 5")
    else:
        print("Invalid option")

    print()
    menu()
    menuSelection = int(input("Enter menu selection 0 - 5:"))

print("End of while loop")

# Dolinski, A. (2020, May 11). Making a Menu in Python. www.youtube.com. https://www.youtube.com/watch?v=63nw00JqHo0