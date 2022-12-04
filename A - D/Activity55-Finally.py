# Activity55-Finally.py

# ExceptionExample3
entryIsValid = False
numberOfGoes = 0
while not entryIsValid:
    try:
        numberEntered = int(input("Enter a valid positive integer\n"))
        if numberEntered <= 0:
            raise ValueError("Entered value is not a positive integer.")
    except ValueError as e:
        print("The entry is not valid:\n{0}\n"
              "Please try again..."
              .format(e))
    else:
        entryIsValid = True
        print("Thankyou. The acceptable number entered "
              "was {0}.".format(numberEntered))
    finally:
        numberOfGoes += 1
        print("The number of goes used is...{0}"
              .format(numberOfGoes))

