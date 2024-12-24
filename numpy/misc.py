import numpy as np

#import data from a text file
filedata = np.genfromtxt('assets/data.txt', delimiter=',') #so using this method, we can load data from a text file, and delimiter is the data separator.
print(filedata)

#automatically casts it to floats, but we can cast it all into a diff type, like this:
intfiledata = filedata.astype('int32')
print(intfiledata)