class Person(object):

    population = 50

    def __init__(self, name, age):
        self.name = name
        self.age = age

    @classmethod # can call on class, don't need an instance
    def getPopulation(cls):
        return cls.population

    @staticmethod # don't need a parameter
    def isAdult(age):
        return age >= 18

    def display(self):
        print(self.name, "is", self.age, 'years old.')

newPerson = Person("Tim", 18)

print(Person.getPopulation())
print(Person.isAdult(21))
