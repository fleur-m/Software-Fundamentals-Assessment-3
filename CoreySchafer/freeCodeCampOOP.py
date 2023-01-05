class Item:
    # class attribute
    #payRate = 0.8 # the pay rate after 20% discount
    all = []
    # instance attributes
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

        # actions to execute
        Item.all.append(self)

    #def calculateTotalPrice(self):
    #    return self.price * self.quantity

    #def applyDiscount(self):
    #    self.price = self.price * self.payRate

# create instances/objects of this class
itemOne = Item('phone', 100, 1)
itemTwo = Item('laptop', 1000, 3)
itemThree = Item('cable', 10, 5)
itemFour = Item('mouse', 50, 5)
itemFive = Item('keyboard', 75, 5)

print(Item.all)






