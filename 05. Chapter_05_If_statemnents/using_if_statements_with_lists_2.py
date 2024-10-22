# using if statements with lists
# # a more interactive version of the pizza ordering program
# doesn't work properly
# TODO - fix me


available_toppings = ['mushrooms', 'extra cheese', 'pepperoni', 'bacon', 'anchovies', 'pineapple', 'ham', 'olives', 'onions', 'green peppers', 'jalapenos']

out_of_stock = ['mushrooms', 'anchovies', 'olives', 'onions']

what_topping = input("What topping would you like to add? ")

for what_topping in available_toppings: 
    if what_topping in out_of_stock:
        print(f"{what_topping} is out of stock and we can not add it to your pizza")
        print(f'the following toppings are currently available {available_toppings}')
        what_topping = input("What topping would you like to add? ")

    else:
        print(f"Adding {what_topping} to your pizza")
    
    print(out_of_stock)
