print("\nThis game can guess your number.")

number = int(input("\nEnter any number between 1-10: "))

if number > 0 and number <= 10:
    
    print(f"Your number is: {number}")
    
else:
    
    print("\nYou muust enter a number between 1-10 for this game to guess it!")