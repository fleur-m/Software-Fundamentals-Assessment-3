class Person:
  def __init__(self, age, gender, address, height):
    self.age = age
    self.gender = gender
    self.address = address
    self.height = height

herry = Person(36,"male", "25 Alex St", "5 ft 3 inches")

sarrah = Person(34, "female", "5 Aldridge St", "6 ft")

print(herry.age, herry.gender, herry.address, herry.height)

print(sarrah.height)
