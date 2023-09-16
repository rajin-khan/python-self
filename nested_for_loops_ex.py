numbers = [5, 2, 5, 2, 2]

for i in numbers: #here, for each iteration, i is taking the value from the list
    
    output = "" #initially, an output string is set as blank
    
    for y in range(i): #so each time, this inner loop iterates up to the number in the list
        
        output += "x" #and that many x-s are appended to the string, so in the first case, 5, second one, 2, and so on
    
    print(output) #then that string is printed, it automatically moves to the next line, and the output string is set to blank again
    
print("\n")
    
#alternatively, you could do it like this:
for i in numbers:
    
    print("x" * i)
    
#but that is too easy and does not require the use of an inner loop, so it's nice to know both