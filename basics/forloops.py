for i in range(10):
    print(i)
    
#range can take 3 numbers at max, namely range(start, stop, step). by default, start = 0, stop = 10, step = 1 (increment).
#so, putting just 10 means that. we can also do range(1, 10), which means we start at 1, stop at 10, so it runs 9 times.

for i in [3, 4, 2, 3, 5, 7]:
    print(i)
    
#i just goes through the list and takes its values one by one.

x = [1, 2, 4, 5, 7]
for i in range(len(x)):
    print(x[i])

#this makes i iterate through and take the value of each index of x, as len returns 5, so it starts at 0 and ends at 4.

y = [9, 8, 7, 5]
for i, element in enumerate(y):
    print(i, element)

#this prints the index, with the values beside it.