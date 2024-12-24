import numpy as np

list1 = [1, 2, 3]
list2 = [4, 5, 6]

nparr1d = np.array(list1) #1d numpy array created from list
print(nparr1d)

nparr2d = np.array((list1, list2)) #2d numpy array created from two lists, must be passed as a tuple.
print(nparr2d)