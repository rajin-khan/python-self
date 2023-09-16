numbers = [1, 2, 3, 4, 99, 6, 7, 8, 9, 0]

highest = numbers[0]

for i in numbers:
    
    if i >= highest:
        
        highest = i

print(f"The highest number is: {highest}")