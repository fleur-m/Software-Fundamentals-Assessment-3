class Employee: # blueprint for creating instances

    def __init__(self, first, last, pay): # method to set-up data attributes automatically for each instance.
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'
# note: when we create methods within a class they recieve the instance as the first argument automatically (self).
    def fullname(self):
        return '{} {}'.format(self.first, self.last) # see manual version outside of class too


###########################

# creates each employee as an instance of this class
emp1 = Employee('Corey', 'Schafer', 50000)
emp2 = Employee('Test', 'User', 60000)

print(emp1.fullname())
print(Employee.fullname(emp1))

#print(emp1)
#print(emp2)

# can delete these manual assignment of data now
'''
emp1.first = 'Corey'
emp1.last = 'Schafer'
emp1.email = 'Corey.Schafer@company.com'
emp1.pay = 50000

emp2.first = 'Test'
emp2.last = 'User'
emp2.email = 'Test.User@company.com'
emp2.pay = 60000
'''

#print(emp1.email)
#print(emp2.email)
#print(emp1.fullname()) # emp1 instance/fullname method

#print('{} {}'.format(emp1.first, emp1.last)) # manual. outside of class