
sales = float(input("Enter sales: $"))
while 0 < sales:
    if sales < 1000:
        sales_bonus = sales * 0.1
        print(f"Your sales bonus is ${sales_bonus:.2f}.")
        sales = float(input("Enter sales: $"))
    else:
        sales_bonus = sales * 0.15
        print(f"Your sales bonus is ${sales_bonus:.2f}.")
        sales = float(input("Enter sales: $"))

