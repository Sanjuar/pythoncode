while True:
    try:
        num = int(input("Enter the number of rows: "))
        if num > 0:
            break
    except:
        continue

for i in range(1, num + 1):
    print(" " * (num - i) + "*" * i)
            
        
    
        
            
