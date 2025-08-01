while True:
    try:
        num = int(input("Enter the number of rows: "))
        if num > 0:
            break
    except:
        continue

for i in range(1,num+1):
    for j in range(1,i+1):
        print("#", end=" ")
    print()      
