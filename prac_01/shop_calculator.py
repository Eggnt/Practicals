number_of_items = int(input("Please enter the number of items: "))
total = 0
while number_of_items <= 0:
    print("Invalid number of items!")
    items = int(input("Please enter the number of items: "))
for i in range(0, number_of_items):
    item_price = float(input("Enter the price of the item: "))
    total = total + item_price
if total > 100:
    total = 0.9 * total
print(f"Total price for {number_of_items} items is ${total:.2f}")
