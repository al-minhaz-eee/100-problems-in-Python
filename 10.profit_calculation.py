"""
 10. Write a program that will take user input of cost price and selling
 price and determines whether its a loss or a profit
"""
cost_price = float(input("Enter cost price: "))
selling_price = float(input("Enter selling price: "))

if selling_price-cost_price == 0:
    print("There's no loss or profit")
elif selling_price - cost_price>0:
    print("It's a profit of ", selling_price - cost_price)
else:
    print("It's a loss of ",  cost_price-selling_price)