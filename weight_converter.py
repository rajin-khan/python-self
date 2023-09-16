weight = input("Weight: ")
l_or_k = input("(L)bs or (K)g: ")
final_weight = 0

if l_or_k.upper() == "K":
    
    final_weight = float(weight) / 0.45
    print(f"You are {final_weight} pounds.")
    
elif l_or_k.upper() == "L":
    
    final_weight = float(weight) * 0.45
    print(f"You are {final_weight} kilos.")