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


#in python, functions are treated as objects, which means technically you could return it, or define a function in another function.

def func1(x):
    def func2():
        print(x)
    
    return func2 #notice how we're not calling func2 (using parentheses), we're just passing it because it's an object.

print(func1(3)) #this will print the location of func2 as that is what is getting returned for func1
#however, we can call func1(value)() like this, it gets called as a function, thus we can execute func2.
func1(3)()

#on another note of deranged things you can do in python, you can assign a function like this:
x = func1(3) #this ONLY works as func1 returns a function object, func2.
x() #this calls the func2 object stored in x.

