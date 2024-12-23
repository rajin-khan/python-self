#the unpack operator, *, separates items in a list and prints/returns them individually. (NOT A POINTER OPERATOR)
x = [1, 23, 456, 78910]
print(*x)

def func(x, y):
    print(x, y)
    
pairs = [(1, 2), (3, 4)]

#we could print the pairs like this:
for i in pairs:
    func(i[0], i[1])
    
#but a better way to do it would be the unpack operator, like this:
for i in pairs:
    func(*i) #this separates the pair values, and passes them spaced out, one by one.
    
#we could do this for dictionaries too, but the syntax is a little diff:
func(**{'x': 2, 'y': 5}) #this separates the key-value pairs, and then passes them spaced out, as key, and then value.

#now, *args unpacks and takes any number of values passed as positional arguments and stores them in a tuple.
#useful for when you don't know how many positional arguments you have to accept.

# **kwargs (keyword arguments) takes any number of key-value arguments passed stores them in a dictionary.

def func(*args, **kwargs):
    print(args, kwargs)
    print(*args) #unpacking and printing args
    
func(1, 2, 3, 4, 5, one=0, two=1)

