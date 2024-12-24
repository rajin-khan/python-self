import numpy as np

#prepping for matrix multiplication
a = np.ones((2, 3))
print(a)

b = np.full((3, 2), 2)
print(b)
#a*b won't work as it would normally compute single element multiplications, if the dims matched.

#to perform actual matrix multiplication, we do:
print(np.matmul(a, b))

#process of finding the determinant of a matrix: linalg.det, to prove this, as we know the det of an identity matrix is 1:
c = np.identity(3)
print(np.linalg.det(c)) #this will print 1.

#we can even find inverses and eigenvalues and eigenvectors this way.
#refer to documentation