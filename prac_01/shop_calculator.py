total = 0
DISCOUNT = 0.9
numbers = int(input("Number of items: "))
while numbers <= 0:
    print("Invalid message!")
    numbers = int(input("Number of items: "))
for i in range(numbers):
    prices = float(input("Price of item: "))
    total += prices
if total > 100:
    total = total * DISCOUNT
print(f"Total price for {numbers} items is {total:.2f} ")
