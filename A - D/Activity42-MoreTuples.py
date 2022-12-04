# Activity42-MoreTuples.py

bankAccounts = (("Joe", 33, "234 Great South Rd", "022629107"),
                ("Tama", 6000),
                ("Suzanne", 21025, "45 Green Lane"),
                ("Anihera", -75))

print("The number of bank accounts is ", len(bankAccounts))

# show names of all customers with less than 100
lowBalance = 100
for i in bankAccounts:
    if i[1] < lowBalance:
        print(i[0], "has less than $100.")

# names of customers with no address and no phone number
for i in bankAccounts:
    if len(i) < 3:
        print(i[0], "has no address or phone number.")
        # Tama has no address or phone number.
        # Anihera has no address or phone number.

######################
bankAccounts = (("Joe", 33, "234 Great South Rd", "022629107"),
                ("Tama", 6000),
                ("Suzanne", 21025, "45 Green Lane"),
                ("Anihera", -75))

# highest and lowest balances
