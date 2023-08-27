command = ""
has_started = False
has_stopped = False

while True:
    
    command = input(">").lower() #since input returns a string, we can use a dot operator on it and make it lowercase right from the input.
    
    if command == "help":
        
        print("start - to start the car\nstop = to stop the car\nquit - to exit")
    
    elif command == "start" and has_started == False:
        
        has_started = True
        has_stopped = False
        print("Car started...Ready to go!")
    
    elif command == "start" and has_started == True:
        
        print("Car has already started!")
    
    elif command == "stop" and has_stopped == False:
        
        has_stopped = True
        has_started = False
        print("Car stopped.")
        
    elif command == "stop" and has_stopped == True:
        
        print("Car has already stopped!")
        
    elif command == "quit":
        
        break
    
    else:
        
        print("Sorry, I don't understand that!")
    