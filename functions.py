def addition(a, b):
    
    result = a + b 
    
    return result   

def subtraction(a, b):
    
    result = a - b
    
    return result

def multiplication(a, b):
    
    result = a * b
    
    return result

def division(a, b):
    
    result = a / b
    
    return result


print("\nThis program will create a simple calculator, using functions.")

while(True):

    print("\nEnter two ingeters, then pick an option.\n")

    first_num = int(input("Enter the first number: "))
    second_num = int(input("Enter the second number: "))

    print("\nWhat would you like to do with these numbers?")

    print("\ni) Add ( + )\nii) Subtract ( - ) \niii) Multiply ( x ) \niv) Divide ( ÷ )")
    choice = input("\nType out your choice: ")

    if choice.lower() == "add":
    
        print(f"\nAnswer: {addition(first_num, second_num)}")
        
    elif choice.lower() == "subtract":
        
        print("\nWhich subtraction would you like to perform?\n")
        print(f"a) {first_num} - {second_num}")
        print(f"b) {second_num} - {first_num}")
        print("c) both.")
        
        sub_choice = input("\nType \"a\", \"b\", or \"c\": ")
        
        if sub_choice.lower() == "a":
            
            print(f"\nAnswer: {subtraction(first_num, second_num)}")
            
        elif sub_choice.lower() == "b":
            
            print(f"\nAnswer: {subtraction(second_num, first_num)}")
            
        elif sub_choice.lower() == "c":
            
            print(f"\nAnswer: {subtraction(first_num, second_num)}")
            print(f"Answer: {subtraction(second_num, first_num)}")
        
        else:
            
            print("\nEnter a valid option!")
            
    elif choice.lower() == "multiply":
        
        print(f"\nAnswer: {multiplication(first_num, second_num)}")
    
    elif choice.lower() == "divide":
        
        print("\nWhich division would you like to perform?\n")
        print(f"a) {first_num} / {second_num}")
        print(f"b) {second_num} / {first_num}")
        print("c) both.")
        
        sub_choice = input("\nType \"a\", \"b\", or \"c\": ")
        
        if sub_choice.lower() == "a":
            
            print(f"\nAnswer: {division(first_num, second_num)}")
            
        elif sub_choice.lower() == "b":
            
            print(f"\nAnswer: {division(second_num, first_num)}")
            
        elif sub_choice.lower() == "c":
            
            print(f"\nAnswer: {division(first_num, second_num)}")
            print(f"Answer: {division(second_num, first_num)}")
        
        else:
            
            print("\nEnter a valid option!")
    
    last_choice = input("\n Would you like to continue? (y/n): ")
    
    if last_choice.lower() == "n":
        
        break
    
    else:
        
        continue