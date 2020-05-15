cost_price = int(input("enter cost price: "))
selling_price = int(input("enter selling price: "))
profit = selling_price - cost_price
print("The profit is: ", profit)
increment = 1.05*profit + cost_price
print("price after 5% profit increment: ", increment)
