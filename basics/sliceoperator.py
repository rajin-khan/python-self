x = [0, 1, 2, 3, 4, 5, 6, 7, 8]
y = ['hi', 'hello', 'goodbye', 'cya', 'sure']
s = 'hello'

sliced = x[0:4:2] #stores [0, 2] 

#the syntax is just square brackets, with colons in the middle, like this: [ start : stop : step ]
#so it basically starts at the 0 index, stops at index 4, and increments the index by 2
#then, it stores that in the list we're calling sliced.

#this is useful in this way:
reverselist = x[::-1]
#so it's starting at index 0, stopping at at the end, but incrementing by -1. so it's going in reverse and storing the elements like that.

#since a string is just a character array, it works on it as well.

reverseString = s[::-1]

print(sliced)
print(reverselist)
print(reverseString)

#the slice operator works on tuples too.