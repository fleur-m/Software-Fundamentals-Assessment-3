'''
def helloFunction(greeting, name = 'You'):
    return '{}, {}'.format(greeting, name)

print(helloFunction('Hi', name = 'Corey'))

def studentInfo(*args, **kwargs):
    print(args)
    print(kwargs)

courses = ['Math', 'Art']
info = {'name': 'John', 'age': 22}

studentInfo(*courses, **info)
'''

monthDays = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30 , 31, 30 , 31]

def isLeap(year):
    '''returns true for leap year and false for non-leap year'''
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

def daysInMonth(year, month):
    '''return number of days in that month in that year'''
    if not 1 <= month <= 12:
        return 'Invalid Month'

    if month == 2 and isLeap(year):
        return 29

    return monthDays[month]

print(isLeap(2020))
print(daysInMonth(2017, 2))










