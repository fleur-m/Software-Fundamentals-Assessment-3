'''
message = "Meet me tonight."
print(message)

message3 = "I'm looking for someone to share an adventure."
# or 'I\'m looking for someone...

movieQuote = """One of my favorite lines from The Godfather is:
"I'm going to make him an offer he can't refuse."
Do you know who said this?"""


# search a string

string1 = "Whanau!"

print("The third letter is {0}\n".format(string1[2]))
print("The length of the string is {0}".format(len(string1)))

# count, find and index functions
# count:
string1 = "here is a translation: Haere mai ki konei, means come here!"

print("The number of times that k appears is {0}\n"
      .format(string1.count("k")))

# find and index:
koneiEndIndex = string1.find("konei") + len("konei")
print("The end index position of konei is {0}\n"
      .format(koneiEndIndex))

# find:
herePosition = string1.find("here", koneiEndIndex, len(string1))
print("Looking for the string1 here, anytime after konei...\n\n"
      "The string1 here appears at the index position..{0}"
      .format(herePosition))

# to find all instances of words that start with Ka - the calling code must loop.
string1 = "Ka mate kaainga tahi ka ora kaainga rua."
print("Does this string start with Ka?...{0}\n".format(string1.startswith("Ka")))

print("Does this string start with Tr?...{0}\n".format(string1.startswith("Tr")))

print("Does this string end with rua?....{0}\n".format(string1.endswith("rua.")))

# editing strings
string1 = "Hello World"

# replace part of a string
print("Replacing part of a string...\n{0}"
      .format(string1.replace("Hello", "Goodbye")),
      "\n")

# change upper and lower case strings
string1 = "hElLo wOrlD"
print("Make a string upper case...\n{0}"
      .format(string1.upper()),
      "\n")

# and lower case
print("Make a string lower case...\n{0}"
      .format(string1.lower()),
      "\n")

# make a title case
print("Make a string a title case...\n{0}"
      .format(string1.title()),
      "\n")

# make a capitalized string
print("Make a string capitalized...\n{0}"
      .format(string1.capitalize()),
      "\n")

# make a string swap case - from hElLo wOrlD to HeLlO WoRLd
print("Making a string swap case...\n{0}"
      .format(string1.swapcase()),
      "\n")

# reverse and insert(.join()) characters to a string
print("Reversing and inserting characters to a string...\n{0}"
      .format("*".join(reversed(string1))),
      "\n")
# D*l*r*O*w* *o*L*l*E*h

# remove content from string: lstrip() and rstrip()
string1 = "Hello World"

# strip newline characters from the end
print(string1.strip("d"))
# Hello Worl

string1 = "Hello World "

# adding to string
print("***", string1, "***\n")
# using strip()
print(string1.strip()) # didn't work?
# using lstrip()
print(string1.lstrip()) # didn't work?

# concatenation
'''
string1 = "Hello World"

# H:e:l:l:o: :W:o:r:l:d
print("Using join method to add : between every character...\n{0}"
      .format(":".join(string1)),
      "\n")

# add whitespace - H e l l o   W o r l d
print("Add whitespace:{0}"
      .format(" ".join(string1)),
      "\n")

# replace part of a string - Hello World becomes, Goodbye World
string1 = "Hello World"
print(string1.replace("Hello", "Goodbye"))

# upper case string - HELLO WORLD
print(string1.upper())

# title case - Hello World
print(string1.title())

# Capitalized - Hello world
print(string1.capitalize())

# swap case - hELLO wORLD
print(string1.swapcase())

# length of string - 11 characters
stringLength = len(string1)

# reverse with slicing:
# create a slice - ('dlroW olleH', '*')
slicedString = (string1[stringLength::-1], "*")
print(slicedString)

print(string1[stringLength::-1]) # dlroW olleH
# print(string1[stringLength::-3]) = dooe
# print(string1[stringLength::-2]) = drWolH














