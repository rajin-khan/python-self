#so basically, item is a variable, that holds a character from the string after "in", being "Python".
#each iteration, it hold a character, and the loop ends when the strong is done.
for item in "Python":
    
    print(item)
    
#alternatively, you could create a list of items for the item variable to iterate through, like this:
for item in ["Rajin", "Hasnaine", "Khan"]: #the square brackets indicate a list
    
    print(item)
    
#if you don't wanna explicitly type out a long list, you can use the "range" function.
for item in range(10): #so this prints from 0 to 10, minus 10 itself. meaning item is assigned values from 0-9. so the iteration happens 10 times.
    
    print(item)

#you could also define the range like this:
for item in range(5, 10):
    
    print(item) #which iterates 5 times, item being 5-9.

#you can even define the number of steps per iteration, similar to how you would set iteration values in other for loops:
for item in range(5, 10, 2): #here, 5-10 is where it iterates, and 2 means it increments by 2 steps each time.
    
    print(item) #so this was supposed to print 5 items from 5-9, but it prints 5, 7 (which is +2), and then 9 itself (+2 increment)