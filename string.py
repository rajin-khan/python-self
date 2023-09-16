course = "Python for \"the\" Beginners"
print(course)
print(course[0]) #in python, strings are indexed with 0 as an array of characters as well, and you could
#technically print "P" with print(course[0])
print(course[-1]) #and you can even access the last character by going to a negative index, with
#print(course[-1]), which will give you "s"
print(course[0:3]) #with this, you can print characters from the 0 to the 2 index sequentially
#but it excludes the character exactl at index 3, meaning it will print "Pyt"
print(course[0:]) #this will print all the characters from the 0 index to the end.
print(course[:5]) #this will print all the characters from the start index to the 4th index
#but it excludes the character exactl at index 5, meaning it will print "Pytho"
print(course[:]) #this would print from the start to the end.

another = course[:] #so you could copy a string like this,
another = course #or like this, doesn't matter

#you can use three single/double quotes to define a string that spans multiple lines.
long_course = '''

Hi Rajin,

How have you been?

Thank you,
The Support Team

'''
print(long_course)

