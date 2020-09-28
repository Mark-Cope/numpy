import numpy as np

integers = np.array([1,2,3])

#print(integers)

#print(type(integers))


integers = np.array([[1,2,3],[4,5,6]])
'''
print(integers.dtype)

print(integers.ndim) #how many sets there are

print(integers.shape)   #number of demensions

print(integers.size)   #size of the elements, how many there are

print(integers.itemsize)  #amount of space it takes up in memory

for row in integers:
    print(row)
    print()

    for col in row:
        print(col, end=" ")  #the end command keeps it all on the same line
    print()

for i in integers.flat:
    print(i, end= " ")

print()
print()
print()


print(np.zeros(5)) #creat an array of five zeros

print(np.ones(5))
print()
print()
print()

array1 = np.ones((2,4), dtype= int)
print(array1)
print()


array2 = np.full ((3,5),13) #creates an array of 3 rows and 5 columbs of the number 13

print(array2)

print()



print(np.arange(5))

print()

print(np.arange(5,10))

print()

print(np.arange(10,1,-2))

print()

print(np.linspace(0.0,1.0, num=5))

print()

array1 = np.arange(1,21) #creates 20 intergers starting form 1 and going to 20

print(array1)

print()
print()

array2 = array1.reshape(4,5) #this reshapes the array above
print(array2)

print()
print()

array3= np.arange(1,100001).reshape(4,25000)

print(array3)

print()
print()


array4= np.arange(1,100001).reshape(100,1000)

print(array4)

print()
print()
print()

'''
numbers= np.arange(1,6)
'''
print(numbers * 2) #multiplies everything in the array times 2

print(numbers) #still unaffected
'''
numbers+= 10
'''
print(numbers) #this changes the array
'''
numbers= np.arange(1,6)
'''
print(numbers* 2)

print(numbers)
'''
numbers *= 2
'''
print(numbers)

print(numbers >= 13)

print()
print()
print()

'''
numbers2= np.arange(5,10)
'''
print(numbers2 > numbers)

print(numbers)
print(numbers2)

print(numbers == numbers2)
'''
#numbers.copy()#deep copy


grades = np.array([[87,96,70], [100,87,90]])

print(grades.reshape(1,6))

print(grades)

flattened= grades.flatten() #makes it into one row

print(flattened)
print(grades)


grades2= grades.T

print(grades2)

h_grades= np.hstack(grades) #adds horizonlte

v_grades= np.vstack(grades) #adds verticle


