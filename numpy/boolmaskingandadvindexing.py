import numpy as np

filedata = np.genfromtxt('assets/data.txt', delimiter=',')

print(filedata > 25)
#checks for every single element if it's > 50, and then creates an array of booleans based on it.

filedata > 25 #this by itself returns an index, where each of the values that are true/match are stored. so if we:
print(filedata[filedata > 25])
#this will print all the elements in the array that are > 25.

print(np.any(filedata > 20, axis = 0)) #checks if any of the values (in each col, not row) is > 20.

print(np.all(filedata > 20, axis = 0)) #checks if all of the values combined (in each col, not row) is > 20.

print((filedata > 25) & (filedata < 100)) #in numpy, ig, logical AND is &, NOT is ~,

#refer to documentation for more.