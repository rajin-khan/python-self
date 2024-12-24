import numpy as np

stats = np.array([[1, 2, 3], [4, 5, 6]])

#get the minimum from the array
print(np.min(stats))

#get the maximum from the array
print(np.max(stats))

#get the min from the rows
print(np.min(stats, axis = 0))

#get the min from the cols
print(np.min(stats, axis = 1))

#get the sum of all elements in a matrix:
print(np.sum(stats))

#get the sum of all rows in a matrix:
print(np.sum(stats, axis = 0)) #here, instead of getting the sum of rows, this adds elements downwards, so you get the sum of cols.