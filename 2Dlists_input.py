matrix = []

rows = int(input("Enter the rows: "))
columns = int(input("Enter the columns: "))

for i in range(rows):
    
    matrix.append([])
    
    for j in range(columns):
        
        user_in = input(f"Enter item at index[{i}][{j}]: ")
        
        matrix[i].append(user_in)
        
for i in range(rows):
    
    for j in range(columns):
        
        print(matrix[i][j])