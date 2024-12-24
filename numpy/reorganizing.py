import numpy as np

before = np.array([[1,2,3,4],[5,6,7,8]])
print(before)

#we can change the shape of the (2, 4) array into an (4, 2) shape, or any shape:
after = before.reshape((2, 2, 2))
print(after)

#vertically stacking arrays (ig making 3d arrays out of two or more 2d arrays)
v1 = np.array([1,2,3,4])
v2 = np.array([5,6,7,8])

print(np.vstack([v1, v2])) #stacks v1 array on top of v2 array

print(np.vstack([v1, v2, v2, v2])) #we can even stack the same array back to back as copies.

#horizontally stacking arrays are very similar. you just stack another array to the left of another.
h1 = np.ones((2, 4))
h2 = np.zeros((2, 2))

print(np.hstack((h1, h2)))