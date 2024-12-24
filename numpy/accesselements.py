import numpy as np

a = np.array([[1,2,3,4,5,6,7],[8,9,10,11,12,13,14]])
print(a)

#access specific elements: arrname[row, col]
print(a[1, 5])

#print a specific row, we use the basic slice syntax:
print(a[0, :]) #in the 0 row, get elements from start to end.

#print a specific row, we use the basic slice syntax:
print(a[0, :]) #row 0, get all columns for that row.

#print a specific column
print(a[:, 2]) #get all rows, for column number 2 (the third)

#more slicing
print(a[0, 1:6:2]) #for row 0, get the elements starting from index 1 to 6, step by 2

#modifying elements
a[1, 5] = 20 #that specific number, (13) changes to 20
a[:, 2] = 5 #the entire 3rd column becomes 5
print(a)

#3d example
b = np.array([[[1,2],[3,4]], [[5,6],[7,8]]])
print(b)

#if you wanna get a specific element from a 3d array, work outside in.
print(b[:, 1, :])

#replace in 3d array:
b[:, 1, :] = ([[9, 9], [8, 8]]) #so this is replacing the 2nd row in all the stack layers, with these two layers.
print(b)