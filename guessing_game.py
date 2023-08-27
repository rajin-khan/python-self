secret_number = 9
guess_count = 0
guess_limit = 3

while guess_count < guess_limit: 
    
    answer = input("Guess: ")
    
    if answer == str(secret_number):
        
        print("You won!")
        break
    
    elif guess_count == 2 and answer != str(secret_number): #alternatively, while loops can also have an else part (which executes if the while loop completes successfully without a break)
        
        print("Sorry, you failed!")
    
    guess_count += 1
