import numpy as np

a = np.array([1, 2, 3]) #1d array
print(a)

b = np.array([[4.5, 6.5, 7.0],[3.0, 4.5, 5.5]]) #2d array
print(b)

#get dimensions of an array
dimensions = b.ndim
print(dimensions)

#get shape (prints num of rows, then cols)
shape = b.shape
print(shape)

#get data type
datatype = a.dtype
print(datatype)

#we can store specific data types, like this:
c = np.array([1, 2, 3], dtype='int16')
print(c, c.dtype)

#get size
print(a.itemsize) #returns bytes

#get total size
print(b.size) #returns num of items in the array.

#so total storage size: 
print(a.size*a.itemsize) #byte value for total size
#same as:
print(a.nbytes)

