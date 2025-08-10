amount = int(input("Enter amount: "))

tens = amount // 10
amount %= 10

fives = amount // 5
amount %= 5

twos = amount // 2
amount %= 2

ones = amount // 1
amount %= 1

print("Give change as:")
if tens > 0:
    print("₹10 x", tens)
if fives > 0:
    print("₹5 x", fives)
if twos > 0:
    print("₹2 x", twos)
if ones > 0:
    print("₹1 x", ones)
