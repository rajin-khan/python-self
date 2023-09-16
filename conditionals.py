is_hot = False
is_cold = False

if is_hot: #format for conditions: you write if, followed be the boolean to be checked and a colon.

    print("It's a hot day.") #if the boolean is true, the lines indented after the if block is executed
    print("Drink plenty of water.")  

elif is_cold: #like else if, you write elif, followed by the boolean variable, and it checks if that's true, then executes the indented line

    print("It's a cold day.")
    print("Wear warm clothes.")    

else: 
    
    print("It's a lovely day") #if none are true, this alternative route is executed, specifically the lines indented after the "else: " part
    
print("Enjoy your day.") #if the indentation is broken, we break out of the conditional statement.