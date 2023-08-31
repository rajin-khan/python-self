#in pattern printing, you wanted to know how to print multiple asterisks in the same line, with normal loop logic
#python, by default shows other print statement in a loop in separate lines for separate iterations, like this:

for i in range(5):
    
    print("*")
    
#the above code will print 5 asterisks in separate lines.

#however, if you use the end parameter, you can use it like a normal loop the way you do in C and Java.

for i in range(5):
    
    print("* ", end = "") # The 'end' parameter ensures the next print is on the same line (note that continuous asterisks cannot be printed)
    
#this is because zsh causes problems with it and probably views multiple asterisks without spaces as something else, and just doesn't show it.

