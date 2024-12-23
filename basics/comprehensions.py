#one-line initialization of lists, tuples, etc.

x = [x for x in range(5)]

# [*element to add in the list* *for loop*] that's it.

y = [0 for y in range(5)] #initializes a list of 0s.

z = [z+5 for z in range(5)] #initializes a list of from 5.

#deranged use case:
a = [[0 for a in range(100)] for a in range(5)] #initializes 5 lists of a hundred 0s, in one line.

#another use case:
i = [i for i in range(100) if i%5 == 0] #initializes a list of a values from 1 to 100 if divisible by 5.

#initialize a dictionary, perhaps:
j = {j:0 for j in range(100) if j%5 == 0} #initializes a dictionary of values divisible by 5 and keys of 0.

#initialize a dictionary, perhaps:
k = tuple(k for k in range(100) if k%5 == 0) #initializes a tuple of values divisible by 5.

print(i)