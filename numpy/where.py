#np.where() can check whether elements meet a condition and then pull one element if the condition is met and another if not.
#syntax:
# np.where(condition, replacement_if_true, replacement_if_false)

import numpy as np

arr = np.array([[1, 2, 3], [4, 5, 6]])

#replacing all the even numbers in array with 0s.
upd_array = np.where(arr%2==0, 0, arr) #inside the parentheses, the 'arr' (name of the array) represents an individual element in the array
print(upd_array)