import numpy as np
import random

grades = np.random.randint(60,101,12).reshape(3,4)



print(grades)

print('All grades',grades.mean())

print('AVG by test:',grades.mean(axis=0))

print('AVG by student:',grades.mean(axis=1))

