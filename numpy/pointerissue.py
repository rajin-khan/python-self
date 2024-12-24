import numpy as np

a = np.array([1, 2, 3])
b = a #this copies the pointer to the array, not the array's copy itself
b[0] = 100
print(b)
print(a)

#thus, to solve this issue, and to actually create a copy, we do:
c = np.array([1, 2, 3])
d = c.copy() #use the copy function
d[0] = 101
print(c)
print(d)