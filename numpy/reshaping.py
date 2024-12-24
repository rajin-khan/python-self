import numpy as np

arr = np.arange(10, 26)

'''
Once we have data stored in an array, NumPy provides huge flexibility manipulating it. 
One example is reshaping using the .reshape() method. 
Reshape an array by passing a tuple of the desired dimension lengths to .reshape(). 

We'd reshape to a two-dimensional array like so:
array.reshape((num_rows, num_columns)) values passed as a tuple
'''

newarr = arr.reshape((8, 2))
print(newarr)

#you could also reshape the existing array into a 3d array, like this:
#array.reshape((number_of_2d_arrays, num_rows, num_columns)) bc 3d arrays are just 2d arrays stacked on top of each other.
newarr3d = arr.reshape((4, 2, 2)) #so 4 2d arrays, each of 2 cols and 2 rows.
print(newarr3d)