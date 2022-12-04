# EDivisibleBy7.py
# E = Example
# author: W3 Resource
# date: August 2022

# Program: find numbers divisible by 7 and multiple of 5, between 1500 and 2700 (inclusive).
nl = []
for index in range(1500,2701):
    if (index % 7 == 0) and (index % 5 == 0):
        nl.append(str(index))
print(",".join(nl))



