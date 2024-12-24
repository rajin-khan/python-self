import numpy as np

#initialize all 0s matrix, pass a shape, which is a tuple: (row, col) into the zeros function.
a = np.zeros((2, 3)) #this initializes a 2 rows, 3 col matrix with 0s. so np.zeros((2, 3, 3)) would create a 2x3x3 matrix with all 0s.
print(a)

#initialize all 1s:
b = np.ones((2, 3, 4)) #3d array of shape: 2 layers, 3 rows, 4 cols.
print(b)

#initialize with datatypes:
c = np.ones((2, 2, 2), dtype='int32')
print(c)

#initialize with any number, pass a shape to the full function, then the number you want to populate it with.
d = np.full((2,2), 99)
print(d)

#initialize with random numbers (decimals):
e = np.random.rand(4, 2, 3) #in this case, no need to pass it as a tuple, just pass the dims.
print(e)

#initialize with random numbers (ints):
f = np.random.randint(7, size = (3,3,3)) #in this case, pass the range (0-7), [or maybe 4, 7 for ints from 4-7] then the dims in the size arg.
print(f)

#you can initialize identity matrices too:
print(np.identity(3))

#problem: 
g = np.ones((5, 5))
h = np.zeros((3, 3))
h[1,1] = 9
g[1:4, 1:4] = h
print(g)