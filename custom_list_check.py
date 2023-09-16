print("This program will take a custom list and then check if the items are present.")

length = int(input("\nEnter the length of the list: "))

items = []

for i in range(length):
    
    user_item = input(f"\nEnter the item at index[{i}]: ").lower()
    
    items.insert(i, user_item)
    print("Entered!")
    
user_check = input("\nEnter the item to be checked: ")

if user_check.lower() in items:
    
    print(f"Yes, {user_check} is present!")

else:
    
    print("Item is not present!")