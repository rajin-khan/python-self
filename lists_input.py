numbers = []

length = int(input("How many numbers would you like to input? "))

for i in range(length):
    
    input_num = input(f"At number at index {i}: ")
    numbers.append(input_num)
    
    
for i in numbers:
    
    print(i)