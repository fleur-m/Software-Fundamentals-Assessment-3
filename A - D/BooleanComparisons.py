# BooleanComparisons.py
#
# @ author: A. N. Other
# date: September 2016

distanceFromSchool = 3
ageInYears = 14
hasResidency = True
payFees = False
print("This program works out eligibility for enrolment....\n")

distanceFromSchool = int(input("How many Kms away from the school do you live? \n"))

if distanceFromSchool > 4:
      print("You live outside the enrolment zone. Please see administration office")
else:
      ageInYears = int(input("What age are you? \n"))


# Test case assertion 1: result should be True

print("The student's eligibility to enrol is ",
      distanceFromSchool < 4
      and ageInYears < 18
      and ageInYears > 10
      and hasResidency
      or ageInYears < 18
      and payFees, "\n")

#print("The student waited for too long...\n")
#ageInYears = 18


# Test case assertion 2: result should be False
'''
print("The student's eligibility to enrol now is ",
      distanceFromSchool < 4
      and ageInYears < 18
      and hasResidency
      or ageInYears < 18
      and payFees, "\n")
'''
'''
# Test case assertion 3: result should be False
print("The student's eligibility to enrol now is ",
      distanceFromSchool < 4
      and ageInYears < 18
      and ageInYears > 10
      and hasResidency
      or ageInYears < 18
      and ageInYears > 10
      and payFees, "\n")
'''











