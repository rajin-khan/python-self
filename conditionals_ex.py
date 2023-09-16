price = 1000000
good_credit = True

if good_credit:
    
    down_payment = 0.1 * price
    
else:
    
    down_payment = 0.2 * price
    
print("The down payment is: $" + str(down_payment))
#or we could've used a formatted string, like:
#print(f"The down payment is: $ {down_payment}")