# Dictionary.py
#
# @ author: A. N. Other
# date: September 2016

dictionary1 = {"V344LDA":2000,
               "J245DWE":6350,
               "K265QWS":500}

print("The car with the registration V344LDA is worth $", dictionary1["V344LDA"])

states = {"Oregon":"OR",
          "Florida":"FL",
          "California":"CA",
          "New York":"NY",
          "Michigan":"MI"}

cities = {"CA":"San Francisco",
          "MI":"Detroit",
          "FL":"Jackonsville"}

cities["NY"] = "New York"
cities["OR"] = "Portland"

print("NY State has:", cities["NY"])
print("OR State has:", cities["OR"])

print("Michigan's abbreviation is:", states["Michigan"])
print("Michigan has:", cities[states["Michigan"]])
print("Florida has:", cities[states["Florida"]])

# print every state abbreviation
for state, abbrev in states.items():
    print("{0} is abbreviated {1}".format(state, abbrev))

# print every city in state
for abbrev, city in cities.items():
    print("{0} has the city {1}".format(abbrev, city))

# now both state abbrev and state city
for state, abbrev in states.items():
    print("{0} state is abbreviated {1} and has city {2}".format(state, abbrev, cities[abbrev]))

state = states.get("Texas")
if not state:
    print("Sorry, no Texas")

city = cities.get("TX", "Does not Exist")
print("The city for the state 'TX' is: {0}".format(city))

# preferred approach for putting variables into a string
'''
for state, abbrev in states.items():
    print("{0} is abbreviated {1}".format(state, abbrev))
'''



