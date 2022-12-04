# EAlphabetL.py
# E = Example
# author: A. N. Other
# date: November 2022

# Program: print alphabet pattern "L".

resultStr = "";
for row in range(0,7):
    for column in range(0,7):
        if(column == 4 or (row == 6 and column != 3 and column < 6)):
            resultStr = resultStr + "*"
        else:
            resultStr = resultStr + " "
    resultStr = resultStr + "\n"
print(resultStr)

# Testing. Assertion 1:
'''
if column = 2
if column = 4
and column < 1
and column != 3
and column != 3 and column < 6
'''