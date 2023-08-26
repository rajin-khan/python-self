name = input("What is your name? ")
chars = len(name)

if chars < 3:
    
    print("Name must be at least 3 characters.")
    
elif chars > 50:
    
    print("Name can only be a maximum of 50 characters.")
    
else:
    
    print("Name looks good!")