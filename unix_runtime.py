inventory = []

def additem():
    
    itemcount = int(input("\nHow many items would you like to add? "))
    
    for i in range(itemcount):
        
        user_input = input("\nEnter the name of the item: ")
        inventory.append(user_input)
        
        print("Item added!")
        
def deleteitem():
    
    print("\nCurrent inventory: ")
     
    viewinventory()
    
    itemcount = int(input("\nHow many items would you like to delete? "))
    
    counter = 0
    
    while counter < itemcount:
        
        delete_index = 0
        
        user_input = int(input("\nEnter the item number you would like to delete: "))
        
        if user_input - 1 >= 0 and user_input - 1 <= len(inventory) - 1:
            
            inventory.pop(user_input-1)
            print("Item deleted!")
            
        else:
                
            print("Enter a valid item number.")
            counter -= 1
                
        counter += 1
 
def updateitem():
    
    print("\nCurrent inventory: ")
     
    viewinventory()
    
    itemcount = int(input("\nHow many items would you like to update? "))
    
    counter = 0
    
    while counter < itemcount:
    
        update_input = int(input("\nEnter the item number you would like to update: "))
        
        if update_input - 1 >= 0 and update_input - 1 <= len(inventory) - 1:
            
            inventory[update_input-1] = input("\nEnter the name of the new item: ")
            print("Item updated!")
        
        else:
            
            print("Enter a valid item number.")
            counter -= 1
        
        counter += 1
    
def viewinventory():
    
    view_index = 0
    
    print("")
    
    while view_index < len(inventory):
        
        print(f"Item {view_index+1}: {inventory[view_index]}")
        
        view_index += 1
        
def searchitem():
    
    search_input = input("\nEnter the name of the item you would like to search for: ")
    
    search_index = 0
    
    while search_index < len(inventory):
        
        if inventory[search_index] == search_input.lower():
            
            print(f"{search_input} found at Serial: {search_index+1}!")
            
            break
        
        search_index += 1
        
        if search_index == len(inventory):
            
            print("Item not found, please try again!")
    
print("\nWelcome to the runtime version of UNIX! To get started, add some items to the inventory.")

additem()

while True:
    
    print("\nWhat would you like to do?")
    
    print("1: Add more items")
    print("2: Delete items")
    print("3: Update items")
    print("4: View inventory")
    print("5: Search for an item")
    print("0: Quit")
    
    main_choice = int(input("\nEnter a number to pick an option: "))
    
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
        
    

