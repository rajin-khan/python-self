#Type coercion can occur if we try to make an array out of a Python list with several data types,
#since NumPy will change the data so that it is all of one type.

import numpy as np

arr = np.array([[1, 2, 3], [4, 5, True]])
print(arr) #true gets changed to 1.

arr2 = np.array([[1, 2, 3], [4, 5, "Hello world!"]])
print(arr2) #numpy changes everything to string.