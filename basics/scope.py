x = 'rajin'

def func(name):
    x = name #this x is local

print(x)
func('changed')
print(x)

y = 'raj'

def func(name):
    global y #this fixed the issue, but try not to use this, there are very rare case you might need it. it's bad practice.
    y = name

print(y)
func('changed')
print(y)