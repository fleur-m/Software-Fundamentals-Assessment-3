# Whitecliffe-Tuple.py

bankAccounts = (("Joe", 33, "234 Great South Rd", "022629107"),
                ("Tama", 6000),
                ("Suzanne", 21025, "45 Green Lane"),
                ("Anihera", -75))
'''
print("The number of bank accounts is ", len(bankAccounts))

# show names and balances
for i in bankAccounts:
    print("The name is ", i[0], "and the balance is $", i[1])

# show names and addresses
for i in bankAccounts:
    if len(i) > 2:
        print("The name is ", i[0], " and the address is ", i[2])


