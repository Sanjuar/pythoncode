while True:
    try:
        num = int(input("Enter the number of rows: "))
        print(num)
        if num > 0: 
            if type(num) == int:
                print("num is an str.")
            else:
                print("num is another type.")
            break
    except:
        continue

for i in range(1,num+1):
    for j in range(1,i+1):
        print("#", end=" ")
    print()      
