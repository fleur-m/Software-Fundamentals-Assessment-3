'''
class Person:
# class code containing data and behaviour will come here
age = 10
gender = "male"

Objects:
# create a new object of Person class
harry = Person()
sarrah = Person()

# output: 10
print(harry.age)
print(sarrah.age)
'''
# the built-in function: __init__()
class Person:
    def __init__(self, age, gender):
        self.age = age
        self.gender = gender

    def myIntro(self):
        print("Hello my gender is" +self.gender)
        print("Hello my age is", self.age)
        # comma is used when we need to show int or float values

    harry = Person(36, "male")
    sarrah = Person(34, "female")
    harry.myIntro()
    sarrah.myIntro()



