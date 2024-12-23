x = [4, True, 'hi'] #list syntax, elements do not need to be of the same type

length = len(x)
x.append('hehe') #add something to the end of a list
x.extend([4, 5, 6]) #take another list and add its elements to the other list.
x.pop(0) #also takes an index

x[0] = 'hello' #lists are mutable, so we can change the items

print(x[2])
print(x)

y = x #list copied by reference, so y is just a pointer to list x
x[0] = '0 index changed'
print(x, y) #y prints the same list as x, although we just modified x

y = x[:] #we can store a copy of a list instead of pointing to it in this way.