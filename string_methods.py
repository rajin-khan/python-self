course = "Python for Beginners"
length = len(course) #general purpose function built into python
uppercase = course.upper() #way more string methods available, just do the strngvariablename and then the dot operator
#for example, we did course.*name of method*()
#the string methods pop up automatically and you can select them from the string class's methods
index_of_p = course.find("P")
index_of_beginners = course.find("Beginners") #this will return the index of the starting letter of the word
replaced_string = course.replace("Beginners", "Absolute Beginners") #this will replace the string in the first argument with the one in the second

#for checking the existence of a character or a sequence of characters or a word in a string, we use the "in" operator.
#for example:
is_present = "Python" in course #produces a boolean value, whereas the find method produces an index only

print (is_present)
#all string methods are case sensitive
