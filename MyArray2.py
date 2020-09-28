import numpy as np

grades = np.array([[87,96,70],[100,87,90],[94,77,90],[100,81,82]])


#print(grades.min())

#print(grades.max())

#print(grades.std()) #standered deviation
'''
print(grades.var())

print(grades.mean(axis=0)) #the mean of the columbs 

print(grades.mean(axis=1)) #average of the students
'''
numbers = np.array([1,4,9,16,25,26])

print(np.sqrt(numbers))


grades = np.array([[87,96,70],[100,87,90],[94,77,90],[100,81,82]])
'''
print(grades[0,1])

print()

print(grades[1])

print()

print(grades[0:2])

print()

print(grades[[1,3]])

print()

print(grades[:,0])
'''


numbers = np.arange(1,6)
numbers2 = numbers.view()

