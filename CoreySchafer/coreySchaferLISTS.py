# coreySchaferLISTS.py
# Strings practise
# Summer 2022

courses = ['history', 'math', 'physics', 'comp sci']
courses2 = ['art', 'education']
nums = [1, 5, 7, 3]

#courses.insert(0, 'math')
#courses.append(courses2)
#courses.extend(courses2)
#courses.remove('math')
#popped = courses.pop() # will return value that is popped off the end of the list.
#courses.reverse()
#courses.sort() # alphabetical order
#nums.sort(reverse = True)
#sortedCourses = sorted(courses)

#for item in courses:
#    print(item)

courseStr = ' | '.join(courses)
newList = courseStr.split(' | ')

#print(sortedCourses) # sorts list without changing the original list
#print(courses)
print(courseStr)
print(newList)
#print(len(courses))
#print(min(nums)) # plus max and sum
#print(courses.index('comp sci'))
#print('art' in courses)
