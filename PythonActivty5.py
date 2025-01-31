cost_price = int(input("Enter the amount of money which you used to buy the product: "))
sales_price = int(input("Enter the amount of money which you used to sell the product: "))
if sales_price>cost_price:
    print("Yayyyyy! You earned a profit of $", sales_price-cost_price)
else:
    print("Oh no! You had a loss of $", sales_price-cost_price)    
