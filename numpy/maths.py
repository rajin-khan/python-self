import numpy as np

a = np.array([1,2,3,4])
print(a)

print(a+2) #adds 2 to each element.
print(a-2) #subtracts 2 from each element.
print(a*2) #multiplies 2 with each element, you get it

b = np.array([1,0,1,0])
print(a+b) #adds all corresponding elements of a and b and prints that.

print(a**2) #prints every element^2

np.sin(a) #take the sin of all the elements of a and store that in an array,
print(np.sin(a))

#read documentation for more