#sets have no order, but they're pretty fast as we only have to check whether something exists, or not.

x = set()
s = {4, 32, 2, 2} # we can't declare a set without the elements, if we do s = {}, it becomes a dictionary. the previous line is a better way to initialize.
#but s is still a set as we have elements in it.

print(s) #prints in random order, removes duplicates.

s.add(5)

s.add(6)
s.remove(6)

print(4 in s) #this will check if the element 4 is in the set s, and return a boolean.

#the main advantage of sets are that they are EXTREMELY fast, and used when looking up values.

s2 = {71, 39, 24, 56}

print(s.union(s2))
print(s.intersection(s2))
print(s.difference(s2))