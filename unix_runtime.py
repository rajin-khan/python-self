inventory = []

def additem():
    
    itemcount = int(input("How many items would you like to add? "))
    
    for i in range(itemcount):
        
        user_input = input("Enter the name of the item: ")
        inventory.append(user_input)
        
        print("Item added!")
        
def deleteitem():
    
    itemcount = int(input("How many items would you like to delete? "))
    
    counter = 0
    
    while counter < itemcount:
        
        delete_index = 0
        
        user_input = input("Enter the name of the item you would like to delete: ")
        
        while delete_index < len(inventory):
            
            if inventory[delete_index] == user_input:
                
                inventory.remove(user_input)
                print("Item deleted!")
                
                break
            
            else:
                
                delete_index += 1
                
        counter += 1
            
        if delete_index == len(inventory):
            
            print("Item not found in inventory.")
            
            counter -= 1
    
def viewinventory():
    
    view_index = 0
    
    while view_index < len(inventory):
        
        print(f"Item {view_index+1}: {inventory[view_index]}")
        
        view_index += 1
    

print("\nWelcome to the runtime version of UNIX! To get started, add some items to the inventory.")

additem()

while True:
    
    print("What would you like to do?")
    
    print("1: Add more items")
    print("2: Delete items")
    print("3: Update items")
    print("4: View inventory")
    print("5: Search for an item")
    print("0: Quit")
    
    main_choice = int(input("Enter a number to pick an option: "))
    
    if main_choice == 1:
        
        additem()
    
    elif main_choice == 2:
        
        deleteitem()
        
    elif main_choice == 3:
        
        updateitem()
        
    elif main_choice == 4:
        
        viewinventory()
        
    elif main_choice == 5:
        
        searchitem()
        
    elif main_choice == 0:
        
        break
        
    else:
        
        print("Please enter a valid option")
        
    

