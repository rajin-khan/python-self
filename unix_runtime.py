store_inventory = []

def add(inventory, size):
    
    space = size
    
    input_size = int(input("How many items would you like to enter?: "))

    for i in range(input_size):
        
        print(f"\nSpace left in inventory: {space}\n")
    
        user_input = int(input(f"Enter the item at index {i}: "))
    
        inventory.append(user_input)
        
        space -= 1
        
    return space

def delete(inventory, size):
    
    space = size
    
    deletion_size = int(input("How many items would you like to delete?: "))

    for i in range(deletion_size):
        
        print(f"\nSpace left in inventory: {space}\n")
        
        user_input = int(input(f"Enter the name of the item to be deleted: "))
            
            
        
        space += 1
        
    return space

        
print("\nWelcome to the runtime version of UNIX!")
        
inventory_size = int(input("\nTo get started, declare the size of your inventory: "))

space = inventory_size

space = add(store_inventory, space)

while True:
    
    print("What would you like to do now?")
    
    print("\n1. Add more items")
    print("\n1. Delete items")
    print("\n1. Search the inventory")
    print("\n1. View the inventory\n")
    
    menu_option = int(input("Enter a number to choose: "))
    
    if menu_option == 1:
        
        space = add(store_inventory, space)
        
    elif menu_option == 2:
        
        space = delete(store_inventory, inventory_size)