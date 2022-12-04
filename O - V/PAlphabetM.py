# PFileName.py
# P = Practice
# author: F. MacRae
# date: November 2022

# Program: print alphabet "M".

resultStr = "";
for row in range(0,7):
    for column in range(0,7):
        if(column == 1 or column == 5 or (row == 2 and (column == 2 or column == 4)) or (row == 3 and column == 3)):
            resultStr = resultStr + "*"
        else:
            resultStr = resultStr + " "
    resultStr = resultStr + "\n"
print(resultStr)

# Testing. Assertion 1:
