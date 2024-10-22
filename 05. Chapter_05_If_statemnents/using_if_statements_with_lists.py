requested_toppings = ['mushrooms', 'extra cheese', 'pepperoni', 'bacon', 'anchovies']

out_of_stock = ['mushrooms', 'anchovies']

out_of_stock_toppings = []


# this version return a print line for each out of stock topping as well as the in stock toppings
for toppings in requested_toppings: 
    if toppings in out_of_stock:
        print(f"{out_of_stock} are out of stock and we can not add them to your pizza")

    else:
        print(f"Adding {toppings} to your pizza")

# this version returns a list of out of stock toppings in a single line based on a list we build using append
for toppings in requested_toppings: 
    if toppings in out_of_stock:
        out_of_stock_toppings.append(toppings)
        print(f"{out_of_stock_toppings} are out of stock and we can not add them to your pizza")

    else:
        print(f"Adding {toppings} to your pizza")


    
