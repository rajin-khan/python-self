# key-value pair.

x = {'key1' : 4}

print(x['key1'])

#add to the dictionary like this:
x['key2'] = 5

# two keys don't need to be of the same data type.
x[2] = 3

# the data types of the values dont have to be the same either.

x['array'] = [1, 6, 2]

print(x)

#also VERY fast.

print('key1' in x) #returns boolean for if the key exists in the dictionary.

print(x.values()) #prints all the values
print(x.keys())

#typically, for the values and keys returned separately, it's a different data type, so better to typecast to a list, like this:
print(list(x.keys()))

del x['key1'] #deletes the key-value pair.

#looping in dictionaries:

for key, value in x.items(): #use the items method if you wanna print both keys and values.
    print(key, value)
    
#it could also be done like this:

for key in x:
    print(key, x[key])