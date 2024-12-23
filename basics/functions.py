def func():
    print('run')

def add(x, y):
    print(x + y)  
      
def sub(x, y):
    return x - y     

func()
add(1, 2)
print(sub(3, 4))

#you get everything so far.
#in python, you can return multiple values. but it gets returned in a tuple.

def possibleSubs(x, y):
    return x-y, y-x

print(possibleSubs(5, 9)) 

#we could access the returned tuple elements individually like possibleSubs(5, 9)[0], or possibleSubs(5, 9)[1], but a cleaner way to do that might be:
a, b = possibleSubs(1, 3) #this automatically stores the returned values separately in diff variables.
print(a, b)

#functions can also take optional parameters, like this:

def printGiven(x, y, z=None):
    print(x, y, z)
    
printGiven(1, 2) #returns none in third place if no third digit passed in this case.