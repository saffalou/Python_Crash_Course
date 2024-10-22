# Let’s watch out for unusual topping requests before we build a pizza. 
# The following example defines two lists. 
# The first is a list of available toppings at the pizzeria, 
# and the second is the list of toppings that the user has requested. 
# This time, each item in requested_toppings is checked against the list of available toppings before it’s added to the pizza:

available_toppings = ['mushrooms', 'olives', 'green peppers',
                      'pepperoni', 'pineapple', 'extra cheese']

requested_toppings = ['mushrooms', 'french fries', 'extra cheese']

for requested_topping in requested_toppings:
     if requested_topping in available_toppings:
        print(f"Adding {requested_topping}.")
     else:
        print(f"Sorry, we don't have {requested_topping}.")

print("\nFinished making your pizza!")

